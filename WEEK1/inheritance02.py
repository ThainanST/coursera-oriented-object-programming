# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 00:13:19 2022

@author: thainan
"""

class Employee:
    def __init__(self, name, CPF, RG):
        self.name = name
        self.CPF = CPF
        self.RG = RG
        
    def calculatePayment(self):
        print("Happiness begin here...")
        
## Testing the class
#generalEmployee = Employee('John', 'cpf', 'rg')
#generalEmployee.calculatePayment()

class HourEmployee(Employee):
    def __init__(self, name, CPF, RG, numHour, paymentHour):
        Employee.__init__(self, name, CPF, RG)
        self.numHour     = numHour
        self.paymentHour = paymentHour

    def calculatePayment(self):
        payment = self.numHour * self.paymentHour
        print("The {}s payment is U$ {:.2f}.".format(self.name, payment))
        return payment

## Testing the class
#numHour     = 40
#paymentHour = 25.50
#hourEmployee = HourEmployee('John', 'cpf', 'rg', numHour, paymentHour)
#hourEmployee.calculatePayment()

class CLTEmployee(Employee):
    def __init__(self, name, CPF, RG, wage):
        Employee.__init__(self, name, CPF, RG)
        self.wage = wage
    
    def calculatePayment(self):
        payment = 13.3333*self.wage
        print("The {}s payment is U$ {:.2f}.".format(self.name, payment))
        return payment

## Testing the class
#wagePerMonth = 13000
#cltEmployee = CLTEmployee('John', 'cpf', 'rg', wagePerMonth)
#cltEmployee.calculatePayment()

class ServiceEmployee(Employee):
    def __init__(self, name, CPF, RG, deal):
        Employee.__init__(self, name, CPF, RG)
        self.deal = deal
        
    def calculatePayment(self):
        print("The {}s payment is U$ {:.2f}.".format(self.name, self.deal))
        return self.deal

## Testing the class
deal = 170000
serviceEmployee = ServiceEmployee('John', 'cpf', 'rg', deal)
serviceEmployee.calculatePayment()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        