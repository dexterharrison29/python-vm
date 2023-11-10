# sHardVM instruction set
this is a simple instruction set for machine instructions(commonly referred to as binary); Each instruction here will have a corresponding "assembly" instruction; Do not assume that the program will take assembly; Also, if  the current version number is less than 1.0, do not assume that all instructions will work. I'm using a versioning system similar to Dwarf Fortress, where the second number represents the percentage finished. For example, the current version number is 0.3.0, so we can assume that this means that I am 3% finished. This is a general guideline of what to expect
# Full Instructions
Full instructions are a combination of 2-3 values; The first being the partial instruction, the second being the register; example: 'add ax 5'; this adds the value 5 to the ax register;  
# Partial Instructions
### LOGIC INSTRUCTIONS  
    00: and  
    01: or  
    02: not  
    03: xor  

### Math Functions
    04: add  
    05: sub  
### Store Functions
    06: mov  
    07: lda  
    08: sta
    09: lab
    0A: cll
### Comparisons
    0B: cmp  
    0C: jeq  
    0D: jls  
    0E: jgt  
    0F: jge  
    10: jle  
    11: jge  
### Other
    12: jmp
    13: hlt
    14: oti
    15: ota

# Registers
### Data Registers
    00: ax; Accumulator; easy math storage
    01: bx; base register; used for indirect addressing
    02: cx; count register; primarily used to count the number of times a loop has run.
    03: dx; data register; 
### Pointer Registers
    04: ip; program counter register
# Example Program
### Here is an assembly program
I have this program stored in a folder called programs; hello_world.asm;
    lab 0x000000, 0x00000C
    mov 0x000000, 72 ; H
    mov 0x000001, 101; e
    mov 0x000002, 108; l
    mov 0x000003, 108; l
    mov 0x000004, 111; o
    mov 0x000005, 44 ; ,
    mov 0x000006, 32 ;  
    mov 0x000007, 119; w
    mov 0x000008, 111; o
    mov 0x000009, 114; r
    mov 0x00000A, 108; l
    mov 0x00000B, 100; d
    mov 0x00000C, 10 ; Newline character
    ota lab ; outputs ascii from every memory address stored in the label
    cll ; clears the label
    hlt ; ends the program

