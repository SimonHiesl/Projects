import secrets
import math
import sys

ASCII = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', '!', '?', ':', ';', "'", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', '+', '-', '*', '/', '(', ')', '[', ']', '{', '}', '@', '§', '$', '%', '&', '~', '#', '_', '<', '>', '|', '^', 'ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü', 'ß']
Num_CS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
CI = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Bin = ['0', '1']
PAO = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x']

def create_password(pw_length, pw_signs, password):
    bits = round(math.log(len(pw_signs),2)*pw_length,1)
    for i in range(pw_length):
        password +=     str(secrets.choice(pw_signs))
    return password, bits

def help():  # help prints little help message
    print(sys.argv[2].isdigit())
    print("""
    
        pwgen [pwlen] [pw_signs]    arguments must be passed in correct order as shown
                                    [pwlen] is length of password as int
                                    [pw_signs] either use one of the avalible pw_sing lists or pass allowed chars your self
                                        avalible pw_sign lists are ASCII, Num_CS, CS, CI, Num, Bin, PAO
    
    """)

if( len(sys.argv) == 4 
    and sys.argv[1] == "pwgen" # check count of passed arguments
    and sys.argv[1] == "pwgen"  # check for first argument beeing "pwgen"
    and sys.argv[2].isdigit() ): # check for second argument beeing a number 
    
    password, bits = create_password( int(sys.argv[2]),  # first argument is pw length as int
                                      eval(sys.argv[3]) if sys.argv[3] in ['ASCII', 'Num_CS', 'CS', 'CI', 'Num', 'Bin', 'PAO'] else sys.argv[3],  # seconde arument is char set to use for pw
                                      "")  # third argument is string to initialise password variable
    
    print(f"""
        Password:  {password}
        Strength:  {bits} bits
    """)

else:
    help()