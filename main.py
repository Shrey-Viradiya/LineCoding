from utilities import text2binary
from linecoding_shrey import polarRZ, AMI

print(text2binary('Hello World'))
for x in AMI('Hello World'):
    print(x, end="")