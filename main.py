from utilities import text2binary
from linecoding_shrey import polarRZ, AMI, pseudoternary

print(text2binary('Hello'))
for x in pseudoternary("Hello"):
    print(x, end="")