'''
Created on 2 feb. 2017

@author: iri_m_000
'''
import unittest
from BilleteraVirtual import*

class Test(unittest.TestCase):
    
    
    def setUp(self):
       self.identificador = 333
       self.nombre = pepe
       self.apellido = perez
       self.ci = 4567
       self.pin = 1234
       self.saldo = 200 

    def testvirificarInicializacion(self):
        self.failUnlessEqual(self.identificador, 333)
        self.failUnlessEqual(self.nombre, pepe)
        self.failUnlessEqual(self.apellido, perez)
        self.failUnlessEqual(self.ci, 4567)
        self.failUnlessEqual(self.pin, 1234)
        self.failUnlessEqual(self.saldo, 200)
        
    def testSaldo(self):
        self.failUnlessEqual(saldo(self), 200)
    
    def testRecarga(self):
        saldo = 300
        lugar = 1342
        recargar(saldo, lugar)
        self.failUnlessEqual(saldo(self), 500)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()