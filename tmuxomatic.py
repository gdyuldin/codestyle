#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

BSD 3-Clause License

Copyright 2013-2016, Oxidane
All rights reserved

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products
derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""

##----------------------------------------------------------------------------------------------------------------------
##
## Name ....... tmuxomatic
## Synopsis ... Automated window layout and session management for tmux
## Author ..... Oxidane
## License .... BSD 3-Clause
## Source ..... https://github.com/oxidane/tmuxomatic
##
##---------------+------------------------------------------------------------------------------------------------------
##     About     |
##---------------+
##
## QUICKSTART: See the session file "session_demo" in the examples folder, then run it with "tmuxomatic session_demo".
##
## The tmux interface for creating window splits is technically simple, but to use those splits to arrange layouts is a
## tedious and inefficient process.  Other tmux session management tools offer no solutions when it comes to splitting
## windows, so they have the same usability problem of tmux, compounded by their needy configuration files.
##
## Ideally I wanted a more intuitive interface, completely reinvented to be as simple and as user-friendly as possible.
## You depict the window pane layout in a "windowgram", where each unique character identifies a pane.  Then each pane
## is linked by its character to an optional directory, run commands, and focus state.  The program would then translate
## this information to the necessary tmux commands for splitting, scaling, pathing, and sendkeys.
##
## So that's exactly what tmuxomatic does.
##
## For a quick introduction that demonstrates the core feature set of tmuxomatic, see the readme file.
##
##-------------------+--------------------------------------------------------------------------------------------------
##     Revisions     |
##-------------------+
##
DESCRIPTION = "Intelligent tmux session management" # Maybe add: "using windowgrams"
HOMEPAGE = "https://github.com/oxidane/tmuxomatic"
VERSION = "2.19-dev" # x.y: x = Major feature, y = Minor feature or bug fix ... Development versions as "x.y-dev"
##
##  2.19    TBD         Improvements and bug fixes
##                      Implemented #10: Adds windows to current session if run within tmux
##                      Optimized window creation by combining tmux commands into fewer executable calls
##                      Fixed issue #13: User defined pane-base-index
##                      Fixed issue #14: Default directory on panes with no commands
##                      Fixed issue #15: Use correct readme when installing from github
##                      Added example file session_test that uses all 62 panes
##
##  2.18    2015-07-03  New flex command: insert
##                      Fixed issues #11, #12: Better handling of the "window" directive
##
##  2.17    2014-12-24  New flex command: reset
##                      Fixed some bugs in the drag command
##
##  2.16    2014-12-18  New flex command: drag
##                      Added smudge core, required by upcoming flex commands
##
##  2.15    2014-12-12  Fixed PyPI readme and screenshot
##                      See PyPI information detailed in the notes section
##
##  2.14    2014-12-11  Applying screenshot scale fix to PyPI readme
##                      Added edge core, required by upcoming flex commands
##
##  2.13    2014-12-06  Fixed PyPI long description by setting the index links to absolute
##                      PyPI does not support relative links (see https://stackoverflow.com/q/16367770)
##
##  2.12    2014-12-05  Various PyPI fixes
##                      Fixed the screenshot link and index links
##
##  2.11    2014-12-03  Fixed PyPI distribution
##                      This version is otherwise identical to the previous release
##
##  2.10    2014-12-03  Better screenshot
##                      Added contributor agreement
##                      Added the readme to PyPI
##
##  2.9     2014-11-26  Added PyPI compatible readme file
##                      Flex scale single parameter mixed type support
##                      Fixed bugs from the windowgram module migration
##
##  2.8     2014-11-24  Added some unit tests, full testing for flex and main classes to be added in 2.x
##                      Windowgram group conversion between pattern and list representations
##                      Flex console supports user window resize
##
##  2.7     2014-11-21  Moved windowgram and flex to its own module, see windowgram.py for details
##                      Various source cleanup in windowgram and flex
##
##  2.6     2014-11-15  New flex command: swap
##                      Support for issue #9: Sessions may be renamed from the session file
##                      Flex command ambiguity resolver to eliminate the need for short aliases
##
##  2.5     2014-11-12  New flex command: rename
##                      Improved the split command
##
##  2.4     2014-09-14  New flex command: split
##                      Multiple flex commands on one line, like a unix shell
##
##  2.3     2014-09-10  New flex command: join
##                      Switched to scale core v1 for more accurate scale results
##
##  2.2     2014-09-08  New flex command: break
##                      Optional window specification with filename when using flex
##                      Fixed scale core to resolve accuracy problems in scale and break commands
##                      Moved windowgram functions into a Windowgram class
##
##  2.1     2014-09-01  New flex command: add
##                      Cleared revision history for 1.x, added link in case it's needed
##                      If specified session file does not exist when using flex, it is created
##                      Improved the window list, shares the table printer code with the help menu
##
##  2.0     2014-08-28  Began tmuxomatic --flex, commands will be added over the next few releases
##                      Fixed the readme to fit the recent github style changes
##                      Fixed issue #8: Uses window name for focus to support tmux base-index
##                      Moved scale feature into flex, added flex section to readme
##                      Source indentation now uses spaces, for github readability
##                      New versioning for tmuxomatic, version 1.1.0 re-released as 2.0
##
##  ------- --------------------------------------------------------------------------------------------------------
##
##  1.x     https://github.com/oxidane/tmuxomatic/blob/ac7290e2206d4470d85c4eb6fa91c88794a17e45/tmuxomatic#L75-157
##
##--------------------+-------------------------------------------------------------------------------------------------
##     Expansions     |
##--------------------+
##
## 2.x:
##
##      Finish flex console
##
##      License and release windowgram library
##
##      Minimal color support for the windowgram
##
## 3.x:
##
##      Refactor flex console to use Python's cmd module
##
##      Add color to flex console with full color support for the windowgram
##
## Minor:
##
##      Definitely add ncurses or urwid.  The 8-bit background colors could be used to highlight panes.  This would be
##      quite awesome for usability, and makes demonstrations easier to follow.  A toggle for edge mode could show
##      background colors on neighboring panes to illustrate edges.  Maybe this could be an objective for 3.x.
##      When ncurses support is added, the flex shell should highlight panes for relevant flex modifier parameters as
##      they're being typed.  Normal pane display is white text on color background.  Highlight is color text on white
##      background.  Use gray for secondary highlight, e.g. the optional scale panes parameter for the commands drag,
##      insert, and clone.
##
##      Video demonstration of tmuxomatic, including the "--scale" feature and how it's used for rapid development
##      and modification of windowgrams ("12\n34" -> 4x -> add small windows).  Keep it short, fast paced,
##      demonstrating at least one small and one large example.
##
##      Manual page.  Include command line examples.
##
##      Possibly embed the examples in the program, allowing the user to run, extract, or view the session files.
##
##      Would be great to add a file format template that adds color to the tmuxomatic session file in text editors.
##      If it could give an even unique color (e.g., evenly spaced over color wheel) to each pane in the windowgram,
##      then I think it would make the custom format much more appealing.  Detection abilities may be limited in some
##      IDEs though, so an extension may be necessary.  Anyway, a dimension of color will allow the windowgram to be
##      more rapidly assessed at-a-glance.
##
##      Support other multiplexers like screen, if they have similar capabilities (vertical splits, shell driven, etc).
##      Screen currently does not have the ability to modify panes from the command line, this is required for support.
##
##      If filename is not specified, show running tmuxomatic sessions, and allow reconnect without file being present.
##
##      Port the readme to a format compatible with pypi.  Add readme and sample sessions to the distribution.
##
##      Command line auto-completion support for zsh, etc.
##
##      Reversing function.  This takes a split-centric configuration and produces a windowgram.  Has size or accuracy
##      parameter that defines the size of the windowgram.  Utility is dubious, as it has not been requested, but it
##      would be easy to code.  Add conversions from popular managers.
##
##      Runnable session files.  Basically the session file invokes tmuxomatic with fixed and/or forwarded arguments.
##      It copies itself via stdin or a /tmp file.  For easy application to any session file, constrain code to only a
##      few short lines at the top of the session file that are easily cut and pasted into another.  A prototype of this
##      concept was done in early development, though it had a slightly different design, so it's best rewritten.
##
##      Pane view toggle in flex.  With the command "pane <pane>", only the pane is shown with "." for other panes, and
##      information about the pane is shown, width and height, along with lines to all the possible axial divisions, so
##      a user could easily find the exact value they need to achieve a precise split, for example.  These values are
##      shown as positive and negative, characters and percentages, e.g., "+6 | +75% | -2 | -25%".
##
##      Maybe unit testing for windowgram parser, and flex commands.
##
##      Run unit testing online.
##
## Major:
##
##      Session Binding: A mode that keeps the session file and its running session synchronized.  Some things won't be
##      easy to do.  Changing the name of a window is easy, but changing windowgram may not be (without unique
##      identifiers in tmux).  Use threading to keep them in sync.  Error handling could be shown in a created error
##      window, which would be destroyed on next session load if there was no error.
##
##      Touch screen interface using flex commands.  Select edges with tap, then drag them as a group, for example.
##
## Possible:
##
##      Multiple commands in a single call to tmux for faster execution (requires tmux "stdin").
##
##      Creating two differently-named tmuxomatic sessions at the same time may conflict.  If all the tmux commands
##      could be sent at once then this won't be a problem (requires tmux "stdin").
##
##      The tmuxomatic pane numbers could be made equal to tmux pane numbers (0=0, a=10, A=36), but only if tmux will
##      support pane renumbering, which is presently not supported (requires tmux "renumber-pane").
##
##      If tmux ever supports some kind of aggregate window pane arrangements then the tmux edge case represented by the
##      example "session_unsupported" could be fixed (requires tmux "add-pane").
##
##------------------+---------------------------------------------------------------------------------------------------
##     Requests     |
##------------------+
##
## These are some features I would like to see in tmux that would improve tmuxomatic.  If anyone adds these features to
## tmux, notify me and I'll upgrade tmuxomatic accordingly.
##
##      1) tmux --stdin                 Run multiple line-delimited commands in one tmux call (with error reporting).
##                                      Upgrades: Faster tmuxomatic run time, no concurrent session conflicts.
##
##      2) tmux renumber-pane old new   Changes the pane number, once set it doesn't change, except from this command.
##                                      Upgrades: The tmux pane numbers will reflect those in the session file.
##
##      3) tmux add-pane x y w h        Explicit pane creation (exact placement and dimensions).  This automatically
##                                      pushes neighbors, subdivides, or re-appropriates, the affected unassigned panes.
##                                      Upgrades: Fast, precise arbitrary windowgram algorithm; resolves the edge case.
##
##      4) tmux preserve-proportions    If tmux preserves proportional pane sizes, when xterm is resized, the panes will
##                                      be proportionally adjusted.  This feature would save from having to restart
##                                      tmuxomatic when the xterm size at session creation differed from what they
##                                      intend to use.  See relative pane sizing notes for more information.
##
##---------------+------------------------------------------------------------------------------------------------------
##     Terms     |
##---------------+
##
##      windowgram      A rectangle comprised of unique alphanumeric rectangles representing panes in a window.
##
##      xterm           Represents the user's terminal window, may be xterm, PuTTY, SecureCRT, iTerm, or similar.
##
##      tmux            The terminal multiplexer program, currently tmuxomatic only supports tmux.
##
##      session         A single tmux attachment, containing one or more windows.
##
##      window          One window within a session that contains one or more panes.
##
##      pane            Any subdivision of a window with its own shell.
##
##---------------+------------------------------------------------------------------------------------------------------
##     Notes     |
##---------------+
##
## This program addresses only the session layout (windows, panes).  For tmux settings (status bar, key bindings), users
## should consult an online tutorial for ".tmux.conf".
##
## For best results, design windowgrams that have a similar width-to-height ratio as your xterm.
##
## The way tmuxomatic (and tmux) works is by recursively subdividing the window using vertical and horizontal splits.
## If you specify a windowgram where such a split is not possible, then it cannot be supported by tmux, or tmuxomatic.
## For more information about this limitation, including an example, see file "session_unsupported" in examples folder.
##
## Supports any pane arrangement that is also supported by tmux.  Some windowgrams, like those in "session_unsupported",
## won't work because of tmux (see "add-pane").
##
## The pane numbers in the session file will not always correlate with tmux (see "renumber-pane").
##
## For a list of other tmux feature requests that would improve tmuxomatic support, see the "Expansions" section.
##
## This was largely written when I was still new to Python, so not everything is pythonic.
##
## Supporting PyPI has been problematic.  Porting the readme from markdown to rst would solve many of the problems,
## since it's supported by both PyPI and Github.  However I prefer it to be in markdown format, and PyPI will probably
## add support for it eventually.  The PyPI rst-to-html conversion (or rst itself) has the following issues: there's no
## support for nested lists (main index), does not produce html/css for image fitting (screenshot size), no relative
## linking (main index), and no inline html (screenshot scaling).  Releases 2.10 to 2.15 primarily dealt with these
## issues.
##
##--------------------+-------------------------------------------------------------------------------------------------
##     Other Uses     |
##--------------------+
##
## The windowgram parser and splitting code could be used for some other purposes:
##
##      * HTML table generation
##
##      * Layouts for other user interfaces
##
##      * Level design for simple tiled games (requires allowing overlapped panes and performing depth ordering)
##
##----------------------------------------------------------------------------------------------------------------------

