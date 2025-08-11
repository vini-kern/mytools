PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

E_INT = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

print(len(E_INT))

def pi_real(casas: int):
    if casas < 1 or casas > 100:
        raise ValueError("Number of decimal places must be between 1 and 100.")
    print("3" + ',' + PI_INT[:casas])

def e_real(casas: int):
    if casas < 1 or casas > 100:
        raise ValueError("Number of decimal places must be between 1 and 100.")
    print("2" + ',' + E_INT[:casas])