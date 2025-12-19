class Producto():
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
        print(f"Producto creado: {nombre} ${precio}")