import sys, os, time, subprocess, argparse, signal, re, math, copy, inspect

import windowgram               # Required for print(windowgram.__version__), eventually this will be the only import
from windowgram import *        # Reorganize windowgram and its use so that only "import windowgram" is needed

try: import yaml ; INSTALLED_PYYAML = True
except ImportError as e: INSTALLED_PYYAML = False



##----------------------------------------------------------------------------------------------------------------------
##
## Globals
##
##----------------------------------------------------------------------------------------------------------------------

ARGS            = None
USERS_TMUX      = None                  # Once identified, the user's tmux version is saved here for later use

# Flexible Settings (may be safely changed)

PROGRAM_THIS    = "tmuxomatic"          # Name of this executable, alternatively: sys.argv[0][sys.argv[0].rfind('/')+1:]
EXE_TMUX        = "tmux"                # Short variable name for short line lengths, also changes to an absolute path
MAXIMUM_WINDOWS = 16                    # Maximum windows (not panes), easily raised by changing this value alone
VERBOSE_WAIT    = 1.5                   # Wait time prior to running commands, time is seconds, only in verbose mode
DEBUG_SCANLINE  = False                 # Shows the clean break scanline in action if set to True and run with -vvv

# Fixed Settings (requires source update)

MINIMUM_TMUX    = "1.8"                 # Minimum supported tmux version is 1.8 (required for absolute sizing)
VERBOSE_MAX     = 4                     # 0 = quiet, 1 = summary, 2 = inputs, 3 = fitting, 4 = commands

# Aliases for flexible directions

ALIASES = {
    'foc': "focus key keys cur cursor", # Use "use user" or reserve them for other use?
    'dir': "directory path cd pwd cwd home",
    'run': "exe exec execute",
}



##----------------------------------------------------------------------------------------------------------------------
##
## Public derivations ... These two functions come from credited sources believed to be in the public domain
##
##----------------------------------------------------------------------------------------------------------------------

