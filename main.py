from random import randint, choice

class Sequence:

    def __init__(self):

        self.type = 0
        # generate sequence until d is an integer
        while True:
            try:
                self.generate()
                if self.d == 0:
                    continue
                if self.d.is_integer():
                    if self.sum.is_integer():
                        if self.sum > 0:
                            break
            except ValueError as e:
                continue
                
    def generate(self):
        self.Sn = randint(10, 30)
        self.n = randint(1, self.Sn - 1)
        self.k = randint(self.n + 1, self.Sn - 1)
        self.an = randint(1, 100)
        self.ak = randint(self.an, 100)

        self.d = (self.ak - self.an) / (self.k - self.n)

        if self.n == 1: self.a1 = self.an
        else:
            self.a1 = self.an - ((self.n-1)*self.d)

        self.sum = (((2*self.a1) + (self.Sn-1)*self.d)/2)*self.Sn

    #an formula
    def a(self, n: int):
        return self.a1 + (n-1)*self.d

    def __str__(self):
        questions = [
            f"The sum of the first {self.Sn} terms in a sequence S is {self.sum}.\na{self.n} is {self.an}.\na{self.k} is {self.ak}.\nFind the difference.\n",
            f"The sum of the first *n* terms in a sequence S is {self.sum}.\na{self.n} is {self.an}.\na{self.k} is {self.ak}.\nFind n.\n",
        ]
        q = choice(questions)
        if q == questions[0]:
            self.type = 1
        else:
            self.type = 2
        return q

while True:
    s = Sequence()
    print(s)
    input_ = str(input(">>> Would you like to know the answer? (y/n): "))
    if input_ == "y":
        if s.type == 1:
            print(f"\nWe can get difference by using (an - ak)/(k - n) = d\nSubstitute:\n({s.an} - {s.ak}) / ({s.k} - {s.n}) = {s.d}\n")
            cont = str(input(">>> Would you like to continue? (y/n): "))
            if cont == "y":
                print("\n\n")
                continue
            else:
                break
        elif s.type == 2:
            print(
                f"\nWe can get difference by using (an - ak)/(k - n) = d\nSubstitute:\n({s.an} - {s.ak}) / ({s.k} - {s.n}) = {s.d}\n\nThen we can get a1 by doing a1 = an - ((n-1)*d)\n"
                f"Substitute: a1 = {s.an} - (({s.n}-1)*{s.d}) = {s.a1}\n\nThen we can put a1 into the formula Sn = ((a1 + a1 + (n-1)*d) / 2) * n\n\n"
                f"Substitute: {s.sum} = (({s.a1} + {s.a1} + (n-1)*{s.d}) / 2) * n\n\n"
                f"Solve for n to (hopefully) get n = {s.Sn}.\n"

            )
            cont = str(input(">>> Would you like to continue? (y/n): "))
            if cont == "y":
                print("\n\n")
                continue
            else:
                break
