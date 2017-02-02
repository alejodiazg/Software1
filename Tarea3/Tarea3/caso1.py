'''
Created on 2 feb. 2017

@author: iri_m_000
'''
import unittest
from datetime import datetime as dt
from Tarea3 import BilleteraVirtual
from Tarea3.BilleteraVirtual import BilleteraVirtual

class Test(unittest.TestCase):
    
    
    def setUp(self):
        self.bi = BilleteraVirtual(333,'pepe','perez', 4567,1234 )

    def testvirificarInicializacion(self):
        self.assertEqual(self.bi.identificador, 333)
        self.assertEqual(self.bi.nombres, 'pepe')
        self.assertEqual(self.bi.apellidos, 'perez')
        self.assertEqual(self.bi.ci, 4567)
        self.assertEqual(self.bi.pin, 1234)
        self.assertEqual(self.bi.saldo, 0)
        
    def testSaldo(self):
        m = self.bi.saldo()
        self.assertEqual(m, 200)
    
    def testRecargaEfectiva(self):
        saldo = 300
        lugar = 1342
        self.bi.recargar(saldo, lugar)
        m = self.bi.saldo()
        self.failUnlessEqual(m, 500)
        
    def testRecargaNegativa(self):
        saldo = -3
        lugar = 1342
        self.failUnlessEqual(self.bi.recargar(saldo, lugar),ValueError('Recarga debe ser positiva'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()