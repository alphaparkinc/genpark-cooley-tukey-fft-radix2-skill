import math
import cmath

class CooleyTukeyFFT:
    """
    Cooley-Tukey Radix-2 Fast Fourier Transform (FFT).
    O(N log N) algorithm for power-of-2 sequence lengths.
    """
    def fft(self, x):
        N = len(x)
        if N <= 1:
            return x
        if (N & (N - 1)) != 0:
            next_pow2 = 1 << (N - 1).bit_length()
            x = list(x) + [0.0] * (next_pow2 - N)
            N = next_pow2

        even = self.fft(x[0::2])
        odd = self.fft(x[1::2])
        factor = [cmath.exp(-2j * math.pi * k / N) for k in range(N // 2)]
        return [even[k] + factor[k] * odd[k] for k in range(N // 2)] +                [even[k] - factor[k] * odd[k] for k in range(N // 2)]
