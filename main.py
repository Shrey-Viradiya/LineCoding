from utilities import text2binary
from linecoding_shrey import polarRZ, AMI, pseudoternary

print(text2binary('Hello World'))
for x in pseudoternary('Hello World'):
    print(x, end="")