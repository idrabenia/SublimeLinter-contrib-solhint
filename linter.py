"""This module exports the Solhint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Solhint(NodeLinter):
    """Solhint class delegate call to solhint tool and return result back."""

    syntax = 'solidity'
    cmd = 'solhint -f visualstudio @'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = (
        r'^.+?\((?P<line>\d+),(?P<col>\d+)\): '
        r'(.?(?P<warning>warning)|(?P<error>error)).+?'
        r':(?P<message>.+)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = 'solidity'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
