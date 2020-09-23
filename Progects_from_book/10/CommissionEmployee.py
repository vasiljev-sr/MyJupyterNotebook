from decimal import Decimal

class  CommissionEmployee:
    def __init__(self,first_name,last_name,ssn,
                 gross_sales,commision_rate):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales
        self.commision_rate = commision_rate

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sales(self):
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, sales):
        if sales < Decimal(0.00):
            raise ValueError('Gross sales должен быть > 0')
        else:
            self._gross_sales = sales

    @property
    def commision_rate(self):
        return self._commision_rate

    @commision_rate.setter
    def commision_rate(self, rate):
        if not (Decimal(0.00)< rate < Decimal(1.00)):
            raise ValueError('Сommision_rate должен быть от 0 до 1')
        else:
            self._commision_rate = rate

    def earnings(self):
        return self.gross_sales*self.commision_rate

    def __repr__(self):
        return ('CommissionEmployee: ' +
            f' {self.first_name} {self.last_name}\n'+
            f'номер соц страхования: {self.ssn}\n' +
            f'обьем продаж: {self.gross_sales:.2f}\n' +
            f'комиссионная ставка: {self.commision_rate:.2f}')
