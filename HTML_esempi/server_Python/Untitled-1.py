print('Ciao raga!')
print(__name__)
import io
import math
sen = math.sin
print(sen(math.pi/2))
import cmath as cx
qa = cx.sqrt(-1)
print(qa)
import sqlite3 as sq
import datetime
class pippo:
    scarpa=123
    def allaccia(self):
        self.scarpa = self.scarpa + 1
anio = pippo()
print(anio.scarpa)
anio.allaccia()
print(anio.scarpa)
print(pippo.scarpa)