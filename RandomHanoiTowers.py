import re
import random
import time
import copy

start_time = time.time()

def initialState():
    while(1):
        rods = input("Nr. rods: ")
        try:
            rods = int(rods)
            if rods >= 3:
                break
            else:
                print("Minimum 3 rods !")
        except ValueError:
            print("Rods must be a number, try again !")
    
    while(1):
        pieces = input("Nr. pieces: ")
        try:
            pieces = int(pieces)
            if pieces >= 1:
                break
            else:
                print("Minimum 1 piece !")
        except ValueError:
            print("Pieces must be a number, try again !")

    while(1):
        end_rod = input("End rod: ")
        if end_rod == "":
            end_rod = rods
            break
        try:
            end_rod = int(end_rod)
            if end_rod >= 1 and end_rod <= rods:
                break
            else:
                print("End rod must be between 1 and " + str(rods) + " !")
        except ValueError:
            print("End rod must be a number, try again !")
    dct = {}
    flag = False
    final_state = {}

    for i in range(int(rods)):
        final_state[i+1] = []
        
    for j in range(int(pieces)):
        final_state[end_rod].append(str(j+1))

    print(final_state)
    temp = int(pieces)
    temp_rods = int(rods)
    for i in range(int(rods)):
        
        if temp <= 0 and temp_rods == 0:
            break
        elif temp <= 0 and temp_rods > 0:
            dct[i+1] = []
            temp_rods -= 1
            continue

        if flag:
            dct[i+1] = []
            continue
        

        while(1):
            user_input = input("Pieces on rod " + str(i+1) + ":")
            if user_input == "":
                if not flag:
                    dct[i+1] = []
                    flag = True
                for j in range(int(pieces)):
                    dct[i+1].append(j+1)
                    flag = True
                break
            elif user_input == '0':
                dct[i+1] = []
                break
            else:
                try:
                    if len(user_input.split(',')) > temp:
                        print("Too many pieces inserted !")
                    elif len(user_input.split(',')) < temp and i+1 == rods:
                        print("There are still some pieces left !")
                        temp_input = input("Insert all the pieces remaining("+ str(temp)+ "):")
                        dct[i].append(temp_input)
                        break
                    else:
                        dct[i+1] = user_input.split(',')
                        temp = temp-len(user_input.split(','))
                        temp_rods -= 1
                        break
    
                except ValueError:
                    print("Invalid input !")

    print (dct)
    return dct,final_state,rods,pieces,end_rod

def validateMove(dct, piece, end_rod):
    flag = False
    for key, value in dct.items():
        for idx in value:
            if int(idx) == int(piece):
                if value.index(idx) == len(value)-1:
                    flag = True
        if flag:
            break

    if flag:
        for key, value in dct.items():
            if key == end_rod:
                try:
                    if int(value[-1]) < piece:
                        return True
                except:
                    return True     
    return False
    

   

def transition(dct, piece, end_rod):
    for key, value in dct.items():
        flag = False
        if key == end_rod:
            value.append(str(piece))
        else:
            for idx in value:
                if int(idx) == int(piece):
                    flag = True
        if flag:
            del value[-1]

    return dct

def strategy():
    dct,final_state,rods,pieces,end = initialState()
    count = 1
    itr = 0
    j=1
    i = 1
    d1 ={}
    print("\n")
    while dct != final_state:
        rod = random.randint(1,rods)
        piece = random.randint(i,pieces)
        if validateMove(dct,piece,rod) == True and rod == end and piece == i:
            dctCopy=copy.deepcopy(dct)
            stateAfterTransition = transition(dctCopy,piece,rod)
            l = noDuplicateState(stateAfterTransition)
            if l not in d1.values():
                transition(dct,piece,rod)
                i+=1
                print(str(count) + ":")
                print(dct)
                print("\n")
                count += 1
                d1[j]={}
                d1[j]=l
                j+=1
        elif validateMove(dct,piece,rod):
                dctCopy=copy.deepcopy(dct)
                stateAfterTransition = transition(dctCopy,piece,rod)
                l = noDuplicateState(stateAfterTransition)
                if l not in d1.values():
                    transition(dct,piece,rod)
                    print(str(count) + ":")
                    print(dct)
                    print("\n")
                    count += 1
                    d1[j]={}
                    d1[j]=l
                    j+=1
                print('@@')
                print(i)
                print('@@\n')
        else:
            itr += 1
            print("d1 len:" +str(j))
            if itr is 25 and len(d1.keys()) > 2:
                itr = 0
                for i in range(1,int(len(d1.keys())/2)):
                    d1.pop(j, None)
                    j -= 1
                print(j)
                dct = d1[j]
                print(dct)
                i = 1
                time.sleep(3)

    l=noDuplicateState(dct)
    d1[j]=l
    print(d1)

def noDuplicateState(dct):
    l1 = {}
    i = 1
    for key,value in dct.items():
        temp = []
        for k in value:
            temp.append(k)
        l1[i] = temp
        i += 1
    return l1

strategy()
print("--- %s seconds ---" % (time.time() - start_time))

#time.sleep(1000)


#d1 = {1:[100,200],2:[]}
#print(d1)
#noDuplicateState(d1)