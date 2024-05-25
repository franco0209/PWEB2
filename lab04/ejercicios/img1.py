from chessPictures import *
from interpreter import draw
blackKn=knight.negative()
figureUp =knight.join(blackKn)
figureDown=blackKn.join(knight)
ima1=figureDown.up(figureUp)
draw(ima1)

