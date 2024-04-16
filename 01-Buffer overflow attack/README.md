# Buffer Overflow attack:


## Description:-
Buffer overflow attacks make use of vulnerabilities in the stack. The simplest form of buffer overflow attacks take in malicious user input, put them onto the stack, and affect the local variables / return address / arguments that are stored on the stack. This could lead to a change in the values of the variables, or even change the instructions the program calls! The worst instances of such attacks could lead to attackers getting remote control of your machine over a network. Here’s an example. That could be done through injecting shellcode and replacing return addresses to point to and run the poisionous shellcode.


## Process:-
### STEP 1 – CREATING A VULNERABLE C APPLICATION (code.c)
![1](https://github.com/the-zoomeee/Application-security/assets/154297263/f730a921-fe57-484e-835c-8a643ba9ea4a)

### STEP 2 – OBSERVING THE STACK
1. list – view code
2. break xxx – Add a breakpoint to pause your program so that you can view the stack frames, the current stack pointers as well as the assembly instruction that is running. xxx can stand for
  ● Line number (eg. break 7) –> breaks before line 7 runs
  ● Assembly instruction (eg. break *0x00000000004005ab) –> this is what an assembly instruction address looks like in a 64-bit machine. breaks before assembly instruction at 0x00000000004005ab runs
  ● function/method name (eg. break main) –> breaks before main method runs
3. r – runs program
4. next – runs next line
5. nexti – runs next assembly instruction
6. disas xxx – Disassemble and view assembly instruction. if only disas is used, the current frame is disassembled. If disas 0x00000000004005ab, assembly instructions of the function/method in which 0x00000000004005ab lies in is shown. *Hint* disas /m shows assembly instructions organized within lines a C code.
7. x/nfu xxx– examine stack at location xxx. (eg. x/10xw 0x7fffffffde90) –> this is what the address of a particular stack frame looks like in a 64-bit machine. These are what nfu can stand for (Further explanation here):
  ● n – number of frames to be displayed, starting in increasing value of addresses. 0x7fffffffde90, followed by 0x7fffffffde94 and so on.
  ● f – display format, either in hexadecimals (x), decimals (d) and so on.
  ● u – unit size, which can be in words (four bytes) (w), bytes (8 bits) (b), and so on.
8. p/x xxx– print values. Here are some examples p/x 0xbffff789-0xbffff779 will output 0x10 (hexadecimal value), while p/d 0x10 will output 16 (decimal value)
9. info xxx – gives information about frames/registers/breakpoints and so on
  ● info break – Display breakpoints
  ● info frame – Display current frame values and pointers
  ● info register – Display current register values (We will be focusing on rbp (base pointer) and rsp (stack pointer)
10. delete xxx – Deletes breakpoints. (eg. delete will delete all breakpoints, delete 2 will delete the second breakpoint).

![2](https://github.com/the-zoomeee/Application-security/assets/154297263/5e4e6f39-9989-4fae-9d42-74384cd23b37)
<p>Add breakpoint at main method, and run program. Program pauses right before main method is run! </p>

![3](https://github.com/the-zoomeee/Application-security/assets/154297263/b31b0eaa-5af9-49b9-bced-eb7777935b2f)
<p>View Register. Base pointer (rbp) points to 0x7fffffffde00 while Stack pointer(rsp) points to 0x7fffffffddf0</p>

This means that the memory space the main method uses lies between 0x7fffffffde00 and 0x7fffffffddf0. We have to view the contents of the stack frame to know what actually happens, where is the return address, where exactly are the local variables stored. Viewing the stack frames after every instruction will allow you to see what changes each instruction make to the stack frame. This will help you find out where the buffer space is for you to attack, and which part of the stack frame you will be able to insert a value into.

![4](https://github.com/the-zoomeee/Application-security/assets/154297263/62634a51-2193-427b-903a-21fddc04c043)
<p>Assembly Code of the main method</p>

![5](https://github.com/the-zoomeee/Application-security/assets/154297263/67f2ee8e-8828-4a0e-8ead-fc0f504b70a2)
<p>Stack frame where main method resides in before user input</p>

We will use next to reach the part of the program where it asks for an input from the user, and enter an input for the variable name. We shall see where the variable name is stored.

![6](https://github.com/the-zoomeee/Application-security/assets/154297263/10cf01b0-3287-4ac0-9ca1-3743bca39bdf)
<p>Stack frame after user input. Do not that “a” is stored as “61”, b is stored as “62”, and so on.</p>

“31” is the ASCII value for the decimal number “1”. storage of the name variable seems to go across 15 bytes, from 0x7fffffffde00 to 0x7fffffffde0e! Now let’s see the age variable printed out. How could it be 6710628? If the name variable staayed within 10 characters, age would still have been 0!

To check the hexadecimal value of 6710628, we did this. Alternatively, you may also use a <b> hexadecimal converter</b>

![7](https://github.com/the-zoomeee/Application-security/assets/154297263/f2a473c3-f9fd-4a8b-82aa-177ad7a26d11)
0x666564 At 0x7fffffffdeac! This means that the age variable is likely to be stored within the 4 bytes here! This, coincidentally, is the 13th character of the user input! Now this allows us to go on to the next step.

### STEP 3 – BUILD AN EXPLOIT! (attack.c)
![8](https://github.com/the-zoomeee/Application-security/assets/154297263/036091de-3891-4779-8ea2-0e56ef361d2b)

‘\x4D’ is the hexadecimal value equivalent of the number 77. Let’s see how you can perform the attack!
![9](https://github.com/the-zoomeee/Application-security/assets/154297263/9d2f816d-5efa-465a-bd10-f8b62aaa65d8)
