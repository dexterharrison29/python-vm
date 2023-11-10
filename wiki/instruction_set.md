# sHardVM instruction set
this is a simple instruction set for machine instructions(commonly referred to as binary); Each instruction here will have a corresponding "assembly" instruction; Do not assume that the program will take assembly; Also, if  the current version number is less than 1.0, do not assume that all instructions will work. I'm using a versioning system similar to Dwarf Fortress, where the second number represents the percentage finished. For example, the current version number is 0.3.0, so we can assume that this means that I am 3% finished. This is a general guideline of what to expect
# Full Instructions
Full instructions are a combination of 2-3 values; The first being the partial instruction, the second being the register; example: 'add ax 5'; this adds the value 5 to the ax register;  
# Partial Instructions
### LOGIC INSTRUCTIONS  
    0: and  
    1: or  
    2: not  
    3: xor  

### Math Functions
    04: add  
    05: sub  
### Store Functions
    06: mov  
    07: lda  
    08: sta  
### Comparisons
    09: cmp  
    0A: jeq  
    0B: jls  
    0C: jgt  
    0D: jge  
    0E: jle  
    0F: jge  
### Other
    10: jmp
    11: hlt
    12: out