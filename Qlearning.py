#Qlearning 经典算法实践
import numpy as ny
import random as rd
#参数
Gamma = 0.8
#初始化Q
Q = ny.zeros((6,6))
R = [[-1,-1,-1,-1,0,-1],
     [-1,-1,-1,0,-1,100],
     [-1,-1,-1,0,-1,-1],
     [-1,0,0,-1,0,-1],
     [0,-1,-1,0,-1,100],
     [-1,0,-1,-1,0,100]
]
#这就非常有意思了，他的list初始化的时候，如果只初始化【】*3，那就是创建了三个指向这个数组的对象，每个都会变
R_av = [[]for i in range(6)]
for row in range(0,6):
    for col in range(0,6):
        if R[row][col] >= 0:
            R_av[row].append(col)

#我们循环十带
for i in range(0,1000):
        state = rd.randint(0, 5)
        nextstate = 0;
        #如果第一次为5，那么为了避免多代，这时候，我们就只做一次
        if state == 5:
            nextstate = R_av[state][rd.randint(0, len(R_av[state]) - 1)]
            maxQ = max(Q[nextstate, :])
            Q[state][nextstate] = R[state][nextstate] + Gamma * maxQ
            continue
        while state != 5:
            #for nextstate in range(6):
            nextstate = R_av[state][rd.randint(0, len(R_av[state])-1)]
            #下一个状态的左右动作
            #if R[state][nextstate] == -1:
            #  continue
            maxQ = max(Q[nextstate, :])
            Q[state][nextstate] = R[state][nextstate] + Gamma*maxQ
            state = nextstate

print(Q)











