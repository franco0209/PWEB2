from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return Picture(vertical)


  def horizontalMirror2(self):
    """ devuelve el espejo horizontal de la imagen """
    mirrored_image = []
    i=len(self.img)-1
    while i>=0:
       mirrored_image.append(self.img[i])
       i-=1       
    return Picture(mirrored_image)

  def negative(self):
        """ devuelve un negativo de la imagen """
        inverted_img = []
        for row in self.img:
            inverted_row = ''
            for color in row:
                inverted_color = self._invColor(color)
                inverted_row += inverted_color
            inverted_img.append(inverted_row)
        return Picture(inverted_img)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    actual=self.img
    derecho=p.img
    final=[]
    for i in range(len(actual)):
       fila=""+actual[i]+derecho[i]
       final.append(fila)
    return Picture(final)

  def up(self, p):
    actual=self.img
    encima=p.img
    final=[]
    for i in range(len(encima)):
       final.append(encima[i])
    for i in range(len(actual)):
       final.append(actual[i])
    return Picture(final)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    actual=self.img
    encima=p.img
    final=[]
    for i in range(len(actual)):
       fila=[]
       for j in range(len(actual[i])):
          if encima[i][j]!=" ":
             fila.append(encima[i][j])
          else:
             fila.append(actual[i][j])
       final.append(fila)
    return Picture(final)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    actual=self.img
    final=Picture(actual)
    for i in range(n):
       final=final.join(self)
    return final

  def verticalRepeat(self, n):
    actual=self.img
    final=Picture(actual)
    for i in range(n):
       final=final.up(self)
    return final
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

