import random
import enum

class Evento(enum):
    Llegada = 1
    Salida = 2

class listaEventos:
    def obtenerEventoInminente(self):
        pass

class simulacion():
    def __init__(self, semilla) -> None:
        self.tiempoMedioEntreLlegadas = 4.5
        self.tiempoMedioServicio = 3.5
        self.SIGMA = 0.6
        self.clientesTotales = 100

        random = random.Random(semilla)
        self.listaDeEventos = listaEventos()
        self.clientes = []

        self.inicializar()


    def inicializar(self):
        pass

    def run(self):
        while(self.numeroDeSalidas < self.clientesTotales):
            evento = self.listaDeEventos.obtenerEventoInminente()
            reloj = evento.obtenerTiempo()

            if(evento.obtenerTipo() == Evento.Llegada):
                self.procesoLlegada()
            else:
                self.procesoSalida()

        self.generarReporte()


    def inicializar():
        pass

    def procesoLlegada(self):
        pass

    def procesoSalida(self):
        pass

    def generarReporte(self):
        pass


def main():
    semilla = 12345
    simulacion = simulacion(semilla)
    simulacion.run()

if __name__ == "__main__":
    main()