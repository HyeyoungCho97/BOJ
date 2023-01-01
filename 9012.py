'''
import sys
import os

currentPath = os.getcwd()
sys.stdin = open(currentPath+"\\boj\\input.txt", "r")
'''
T = int(input())

for i in range(1, T+1):

    test = []
    t = -1
    ps = list(input())
    #print(len(vps))
    
    for n in range(0, len(ps)):

        v = ps.pop()
        
        if t == -1:
            test.append(v)
            if v == '(':
                break
            else:
                t += 1
            '''
            print("-------------")
            print('if: ')
            print(n, t)
            print(test)
            print(vps)
            '''
        elif test[t] == v:
            test.append(v)
            t += 1
            '''    
            print("-------------")
            print('elif: ')
            print(n, t)
            print(test)
            print(vps)
            '''

        elif test[t] != v:
            test.pop()
            t -= 1
            '''
            print("-------------")
            print('else: ')
            print(n, t)
            print(test)
            print(vps)
            '''
        
    '''
    print("-------------")
    print('-for: ')
    print(n, t)
    print(test)
    print(vps)
    '''
    if len(test) == 0:
        print("YES")
    else:
        print("NO")    