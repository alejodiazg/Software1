'''
Created on 2 feb. 2017

@author: iri_m_000
'''
import unittest
from BilleteraVirtual import BilleteraVirtual as bv

class Test(unittest.TestCase):
    
    
    def setUp(self):
        self.identificador = 333
        self.nombre = 'pepe'
        self.apellido = 'perez'
        self.ci = 4567
        self.pin = 1234
        self.billetera = bv(self.identificador , self.nombre , self.apellido, self.ci ,self.pin)

    def testVerificarInicializacion(self):
        self.failUnlessEqual(self.billetera.identificador, 333)
        self.failUnlessEqual(self.billetera.nombres, 'pepe')
        self.failUnlessEqual(self.billetera.apellidos, 'perez')
        self.failUnlessEqual(self.billetera.ci, 4567)
        self.failUnlessEqual(self.billetera.pin, 1234)
        self.failUnlessEqual(self.billetera.saldo(), 0.0)
        
    
    def testRecarga(self):
        saldo = 300
        lugar = 1342
        self.billetera.recargar(saldo, lugar)
        self.failUnlessEqual(self.billetera.saldo(), 300)
        
        #prueba con una recarga de 0 
        try:
            self.billetera.recargar(0 , lugar)
        except ValueError:
            #se hace fallar el codigo para probar si maneja el problema correctamente
            self.failUnlessEqual(self.billetera.saldo(), 300)
        
        #se verifica otra vez luego de la falla 
        self.failUnlessEqual(self.billetera.saldo(), 300)
        
        #prueba con numeros negativos
        try:
            self.billetera.recargar(-100 , lugar)
        except ValueError:
            #se hace fallar el codigo para probar si maneja el problema correctamente
            self.failUnlessEqual(self.billetera.saldo(), 300)
        
        #se verifica otra vez luego de la falla 
        self.failUnlessEqual(self.billetera.saldo(), 300)
        
        #se prueba que maneje bien pasarle menos parametros
        try:
            self.billetera.recargar(-100)
        except ValueError:
            #se hace fallar el codigo para probar si maneja el problema correctamente
            self.failUnlessEqual(self.billetera.saldo(), 300)
        
        #se verifica otra vez luego de la falla 
        self.failUnlessEqual(self.billetera.saldo(), 300)
        
    def testConsumir(self):
        lugar = 1342
        
        self.billetera.recargar(300 , lugar)
        #probar pin incorrecto
        try:
            self.billetera.consumir(100 , lugar , 0000)    
        except ValueError:
            self.failUnlessEqual(self.billetera.saldo(), 300)

        self.failUnlessEqual(self.billetera.saldo(), 300)
        
        #probar parametros faltantes
        try:
            self.billetera.consumir(100 , lugar)    
        except ValueError:
            self.failUnlessEqual(self.billetera.saldo(), 300)

        self.failUnlessEqual(self.billetera.saldo(), 300)
        
        #probar consumo negativo
        try:
            self.billetera.consumir(-100 , lugar , 1234)    
        except ValueError:
            self.failUnlessEqual(self.billetera.saldo(), 300)
        
        #probar consumo 0
        try:
            self.billetera.consumir(0 , lugar , 1234)    
        except ValueError:
            self.failUnlessEqual(self.billetera.saldo(), 300)

        self.failUnlessEqual(self.billetera.saldo(), 300)

        #probar consumo mayor a balance 
        try:
            self.billetera.consumir(10000 , lugar , 1234)    
        except ValueError:
            self.failUnlessEqual(self.billetera.saldo(), 300)


        self.failUnlessEqual(self.billetera.saldo(), 300)
        
        #probar consumo menor al balance
        self.billetera.consumir(200 , lugar , 1234)
        self.failUnlessEqual(self.billetera.saldo(), 100)
        
        #probar consumo igual al balance
        self.billetera.consumir(100 , lugar , 1234)
        self.failUnlessEqual(self.billetera.saldo(), 0)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()