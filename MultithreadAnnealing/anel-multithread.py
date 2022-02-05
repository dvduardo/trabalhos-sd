import threading
import time


class thread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.acordado = False
        self.finalizado = False
        self.texto = ''
        self.proximo = None

    def setProximo(self, proximo):
        self.proximo = proximo

    def run(self):
        print(f'Thread {self.id} - Iniciada')

        while not self.finalizado:
            if not self.acordado:
                time.sleep(1)
            else:
                find = False
                for i in range(0, len(self.texto)):
                    if self.texto[i].islower():
                        find = True
                        self.texto = self.texto[:i] + self.texto[i].upper() + self.texto[i + 1:]
                        break

                if find:
                    print(f'im #{self.id} --- {self.texto}')
                    self.acordado = False
                    self.proximo.acordaProximo(self.texto)
                else:
                    self.finalizado = True

        self.proximo.finalizado = True
        print(f'Thread {self.id} - Finalizando')

    def acordaProximo(self, texto):
        self.texto = texto
        self.acordado = True


class Anel:
    def __init__(self, x):
        self.threads = [thread(i) for i in range(0, x)]
        for i in range(0, x-1):
            self.threads[i].setProximo(self.threads[i+1])
        self.threads[x-1].setProximo(self.threads[0])

    def inicia(self, texto):
        for t in self.threads:
            t.start()
        self.threads[0].acordaProximo(texto)


def main():
    aneis = int(input('Digite a quantidade de anel para a thread:\n'))
    anel = Anel(aneis)

    texto = input('Digite um texto:\n')

    anel.inicia(texto)


main()
