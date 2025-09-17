# Defino la clase EventoDeportivo que representa un evento individual
# Agrego constructor
# Asigno los valores recibidos a los atributos de objeto
class EventoDeportivo:
    def __init__(self, nombre, fecha, tipo_evento, estado):
        self.nombre = nombre
        self.fecha = fecha
        self.tipo_evento = tipo_evento
        self.estado = estado

    # Método especial que define cómo se muestra el objeto cuando lo imprimimos
    # Retorno una cadena con todos los datos del evento 
    def __str__(self):
        return f"{self.nombre} - {self.fecha} - {self.tipo_evento} - {self.estado}"
    
# Defino la clase SistemaEventos que maneja todos los eventos
# Creo lista vacía para guardar todos los eventos    
class SistemaEventos:
    def __init__(self):
        self.eventos = []

    # Método para registrar un evento nuevo
    # Creo un nuevo objeto EventoDeportivo con los datos recibidos
    def registrar_evento(self, nombre, fecha, tipo_evento, estado):
        evento = EventoDeportivo(nombre, fecha, tipo_evento, estado)
        self.eventos.append(evento)
        print(f"Evento registrado: {evento}")

    # Método para mostrar todos los eventos registrados
    # Verifico si la lista está vacía
    # Salgo del método si no hay eventos
    def listar_eventos(self):
        if not self.eventos:
            print("No hay eventos registrados")
            return
        
        # Si hay eventos, los mostramos
        # Enumerate nos da tanto el índice como el objeto en cada iteración
        # Empieza a contar desde 1
        # Muestra cada evento con su número
        print("Lista de eventos:")
        for i, evento in enumerate(self.eventos, 1):
            print(f"{i}. {evento}")

# Función principal del programa (fuera de las clases)
def main():
        sistema = SistemaEventos()

        while True:
            print("\n1. Registrar evento")
            print("2. Listar eventos")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Nombre del evento: ")
                fecha = input("Fecha: ")
                tipo_evento = input("Tipo de evento: ")
                estado = input("Estado: ")
                sistema.registrar_evento(nombre, fecha, tipo_evento, estado)

            elif opcion == "2":
                sistema.listar_eventos()

            elif opcion == "3":
                break

            else:
                print("Opción inválida")

if __name__ == "__main__":
    main()