from chessPictures import *
from interpreter import draw

squareN=square.negative()
squares2=square.join(squareN)
row=squares2.horizontalRepeat(3)
rowN=row.negative()
rows4=(rowN.up(row)).verticalRepeat(1)

midPieces1=(rock.join(knight)).join(bishop)
midPieces2=(bishop.join(knight)).join(rock)
midPieces=midPieces1.join(queen).join(king).join(midPieces2)
pawns=pawn.horizontalRepeat(7)
pawnsT=row.under(pawns)
midPiecesT=rowN.under(midPieces)

#BLANCAS
whites=midPiecesT.up(pawnsT)
#NEGRAS
blacks=(pawnsT.up(midPiecesT)).negative()

final=whites.up(rows4).up(blacks)
draw(final)

