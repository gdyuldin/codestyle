from collections import defaultdict


class Sniffer:

    #
    # Some code above
    #

    def _update_char_frequency(self, chunk, char_frequency):
        for line in chunk:
            for char in char_frequency:
                # must count even if frequency is 0
                freq = line.count(char)
                char_frequency[char][freq] += 1

    def _update_modes(self, modes, char_frequency):
        for char, meta_freq in char_frequency.items():
            items = list(meta_freq.items())
            # items - (char count per line, lines)
            if len(items) == 1 and items[0][0] == 0:
                continue
            # get the mode of the frequencies
            if len(items) > 1:
                modes[char] = max(items, key=lambda x: x[1])
                # adjust the mode - subtract the sum of all
                # other frequencies
                items.remove(modes[char])
                modes[char] = (modes[char][0],
                               modes[char][1] - sum(item[1] for item in items))
            else:
                modes[char] = items[0]

    def _update_delims(self, delims, total, modes, delimiters):
        # (rows of consistent data) / (number of rows) = 100%
        consistency = 1.0
        # minimum consistency threshold
        threshold = 0.9
        while len(delims) == 0 and consistency >= threshold:
            for char, (per_line, lines_count) in modes.items():
                if per_line > 0 and lines_count > 0:
                    consistency_is_ok = (lines_count / total) >= consistency
                    char_is_allowed = delimiters is None or char in delimiters
                    if consistency_is_ok and char_is_allowed:
                        delims[char] = per_line, lines_count
            consistency -= 0.01

    def _determine_skipinitialspace(self, lines, delim):
        return lines[0].count(delim) == lines[0].count("%c " % delim)

    def _guess_delimiter(self, data, delimiters):
        """
        The delimiter /should/ occur the same number of times on
        each row. However, due to malformed data, it may not. We don't want
        an all or nothing approach, so we allow for small variations in this
        number.
          1) build a table of the frequency of each character on every line.
          2) build a table of frequencies of this frequency (meta-frequency?),
             e.g.  'x occurred 5 times in 10 rows, 6 times in 1000 rows,
             7 times in 2 rows'
          3) use the mode of the meta-frequency to determine the /expected/
             frequency for that character
          4) find out how often the character actually meets that goal
          5) the character that best meets its goal is the delimiter
        For performance reasons, the data is evaluated in chunks, so it can
        try and evaluate the smallest portion of the data possible, evaluating
        additional chunks as necessary.
        """

        data = list(filter(None, data.split('\n')))

        # build frequency tables
        char_frequency = {chr(c): defaultdict(int) for c in range(127)}
        chunk_length = min(10, len(data))
        modes = {}
        delims = {}
        start, end = 0, min(chunk_length, len(data))
        while start < len(data):
            chunk = data[start:end]
            total = end

            self._update_char_frequency(chunk, char_frequency)
            self._update_modes(modes, char_frequency)
            self._update_delims(delims, total, modes, delimiters)

            if len(delims) == 1:
                delim = list(delims.keys())[0]
                skipinitialspace = self._determine_skipinitialspace(data,
                                                                    delim)
                return (delim, skipinitialspace)

            # analyze another chunk_length lines
            start = end
            end += chunk_length

        if not delims:
            return ('', 0)

        # if there's more than one, fall back to a 'preferred' list
        if len(delims) > 1:
            for d in self.preferred:
                if d in delims:
                    skipinitialspace = self._determine_skipinitialspace(data,
                                                                        d)
                    return (d, skipinitialspace)

        # nothing else indicates a preference, pick the character that
        # dominates(?)
        items = delims.items()
        delim, _ = max(items, key=lambda x: x[1][1])

        skipinitialspace = self._determine_skipinitialspace(data, d)
        return (delim, skipinitialspace)
