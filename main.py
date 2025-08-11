import MYTOOLS as tools

tools.e_real(10)
tools.pi_real(5)

print(tools.PI_INT)
print(tools.E_INT)

try:
    tools.pi_real(101)
except ValueError as e:
    print(e)