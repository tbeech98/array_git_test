import matrix

class matrix3:
    def __init__(self,a11,a12,a13,a21,a22,a23,a31,a32,a33):
        self.a11 = a11
        self.a12 = a12
        self.a13 = a13
        self.a21 = a21
        self.a22 = a22
        self.a23 = a23
        self.a31 = a31
        self.a32 = a32
        self.a33 = a33
    def form(self):
        matrix.threebythree(self.a11,self.a12,self.a13,self.a21,self.a22,self.a23,self.a31,self.a32,self.a33)

a = matrix3(1,6,9,29,34,48,98,63,40)

a.form()

