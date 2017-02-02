'''
Created on Feb 2, 2017

@author: Alejandro
'''

from datetime import datetime as dt

class BilleteraVirtual(object):
    '''
    classdocs
    '''


    def __init__(self, identificador , nombres , apellidos , ci , pin):
        '''
        Constructor
        '''
        self.identificador = identificador
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.pin = pin
        self.saldo = 0
        self.recargas = []
        self.consumos = []
    
    def saldo(self):
        return self.saldo
    

    def recargar(self , recarga = False , establecimiento = False):
        if((not recarga) or (not establecimiento)):
            raise ValueError('Parametros no validos') 
        
        if(recarga <= 0):
            raise ValueError('Recarga debe ser positiva')
        
        fecha = dt.now()
        self.saldo = self.saldo + recarga
        self.recargas.push((recarga , establecimiento , fecha))
        
        print('hacer la recarga')
    
    def consumir(self , consumo = False , establecimiento = False , pin = False):

        if((not consumo) or (not establecimiento) or (not pin)):
            raise ValueError('Parametros no validos')

        if (self.pin != pin):
            raise ValueError('Pin no valido')
        if(consumo <= 0 ):
            raise ValueError('Consumo debe ser positivo')
        if (self.saldo - consumo < 0):
            raise ValueError('Consumo no valido')
        
        fecha = dt.now()
        self.saldo = self.saldo - consumo
        self.consumos.append((consumo , establecimiento , fecha ))
    
    