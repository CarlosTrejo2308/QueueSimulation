import random
import enum

class Evento(enum):
    def __init__(self):
        self.tiempo = 0
        self.tipoEvento = 0
        

class listaEventos:
    def obtenerEventoInminente(self):
        pass
    
    def agregarEveneto(self):
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
    
    

        
        """
        reloj = 0.0 #va a ser en minutos
        num_llegadas = 0 #numero de llegadas
        t_llegada = 0 (gen_int_arr()) #tiempo de llegada
        t_salida = 0.0 #tiempo de salida
        suma_salidas = 0 "#suma de tiempo de servicios ofrecidos por quien este atendiendo
        estado = 0 
        t_total_espera = 0 #tiempo total de espera
        en_fila = 0 #total de cosas que esperan en la fila
        contador_fila = 0 #total de personas que estuvieron formadas
        tot_servido = 0 #el total de cosas que fueron servidas por el servidor 
        
        #ya deberia de haber quedado listo lo de inicializar
        """