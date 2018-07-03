class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s
    def get_stu_name(self):
        return self.name
    def set_stu_name(self, n):
        self.name = n
    def get_stu_age(self):
        return self.age
    def set_stu_age(self, a):
        self.name = a    
    def get_stu_score(self):
        return self.score
    def set_stu_score(self, s):
        self.score = s
    def get_stu_data(self):
        return (self.name, self.age, self.score)
    def save_to_file(self, f):
        f.write('%s,%s,%s\n' % (self.name, self.age, self.score))
class StuAddr(Student):
    def __init__(self, sn, n, a, s, addr):
        super().__init__(n, a, s)
        self.sn = sn
        self.address = addr
    def get_stu_addr(self):
        return self.address
    def set_stu_addr(self, addr):
        self.address = addr
    def get_stu_sn(self):
        return self.sn
    def set_stu_sn(self, sn):
        self.sn = sn
    def get_stu_data(self):
        return (self.sn,) + super().get_stu_data() + (self.address,)
    def save_to_file(self, f):
        f.write('%d,%s,%s,%s,%s\n' % (int(self.sn), self.name, self.age, self.score, self.address))