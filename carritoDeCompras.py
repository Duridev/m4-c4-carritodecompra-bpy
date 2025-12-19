class Producto():
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
        print(f"Producto creado: {nombre} ${precio}")
        
    #===GETTERS
    def get_nombre(self):
        return self.__nombre
    
    def fet_precio(self):
        return self.__precio
    
    #===SETTERS
    def set_nombre(self, new_name):
        self.__nombre = new_name
        
    def set_precio(self, new_price):
        if new_price > 0:
            self.__precio = new_price
        else:
            print("Precio debe ser mayor a 0")