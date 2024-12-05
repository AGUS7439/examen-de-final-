# clase Usuario uso con encapsulamiento
class Usuario:
    def __init__(self, nombre, ID):
        self.__nombre = nombre  # atributo encapsulado
        self.__ID = ID
        self.__cuentaActiva = True

    def buscar_autor(self, autor, catalogo):
        return catalogo.buscar_libros_por_autor(autor)

    def get_nombre(self):
        return self.__nombre


# clase catálogo
class Catalogo:
    def __init__(self):
        self.lista_libros = []

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)

    def buscar_libros_por_autor(self, autor):
        # manejo de errores
        try:
            return [libro for libro in self.lista_libros if libro.autor == autor and libro.disponible]
        except Exception as e:
            print(f"Error al buscar libros: {e}")
            return []


# clase libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True


# clase de préstamo con polimorfismo
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fechaInicio = None
        self.fechaFin = None

    def registrar_prestamo(self):
        if self.libro.disponible:
            self.libro.disponible = False
            print(f"Préstamo registrado para {self.usuario.get_nombre()} con el libro '{self.libro.titulo}'")
        else:
            print("El libro no está disponible.")


# el uso de herencia
class UsuarioVIP(Usuario):
    def __init__(self, nombre, ID, nivelVIP):
        super().__init__(nombre, ID)
        self.nivelVIP = nivelVIP


# ejemplos de uso para el libro 
if __name__ == "__main__":
    
    
    catalogo = Catalogo()
    libro1 = Libro("El Quijote", "Miguel de Cervantes")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
    catalogo.agregar_libro(libro1)
    catalogo.agregar_libro(libro2)
    
    usuario = Usuario("Gustavo", 1)
    libros_encontrados = usuario.buscar_autor("Miguel de Cervantes", catalogo)
    print("Libros encontrados:")
    print([libro.titulo for libro in libros_encontrados])

    prestamo = Prestamo(usuario, libro1)
    prestamo.registrar_prestamo()
