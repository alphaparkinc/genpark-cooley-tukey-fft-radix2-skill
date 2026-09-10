from client import CooleyTukeyFFT

def main():
    print("=== Testing Cooley-Tukey Radix-2 FFT ===")
    fft_eng = CooleyTukeyFFT()
    signal = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]

    freqs = fft_eng.fft(signal)
    print("Computed complex spectrum bins:")
    for idx, f in enumerate(freqs):
        print(f"  Bin {idx}: {round(f.real, 3)} + {round(f.imag, 3)}j (mag: {round(abs(f), 3)})")

    assert len(freqs) == 8
    assert abs(freqs[0]) == 4.0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
