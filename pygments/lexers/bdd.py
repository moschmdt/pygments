"""
    pygments.lexers.bdd
    ~~~~~~~~~~~~~~~~~~~~~

    Lexer for BDD(Behavior-driven development). 
    More information: https://en.wikipedia.org/wiki/Behavior-driven_development

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, include
from pygments.token import Comment, Keyword, Name, String, Number, Text, Punctuation, Whitespace

__all__ = ['BddLexer']

class BddLexer(RegexLexer):
    """
    Lexer for BDD(Behavior-driven development), which highlights not only keywords, 
    but also comments, punctuations, strings, numbers, and variables.

    .. versionadded:: 2.10
    """

    name = 'Bdd'
    aliases = ['bdd']
    filenames = ['*.feature']
    mimetypes = ['text/x-bdd']

    step_keywords = r'Given|When|Then|Add|And|Feature|Scenario Outline|Scenario|Background|Examples|But'

    tokens = {
        'comments': [
            (r'^\s*#.*$', Comment),
        ],
        'miscellaneous': [
            (r'(<|>|\[|\]|=|\||:|\(|\)|\{|\}|,|\.|;|-|_|\$)', Punctuation),
            (r'((?<=\<)[^\\>]+(?=\>))', Name.Variable),
            (r'"([^\"]*)"', String),
            (r'^@\S+', Name.Label),
        ],
        'numbers': [
            (r'(\d+\.?\d*|\d*\.\d+)([eE][+-]?[0-9]+)?', Number),
        ],
        'root': [
            (r'\n|\s+', Whitespace),
            (step_keywords, Keyword),
            include('comments'),
            include('miscellaneous'),
            include('numbers'),            
            (r'\S+', Text),
        ]
    }