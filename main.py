import matrix

class matrix2:
    def __init__(self,a11,a12,a21,a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22
    def form(self):
        matrix.twobytwo(self.a11,self.a12,self.a21,self.a22)

a = matrix2(1,6,9,48)

a.form()

