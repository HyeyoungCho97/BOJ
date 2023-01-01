pipes = input()

laserStack = []
lsTop = -1

pipeStack = []
psTop = -1

isLaser = 0
answerList = []
atop = -1
stack = []
laser = 0
top = 0
pipe = 0
answer = 0

for i in range(0, len(pipes)-1):

        if pipes[i] =='(' and pipes[i+1] == ')':
            isLaser = 1
        
        if isLaser == 1:
            if pipes[i] == '(':
                break
            elif pipes[i] == ')':
                laser +=1
                isLaser = 0
                
                if len(pipeStack) == 0:
                    laser = 0

        elif isLaser == 0:
            if pipes[i] == '(':
                pipeStack.append(0)
                atop += 1
            if pipes[i] == ')':
                answer += laser+1
                laserStack.append(laser)
                laser = 0



        



    