def get_xterm_dimensions_wh(): # cols (x), rows (y)
    """
    Returns the dimensions of the user's xterm
    Based on: https://stackoverflow.com/a/566752
    """
    rows = cols = None
    #
    # Linux
    #
    stty_exec = os.popen("stty size", "r").read()
    if stty_exec:
        stty_exec = stty_exec.split()
        if len(stty_exec) >= 2:
            rows = stty_exec[0]
            cols = stty_exec[1]
    if rows and cols:
        return int(cols), int(rows) # cols, rows
    #
    # Solaris
    #
    rows = os.popen("tput lines", "r").read() # Issue #4: Use tput instead of stty on some systems
    cols = os.popen("tput cols", "r").read()
    if rows and cols:
        return int(cols), int(rows) # cols, rows
    #
    # Unix
    #
    def ioctl_gwinsz(fd):
        # Get xterm size via ioctl
        try:
            import fcntl, termios, struct
            cr = struct.unpack("hh", fcntl.ioctl(fd, termios.TIOCGWINSZ, "1234"))
        except (IOError, RuntimeError, TypeError, NameError):
            return
        return cr
    cr = ioctl_gwinsz(0) or ioctl_gwinsz(1) or ioctl_gwinsz(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_gwinsz(fd)
            os.close(fd)
        except (IOError, RuntimeError, TypeError, NameError):
            pass
    if not cr:
        env = os.environ
        cr = (env.get("LINES", 25), env.get("COLUMNS", 80))
    if cr and len(cr) == 2 and int(cr[0]) > 0 and int(cr[1]) > 0:
        return int(cr[1]), int(cr[0]) # cols, rows
    #
    # Unsupported ... Other platforms not needed since tmux doesn't run there
    #
    return 0, 0 # cols, rows

def which(program):
    """
    Returns the absolute path of specified executable
    Source: https://stackoverflow.com/a/377028
    """
    def is_exe(fpath):
        # Return true if file exists and is executable
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
    fpath, _ = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return None



##----------------------------------------------------------------------------------------------------------------------
##
## Miscellaneous functions ... These are general use functions used throughout tmuxomatic
##
##----------------------------------------------------------------------------------------------------------------------

def synerr( errpkg, errmsg ):
    """
    Syntax error: Display error and exit
    """
    if 'quiet' in errpkg:
        print("Error: " + errmsg)
    elif errpkg['format'] == "shorthand":
        # Shorthand has exact line numbers
        print("Error on line " + str(errpkg['line']) + ": " + errmsg)
    else:
        # The exact line number in YAML is not easily known with pyyaml
        print("Error on or after line " + str(errpkg['line']) + ": " + errmsg)
    exit(0)

def tmux_run( command, nopipe=False, force=False, real=False ):
    """
    Executes the specified shell command (i.e., tmux)
        nopipe ... Do not return stdout or stderr
        force .... Force the command to execute even if ARGS.noexecute is set
        real ..... Command should be issued regardless, required for checking version, session exists, etc
    """
    noexecute = ARGS.noexecute if ARGS and ARGS.noexecute else False
    printonly = ARGS.printonly if ARGS and ARGS.printonly else False
    verbose   = ARGS.verbose   if ARGS and ARGS.verbose   else 0
    if not noexecute or force:
        if printonly and not real:
            # Print only, do not run
            print(str(command)) # Use "print(str(command), end=';')" to display all commands on one line
            return
        if verbose >= 4 and not real:
            print("(4) " + str(command))
        if nopipe:
            os.system(command)
        else:
            proc = subprocess.Popen( command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
            stdout, stderr = proc.communicate()
            # Return stderr or stdout
            if stderr: return str(stderr, "ascii")
            return str(stdout, "ascii")

def tmux_version(): # -> name, version
    """
    Queries tmux for the version
    """
    result = tmux_run( EXE_TMUX + " -V", nopipe=False, force=True, real=True )
    result = [ line.strip() for line in result.split("\n") if line.strip() ]
    name = result[0].split(" ", 1)[0] # Name that was reported by tmux (should be "tmux")
    version = result[0].split(" ", 1)[1] # Only the version is needed
    return name, version

def signal_handler_break( signal_number, frame ):
    """
    On break, displays interruption message and exits.
    """
    _ = repr(signal_number) + repr(frame) # Satisfies pylint
    print("User interrupted...")
    exit(0)

def signal_handler_hup( signal_number, frame ):
    """
    Use the KeyboardInterrupt exception to communicate user disconnection
    """
    _ = repr(signal_number) + repr(frame) # Satisfies pylint
    raise KeyboardInterrupt

def satisfies_minimum_version(minimum, version):
    """
    Asserts compliance by tmux version.  I've since seen a similar version check somewhere that may come with Python
    and could probably replace this code, but this works fine for now.
    Update:
        Option 1: setuptools.pkg_resources.parse_version() ... The setuptools library is non-standard
        Option 2: distutils.version.LooseVersion() ... Required for "1.9a" to be recognized
    """
    qn = len(minimum.split("."))
    pn = len(version.split("."))
    if qn < pn: minimum += ".0" * (pn-qn) # Equalize the element counts
    if pn < qn: version += ".0" * (qn-pn) # Equalize the element counts
    ver_intlist = lambda ver_str: [int(re.sub(r'\D', r'', x)) for x in ver_str.split(".")] # Issues: #1, #2
    for p, q in zip( ver_intlist(version), ver_intlist(minimum) ):
        if int(p) == int(q): continue # Qualifies so far
        if int(p) > int(q): break # Qualifies
        return False
    return True

def command_matches(command, primary):
    """
    Matches the command (from file) with the primary (for branch)
    Returns True if command is primary or a supported alias
    """
    if command == primary: return True
    if primary in ALIASES and command in ALIASES[primary].split(" "): return True
    return False

def qsplit(string, maxsplit=None):
    # Just like string.split() but respects quoted strings
    #   "1 \"t w o\" 3"   ->   [ '1', '"t w o"', '3' ]
    result = re.findall(r"[^\"]+|\"[^\"]*\"", string) # Based on: https://stackoverflow.com/a/366532
    if maxsplit is not None: result = result[:maxsplit]
    result, result_scan = [], result
    for e1 in result_scan:
        if e1.startswith("\""):
            result.append(e1)
        else:
            result = result + [ e2 for e2 in e1.split(" ") if e2 ]
    return result



##----------------------------------------------------------------------------------------------------------------------
##
## Session file objects
##
##----------------------------------------------------------------------------------------------------------------------

##
## Window declaration macros
## A window declaration without a specified name is not allowed, except during the file parsing
##

is_windowdeclaration = lambda line: re.search(r"^[ \t]*window", line)
windowdeclaration_name = lambda line: " ".join(re.split(r"[ \t]+", line)[1:]) if is_windowdeclaration(line) else ""

##
## Session declaration macros
##

is_sessiondeclaration = lambda line: re.search(r"^[ \t]*session", line)
sessiondeclaration_name = lambda line: " ".join(re.split(r"[ \t]+", line)[1:]) if is_sessiondeclaration(line) else ""

##
## Parsed session file classes
##

class BatchOfLines(object): # A batch of lines (delimited string) with the corresponding line numbers (int list)
    def __init__(self):
        self.lines = ""             # Lines delimited by \n, expects this on the last line in each batch of lines
        self.counts = []            # For each line in lines, an integer representing the corresponding line number
    def __repr__(self): # Debugging
        return "lines = \"" + self.lines.replace("\n", "\\n") + "\", counts = " + repr(self.counts)
    def AppendBatch(self, lines, start, increment=True):
        linecount = len(lines.split("\n")[:-1]) # Account for extra line
        self.lines += lines
        self.counts += [line for line in range(1, linecount+1)] if increment else ([start] * linecount)
    def IsEmpty(self):
        return True if not self.lines else False

class Window(object): # Common container of window data, divided into sections identified by the keys below
    def __init__(self):
        self.__dict__['data'] = {} # { 'title_comments': string_of_lines, 'title': string_of_lines, ... }
        self.__dict__['line'] = {} # { 'title_comments': first_line_number, 'title': first_line_number, ... }
        for key in self.ValidKeys(): self.ClearKey(key) # Clear all keys
    def __getitem__(self, key): # Invalid keys always return ""
        return self.__dict__['data'][key] if key in self.ValidKeys() else ""
    def __setitem__(self, key, value): # Invalid keys quietly dropped
        if key in self.ValidKeys(): self.__dict__['data'][key] = value
    def __repr__(self): # Debugging
        return "\n__repr__ = [\n" + \
            ", ".join(
                [ "'" + key + "': [ data = \"" + self.__dict__['data'][key].replace("\n", "\\n") + \
                "\", starting_line_number = " + str(self.__dict__['line'][key]) + " ]\n" \
                for key in self.ValidKeys() if self[key] is not "" ] \
            ) + \
        " ]\n"
    def ClearKey(self, key):
        if key in self.ValidKeys():
            self.__dict__['data'][key] = ""
            self.__dict__['line'][key] = 0
    def ValidKeys(self): # Ordered by appearance
        return "title_comments title windowgram_comments windowgram directions_comments directions".split(" ")
    def Serialize(self): # Serialized by appearance
        return "".join( [ self[key] for key in self.ValidKeys() ] )
    def WorkingKeys(self):
        return [ key for key in self.ValidKeys() if self[key] is not "" ]
    def IsFooter(self):
        summary = " ".join( self.WorkingKeys() )
        return True if summary == "title_comments" or summary == "" else False
    def FirstLine(self, key):
        return True if key in self.ValidKeys() and self.__dict__['line'][key] == 0 else False
    def SetLine(self, key, line):
        if key in self.ValidKeys(): self.__dict__['line'][key] = line
    def GetLine(self, key):
        return self.__dict__['line'][key] if key in self.ValidKeys() else 0
    def SetIfNotSet(self, key, line):
        if self.FirstLine(key): self.SetLine(key, line)
    def GetLines(self, key):
        return self.__dict__['line'][key]
    def SplitCleanByKey(self, key):
        return [ line[:line.index('#')].strip() if '#' in line else line.strip() for line in self[key].split("\n") ]

class SessionFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.Clear()
        self.modified = False   # Explicit modification
    def Clear(self):
        self.format = None      # "shorthand" or "yaml"
        self.footer = ""        # footer comments
        self.windows = []       # [ window, window, ... ]
    def Load_Shorthand_SharedCore(self, bol):
        # Actually locals
        self.state = 0
        self.window = None
        self.line = [ None, None ]      # line without cr, line number
        self.comments = [ "", None ]    # lines with cr, first line number
        # Switchboard
        switchboard = [
            "title_comments",       # state == 0 <- loop to / file footer saved here in its own window
            "title",                # state == 1
            "windowgram_comments",  # state == 2
            "windowgram",           # state == 3
            "directions_comments",  # state == 4
            "directions",           # state == 5
            "UNUSED_comments",      # state == 6 <- loop from / always appends this to "title_comments"
        ]
        # Iterate lines and append onto respective window keys
        lines = bol.lines.split("\n")[:-1] # Account for extra line
        lines_index = 0
        while True:
            def transfercomments(): # Transfer comments (if any) to the current window block
                if self.comments[0] is not None:
                    self.window[ switchboard[self.state] ] += self.comments[0]
                    self.window.SetIfNotSet( switchboard[self.state], self.comments[1] )
                self.comments[0] = self.comments[1] = None
            def nextwindow(): # This is called in two cases: 1) window declaration found, 2) end of file reached
                if self.window: self.windows.append( self.window )
                self.window = Window() ; self.state = 0 ; transfercomments() ; self.state = 1
            def addline(): # Adds current line to current block or comments
                if switchboard[self.state].endswith("_comments"): # Add to comments
                    if self.comments[0] is None: self.comments[0] = self.line[0] + "\n"
                    else: self.comments[0] += self.line[0] + "\n"
                    self.comments[1] = self.line[1] if self.comments[1] is None else self.comments[1]
                else: # Add to block
                    self.window[ switchboard[self.state] ] += self.line[0] + "\n"
                    self.window.SetIfNotSet( switchboard[self.state], self.line[1] )
                self.line[0] = self.line[1] = None # Ready to load next line
            # Load line with corresponding line number
            if self.line[0] is None and lines_index < len(lines): # Line
                self.line[0] = lines[lines_index] ; self.line[1] = bol.counts[lines_index]
                lines_index += 1
            if self.line[0] is None: # EOF
                # Hold comments so the footer doesn't get lost to the non-existent state 6 block
                hold = [ None, None ]
                hold[0], hold[1] = self.comments[0], self.comments[1]
                self.comments[0], self.comments[1] = None, None
                nextwindow()
                # Restore comments so they are assimilated as a proper footer
                self.comments[0], self.comments[1] = hold[0], hold[1]
                if self.comments[0] is not None:
                    self.state = 0
                    transfercomments()
                    nextwindow()
                # Done parsing
                break
            # Line used for analysis is stripped of all comments and whitespace
            lineused = self.line[0].strip()
            if lineused.find("#") >= 0: lineused = lineused[:lineused.find("#")].strip()
            # Append this line to section or comments
            if is_windowdeclaration(lineused): nextwindow() ; addline() ; self.state = 2 # New window declaration
            elif ( self.state == 2 or self.state == 4 ) and lineused: transfercomments() ; self.state += 1 ; addline()
            elif ( self.state == 3 or self.state == 5 ) and not lineused: self.state += 1 ; addline()
            elif self.state == 6 and lineused: addline() ; self.state = 5 ; transfercomments() # Back up and add to 5
            else: addline() # Everything else adds the line / Until first window declaration is found add to comments
        # Any comments at end of file should be extracted into the footer string
        if len(self.windows) and self.windows[len(self.windows)-1].IsFooter():
            window = self.windows.pop(len(self.windows)-1)
            self.footer = window.Serialize()
    def Load_Shorthand(self, rawfile):
        self.Clear()
        self.format = "shorthand"
        bol = BatchOfLines()
        bol.AppendBatch( rawfile, 1 )
        self.Load_Shorthand_SharedCore( bol )
    def Load_Yaml(self, rawfile):
        self.Clear()
        self.format = "yaml"
        # Yaml -> Dict
        try:
            # Line numbers (per window) with pyyaml from: https://stackoverflow.com/a/13319530
            loader = yaml.SafeLoader(rawfile)
            def compose_node(parent, index):
                line = loader.line # The line number where the previous token has ended (plus empty lines)
                node = yaml.SafeLoader.compose_node(loader, parent, index)
                node.__line__ = line + 1
                return node
            def construct_mapping(node, deep=False):
                mapping = yaml.SafeLoader.construct_mapping(loader, node, deep=deep)
                mapping['__line__'] = node.__line__
                return mapping
            loader.compose_node = compose_node
            loader.construct_mapping = construct_mapping
            # Load into dict, now with line numbers for location of window in YAML
            filedict = loader.get_single_data() # filedict = yaml.safe_load( rawfile ) # Without line numbers
        except:
            filedict = {}
        # Dict -> Shorthand
        group_session = []
        group_other = []
        bol = BatchOfLines()
        bol.AppendBatch( "\n", 0, False ) # Translated YAML -> Shorthand, no need for header
        if type(filedict) is list:
            for entry in filedict:
                # Session renames
                if type(entry) is dict and 'session' in entry:
                    linenumber = entry['__line__'] if '__line__' in entry else 0
                    rawfile_shorthand = "session " + str(entry['session']) + "\n\n"
                    group_session.append( [ rawfile_shorthand, linenumber, False ] )
                # Name blocks... Windows are identified by 'name' key
                elif type(entry) is dict and 'name' in entry:
                    # Must contain 'windowgram' and 'directions' as block literals
                    windowgram = entry['windowgram'] if 'windowgram' in entry else ""
                    directions = entry['directions'] if 'directions' in entry else ""
                    linenumber = entry['__line__'] if '__line__' in entry else 0
                    rawfile_shorthand = \
                        "window " + str(entry['name']) + "\n\n" + windowgram + "\n" + directions + "\n\n\n"
                    group_other.append( [ rawfile_shorthand, linenumber, False ] )
        # Append data, if any; this will force session renames to the top of the shorthand file
        if group_session or group_other:
            # Session renaming is only valid at top of file
            for rawfile_shorthand, linenumber, flag in group_session:
                bol.AppendBatch( rawfile_shorthand, linenumber, False )
            # Everything else follows
            for rawfile_shorthand, linenumber, flag in group_other:
                bol.AppendBatch( rawfile_shorthand, linenumber, False )
        # Shorthand -> Core
        self.Load_Shorthand_SharedCore( bol )
    def Load(self):
        # Load raw data
        rawfile = ""
        f = open(self.filename, "rU")
        while True:
            line = f.readline()
            if not line: break # EOF
            rawfile += line
        # Detect file format
        format_yaml = False
        for line in rawfile.split("\n"):
            if line.find("#") >= 0: line = line[:line.find("#")]
            line = line.strip()
            if line:
                if line[0] == "-":
                    format_yaml = True
                break
        # Parse the file
        if format_yaml:
            if not INSTALLED_PYYAML:
                print("You have specified a session file in YAML format, yet you do not have pyyaml installed.")
                print("Install pyyaml first, usually with a command like: `sudo pip-python3 install pyyaml`")
                exit(0)
            self.Load_Yaml( rawfile )
        else:
            self.Load_Shorthand( rawfile )
    def Save(self):
        self.modified = False
        if self.filename and self.format:
            if self.format == "shorthand":
                # Shorthand
                f = open(self.filename, 'w')
                for window in self.windows: f.write( window.Serialize() )
                f.write( self.footer )
            if self.format == "yaml":
                # YAML
                formatted = "##\n## YAML session file generated by tmuxomatic flex " + VERSION + "\n##\n\n---\n\n"
                # Required for writing block literals, source: https://stackoverflow.com/a/6432605
                def change_style(style, representer):
                    def new_representer(dumper, data):
                        scalar = representer(dumper, data)
                        scalar.style = style
                        return scalar
                    return new_representer
                class literal_str(str): pass
                represent_literal_str = change_style('|', yaml.representer.SafeRepresenter.represent_str)
                yaml.add_representer(literal_str, represent_literal_str)
                # Add the session name change
                rename = self.RenameIfSpecified_Raw()
                if rename is not None:
                    formatted += yaml.dump( [{'session': rename}], \
                        indent=2, default_flow_style=False, explicit_start=False )
                    formatted += "\n"
                # Now add all windows to a dictionary for saving
                for ix, window in enumerate(self.windows):
                    serial = 1+ix
                    # Extract name: "window panel 1\n" -> "panel 1"
                    name = windowdeclaration_name( self.Get_WindowDeclarationLine( serial ) )
                    # Append window definition
                    # TODO: Sort as "name", "windowgram", "directions".  Maybe use: http://pyyaml.org/ticket/29
                    window_dict = {
                        'name': str(name),
                        'windowgram': literal_str(window['windowgram']),
                        'directions': literal_str(window['directions']),
                    }
                    # Dump to string, with linebreaks
                    formatted += yaml.dump( [window_dict], indent=2, default_flow_style=False, explicit_start=False )
                    formatted += "\n"
                # Write file
                f = open(self.filename, 'w')
                f.write( formatted )
    def Ascertain_Trailing_Padding(self, string):
        count = 0
        for ix in range( len(string)-1, -1, -1 ):
            if string[ix] == "\n": count += 1
            else: break
        return count
    def Duplicate_Trailing_Padding(self, string, minimum):
        count = self.Ascertain_Trailing_Padding(string)
        if count < minimum: count = minimum
        return "\n" * count
    def Replace_TitleComments(self, serial, comments):
        if serial < 1 or serial > self.Count_Windows(): return
        padding = self.Duplicate_Trailing_Padding(self.windows[serial-1]['title_comments'], 1)
        self.windows[serial-1]['title_comments'] = comments + padding
        self.modified = True
    def Replace_Title(self, serial, name):
        if serial < 1 or serial > self.Count_Windows(): return
        padding = self.Duplicate_Trailing_Padding(self.windows[serial-1]['title'], 1)
        self.windows[serial-1]['title'] = "window " + name + padding
        self.modified = True
    def Replace_Windowgram(self, serial, windowgram_string): # TODO: Replace by wg
        if serial < 1 or serial > self.Count_Windows(): return
        self.windows[serial-1]['windowgram'] = Windowgram( windowgram_string ).Export_String() # Clean via class
        self.modified = True
    def Modified(self): # See flag use for limitations
        return self.modified
    def Count_Windows(self):
        return len(self.windows)
    def Serial_Is_Valid(self, serial):
        return serial >= 1 and serial <= len(self.windows)
    def Get_WindowDeclarationLine(self, serial):
        if serial < 1 or serial > self.Count_Windows(): return "???" # Out of range
        return linestrip(self.windows[serial-1]['title'].split("\n")[0]) # Window declaration is on first line
    def Get_Name(self, serial):
        if serial < 1 or serial > self.Count_Windows(): return "???" # Out of range
        return windowdeclaration_name( self.Get_WindowDeclarationLine( serial ) )
    def Get_WindowgramDimensions_Int(self, serial):
        windowgram_string = self.windows[serial-1]['windowgram']
        return Windowgram(windowgram_string).Analyze_WidthHeight()
    def Get_Windowgram(self, serial): # windowgram_string
        if serial < 1 or serial > self.Count_Windows():
            if warning is None: return None
            return None, "Out of range"
        windowgram_string = Windowgram_Convert.PurifyString(self.windows[serial-1]['windowgram'])
        return windowgram_string
    def Get_Wg(self, serial): # wg
        windowgram_string = self.Get_Windowgram(serial)
        return Windowgram(windowgram_string) if windowgram_string else None
    def Add_Windowgram(self, comments, name, windowgram_string):
        self.windows.append( Window() )
        serial = len(self.windows)
        # Transfer footer to title comments for new window
        while len(self.footer) > 1 and not self.footer.endswith("\n\n"): self.footer += "\n"
        if not self.footer: self.footer = "\n"
        self.windows[serial-1]['title_comments'] = self.footer
        self.footer = ""
        # Build window
        self.windows[serial-1]['title_comments'] += comments if comments[-1:] == "\n" else comments + "\n"
        name = "window " + name # Make a declaration
        self.windows[serial-1]['title'] = name if name[-1:] == "\n" else name + "\n"
        self.windows[serial-1]['windowgram_comments'] = "\n"
        self.windows[serial-1]['windowgram'] = \
            windowgram_string if windowgram_string[-1:] == "\n" else windowgram_string + "\n"
        # Modified
        self.modified = True
        return serial
    def RenameIfSpecified_Raw(self): # new_name (raw) or None
        # Parse every line and change the name if specified (session rename only valid in comments sections)
        new_name = None
        if self.windows:
            batch = self.windows[0].SplitCleanByKey('title_comments')
            for line in batch:
                if is_sessiondeclaration(line):
                    new_name = sessiondeclaration_name(line)
        return new_name
    def RenameIfSpecified(self): # new_name (modified) or None
        new_name = self.RenameIfSpecified_Raw()
        return None if new_name is None else (PROGRAM_THIS + "_" + new_name)

def DetectParsingError(window): # -> windowgram, layout, error, linestart, linenumber
    windowgram_lines = window.SplitCleanByKey('windowgram')
    windowgram = Windowgram_Convert.Lines_To_String( windowgram_lines )
    layout, error, linenumber = Windowgram_Convert.String_To_Parsed(windowgram)
    return windowgram, layout, error, window.GetLines('windowgram'), linenumber



##----------------------------------------------------------------------------------------------------------------------
##
## Flex ... Text console and related extensions for tmuxomatic
##
##----------------------------------------------------------------------------------------------------------------------
##
## Planned other:
##
##      again                                       repeat last command (flex recognized, not official)
##      undo                                        stack: undo command
##      redo                                        stack: redo command
##      wipe                                        stack: discard the windowgram modification history (cannot undo)
##      clip                                        stack: discard any commands that had been undone (cannot undo)
##
## Possible non-modifiers:
##
##      links                                       show list of directions
##      link [data...]                              add line to directions
##      unlink <line>                               remove from directions by line number
##      mvlink <line_from> <line_to>                move line in directions
##      duplicate <newname>                         copy current selected window into a new window and select
##      erase <window>                              remove a windowgram from the session (maybe "deletewindow")
##      arguments <command>                         like help but only shows the arguments
##      examples <command>                          like help but only shows the examples
##
## Stack Sketch:
##
##      new                 base
##      scale               base < scale
## ...  mirror              base   scale   scale   break   scale < mirror
## ...  undo                base   scale < scale > break   scale   mirror
##      redo                base   scale   scale < break > scale   mirror
## ...  undo                base < scale > scale   break   scale   mirror
##      break               base   scale < break
## ...  undo                base > scale   break
##      clear               base
##
##      The current element on stack should include arguments, all others show only the command
##
##      Any modification of the windowgram outside of flex will result in a "manual" entry in flex stack
##
## Stack Storage:
##
##      @ FLEX HISTORY : Used by --flex shell, use flex command "clear" to remove, or manually remove these lines
##      @ aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
##      @ aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
##      @ aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
##      @ aaaaaaaaaaaaaaaaaaaaaaaaaa
##
##      Data has initial windowgram, current stack pointer, easily allows any step to be reproduced on demand
##      Data also has version, length, data checksum, current windowgram checksum for detecting manual edits
##      Data is stored between window header and the windowgram as compressed JSON + utf-8 encoded in base64
##      Overwrites entire session file with updated history block for every windowgram modification
##
## Console will be simple text, possibly use ncurses or urwid if it's present (installation is optional like yaml)
## Aliases for commands: "u" = undo.  Include control keys if possible: ^Z = undo, ^Y = redo, ^U = clear, ^D = exit
## Print warnings if common divisors could not be found (within a reasonable range, say up to 120 characters)
## Display / print: clear, windowgram, gap, warnings, stack, gap, menu, gap, prompt
##
##----------------------------------------------------------------------------------------------------------------------

unittestgen_name1 = "unittest"          # Unit testing is activated when user creates a window starting with this name
unittestgen_name2 = "unittest_ignore"   # Or this name
unittestgen_run = 0                     # See notes in flex unit testing
unittestgen_fcl = []                    # Flex Command List
unittestgen_wgp = ""                    # Windowgram Group Pattern
unittestgen_ign = 0                     # Nonzero if "unittest_ignore" was used

##
## Table Printer (used by help and list)
##

def table(output, markers, marklines, title, contents):
    def table_divider(marker, row):
        output.append(marker + "+-" + "-+-".join( [ len(col) * "-" for col in row ] ) + "-+")
    def table_line(marker, row):
        output.append(marker + "| " + " | ".join( [ col for col in row ] ) + " |")
    # Count columns
    columns = 0
    for row in contents:
        if len(row) > columns: columns = len(row)
    # Maximum width of each column, taking into account title and all lines
    widths = [ len(col) for col in title ]
    for line in contents: widths = [ l if l > n else n for l, n in zip( widths, [ len(n) for n in line ] ) ]
    # Pad all lines
    contents.insert( 0, title )
    contents_unpadded = contents
    contents = []
    for line in contents_unpadded:
        contents.append( [ l + ((((w - len(l)) if len(l) < w else 0)) * " ") for w, l in zip( widths, line ) ] )
    if columns:
        first = True
        line = 0
        for row in contents:
            line += 1
            marker = markers[1] if line in marklines else markers[0]
            if first: table_divider( markers[0], row )
            table_line( marker, row )
            if first: table_divider( markers[0], row )
            first = False
        table_divider( markers[0], row )
        output.append("")

##
## Flex: Help
##

@flex(
    command     = "help",
    group       = "helpers",
    description = "Show information for one or more commands",
    insert      = True,
)
def cmd_help_0(fpp_PRIVATE):
    return cmd_help_N( fpp_PRIVATE ) # Wrapper

@flex(
    command     = "help",
    group       = "helpers",
    examples    = [ "help new scale" ],
    aliases     = [ ["?", "help "], ["/", "help "] ],
    insert      = True,
)
def cmd_help_N(fpp_PRIVATE, *commands):
    # Filter specified commands into a list of unique commands, sorted by the official command order
    args = commands
    commands = []
    for arg in args:
        if arg not in commands:
            commands.append(arg)
    commands = [ cmd_dict['about'][0] for cmd_dict in flexmenu_top + flexmenu_bot if cmd_dict['about'][0] in commands ]
    # Macros
    lengths = lambda name, about, usage, example: [ len(name), len(about), len(usage), len(example) ]
    # All menus are four columns representing: name, about, usage, example
    menu_title = [ "Command", "Description", "Usage", "Examples" ]
    menu_lines = [] # Printed columns, not padded
    # Build menu print list from all known commands
    add = lambda name="", about="", usage="", example="": menu_lines.append( [ name, about, usage, example ] )
    for cmd_dict in flexmenu_top + flexmenu_bot:
        if commands and cmd_dict['about'][0] not in commands: continue
        fnew = True
        name, about = cmd_dict['about']
        for usage, examples, arglens in usage_triplets(cmd_dict):
            fuse = True
            if not examples: examples = [ None ] # Allow usage without a corresponding example
            for example in examples: # Add to menu_lines
                if fnew: add()
                add( name if fnew else "", about if fnew else "", usage if fuse else "", example if example else "" )
                fnew = fuse = False
        if fnew:
            add()
            add( name, about )
    add()
    # Spread the description over multiple lines, adding blank lines where necessary
    # Note: Only the about column ("Description") supports word-wrap
    lines = menu_lines
    menu_lines = []
    width = 60
    carry = ""
    for name, about, usage, example in lines:
        def recursive_carry(carry, name, about, usage, example): # carry
            def carry_on(about, carry): # about, carry
                if len(about) > width:
                    hardbreak = width # In the event the max width exceeds a word width
                    for ix in range(width-1, -1, -1):
                        if about[ix] == " " or about[ix] == "\t":
                            hardbreak = ix
                            break
                    if about[hardbreak] == " " or about[hardbreak] == "\t":
                        carry, about = about[hardbreak+1:].strip(), about[:hardbreak].strip()
                else:
                    carry = ""
                return about, carry
            if carry:
                about = carry
                about, carry = carry_on( about, carry )
                add( name, about, usage, example )
                about = ""
                if not name+about+usage+example:
                    # Inserting new lines to list to accommodate a lengthy description
                    return recursive_carry( carry, name, about, usage, example )
                return carry
            about, carry = carry_on( about, carry )
            add( name, about, usage, example )
            return carry
        carry = recursive_carry( carry, name, about, usage, example )
    # Print introduction
    fpp_PRIVATE.flexsense['output'].append( "  Flex menu" + ((" (" + ", ".join(commands) + ")") \
        if len(commands) else "") + ":" )
    fpp_PRIVATE.flexsense['output'].append( "" )
    # Print menu table
    table( fpp_PRIVATE.flexsense['output'], ["    ", "    "], [], menu_title, menu_lines )

##
## Flex: List
##

@flex(
    command     = "list",
    group       = "selectors",
    description = "List all available windows in this tmuxomatic session",
    insert      = True,
)
def cmd_list(fpp_PRIVATE):
    fpp_PRIVATE.flexsense['output'].append( "  Available windows in this session file (use number or name):" )
    fpp_PRIVATE.flexsense['output'].append( "" )
    list_lines = [] # Printed columns, not padded
    for serial in range(1, fpp_PRIVATE.flexmenu_session.Count_Windows()+1):
        number_str = str(serial)
        name = fpp_PRIVATE.flexmenu_session.Get_Name(serial)
        dimensions_int = fpp_PRIVATE.flexmenu_session.Get_WindowgramDimensions_Int(serial) # Avoid reinitialization
        dimensions_str = str(dimensions_int[0]) + "x" + str(dimensions_int[1])
        wg = fpp_PRIVATE.flexmenu_session.Get_Wg( serial )
        used, unused = wg.Panes_GetUsedUnused()
        panecount = str(len(used))
        list_lines.append( [ number_str, dimensions_str, panecount, name ] )
    if not list_lines:
        fpp_PRIVATE.flexsense['output'].append( "    There are no windows, create one with: new <name>" )
        fpp_PRIVATE.flexsense['output'].append( "" )
    else:
        selected = []
        if flexmenu_index[0]: selected.append( flexmenu_index[0] + 1 ) # Skip title line
        list_title = [ "Number", "Dimensions", "Panes", "Name" ]
        table( fpp_PRIVATE.flexsense['output'], ["    ", " -> "], selected, list_title, list_lines )

##
## Flex: Use
##

@flex(
    command     = "use",
    group       = "selectors",
    examples    = [ "use my example", "use 1" ],
    description = "Select the window to use, by either its name or number",
    insert      = True,
)
def cmd_use(fpp_PRIVATE, *name_or_number_REQUIRED):
    global unittestgen_run
    if unittestgen_run: unittestgen_run = 0 # Turn off unit testing mode
    name_or_serial = " ".join(name_or_number_REQUIRED)
    def using(serial):
        flexmenu_index[0] = serial
        wg = fpp_PRIVATE.flexmenu_session.Get_Wg(serial)
        if wg.Analyze_IsBlank():
            fpp_PRIVATE.flexmenu_session.Replace_Windowgram(serial, NEW_WINDOWGRAM)
            wg = fpp_PRIVATE.flexmenu_session.Get_Wg(serial)
            return fpp_PRIVATE.flexsense['notices'].append( FlexWarning( \
                "The windowgram was blank and required initialization" ) )
    if name_or_serial.isdigit():
        serial = int(name_or_serial)
        if fpp_PRIVATE.flexmenu_session.Serial_Is_Valid(serial):
            return using(serial)                                                        # Winow number match
    for serial in range(1, fpp_PRIVATE.flexmenu_session.Count_Windows()+1):
        if name_or_serial == fpp_PRIVATE.flexmenu_session.Get_Name(serial):
            return using(serial)                                                        # Exact window name match
    matches = matched = 0
    for serial in range(1, fpp_PRIVATE.flexmenu_session.Count_Windows()+1):
        if fpp_PRIVATE.flexmenu_session.Get_Name(serial).startswith(name_or_serial):
            matched = serial ; matches += 1
    if matches == 1: return using(matched)                                              # Starting window name match
    if matches:
        return fpp_PRIVATE.flexsense['notices'].append( FlexError( "The name \"" + \
            name_or_serial + "\" is ambiguous (" + str(matches) + " matches)" ) )       # Name ambiguous
    else:
        return fpp_PRIVATE.flexsense['notices'].append( FlexError( \
            "This name or number is invalid: " + name_or_serial ) )                     # No match
    fpp_PRIVATE.flexsense['output'].append( "" )

##
## Flex: New
##

@flex(
    command     = "new",
    group       = "selectors",
    examples    = [ "new some feeds" ],
    description = "Create a new window, initialized to '1'",
    insert      = True,
)
def cmd_new(fpp_PRIVATE, *window_name_REQUIRED):
    global unittestgen_run
    if unittestgen_run: unittestgen_run = 0 # Turn off unit testing mode
    name = " ".join(window_name_REQUIRED)
    for serial in range(1, fpp_PRIVATE.flexmenu_session.Count_Windows()+1):
        if name == fpp_PRIVATE.flexmenu_session.Get_Name(serial):
            return fpp_PRIVATE.flexsense['notices'].append( FlexError( \
                "The name \"" + name + "\" is already in use, try another" ) )
    # Create window
    comments = "## Window added by tmuxomatic flex " + VERSION + "\n\n"
    serial = fpp_PRIVATE.flexmenu_session.Add_Windowgram( comments, name, NEW_WINDOWGRAM )
    # Use it (note that for unit testing, this function clears the flag so it should be run first)
    cmd_use(fpp_PRIVATE, *[str(serial)])
    # Activate unit testing mode if the window name begins with a recognized unit test name
    global unittestgen_ign
    if name.startswith(unittestgen_name1 + " "): unittestgen_run = 1
    if name.startswith(unittestgen_name2 + " "): unittestgen_run = unittestgen_ign = 1

##
## Flex: Print
##

@flex(
    command     = "print",
    group       = "printers",
    description = "Display windowgram (automatic if there is no other output)",
    aliases     = [ [".", "print "], ],
    insert      = True,
)
def cmd_print(fpp_PRIVATE):
    serial = flexmenu_index[0]
    if fpp_PRIVATE.flexmenu_session.Serial_Is_Valid(serial):
        fpp_PRIVATE.flexsense['output'].append( "\n".join([ "    " + l \
            for l in fpp_PRIVATE.flexmenu_session.Get_Windowgram(serial).split("\n") ]) )

##
## Flex: Oops
##

@flex(
    command     = "oops",
    group       = "terminators",
    description = "Restore the original session, then exit without execution",
)
def cmd_oops(fpp_PRIVATE):
    fpp_PRIVATE.flexsense['finished'] = fpp_PRIVATE.flexsense['restore'] = True

##
## Flex: Done
##

@flex(
    command     = "done",
    group       = "terminators",
    description = "Keep changes to session, then execute",
    aliases     = [ ["run", "done"], ["go", "done"] ],
)
def cmd_done(fpp_PRIVATE):
    fpp_PRIVATE.flexsense['finished'] = fpp_PRIVATE.flexsense['execute'] = True

##
## Flex: Exit
##

@flex(
    command     = "exit",
    group       = "terminators",
    description = "Keep changes to session, but do not execute",
    aliases     = [ ["x", "exit"] ],
)
def cmd_exit(fpp_PRIVATE):
    fpp_PRIVATE.flexsense['finished'] = True

##
## Flex Shell
##
## TODO: Support "again" that repeats the last command
##

def flex_shell(session, serial=0):
    ##
    ## Poll dimensions
    ##
    user_wh = [ 0, 0 ]
    def poll_xterm():
        nonlocal user_wh
        user_wh = get_xterm_dimensions_wh()
    poll_xterm()
    ##
    ## Print buffer
    ##
    leftgap = rightgap = 4
    buf = []
    def flexout(l):
        if l is None: buf.append( None )
        elif "\n" in l: return [ flexout(l) for l in l.split("\n") ]
        elif not l.strip(): buf.append( "" ) # Do not print leading spaces if line is blank, unit test compatibility
        else: buf.append( (" " * leftgap) + str(l) )
    def flexout_divider():
        flexout( "-" * ( user_wh[0] - (leftgap + rightgap) ) )
    ##
    ## Session setup
    ##
    flexmenu_session = session
    session_original = copy.deepcopy(session) # Original copy
    fpp = FlexPointersParameter( flexmenu_session, None, copy.deepcopy( flexsense_reset ) )
    ##
    ## Parse all windowgrams to make sure they're valid before entering the flex console
    ## This catches errors like missing a blank line between a windowgram and its directives
    ##
    for window_number, window in enumerate(session.windows, 1):
        _, _, error, linestart, linenumber = DetectParsingError(window)
        if error:
            print("Windowgram parsing error for window number " + str(window_number) + " (on line " + \
                str(linestart+linenumber-1) + "): " + error)
            exit(0)
    ##
    ## Show list of windows, or assign selected window
    ##
    if serial is 0:
        cmd_list(fpp)
    else:
        flexmenu_index[0] = serial
        cmd_use(fpp, *[str(serial)]) # By calling this we assure blank windowgrams are properly initialized
    ##
    ## Easily generate flex unit tests by creating a new window starting with the name "unittest"
    ##
    global unittestgen_run, unittestgen_fcl, unittestgen_wgp
    ##
    ## Input loop
    ##
    warnings = []
    queue = ""
    lastcmd = ""
    sc_support = None
    sc_serial = 0
    split_check = lambda: True \
        if not sc_serial or session.Get_Wg(sc_serial).Analyze_Type(ARGS.relative) == "split" else False
    while True:
        label_w = 12
        labeler = lambda name: name + ( (" "*(label_w-len(name))) if len(name) < label_w else name ) + ": "
        if not flexmenu_session.Serial_Is_Valid(flexmenu_index[0]): flexmenu_index[0] = 0 # Serial is invalid, clear it
        # Macros
        string_to_list = lambda string: [ x.strip() for x in string.strip().split() ]
        filter_input = lambda string: ( string_to_list( string ), " ".join( string_to_list( string ) ) )
        # Multiple commands are expected to be without output
        if fpp.flexsense['output'] and queue:
            fpp.flexsense['notices'].append( FlexError( "Command \"" + lastcmd + "\" had output, " + \
            "commands with output interrupt multiple commands mode" ) )
        # Prepare for new command
        output = fpp.flexsense['output']
        warnings += fpp.flexsense['notices']
        # Check errors
        errors = True if [ 1 for warn in warnings if warn.GetLvl() ] else False
        # Flush queue if an error occurred
        if errors and queue:
            pending = queue.count(";") + (1 if len(queue) else 0)
            # Append to warnings accumulator, note that although this generates an error, there already was one
            warnings.append( FlexError( "Errors occurred, dropping " + str(pending) + \
                " pending command" + ("s" if pending-1 else "") ) )
            queue = ""
        # Poll xterm dimensions before anything is printed using flexout
        poll_xterm()
        # Shell header
        if not queue:
            flexout("")
            flexout("___ _   ___ _ _")
            flexout("__  _   __   _     Flex for tmuxomatic " + VERSION)
            flexout("_   ___ ___ _ _    The object-oriented windowgram editor")
            flexout("")
            flexout_divider()
            flexout("")
            flexout(None) # The fill marker used for later padding to keep header consistently on top
        # Always show windowgram as long as: the command produced no output, and no commands are enqueued
        if not fpp.flexsense['output'] and not queue:
            if unittestgen_run == 1:
                unittestgen_run = 2 # 0 = Not Used / 1 = Initialization Required / 2 = Process Normally
                unittestgen_fcl = []
                unittestgen_wgp = ""
            if unittestgen_run:
                # Print the command-result array in code form for easy implementation
                serial = flexmenu_index[0]
                name = flexmenu_session.Get_Name(serial)
                name_func = "".join(name.split()[1:])
                if not name_func: name_func = "NAMEHERE"
                flexout("def test_" + name_func + "(self): # Created in flex using \"new " + name + "\"")
                flexout("    self.assertFlexSequence( [")
                if unittestgen_fcl:
                    flexout("\n".join([ "        \"" + command + "\"," for command in unittestgen_fcl ]))
                flexout("    ], \"\"\"")
                aftergroup = "    \"\"\" )" if not unittestgen_ign else "    \"\"\", True ) # Ignore notices"
                if unittestgen_wgp:
                    flexout("\n".join([ line for line in unittestgen_wgp.split("\n") ]) + aftergroup)
                else:
                    flexout(aftergroup)
                flexout("")
            else:
                # Print the selected windowgram
                cmd_print(fpp)
        # Show output if there was any
        if fpp.flexsense['output']:
            line = ""
            for line in fpp.flexsense['output']:
                for line in line.split("\n"):
                    flexout(line)
            if line.strip():
                flexout("") # Force extra line at end if it does not exist
        # Divider
        if not queue:
            flexout_divider()
            flexout("")
        # Show warnings (only after queue is exhausted)
        if warnings and not queue:
            for warn in warnings:
                flexout( ( labeler("WARNING") if not warn.GetLvl() else labeler("ERROR") ) + warn.GetMsg() )
            warnings = []
            flexout("")
        # Show short command list in the context of a selection
        commands = flexmenu_grouped['helpers'] + flexmenu_grouped['selectors']
        if flexmenu_index[0]: commands = flexmenu_grouped['helpers'] + flexmenu_grouped['modifiers']
        if not queue:
            flexout(labeler("Quick Menu") + ", ".join(commands))
            flexout("")
        # Show selected window information
        if not queue:
            serial = flexmenu_index[0]
            if not serial:
                flexout( labeler("Window") + "None ... Try \"list\" or \"use <window>\"" )
            else:
                name = flexmenu_session.Get_Name(serial)
                fpp.wg = flexmenu_session.Get_Wg( serial )
                used, unused = fpp.wg.Panes_GetUsedUnused()
                flexout( labeler("Window") + "#" + str(serial) + " (" + name + ")" )
                flexout( labeler("Panes") + used + " < used " + str(len(used)) + " ... " + \
                    str(len(unused)) + " unused > " + unused )
            flexout("")
        # If the windowgram is unsupportable by tmux, the user should know
        # Example: "new unsupported ; break 1 3x3 1 ; join 12 36.2 98.3 74.4"
        if not queue:
            # If window changed, check the new window
            if not flexmenu_index[0]:
                sc_serial = 0
                sc_support = True
            elif sc_serial != flexmenu_index[0]:
                sc_serial = flexmenu_index[0]
                sc_support = split_check()
            # Notify user if window is incompatible with tmux
            if not sc_support:
                flexout( labeler("ATTENTION") + "This windowgram is not compatible with the split mechanics of tmux" )
                flexout("")
        # Display output
        if not queue:
            padding = user_wh[1] - len(buf) # Account for prompt
            if padding < 0: padding = 0
            for l in buf:
                if l is not None: print( l )
                elif padding: print( "\n" * (padding - 1) ) # Ignore otherwise
            buf = []
        # User input
        if not queue:
            try: thisinput_str = input("<<< tmuxomatic flex >>> ")
            except EOFError as e: thisinput_str = "exit" ; print("") # About to exit: print, not flexout
            if unittestgen_run and thisinput_str.strip(): unittestgen_fcl.append( thisinput_str )
            if ";" in thisinput_str: queue = thisinput_str
        if queue:
            thisinput_str, queue = queue.split(";", 1) if ";" in queue else (queue, "")
            queue = " ; ".join( [ cmd.strip() for cmd in queue.split(";") if cmd.strip() ] )
        thisinput_lst, thisinput_str = filter_input( thisinput_str )
        lastcmd = thisinput_lst[0] if len(thisinput_lst) else lastcmd
        # Prepare for new command
        fpp.flexsense = copy.deepcopy( flexsense_reset )
        # Command specified
        if len(thisinput_lst):
            invoked = False
            # Ambiguity handler (repackages input)
            # This corrects the command or alias where possible, and reports ambiguity error otherwise
            # Eliminates the need for the manual entry of short aliases for flex commands
            # For example: "sp" -> "split"
            def AmbiguityMatch(part, whole): # True if part matches with whole[:part]
                if len(part) > len(whole): return False
                return False if [ True for p, w in zip(list(part), list(whole)) if p != w ] else True
            hits = []
            for alias_tup in flexmenu_aliases:
                of = alias_tup[0]
                if AmbiguityMatch( lastcmd, of ): hits.append( of )
            for cmd_dict in flexmenu_top + flexmenu_bot:
                of = cmd_dict['about'][0]
                if AmbiguityMatch( lastcmd, of ): hits.append( of )
            if len(hits) == 1: lastcmd = hits[0]
            elif len(hits) > 1:
                fpp.flexsense['notices'].append( FlexError( "Ambiguous command \"" + lastcmd + "\" has " + \
                    str(len(hits)) + " matches: " + ", ".join(hits) ) )
                continue
            # Alias handler (repackages input)
            # Note that trailing space means duplicate parameters: ["?", "help "] forwards "? use new" to "help use new"
            for alias_tup in flexmenu_aliases:
                if alias_tup[0] == lastcmd:
                    newinput = alias_tup[1]
                    if newinput[-1:] == ' ': newinput += " ".join(thisinput_lst[1:]) # End space == duplicate arguments
                    thisinput_lst, thisinput_str = filter_input( newinput )
                    lastcmd = thisinput_lst[0] if len(thisinput_lst) else lastcmd
                    break
            # Command handler (based on provided arguments and matching function)
            finished = False
            argcount = len(thisinput_lst) - 1
            for cmd_dict in flexmenu_top + flexmenu_bot:
                if cmd_dict['about'][0] == lastcmd:
                    availability = [] # Available arguments if user error: [ [from, to], [from, to], ... ]
                    for ix, triplet in enumerate(usage_triplets(cmd_dict)):
                        usage, examples, arglens = triplet
                        group = cmd_dict['group'][ix]
                        if argcount >= arglens[0] and (argcount <= arglens[1] or arglens[1] == -1):
                            serial = flexmenu_index[0]
                            arguments = []
                            if flexmenu_session.Serial_Is_Valid(serial): fpp.wg = flexmenu_session.Get_Wg(serial)
                            else: fpp.wg = None
                            arguments.append( fpp ) # Now applies to every command
                            if argcount: arguments += thisinput_lst[1:]
                            skip = False
                            if group == "modifiers" and not fpp.wg: # Check wg selection prior to executing modifiers
                                fpp.flexsense['notices'].append( FlexError(
                                    "Please specify a window with `use` or `new`" ) )
                                skip = True
                            if not skip:
                                cmd_dict['funcs'][ix]( *arguments ) # Run this command
                            if fpp.wg is not None:
                                fpp.wg.Disable_Extended() # In case the windowgram was created with mask support
                                flexmenu_session.Replace_Windowgram( serial, fpp.wg.Export_String() )
                            invoked = True
                            if not queue and serial:
                                if unittestgen_run:
                                    windowgramgroup_list = WindowgramGroup_Convert.Pattern_To_List( unittestgen_wgp ) \
                                        + [ flexmenu_session.Get_Wg(serial).Export_String() ]
                                    unittestgen_wgp = WindowgramGroup_Convert.List_To_Pattern( windowgramgroup_list,
                                        FLEXUNIT_MAXWIDTH-leftgap, FLEXUNIT_INDENT-leftgap, FLEXUNIT_SPACE )
                            break
                    if not invoked:
                        # No invocation, could show available parameter counts, but showing help may be more useful
                        fpp.flexsense['notices'].append( FlexError( "Parameter mismatch for valid command \"" + \
                            lastcmd + "\", displaying help instead" ) )
                        cmd_help_N( fpp, lastcmd )
                        finished = True
                    break
            if finished: continue
            # Invalid command handler
            if not invoked:
                # Throw it in the warnings queue as an error and it will flush the queue on the next pass
                fpp.flexsense['notices'].append( FlexError( "Invalid command \"" + lastcmd + "\"" ) )
            # Save if session modified and print next pass
            if session.Modified():
                # TODO: Add to stack if command resulted in a modification
                session.Save()
                sc_support = split_check()
            # Finish handler
            if fpp.flexsense['finished']:
                if fpp.flexsense['restore']:
                    session = session_original
                    session.Save()
                if fpp.flexsense['execute']:
                    return session # Return object in case of restore
                exit()
        # Previous block assumes nothing follows, so it may continue to next command
    ##
    ## Not reached
    ##



##----------------------------------------------------------------------------------------------------------------------
##
## QuerySession class for tmux
##
##      Query tmux, including static queries unrelated to context
##      Session context sensing, determine if running inside or outside session
##
## NOTE: This will break if tmux changes output format
##
##----------------------------------------------------------------------------------------------------------------------

class QuerySession_tmux(object):

    def SessionName(self):
        return self.session_name

    def WindowID(self):
        return self.current_window_id

    def HasWindow(self, check_window_name):
        for window_id, window_name in self.all_windows:
            if window_name == check_window_name:
                return True
        return False

    def HadProblem(self):
        return self.unexpected

    def Inside(self):
        return True if not self.error else False

    def Outside(self):
        return not self.Inside()

    def __init__(self):
        self.error = "Initialization incomplete"
        self.unexpected = False # True if an unexpected error occurred
        self.session_name = None
        self.current_window_id = None
        self.all_windows = None
        self.user_wh = None
        if "TMUX_PANE" in os.environ:
            # We're within tmux ... Find the session and get the list of windows
            sessions = self.tmux_query_sessionnames()
            for session_ent in sessions:
                windows = self.tmux_query_windowidsandnames(session_ent)
                for window_id, window_name in windows:
                    panes = self.tmux_query_paneids(session_ent, window_id)
                    for pane in panes:
                        if pane == os.environ['TMUX_PANE']:
                            self.error = None # Inside tmux and have identified the session, window, pane
                            self.session_name = session_ent
                            self.current_window_id = window_id
                            self.all_windows = windows
                            self.user_wh = self.tmux_get_client_wh() # Get the real xterm dimensions from tmux
                            if not self.user_wh or type(self.user_wh) is not tuple or len(self.user_wh) != 2 \
                            or not self.user_wh[0] or not self.user_wh[1]:
                                self.error = "Could not get the width and/or height of the xterm!"
                                self.unexpected = True
                            return
            self.error = "Unable to locate the corresponding tmux session for the current shell"
            self.unexpected = True
        else:
            self.error = "Not running within a tmux session"

    ##--------------------------------------------------------------------------------------------------------------
    ##
    ## Informational Methods (force=True in case of printonly)
    ##
    ##--------------------------------------------------------------------------------------------------------------

    def tmux_get_client_wh(self): # -> error, (w, h)
        # Gets the actual xterm width height from within a tmux pane, required for proper sizing when adding windows
        result_w = tmux_run( EXE_TMUX + " display -p \"#{client_width}\"", nopipe=False, force=True, real=True )
        result_h = tmux_run( EXE_TMUX + " display -p \"#{client_height}\"", nopipe=False, force=True, real=True )
        try:
            return ( int( result_w.strip().split()[0] ), int( result_h.strip().split()[0] ) )
        except ValueError:
            return ( 0, 0 )

    def tmux_query_sessionnames(self): # -> [ name, name, ... ]
        sessions = []
        result = tmux_run( EXE_TMUX + " list-sessions", nopipe=False, force=True, real=True )
        if result:
            for line in result.split("\n"):
                name = line.split(":", 1)[0]
                if name:
                    sessions.append( name )
        return sessions

    def tmux_query_windowidsandnames(self, session): # -> [ [window_id, window_name], [window_id, window_name], ... ]
        windows = []
        result = tmux_run( EXE_TMUX + " list-windows -t " + session, nopipe=False, force=True, real=True )
        for line in result.split("\n"):
            data = line.strip()
            if data:
                data = line.split(":", 1)
                if len(data) > 1:
                    window_id = data[0].strip()
                    window_name = None
                    match = re.search(r"\(([0-9]+) panes\)", data[1].strip())
                    if match:
                        span = match.span()
                        window_name = data[1].strip()[:span[0]].strip()
                    if window_id and window_name:
                        has_flag = sum([ 1 if window_name.endswith(ch) else 0 for ch in list("*-#!+~") ])
                        if has_flag: window_name = window_name[:-1] # Strip tmux status line flags
                        windows.append( [window_id, window_name] )
        return windows

    def tmux_query_paneids(self, session, window_id): # -> [ id, id, ... ]
        panes = []
        result = tmux_run( EXE_TMUX + " list-panes -t " + session + ":" + window_id,
            nopipe=False, force=True, real=True )
        for line in result.split("\n"):
            data = line.split(" ")
            for elem in line.split(" "):
                if elem and elem[0] == "%":
                    panes.append( elem )
        return panes

    ##--------------------------------------------------------------------------------------------------------------
    ##
    ## Affective Methods (force=False)
    ##
    ##--------------------------------------------------------------------------------------------------------------

    def tmux_destroy_window(self, session, check_window_name): # -> error
        for window_id, window_name in self.all_windows:
            if window_name == check_window_name:
                result = tmux_run( EXE_TMUX + " kill-window -t " + session + ":" + window_id,
                    nopipe=False, force=False, real=True )
                result = result.strip()
                if not result:
                    return None
                return result
        return "Window not found"

    ##--------------------------------------------------------------------------------------------------------------
    ##
    ## Informational Static Methods (force=True)
    ##
    ##--------------------------------------------------------------------------------------------------------------

    @staticmethod
    def static_tmux_base_index_window():
        # This is not used because tmuxomatic references windows by name; function retained in case this changes
        result = tmux_run( EXE_TMUX + " show-option -g base-index", nopipe=False, force=True, real=True )
        if "\n" in result:
            result, _ = result.split("\n", 1)
        label, value = result.split(" ", 1)
        if label == "base-index":
            return int(value)
        return None

    @staticmethod
    def static_tmux_base_index_pane():
        result = tmux_run( EXE_TMUX + " show-window-option -g pane-base-index", nopipe=False, force=True, real=True )
        if "\n" in result:
            result, _ = result.split("\n", 1)
        label, value = result.split(" ", 1)
        if label == "pane-base-index":
            return int(value)
        return None

    ##
    ## A placeholder session must be created when starting a tmux server, or the server will immediately exit.  After
    ## the real session is created, the placeholder can then be destroyed.  An active server is required for many
    ## informational queries, including the pane-base-index query that is needed to create the real session.
    ##
    ## This placeholder is created regardless, as a preemptive measure, in the event that any preexisting sessions may
    ## disappear in the interim, leading to tmux server shutdown.  Such an occurrence could produce a heisenbug.
    ##
    ## A caveat with this technique is that tmuxomatic may crash or exit due to error, resulting in a lingering
    ## placeholder.  The odds of this happening are low, but if it does the placeholder will have a name that's clear
    ## to the user where it came from, and these comments explain why it's there.  Refactoring tmuxomatic to better
    ## handle crashes and exits could include automatic removal of this placeholder.
    ##

    Placeholder = "tmuxomatic_temporary_placeholder"

    @staticmethod
    def static_serverplaceholder_create():
        tmux_run( EXE_TMUX + " new-session -ds " + QuerySession_tmux.Placeholder + " 2>/dev/null",
            nopipe=False, force=True, real=True )

    @staticmethod
    def static_serverplaceholder_destroy():
        tmux_run( EXE_TMUX + " kill-session -t " + QuerySession_tmux.Placeholder,
            nopipe=False, force=True, real=True )



##----------------------------------------------------------------------------------------------------------------------
##
## Processing (session file -> tmux commands)
##
##----------------------------------------------------------------------------------------------------------------------

def tmuxomatic( program_cli, full_cli, user_wh, session_name, session, active_session ):
    """

    Parse session file, build commands, execute.

    """

    # Show configuration
    if ARGS.verbose >= 1:
        print( "" )
        print( "(1) Session   : " + session_name )
        print( "(1) Running   : " + full_cli )
        print( "(1) Xterm     : " + str(user_wh[0]) + "x" + str(user_wh[1]) + " (WxH)" )
        print( "(1) Filename  : " + ARGS.filename )
        print( "(1) Verbose   : " + str(ARGS.verbose) + \
            " (" + ", ".join([ 'summary', 'inputs', 'fitting', 'commands' ][:ARGS.verbose]) + ")" )
        print( "(1) Recreate  : " + str(ARGS.recreate) )
        print( "(1) Noexecute : " + str(ARGS.noexecute) )
        print( "(1) Sizing    : " + [ "Absolute (characters)", "Relative (percentages)" ][ARGS.relative] )

    # Initialize
    list_execution = []         # List of tmux command lists for a session, only executed on successful parsing
    cwd_execution = ""          # Required to set the directory for the first window
    window_serial = 0           # 1+
    window_name = ""            # Set later
    window_names_seen = []      # Assert unique window names (related to issue #8)
    focus_window_name = None    # Use window name rather than window index (supports tmux option: base-index)
    line = ""                   # Loaded line stored here

    #
    # Error reporting
    #
    errpkg = {}
    errpkg['command'] = program_cli
    errpkg['format'] = session.format
    errpkg['line'] = 0

    #
    # Reporting line numbers
    #
    def SetLineNumber(linebase, lineoffset):
        if errpkg['format'] == "shorthand":
            errpkg['line'] = linebase + lineoffset # Exact line (shorthand)
        else:
            errpkg['line'] = linebase # Approximate line (yaml)

    #
    # Make sure tmux server is running before informational queries
    #
    active_session.static_serverplaceholder_create()

    #
    # Get current session base index
    #
    baseindex_pane = active_session.static_tmux_base_index_pane()
    if baseindex_pane is None:
        print("Unable to get pane-base-index from tmux")
        exit(0)

    #
    # Parse session file
    #
    #   Each window:
    #
    #       1 = Initialize window
    #       2 = Windowgram parser
    #       3 = Build list_panes
    #       4 = Directions parser
    #       5 = Generate tmux commands
    #
    eof = False
    window = 0
    line = 0
    for window in session.windows:

        #
        # 1) Initialize window
        #
        title_lines = window.SplitCleanByKey('title')
        line = title_lines[0] if len(title_lines) else ""
        SetLineNumber( window.GetLines('title'), 0 )
        if not line or not is_windowdeclaration(line):
            synerr(errpkg, "Expecting a window section, found nothing")
        window_serial += 1 # 1+
        if window_serial > MAXIMUM_WINDOWS:
            synerr(errpkg, "There's a maximum of " + str(MAXIMUM_WINDOWS) + " windows in this version")
        window_process = line[6:].strip()
        window_name = "" # Window name enclosed in double-quotes
        window_name = "".join( [ ch if ch != '\"' else '\\"' for ch in window_process ] ) # Escape double-quotes
        if not window_name:
            synerr(errpkg, "Window #" + str(window_serial) + " does not have a name")
        for ix, seen_name in enumerate(window_names_seen):
            if window_name == seen_name:
                synerr(errpkg, "Session window names must be unique.  The duplicate name, \"" + window_name + \
                    "\", for window #" + str(window_serial) + ", already used by window #" + str(1+ix))
                break
        window_names_seen.append( window_name )
        if ARGS.verbose >= 2: print("")

        #
        # If adding windows, this window name must be unique
        # No need to check windows added during this process since we're already asserting unique names
        #
        if active_session.Inside():
            if ARGS.printonly: print("### ", end="")
            if active_session.HasWindow( window_name ):
                if ARGS.recreate:
                    print("Recreating window: " + window_name)
                    active_session_name = active_session.session_name # Do not use session_name, that's the input file
                    error = active_session.tmux_destroy_window( active_session_name, window_name )
                    if error:
                        print("  Skipping because of error destroying existing window: " + error)
                        continue
                else:
                    print("Skipping existing: " + window_name)
                    continue
            else:
                print("Adding new window: " + window_name)

        #
        # 2) Windowgram parser
        #
        windowgram, layout, error, linestart, linenumber = DetectParsingError(window)
        wg = Windowgram(windowgram)
        if ARGS.verbose >= 2:
            print( "\n".join([ "(2) Windowgram: " + line for line in wg.Export_Lines() if line ]) )
        if error:
            SetLineNumber( linestart, linenumber - 1 )
            synerr(errpkg, "Windowgram parsing error for window #" + str(window_serial) + ": " + error)
        # For every pane, add an initialized 'l' key that's used later for linking
        for pane in layout.keys(): layout[pane]['l'] = 0

        #
        # 3) Build list_panes
        #
        # Sort t to b, l to r, move into list (layout[] -> list_panes[])
        list_panes, layout = Windowgram_Miscellaneous.SortPanes( layout )
        # Now check for overlaps
        overlap_pane1, overlap_pane2 = Windowgram_Miscellaneous.PaneOverlap( list_panes )
        if overlap_pane1 or overlap_pane2:
            synerr(errpkg, "Overlapping panes: " + overlap_pane1 + " and " + overlap_pane2)

        #
        # 4) Directions parser
        #
        default_directory = "" # Never set a default, assume the path that tmuxomatic was run from
        first_pdl = False # Verbose only
        for ix, line in enumerate(window.SplitCleanByKey('directions')):
            SetLineNumber( window.GetLines('directions'), ix )
            if not line: continue
            if ARGS.verbose >= 2:
                if not first_pdl: print("") ; first_pdl = True
                print("(2) Directions: " + line)
            if command_matches(line, "foc"):
                # Window focus
                focus_window_name = window_name
                continue # Next line
            if command_matches(line[:3], "dir"):
                # Default directory
                if ' ' in line or '\t' in line:
                    # Set or change the default directory.  Applies to successive panes until changed again.
                    values = line.split( None, 1 )
                    default_directory = values[1]
                continue # Next line
            # Splits the line into easier to handle strings, there's probably a better way to do this
            if not ' ' in line and not '\t' in line:
                synerr(errpkg, "Directions line syntax error")
            panedef_paneids, panedef_cmdplusargs = line.split( None, 1 )
            if not ' ' in panedef_cmdplusargs and not '\t' in panedef_cmdplusargs:
                panedef_cmd = panedef_cmdplusargs
                panedef_args = ''
            else:
                panedef_cmd, panedef_args = panedef_cmdplusargs.split( None, 1 )
            #
            # Make the list of targets from the specified panes
            #
            panelist = list(panedef_paneids)
            for paneid in panelist:
                if not paneid in PANE_CHARACTERS:
                    synerr(errpkg, "Directions pane id is outside of the supported range: [0-9a-zA-Z]")
            def into(key, value, mode=0): # 0 = Set, 1 = Set or append if present, 2 = Set or skip if present
                found = []
                for pane in list_panes:
                    if pane['n'] in panelist:
                        if mode == 0:
                            pane[key] = value
                        if mode == 1:
                            if key in pane: pane[key].append( value )
                            else: pane[key] = [value]
                        if mode == 2:
                            if not key in pane or not pane[key]: pane[key] = value
                        found.append( pane['n'] )
                delta = list(set(panelist) - set(found))
                if delta:
                    synerr(errpkg, "Pane(s) '" + "".join(delta) + "' were not specified in the windowgram")
            def all_panes_that_have_key(key):
                found = []
                for pane in list_panes:
                    if pane['n'] in panelist:
                        if key in pane:
                            found += [ pane['n'] ]
                return "".join(found)
            #
            # Target pane specified ... Set default directory if not already set for this pane
            #
            into('dir', default_directory, 2)
            #
            # Command handlers
            #
            if command_matches(panedef_cmd, "run"):
                if not panedef_args: synerr(errpkg, "Directions command 'run' must have arguments")
                into('run', panedef_args, 1)
            elif command_matches(panedef_cmd, "dir"):
                if not panedef_args: synerr(errpkg, "Directions command 'dir' must have arguments")
                into('dir', panedef_args)
            elif command_matches(panedef_cmd, "foc"):
                if panedef_args: synerr(errpkg, "Directions command 'foc' must have no arguments")
                panes = all_panes_that_have_key('foc')
                if panes: synerr(errpkg, "Directions command 'foc' already specified for panes: " + panes)
                into('foc', True)
            else:
                synerr(errpkg, "Unknown command '" + panedef_cmd + "'")

        #
        # 5) Generate tmux commands ... After splitting and cross-referencing
        #

        #
        # 5.1) Refine list_panes so all expected variables are present for cleaner reference
        #
        for pane in list_panes:
            if not 'dir' in pane: pane['dir'] = default_directory
            if not 'run' in pane: pane['run'] = [ "" ]
            if not 'foc' in pane: pane['foc'] = False

        #
        # 5.2) Split window into panes
        #
        if ARGS.verbose >= 3:
            print("")
            print("(3) Fitting panes = {")
        sw = { 'print': print, 'verbose': ARGS.verbose, 'relative': ARGS.relative, 'scanline': DEBUG_SCANLINE } # Print
        list_split, list_links = SplitProcessor( sw, wg, user_wh[0], user_wh[1], list_panes )
        if ARGS.verbose >= 3:
            print("(3) }")

        #
        # 5.3) Build the execution list for: a) creating windows, b) sizing panes, c) running commands
        #
        list_build = []     # Window is independently assembled

        #
        # Target fix for tmux 2.1 (not a problem with 2.0 or 2.2)
        #
        # When calling tmuxomatic from within tmux (managerless mode), the following tmux commands do not select
        # windows and/or panes as they do in other tmux versions.
        #
        #       send-keys
        #       split-window
        #       select-pane
        #
        # Fortunately this is easily fixed by explicitly declaring window name and pane number on these commands.  This
        # fix would probably work for all versions of tmux, but doing so would take significantly more command space.
        # In the interest of performance, these changes are only applied when tmux 2.1 is used.
        #
        tgtfix = True if USERS_TMUX == "2.1" else False
        ewpo = lambda wp: ("-t:\"" + window_name + "\"." + wp + " ") if tgtfix else ""  # Explicit Window Pane Optional
        ewpi = lambda wp: (("-t:\"" + window_name + "\"." + wp) if tgtfix else ("-t " + wp))             # EWP Imposed

        #
        # 5.3a) Create window panes by splitting windows
        #
        first_pane = True
        for split in list_split:
            #
            # Readability
            #
            list_split_linkid = split['linkid']     # 1234          This is for cross-referencing
            list_split_orient = split['split']      # "v" / "h"     Successive: Split vertical or horizontal
            list_split_paneid = split['tmux']       # 0             Successive: Pane split at time of split
            list_split_inst_w = split['inst_w']     # w             Successive: Ensuing window size in chars
            list_split_inst_h = split['inst_h']     # h             Successive: Ensuing window size in chars
            list_split_percnt = split['per']        # 50.0          Successive: Percentage at time of split
            ent_panes = ''
            for i in list_panes:
                if 'l' in i and i['l'] == list_split_linkid:
                    ent_panes = i
                    break
            if not ent_panes:
                SetLineNumber( window.GetLines('windowgram'), 0 )
                synerr(errpkg,
                    "Unable to fully cross-link.  This is because of an unsupported window layout.  See the " + \
                    "included example file `session_unsupported` for more information on what layouts are and " + \
                    "aren't possible in tmux.  If you use flex to generate windowgrams, it will notify you as soon " + \
                    "as you create a pane layout that is not supported by tmux.  For more information, look up the " + \
                    "clean split rule in the tmuxomatic documentation.")
            list_panes_dir = ent_panes['dir']       # "/tmp"        Directory of pane
            if list_panes_dir: adddir = " -c " + list_panes_dir
            else: adddir = ""
            #
            # Add the commands for this split
            #
            if first_pane: # First
                first_pane = False
                if window_serial == 1 and active_session.Outside():
                    # First pane of first window (if not adding windows to existing session)
                    # The shell's cwd must be set, the only other way to do this is to discard the
                    # window that is automatically created when calling "new-session".
                    cwd_execution = ("cd " + list_panes_dir) if list_panes_dir else ""
                    list_build.append( "new-session -d -s " + session_name + " -n \"" + window_name + "\"" )
                    # Normally, tmux automatically renames windows based on whatever is running in the focused pane.
                    # There are two ways to fix this.  1) Add "set-option -g allow-rename off" to your ".tmux.conf".
                    # 2) Add "export DISABLE_AUTO_TITLE=true" to your shell's run commands file (e.g., ".bashrc").
                    # Here we automatically do method 1 for the user, unless the user requests otherwise.
                    list_build.append( "set-option -t " + session_name + " quiet on" )
                    renaming = [ "off", "on" ][ARGS.renaming]
                    list_build.append( "set-option -t " + session_name + " allow-rename " + renaming )
                    list_build.append( "set-option -t " + session_name + " automatic-rename " + renaming )
                else:
                    # First pane of successive window (or first window if adding to existing session)
                    list_build.append( "new-window -n \"" + window_name + "\"" + adddir )
            else: # Successive
                window_pane = str(baseindex_pane + list_split_paneid)
                window_pane_n = str(baseindex_pane + list_split_paneid + 1) # The new pane
                # Perform the split on this pane
                list_build.append( "select-pane " + ewpi(window_pane) )
                # Pane sizing
                if ARGS.relative:
                    # Relative pane sizing (percentage)
                    percentage = str( int( float( list_split_percnt ) ) ) # Integers are required by tmux 1.8
                    list_build.append( "split-window " + ewpo(window_pane) + "-" + list_split_orient + \
                        " -p " + percentage + adddir )
                else:
                    # Absolute pane sizing (characters)
                    if list_split_orient == 'v': addaxis = " -y " + str( list_split_inst_h )
                    else: addaxis = " -x " + str( list_split_inst_w )
                    list_build.append( "split-window " + ewpo(window_pane) + "-" + list_split_orient + adddir )
                    list_build.append( "resize-pane " + ewpi(window_pane_n) + " " + addaxis )

        #
        # 5.3b) Prepare shell commands ... This is done separately after the pane size has been established
        #
        for ent_panes in list_panes:
            # Now that the tmux pane index correlates, cross-reference for easier lookups
            list_panes_l = ent_panes['l']           # 1234          This is for cross-referencing
            ent_panes['tmux'] = str([tup[1] for tup in list_links if tup[0] == list_panes_l][0])
        focus_actual_tmux_pane_index = str(baseindex_pane) # Default pane_index
        for ent_panes in list_panes:
            #
            # Readability
            #
            list_panes_l = ent_panes['l']           # 1234          This is for cross-referencing
            list_panes_run = ent_panes['run']       # ["cd", "ls"]  Commands to run on pane
            list_panes_foc = ent_panes['foc']       # True          Determines if pane is in focus
            list_panes_index = str( baseindex_pane + int(ent_panes['tmux']) )
            #
            # Run
            #
            if list_panes_run:
                for run in list_panes_run:
                    clean_run = re.sub(r'([\"])', r'\\\1', run) # Escape double-quotes
                    if clean_run:
                        window_pane = list_panes_index
                        list_build.append( "select-pane " + ewpi(window_pane) )
                        list_build.append( "send-keys " + ewpo(window_pane) + "\"" + clean_run + "\" C-m" )
            if not focus_actual_tmux_pane_index or list_panes_foc:
                focus_actual_tmux_pane_index = list_panes_index
        if focus_actual_tmux_pane_index:
            window_pane = focus_actual_tmux_pane_index
            list_build.append( "select-pane " + ewpi(window_pane) )

        #
        # 5.4) Add this batch to the main execution list to be run later
        #
        list_execution.append( list_build )

    #
    # Set default window
    #
    if focus_window_name is not None:
        list_build = []
        list_build.append( "select-window -t \"" + focus_window_name + "\"" )
        list_execution.append( list_build )

    #
    # Notify user that tmux execution will begin and allow for time to break (ARGS.verbose >= 1)
    #
    if ARGS.verbose >= 1:
        print("")
        if VERBOSE_WAIT != 0:
            print("(1) Waiting " + str(VERBOSE_WAIT) + " seconds before running tmux commands...")
            time.sleep(VERBOSE_WAIT)
        print("(1) Running tmux commands...")
        print("")

    #
    # Switch back to the user's pane if this is being run in an existing session
    #
    switch_back = ""
    if active_session.Inside():
        switch_back = "select-window -t " + active_session.WindowID()

    #
    # Run the tmux commands
    #
    # 2.19: Optimized to run commands with as few executable calls as possible.  This was necessary to support window
    # addition, as one command at a time showed the user the build in process (not ideal).  If there's a way for tmux
    # to suspend the client during the execution of commands, it should be added here.  Even with such a feature, the
    # batching will be retained because it should be faster.
    #
    # Note: tmux command limitations necessitate multiple batches.  Batching requires: tracking and preserving window
    # and pane focus, starting each batch by returning to the previous focus, and (in addition mode) switching back to
    # the user's window at the end of each batch.
    #
    # As of tmux 2.1, the command length was changed from 2048 (COMMAND_LENGTH) to 16384 (MAX_IMSGSIZE).  The length
    # used here will stay at 2048 for now.  This note is for future reference in case a higher limit is preferred.
    #
    batch_len = 2048        # Limitation of 2048 bytes for tmux 1.8 ("command too long" if exceeded)
    last_window = ""        # Recent "new-window" (changed to "select-window" on save)
    last_pane = ""          # Recent "select-pane" (unmodified)
    list_commands = [ cmd for cmdlist in list_execution for cmd in cmdlist ]
    semicolon = " \; "
    switch_back = semicolon + switch_back
    batch = ""
    def execute(batch, switch_back):
        if batch:
            batch += switch_back
            error = tmux_run( ( ( cwd_execution + " ; " ) if cwd_execution else "" ) + ( EXE_TMUX + " " + batch ) )
            if error:
                if "pane too small" in error:
                    errpkg['quiet'] = True
                    msg = "Window splitting error (pane too small), make your window larger and try again"
                else:
                    msg = "An error occurred in tmux: " + error
                synerr(errpkg, msg)
    for cmd in list_commands:
        # Make sure command fits if it's the only command in this tmux batch .... V command goes here
        req = len(last_window) + len(semicolon) + len(last_pane) + len(semicolon) + len(switch_back)
        if len(cmd) > batch_len - req:
            synerr(errpkg,
                "The command length ({}) exceeds maximum length available ({}) in a tmux message ({}): {}".format(
                    len(cmd), batch_len - req, batch_len, cmd))
        restart = False
        if not batch:
            restart = True
        else:
            batchlet = semicolon + cmd
            if len(batch + batchlet + switch_back) < batch_len:
                batch += batchlet
            else:
                execute(batch, switch_back)
                restart = True
        if restart:
            batch = ""
            def addcmd(cmd):
                nonlocal batch
                batch += (semicolon if batch else "") + cmd
            if last_window:
                addcmd(last_window)
                if last_pane:
                    addcmd(last_pane)
            addcmd(cmd)
        if cmd.startswith("new-window"):
            last_window = "select-window -t " + qsplit(cmd)[2] # Supports window names with spaces
            last_pane = ""
        if cmd.startswith("select-pane"):
            last_pane = cmd
    execute(batch, switch_back) # Execute whatever is left

    #
    # Clean up placeholder before entering session
    #
    active_session.static_serverplaceholder_destroy()

    #
    # Attach to the newly created session
    #
    if active_session.Outside():
        tmux_run( EXE_TMUX + " attach-session -t " + session_name )

    #
    # Let the user know we're done with addition
    #
    if active_session.Inside():
        if ARGS.printonly: print("### ", end="")
        print("Finished!")



##----------------------------------------------------------------------------------------------------------------------
##
## Main (tmuxomatic)
##
##----------------------------------------------------------------------------------------------------------------------

def main():

    # Verify pane count
    if MAXIMUM_PANES != 62 or len(PANE_CHARACTERS) != MAXIMUM_PANES:
        print("Pane count does not match")
        exit(0)

    # Check tmux version (req = required, rep = reported)
    tmux_req = MINIMUM_TMUX
    tmux_cli, tmux_rep = tmux_version()
    if tmux_cli != "tmux" or not tmux_rep:
        print("The tmux executable cannot be found")
        exit(0)
    if not satisfies_minimum_version( tmux_req, tmux_rep ):
        print("This version of tmuxomatic requires tmux " + tmux_req + " or higher, found tmux " + tmux_rep)
        exit(0)
    global USERS_TMUX
    USERS_TMUX = tmux_rep

    # Settings
    program_cli = sys.argv[0]                   # Program cli: "./tmuxomatic"
    user_wh = get_xterm_dimensions_wh()         # Screen dimensions

    # Constrain arguments
    ancillary = False # Used with printonly and scale, to skip over the main tmuxomatic functionality
    ARGS.verbose = int(ARGS.verbose or 0)
    if ARGS.verbose > VERBOSE_MAX: ARGS.verbose = VERBOSE_MAX
    elif ARGS.printonly:                        # Overrides for --printonly
        ancillary = True
        ARGS.noexecute = False
        ARGS.verbose = 0

    # If using flex and a serial was specified
    serial = 0
    if ARGS.flex and ":" in ARGS.filename:
        ARGS.filename, serial = ARGS.filename.split(":", 1)
        if not serial.isdigit():
            print("You specified a flex window number that does not make sense: " + serial)
            exit(0)
        serial = int(serial)

    # Check for presence of specified session filename
    if not os.path.exists(ARGS.filename):
        if ARGS.flex:
            f = open(ARGS.filename, 'w')
            line = "##" + "-" * 78
            f.write( line + "\n##\n## Session file created by tmuxomatic flex " + VERSION + "\n##\n" + line + "\n\n" )
            f.close() # Required for proper updating on first new window
        else:
            print("The specified session file does not exist: " + ARGS.filename)
            exit(0)

    # Make sure the session file is not unexpectedly large (say the user accidentally specified a binary file)
    if 2**20 < os.stat(ARGS.filename).st_size:
        print("The specified session exceeds 1 megabyte, that's nearly 1 megabyte more than expected.")
        exit(0)

    # Session name in tmux is always derived from the filename (pathname is dropped to avoid confusion)
    filename_only = ARGS.filename[ARGS.filename.rfind('/')+1:] # Get the filename only (drop the pathname)
    session_name = PROGRAM_THIS + "_" + filename_only # Session name with the executable name as a prefix
    session_name = re.sub(r'([/])', r'_', session_name) # In case of session path: replace '/' with '_'
    session_name = re.sub(r'\_\_+', r'_', session_name) # Replace two or more consecutive underscores with one

    # Load session file
    session = SessionFile( ARGS.filename )
    session.Load()
    new_name = session.RenameIfSpecified()
    if new_name is not None: session_name = new_name

    #
    # Unit testing required before entering flex
    #
    if ARGS.tests:
        print("Running unit tests, please wait...")
        error = Flex_UnitTests()
        if error:
            print("\nUnit Test Failure:\n" + error)
            exit()

    # Flex shell entry
    if ARGS.flex:
        session = flex_shell( session, serial )
        # Force reload of session file in order to get accurate line counts in the event of changes by user in flex
        session.Load()

    # No defined windows check
    if not len(session.windows):
        print("This session has no defined windows")
        exit()

    #
    # Execution of tmux commands depends on context:
    #
    #   Executed within tmux .... Append windows to existing session and drop back to shell with relevant information
    #   Executed outside tmux ... Create new tmux session from scratch and handle it accordingly (classic behavior)
    #

    # Set up query session object
    active_session = QuerySession_tmux()
    if active_session.HadProblem():
        print("Query session object unexpected error: " + active_session.error)
        exit(0)
    if active_session.Inside():
        # Copy the real xterm dimensions obtained from tmux, required for correct sizing
        user_wh = active_session.user_wh

    # Optional kill session on disconnect
    def destroy():
        if ARGS.destroy:
            tmux_run( EXE_TMUX + " kill-session -t " + session_name, nopipe=True, force=True, real=True )

    # Existing session handler (skipped when printing or scaling)
    if not ancillary and active_session.Outside():
        # Detect existing session
        result = tmux_run( EXE_TMUX + " has-session -t " + session_name, nopipe=False, force=True, real=True )
        if not result:
            # Handle existing session
            if ARGS.recreate:
                # Destroy existing session (optional)
                print("Destroying running session, \"" + session_name + "\"...")
                tmux_run( EXE_TMUX + " kill-session -t " + session_name, nopipe=False, force=False, real=True )
            else:
                # Attach existing session
                print("Attaching running session, \"" + session_name + "\"...")
                try:
                    tmux_run( EXE_TMUX + " attach-session -t " + session_name, nopipe=True, force=False, real=True )
                except KeyboardInterrupt: # User disconnected
                    destroy()
                exit(0)

    # If printing, display header
    if ARGS.printonly:
        print("###")
        print("### Session \"" + session_name + "\"")
        print("### Generated by tmuxomatic for static configurations")
        print("### Using screen dimensions: " + str(user_wh[0]) + "x" + str(user_wh[1]) + " (WxH)")
        print("###")

    # Process session: generates a new session and attaches, or prints, or scales
    if not ancillary:
        if active_session.Inside():
            print("Adding windows from the session \"" + session_name + "\" to the running session \"" + \
                active_session.SessionName() + "\"...")
            print("IMPORTANT: Do not change focus of the pane or window until finished!")
        else:
            print("Running new session, \"" + session_name + "\"...")
    try:
        tmuxomatic( program_cli, " ".join(sys.argv), user_wh, session_name, session, active_session )
    except KeyboardInterrupt: # User disconnected
        destroy()
    exit(0)



##----------------------------------------------------------------------------------------------------------------------
##
## Main (python)
##
##----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Signal handlers
    signal.signal(signal.SIGINT, signal_handler_break)  # SIGINT (user break)
    signal.signal(signal.SIGHUP, signal_handler_hup)    # SIGHUP (user disconnect)

    # Argument deprecations
    for arg in sys.argv[1:]:
        dep = [ [ "Argument " + arg + " removed in version " + version + ": " + reason ] \
            for version, reason, commands in [
            [ "1.0.20", "Absolute positioning enabled by default", [ "-a", "--absolute" ] ],
            [ "2.0",    "Use --flex to scale your windowgrams",    [ "-s", "--scale" ] ],
            [ "2.0",    "Use --flex for windowgram modification",  [ "-w", "--scale-replace" ] ],
            ] if arg in commands ]
        if dep:
            print("!!! " + dep[0][0])
            skip = True
    if 'skip' in vars() and skip is True:
        print("Exiting...")
        exit()

    # Argument parser
    PARSER = argparse.ArgumentParser( description=\
        "The easiest way to define sessions in tmux! ... Visit the official site for an introduction and " + \
        "example sessions ... " + HOMEPAGE,
        epilog="Official site ... " + HOMEPAGE )
    PARSER.add_argument( "-V", "--version", action="version", version=PROGRAM_THIS + " " + VERSION, help=\
        "Show the version number and exit" )
    PARSER.add_argument( "-v", "--verbose", action="count", help=\
        "Increase the verbosity level, up to " + str(VERBOSE_MAX) + " (-" + (VERBOSE_MAX * 'v') + ")" )
    PARSER.add_argument( "-n", "--renaming", action="store_true", help=\
        "Let tmux automatically rename the windows" )
    PARSER.add_argument( "-p", "--printonly", action="store_true", help=\
        "Print only the tmux commands, then exit" )
    PARSER.add_argument( "-x", "--noexecute", action="store_true", help=\
        "Do everything except issue commands to tmux" )
    PARSER.add_argument( "-F", "--files", action="store_true", help=\
        "List PyPI session examples and documentation, then exit" )
    PARSER.add_argument( "-t", "--tests", action="store_true", help=\
        "Perform all unit tests.  Execution will proceed as normal " + \
        "unless unit tests fail." )
    PARSER.add_argument( "-r", "--recreate", action="store_true", help=\
        "If the session exists, it will be destroyed then recreated.  " + \
        "Normally, if it exists, tmuxomatic will reattach to it.  If " + \
        "used in managerless mode, windows that exist by name will " + \
        "be destroyed then recreated, rather than skipped." )
    PARSER.add_argument( "-d", "--destroy", action="store_true", help=\
        "When you disconnect, your session will be destroyed.  This " + \
        "is useful in situations where you don't want to consume " + \
        "resources when you're not 'plugged in'.  This option has no " + \
        "effect in managerless mode." )
    PARSER.add_argument( "-f", "--flex", action="store_true", help=\
        "Enter the flex console.  Type 'help' for a list of commands.  " + \
        "Flex is a powerful windowgram editor that allows you to " + \
        "create or modify your windowgrams using visually oriented " + \
        "commands (scale, break, etc).  If you know which window " + \
        "you'll edit, add \":<number>\" after the filename." )
    PARSER.add_argument( "filename", help=\
        "The tmuxomatic session filename (required)" )
    ARGS = PARSER.parse_args()

    # Only absolute placement is supported in this version, relative placement could be useful for programs like weechat
    ARGS.relative = False

    # List the PyPI installed example session files on request
    if ARGS.files:
        print("")
        from distutils import sysconfig
        basepath = os.path.join( sysconfig.get_python_lib(), "tmuxomatic" )
        allfiles = []
        for root, _, files in os.walk(basepath):
            allfiles += [ os.path.join(root, f) for f in files ]
        if allfiles:
            print("Found {} files accompanying the PyPI installation of tmuxomatic:".format(len(allfiles)))
            print("")
            for f in allfiles:
                print("  " + f)
        else:
            print("Unable to find a PyPI installation of tmuxomatic")
            print("")
            print("  To install tmuxomatic from PyPI, run 'pip3 install tmuxomatic'")
            print("  Visit the official site for documentation and example files")
            print("  " + HOMEPAGE)
        print("")
        exit(0)

    # Locate tmux
    EXE_TMUX = which( EXE_TMUX )
    if not EXE_TMUX:
        print("This requires tmux to be installed on your system...")
        print("If it's already installed, update your $PATH, or set EXE_TMUX in the source to an absolute filename...")
        exit(0)

    # Run tmuxomatic ... A separate function was needed to quiet pylint (local variable scope)
    main()



