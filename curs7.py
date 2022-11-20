numar = 3

try:
    assert numar % 2 == 0, "pacat"

except AssertionError as e:
    print(e)
from abc import abstractmethod


# ---------------------------------
def masina ():
    try:
        numar_roti = int(input('Introdu numarul de roti'))
    except ValueError:
        print('Nu este numar')
    culoare = None
    try:
        return numar_roti
    except UnboundLocalError:
        print('Numar roti este gol')
masina()
try:
    if masina() == 3:
        print('masina are 3 roti')
except:
#
# # -------------------------------Mostenire
class om:#superclasa
    def __init__(self, inaltime, greutate, culoare_ochi):
        self.inaltime = inaltime
        self.greutate = greutate
        self.culoare_ochi = culoare_ochi
    __tip_vestimentatie = 'Elegant'#vizibil doar in clasa om (incapsulare)
ion = om(180,80,'caprui')

class elev(om):
    def __init__(self, inaltime, greutate, culoare_ochi, clasa):
        super().__init__(inaltime, greutate, culoare_ochi)
        self.clasa = clasa
    def invata(self):
        print('Eu invat matematica')


class elev_absolvent(elev):
    def __init__(self, inaltime, greutate, culoare_ochi, clasa):
        super().__init__(inaltime, greutate, culoare_ochi, clasa)
    def invata(self):
        print('Eu invat fizica avansata')

elev1 = elev(120,50,'caprui',12)
elev2 = elev_absolvent(130,60,'caprui',12)
elev1.invata()
elev2.invata()

# ---------------------------------------
class figura_geometrica():
    @abstractmethod
    def defineste_forma(self):
        raise NotImplementedError

    @abstractmethod
    def stabileste_perimetrul(self):
        raise NotImplementedError


class patrat(figura_geometrica):
    def defineste_forma(self):
        numar_laturi = input('Introdu numarul laturilor')

patrat1 = patrat()
patrat1.defineste_forma()
patrat2 = figura_geometrica() # eroare deoarece face apel la clasa abstracta care nu este definita
patrat2.defineste_forma()
patrat2.stabileste_perimetrul()