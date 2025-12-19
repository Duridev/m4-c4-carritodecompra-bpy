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
            
    def mostrar(self):
        print(f"Producto: {self.get_nombre()}, {self.get_precio()}")
        
#===================================================================

class Carrito():
    def __init__(self, dueno):
        self.dueno = dueno
        self.productos = []
        print("Carrito creado para ", dueno)


    #===GETTERS
    def get_dueno(self):
        return self.__dueno
    
    def get_productos(self):
        return self.get_producto
    
    #===SETTERS
    def set_dueno(self, nuevo_dueno):
        self.__dueno = nuevo_dueno
        
    #agregar_producto(producto): agrega un producto al carrito
    
    def agregar_producto(self, producto):
        self.__productos.append(producto)
        print(f"Se ha agregado el producto {producto.get_nombre()} a su carrito")
        
    #mostrar_producto(): muestra todos los productos en el carrito
    def mostrar_productos(self):
        for item in self.get_productos():
            item.mostrar()
            
    #calcular total
    def calcular_total(self):
        precio_total=0
        for item in self.productos():
            precio_total+=item.get_precio()
        return precio_total
    
#=============================================================

p1=Producto("Leche", 999)
p2=Producto("Queso", 2500)
p3=Producto("Cereales", 1250)
p4=Producto("Café", 2500)

carro1 = Carrito("Juan")
carro2 = Carrito("Pepa")

carro1.agregar_producto(p1)
carro1.agregar_producto(p2)
carro1.mostrar_productos()
print("Valor Total carro1: ", carro1.calcular_total() )

carro2.agregar_producto(p3)
carro2.agregar_producto(p4)
carro2.mostrar_productos()
print("Valor Total carro2: ", carro2.calcular_total() )
