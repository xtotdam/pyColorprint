import sys

__author__ = 'xtotdam'

_esc = chr(0x1b)
_colors = {
    'none': 0,
    'red': 196,
    'orange': 214,
    'yellow': 226,
    'green': 46,
    'cyan': 51,
    'lightblue': 68,
    'blue': 21,
    'purple': 129,
    'pink': 201,
    'white': 15,
    'grey': 242,
    'black': 232
}


def color_print_name(text='  ', tone='white', bg='black', end=''):
    """
Return colored text, with colors - strings from _colors dict

    :type text: str
    :param text: text to color
    :type tone: str
    :param tone: color of text
    :type bg: str
    :param bg: color of text background
    :type end: str
    :param end: end of string
    :rtype: string
    :return: colored text
    """
    if sys.platform.startswith('win'):
        return text + end
    else:
        return _esc + '[01;38;05;{:02d};48;05;{:02d}m'.format(_colors[tone], _colors[bg]) + text + _esc + '[00m' + end


def color_print_num(text='  ', tone=15, bg=None, end=''):
    """
Returns colored text, colors are color numbers from weird escape sequences

    :type text str
    :param text: text to color
    :type tone: int
    :param tone: color of text
    :type bg: int
    :param bg: color of background
    :type end: str
    :param end: end of string
    :rtype: string
    :return: colored text
    """
    if sys.platform.startswith('win'):
        return text + end
    else:
        if bg:
            return _esc + '[01;38;05;{:02d};48;05;{:02d}m'.format(tone, bg) + text + _esc + '[00m' + end
        else:
            return _esc + '[01;38;05;{:02d}m'.format(tone) + text + _esc + '[00m' + end


def test():
    if sys.platform.startswith('win'):
        raise NotImplementedError('Sorry, Windows - colors not implemented yet')
    else:
        for key in _colors.keys():
            print clrprint(bg=key)
