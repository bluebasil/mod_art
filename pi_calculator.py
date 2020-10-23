
characters = list(range(0,10)) + [chr(c) for c in list(range(ord("A"),ord("Z")+1))]

class PiCalculator:

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    decimal = 0
    counter = 0
    #yielded = ""
    yielded_technical = []

    def get_next_digit(self, base=6):
        self.decimal += 1

        while self.counter != self.decimal + 1:
            if 4 * self.q + self.r - self.t < self.n * self.t:
                # yield digit
                next_digit = self.n
                #self.yielded += str(characters[next_digit])
                self.yielded_technical.append(next_digit)
                # insert period after first digit
                if self.counter == 0:
                    #self.yielded += '.'
                    self.yielded_technical.append('.')

                self.nr = base * (self.r - self.n * self.t)
                self.n = ((base * (3 * self.q + self.r)) // self.t) - base * self.n
                self.q *= base
                self.r = self.nr

                # end
                if self.decimal == self.counter:
                    return self.yielded_technical[self.decimal-1]
                    # else:
                    #     #print("*",next_digit, self.yielded[-10:-1])
                    #     print()
                    #     print("---")
                    #     #print(self.yielded)
                    #     print(next_digit)
                    #
                    #     return self.yielded
                self.counter += 1

            else:
                self.nr = (2 * self.q + self.r) * self.l
                self.nn = (self.q * (7 * self.k) + 2 + (self.r * self.l)) // (self.t * self.l)
                self.q *= self.k
                self.t *= self.l
                self.l += 2
                self.k += 1
                self.n = self.nn
                self.r = self.nr
