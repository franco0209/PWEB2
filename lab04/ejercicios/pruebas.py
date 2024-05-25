from chessPictures import *
from interpreter import draw

# Obtener el cuadrado con colores invertidos
figure=rock
figure2=king
figure1 = figure.up(figure2)
#figure1=knight
# Dibujar el cuadrado con colores invertidos
#draw(bishop_inverted)
#draw(bishop)
draw(figure1)
