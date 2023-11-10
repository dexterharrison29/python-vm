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
