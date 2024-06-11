class A:
    def info_A(self):
        return "this is class A"

class B:
    def info_B(self):
        return "this is class B"

class C(A, B):
    pass

c = C();
print(c.info_A())
print(c.info_B())