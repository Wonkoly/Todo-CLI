class Cola:
    
    def __init__(self):
        self.elementos = []
        
    def encolar(self, item):
        self.elementos.append(item)
        
    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            raise IndexError("Desencolar de una cola vacia")
        
    def esta_vacia(self):
        return len(self.elementos) == 0
    
cola = Cola()
cola.encolar("item1")
cola.encolar("item2")
cola.encolar("item3")

print(f"Elemento desencolado: {cola.desencolar()}")

