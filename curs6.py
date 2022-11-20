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