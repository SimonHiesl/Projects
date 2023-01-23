from mpmath import mp
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

mp.dps = 1+1000000
pi = str(mp.pi)[2:]

def Learn_Pi(skip=0, max_digit=100000):
    i = 1
    pos = skip
    total = 0
    start = dt.datetime.now()
    while i>0 and not pos>=max_digit:
        x = input()
        i = len(x)
        if i!=0:
            break
        i = 1
        y = pi[pos]+pi[pos+1] + " " + pi[pos+2]+pi[pos+3] + " " + pi[pos+4]+pi[pos+5]
        print(y)
        total += 1
        pos += 6
    stop = dt.datetime.now()
    print("You learned: ", 6*total, " digits of pi.")
    print("You took: ", stop-start)

def pao(w_pos, start_digit):
    if w_pos % 6 == 0:
        w_pos -= 1
    return pi[start_digit+int((w_pos)//6)*6:start_digit+int((w_pos)//6)*6+6:1]

def in_inp(inp, i, offset):
    if (i+offset+1) % 6 == 0:
        i -= 1
    skip = ((i+offset)//6)*6-offset
    return str(inp)[skip:skip+6:1]
    
def Ask_Pi(start_digit=0, mistake_limit=20):
    print("Push ENTER to start the timer!")
    enter = input()
    if len(enter) == 0:
        print("Start!")
        start = dt.datetime.now()
    else: return print("Attempt aborted!")
    inp = input()
    if str(inp) == pi[start_digit:(len(str(inp))+start_digit)]:
        print("Everything is correct!")
        print("You learned: ", len(str(inp)), " digits of pi.")
        stop = dt.datetime.now()
    else:
        stop = dt.datetime.now()
        print("Incorrect!")
        mistake_count = 0
        offset = 0
        for i in range(len(inp)):
            if str(inp)[i]==pi[i+start_digit+offset]:
                continue
            else:
                if mistake_count+offset == 0:
                    print("Only the first", i, "digits of pi were correct.")
                if str(inp)[i]==pi[i+1+start_digit+offset] and str(inp)[i+1]==pi[i+2+start_digit+offset] and str(inp)[i+2]==pi[i+3+start_digit+offset]:
                    print("You missed digit", i+offset+1, "which is:", pi[i+start_digit+offset], " (PAO:" + str(pao(i+offset+1, start_digit)) + ")  in:", in_inp(inp, i, offset))
                    offset += 1
                elif str(inp)[i]==pi[i+2+start_digit+offset] and str(inp)[i+1]==pi[i+3+start_digit+offset] and str(inp)[i+2]==pi[i+4+start_digit+offset]:
                    print("You missed two digits", i+offset+1, "and", i+offset+2, "which are:", str(pi[i+start_digit+offset]) + str(pi[i+1+start_digit+offset]), " (PAO:" + str(pao(i+offset+1, start_digit)) + ")")
                    offset += 2
                elif str(inp)[i]==pi[i+6+start_digit+offset] and str(inp)[i+1]==pi[i+7+start_digit+offset] and str(inp)[i+2]==pi[i+8+start_digit+offset]:
                    print("You missed six digits between", i+offset+1, "and", i+offset+6, "which are:", pi[i+start_digit+offset:i+6+start_digit+offset:1])
                    offset += 6
                else:
                    print("You got position", i+offset+1, "wrong:", str(inp)[i], "should be", pi[i+start_digit+offset], " (PAO:" + str(pao(i+offset+1, start_digit)) + ") in:", in_inp(inp, i, offset))
                    mistake_count += 1
                if mistake_count >= mistake_limit:
                    print("Too many mistakes!")
                    break
        print("You got a total of", len(str(inp))-mistake_count, "digits of", len(str(inp))+offset, "correct!")
    print("You took: ", stop-start)


#Learn_Pi()
#Ask_Pi()