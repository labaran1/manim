r"""SVG 1.1 Colors

This module contains the colors defined in the SVG 1.1 specification, which are commonly
accessed as named colors in LaTeX via the ``\usepackage[svgnames]{xcolor}`` package.

To use the colors from this list, access them directly from the module (which
is exposed to Manim's global name space):

.. code:: pycon

    >>> from manim import SVGNAMES
    >>> SVGNAMES.LIGHTCORAL
    ManimColor('#EF7F7F')

List of Color Constants
-----------------------

These hex values are derived from those specified in the ``xcolor`` package
documentation (see https://ctan.org/pkg/xcolor):

.. automanimcolormodule:: manim.utils.color.SVGNAMES

"""

from __future__ import annotations

from .core import ManimColor

ALICEBLUE = ManimColor("#EFF7FF")
ANTIQUEWHITE = ManimColor("#F9EAD7")
AQUA = ManimColor("#00FFFF")
AQUAMARINE = ManimColor("#7EFFD3")
AZURE = ManimColor("#EFFFFF")
BEIGE = ManimColor("#F4F4DC")
BISQUE = ManimColor("#FFE3C4")
BLACK = ManimColor("#000000")
BLANCHEDALMOND = ManimColor("#FFEACD")
BLUE = ManimColor("#0000FF")
BLUEVIOLET = ManimColor("#892BE2")
BROWN = ManimColor("#A52A2A")
BURLYWOOD = ManimColor("#DDB787")
CADETBLUE = ManimColor("#5E9EA0")
CHARTREUSE = ManimColor("#7EFF00")
CHOCOLATE = ManimColor("#D2681D")
CORAL = ManimColor("#FF7E4F")
CORNFLOWERBLUE = ManimColor("#6395ED")
CORNSILK = ManimColor("#FFF7DC")
CRIMSON = ManimColor("#DC143B")
CYAN = ManimColor("#00FFFF")
DARKBLUE = ManimColor("#00008A")
DARKCYAN = ManimColor("#008A8A")
DARKGOLDENROD = ManimColor("#B7850B")
DARKGRAY = ManimColor("#A9A9A9")
DARKGREEN = ManimColor("#006300")
DARKGREY = ManimColor("#A9A9A9")
DARKKHAKI = ManimColor("#BCB66B")
DARKMAGENTA = ManimColor("#8A008A")
DARKOLIVEGREEN = ManimColor("#546B2F")
DARKORANGE = ManimColor("#FF8C00")
DARKORCHID = ManimColor("#9931CC")
DARKRED = ManimColor("#8A0000")
DARKSALMON = ManimColor("#E8967A")
DARKSEAGREEN = ManimColor("#8EBB8E")
DARKSLATEBLUE = ManimColor("#483D8A")
DARKSLATEGRAY = ManimColor("#2F4F4F")
DARKSLATEGREY = ManimColor("#2F4F4F")
DARKTURQUOISE = ManimColor("#00CED1")
DARKVIOLET = ManimColor("#9300D3")
DEEPPINK = ManimColor("#FF1492")
DEEPSKYBLUE = ManimColor("#00BFFF")
DIMGRAY = ManimColor("#686868")
DIMGREY = ManimColor("#686868")
DODGERBLUE = ManimColor("#1D90FF")
FIREBRICK = ManimColor("#B12121")
FLORALWHITE = ManimColor("#FFF9EF")
FORESTGREEN = ManimColor("#218A21")
FUCHSIA = ManimColor("#FF00FF")
GAINSBORO = ManimColor("#DCDCDC")
GHOSTWHITE = ManimColor("#F7F7FF")
GOLD = ManimColor("#FFD700")
GOLDENROD = ManimColor("#DAA51F")
GRAY = ManimColor("#7F7F7F")
GREEN = ManimColor("#007F00")
GREENYELLOW = ManimColor("#ADFF2F")
GREY = ManimColor("#7F7F7F")
HONEYDEW = ManimColor("#EFFFEF")
HOTPINK = ManimColor("#FF68B3")
INDIANRED = ManimColor("#CD5B5B")
INDIGO = ManimColor("#4A0082")
IVORY = ManimColor("#FFFFEF")
KHAKI = ManimColor("#EFE58C")
LAVENDER = ManimColor("#E5E5F9")
LAVENDERBLUSH = ManimColor("#FFEFF4")
LAWNGREEN = ManimColor("#7CFC00")
LEMONCHIFFON = ManimColor("#FFF9CD")
LIGHTBLUE = ManimColor("#ADD8E5")
LIGHTCORAL = ManimColor("#EF7F7F")
LIGHTCYAN = ManimColor("#E0FFFF")
LIGHTGOLDENROD = ManimColor("#EDDD82")
LIGHTGOLDENRODYELLOW = ManimColor("#F9F9D2")
LIGHTGRAY = ManimColor("#D3D3D3")
LIGHTGREEN = ManimColor("#90ED90")
LIGHTGREY = ManimColor("#D3D3D3")
LIGHTPINK = ManimColor("#FFB5C0")
LIGHTSALMON = ManimColor("#FFA07A")
LIGHTSEAGREEN = ManimColor("#1FB1AA")
LIGHTSKYBLUE = ManimColor("#87CEF9")
LIGHTSLATEBLUE = ManimColor("#8470FF")
LIGHTSLATEGRAY = ManimColor("#778799")
LIGHTSLATEGREY = ManimColor("#778799")
LIGHTSTEELBLUE = ManimColor("#AFC4DD")
LIGHTYELLOW = ManimColor("#FFFFE0")
LIME = ManimColor("#00FF00")
LIMEGREEN = ManimColor("#31CD31")
LINEN = ManimColor("#F9EFE5")
MAGENTA = ManimColor("#FF00FF")
MAROON = ManimColor("#7F0000")
MEDIUMAQUAMARINE = ManimColor("#66CDAA")
MEDIUMBLUE = ManimColor("#0000CD")
MEDIUMORCHID = ManimColor("#BA54D3")
MEDIUMPURPLE = ManimColor("#9270DB")
MEDIUMSEAGREEN = ManimColor("#3BB271")
MEDIUMSLATEBLUE = ManimColor("#7B68ED")
MEDIUMSPRINGGREEN = ManimColor("#00F99A")
MEDIUMTURQUOISE = ManimColor("#48D1CC")
MEDIUMVIOLETRED = ManimColor("#C61584")
MIDNIGHTBLUE = ManimColor("#181870")
MINTCREAM = ManimColor("#F4FFF9")
MISTYROSE = ManimColor("#FFE3E1")
MOCCASIN = ManimColor("#FFE3B5")
NAVAJOWHITE = ManimColor("#FFDDAD")
NAVY = ManimColor("#00007F")
NAVYBLUE = ManimColor("#00007F")
OLDLACE = ManimColor("#FCF4E5")
OLIVE = ManimColor("#7F7F00")
OLIVEDRAB = ManimColor("#6B8D22")
ORANGE = ManimColor("#FFA500")
ORANGERED = ManimColor("#FF4400")
ORCHID = ManimColor("#DA70D6")
PALEGOLDENROD = ManimColor("#EDE8AA")
PALEGREEN = ManimColor("#97FB97")
PALETURQUOISE = ManimColor("#AFEDED")
PALEVIOLETRED = ManimColor("#DB7092")
PAPAYAWHIP = ManimColor("#FFEED4")
PEACHPUFF = ManimColor("#FFDAB8")
PERU = ManimColor("#CD843F")
PINK = ManimColor("#FFBFCA")
PLUM = ManimColor("#DDA0DD")
POWDERBLUE = ManimColor("#AFE0E5")
PURPLE = ManimColor("#7F007F")
RED = ManimColor("#FF0000")
ROSYBROWN = ManimColor("#BB8E8E")
ROYALBLUE = ManimColor("#4168E1")
SADDLEBROWN = ManimColor("#8A4413")
SALMON = ManimColor("#F97F72")
SANDYBROWN = ManimColor("#F3A45F")
SEAGREEN = ManimColor("#2D8A56")
SEASHELL = ManimColor("#FFF4ED")
SIENNA = ManimColor("#A0512C")
SILVER = ManimColor("#BFBFBF")
SKYBLUE = ManimColor("#87CEEA")
SLATEBLUE = ManimColor("#6959CD")
SLATEGRAY = ManimColor("#707F90")
SLATEGREY = ManimColor("#707F90")
SNOW = ManimColor("#FFF9F9")
SPRINGGREEN = ManimColor("#00FF7E")
STEELBLUE = ManimColor("#4682B3")
TAN = ManimColor("#D2B38C")
TEAL = ManimColor("#007F7F")
THISTLE = ManimColor("#D8BFD8")
TOMATO = ManimColor("#FF6347")
TURQUOISE = ManimColor("#3FE0CF")
VIOLET = ManimColor("#ED82ED")
VIOLETRED = ManimColor("#D01F90")
WHEAT = ManimColor("#F4DDB2")
WHITE = ManimColor("#FFFFFF")
WHITESMOKE = ManimColor("#F4F4F4")
YELLOW = ManimColor("#FFFF00")
YELLOWGREEN = ManimColor("#9ACD30")
