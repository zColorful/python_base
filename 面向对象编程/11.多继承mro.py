
class A:
    pass
    # def test(self):
    #     print('from A')

class B(A):
    # def test(self):
    #     print('from B')
    pass

class B2:
    def test(self):
        print('from B2')

class C(A):
    pass
    # def test(self):
    #     print('from C')

class C2:
    def test(self):
        print('from C2')

class D(B,B2):
    # def test(self):
    #     print('from D')
    pass

class E(C,C2):
    pass
    # def test(self):
    #     print('from E')

class F(D,E):
    # def test(self):
    #     print('from F')
    pass

# 打印继承顺序
print(F.mro())

f1=F()
f1.test()