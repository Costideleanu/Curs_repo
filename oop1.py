class Masina:
    culoare = None
    roti = None
    tractiune = None
    forma = None


    def putere(self):
        if self.tractiune == 4:
            print('Puterea creste cu 50 de cai.')

object = Masina()
object.tractiune = 4
object.putere()

class Floare:
    petale = 4
    culoare = "Rosie"
    inaltime = 5

# Acesta este constructor
    def __init__(self, a, b):  #initializarea clasei
        self.culoare = a
        self.inaltime = b

    def verifica_floarea(self):
        if self.culoare == 'Rosie':
            print('Floarea este trandafir')
        elif self.culoare == 'Galben':
            print('Floarea este galbena')

    def verifica_inaltimea(self):
        if not self.inaltime == 0:
            print('floarea este vie')
        else:
            print('Floarea este moarta')
            return True

