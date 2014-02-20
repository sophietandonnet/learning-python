class Fila:
    '''Fila is a queue, i.e, the first element to go in is the first element to go out.

    Fila has 4 methods:
    - adicionar: add one element to the end of the queue
    - remover: remove the first element from the queue
    - espiar: See the first element of the queue
    - vazia: returns True is the queue is empty, False otherwise'''

    def __init__(self):
        self.fila = []
    
    def __str__(self):
        return 'object is queue not string. Use print(your_queue.fila)'

    def adicionar(self, element):
        self.fila += [element]
    
    def remover(self):
        self.fila = self.fila[1:]
    
    def espiar(self):
        return self.fila[0]
        
    def vazia(self):
        return not self.fila
        
us = Fila()
us.adicionar('Tassio')
us.adicionar('Sophie')
print(us)
print(us.espiar())
print(us.fila)
us.remover()
print(us.espiar())
print(us.vazia())
us.remover()
print(us.vazia())


