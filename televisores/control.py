class Control:
#atributos :p
    __tv = 0
#metodos xd
    def turnOn(self):
        self.__tv.turnOn()
    def turnOff(self):
        self.__tv.turnOff()
    def canalUp(self):
        self.__tv.canalUp()
    def canalDown(self):
        self.__tv.canalDown()
    def volumenDown(self):
        self.__tv.volumenDown()
    def volumenUp(self):
        self.__tv.volumenUp()
    def setCanal(self, canal):
        self.__tv.setCanal(canal)
    

    def enlazar(self,tv):
        self.__tv = tv
        tv.setControl(self)

    @classmethod
    def setTv(cls,tv):
        cls.__tv = tv
    @classmethod    
    def getTv(cls):
        return cls.__tv
    
