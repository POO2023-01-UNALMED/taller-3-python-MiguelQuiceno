class TV:
    __numTV = 0
    #Metodo de clase para aumentar el numero de televisores
    @classmethod
    def aumentarNumTV(cls):
        cls.__numTV += 1


    def __init__(self, marca, estado):
        self.__marca = marca
        self.__estado = estado
        self.__canal = 1
        self.__precio = 500
        self.__volumen = 1
        self.__control = None
        self.aumentarNumTV()

    def setMarca(self, marca):
        self.__marca = marca
    def setControl(self, control):
        self.__control = control
    def setPrecio(self, precio):
        self.__precio = precio
    def setVolumen(self,volumen):
        if 0 <= volumen <= 7 and self.__estado == True:
            self.__volumen = volumen 
    def setCanal(self,canal):
        if 1 <= canal <=120 and self.__estado == True:
            self.__canal = canal
    

    def getMarca(self):
        return self.__marca
    def getControl(self):
        return self.__control
    def getPrecio(self):
        return self.__precio
    def getVolumen(self):
        return self.__volumen
    def getCanal(self):
        return self.__canal
    def getEstado(self):
        return self.__estado  
    def turnOn(self):
        self.__estado = True
    def turnOff(self):
        self.__estado = False
    def canalUp(self):
        if (self.__canal + 1 <= 120) and (self.__estado == True):
            self.__canal += 1
    def canalDown(self):
        if (self.__canal - 1 >= 1) and (self.__estado == True):
            self.__canal -= 1
    def volumenUp(self):
        if (self.__volumen + 1 <= 7) and (self.__estado == True):
            self.__volumen += 1
    def volumenDown(self):
        if (self.__volumen - 1 >= 0) and (self.__estado == True):
            self.__volumen -= 1
    @classmethod
    def getNumTV(cls):
        return cls.__numTV  
    @classmethod
    def setNumTV(cls,numTV):
        cls.__numTV = numTV