class Tv:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumentar_canal(self):
        if self.ligada:
            self.canal += 1

    def diminuir_canal(self):
        if self.ligada:
            self.canal -= 1


print(__name__)

if __name__ == '__main__':
    tv = Tv()
    print('Televisão está ligada: {}'.format(tv.ligada))
    tv.power()
    print('Televisão está ligada: {}'.format(tv.ligada))
    tv.power()
    print('Televisão está ligada: {}'.format(tv.ligada))
