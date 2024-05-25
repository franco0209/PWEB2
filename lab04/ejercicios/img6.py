from chessPictures import *
from interpreter import draw

squareN=square.negative()
figureDoble=square.join(squareN)
ima4=figureDoble.horizontalRepeat(3)
ima5=ima4.verticalMirror()
ima45=ima5.up(ima4)
ima6=ima45.up(ima45)
draw(ima6)
