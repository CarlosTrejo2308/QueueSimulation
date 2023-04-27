import random
from enum import Enum

class Evento:
    def __init__(self):
        self.tiempo = 0
        self.tipoEvento = TipoEvento.Llegada

    def obtenerTiempo(self):
        pass

    def obtenerTipo(self):
        pass

class TipoEvento(Enum):
    Llegada = 1
    Salida = 2

class listaEventos:
    def obtenerEventoInminente(self):
        pass

class Simulacion():
    def __init__(self, semilla) -> None:
        self.tiempoMedioEntreLlegadas = 4.5
        self.tiempoMedioServicio = 3.5
        self.SIGMA = 0.6
        self.clientesTotales = 100

        random.Random(semilla)
        self.listaDeEventos = listaEventos()
        self.clientes = []

        self.inicializar()


    # Agendar llegadas de clientes de forma aleatoria, llenar la lista de eventos
    def inicializar(self):
        self.numeroDeSalidas = 0

    def run(self):
        while(self.numeroDeSalidas < self.clientesTotales):
            evento = self.listaDeEventos.obtenerEventoInminente()
            reloj = evento.obtenerTiempo()

            if(evento.obtenerTipo() == Evento.Llegada):
                self.procesoLlegada()
            else:
                self.procesoSalida()

        self.generarReporte()

    def procesoLlegada(self):
        pass

    def procesoSalida(self):
        pass

    def generarReporte(self):
        pass


def main():
    semilla = 12345
    simulacion = Simulacion(semilla)
    simulacion.run()

if __name__ == "__main__":
    main()