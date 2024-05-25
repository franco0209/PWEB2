from chessPictures import *
from interpreter import draw
blackKn=knight.negative()
blackKnRY=blackKn.verticalMirror()
figureUp =knight.join(blackKn)
figureDown=blackKnRY.join(knight)
ima1=figureDown.up(figureUp)
draw(ima1)

