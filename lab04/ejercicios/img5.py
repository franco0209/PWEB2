from chessPictures import *
from interpreter import draw

squareN=square.negative()
figureDoble=square.join(squareN)
ima4=figureDoble.horizontalRepeat(3)
ima5=ima4.verticalMirror()
draw(ima5)

