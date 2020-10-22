
class PiCalculator:

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    decimal = 0
    counter = 0
    yielded = ""

    def get_next_digit(self):
        self.decimal += 1

        while self.counter != self.decimal + 1:
            if 4 * self.q + self.r - self.t < self.n * self.t:
                # yield digit
                self.yielded += str(self.n)
                # insert period after first digit
                if self.counter == 0:
                    self.yielded += '.'
                # end
                if self.decimal == self.counter:
                    print('')
                    return self.yielded
                self.counter += 1
                self.nr = 10 * (self.r - self.n * self.t)
                self.n = ((10 * (3 * self.q + self.r)) // self.t) - 10 * self.n
                self.q *= 10
                self.r = self.nr
            else:
                self.nr = (2 * self.q + self.r) * self.l
                self.nn = (self.q * (7 * self.k) + 2 + (self.r * self.l)) // (self.t * self.l)
                self.q *= self.k
                self.t *= self.l
                self.l += 2
                self.k += 1
                self.n = self.nn
                self.r = self.nr
