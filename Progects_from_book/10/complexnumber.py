

class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __iadd__(self, other):
        self.real += other.real
        self.imaginary += other.imaginary
        return self

    def __repr__(self):
        return (f'({self.real}' +
                ('+' if self.imaginary > 0 else '-') +
                f'{abs(self.imaginary)}i)')

