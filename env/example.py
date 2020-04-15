#coding:utf-8
from Model import *
import numpy as np
sim_step = 0.1
#初始化环境边界

############# 改动 ###########
env = Env(-9.0, -5.0, 8.0, 5.0) # 边界扩大
############# 改动 ###########

env.setgoal(8.0,0.0) 
#初始化进攻方小车

############# 改动 ###########
car1 = Car(-8.0,0,step=sim_step)
############# 改动 ###########

car1goal = [8.0,0.0]
#初始化防御方小车
car2x0 = np.random.randint(3, 7) # 可修改
car2y0 = np.random.randint(-3, 3) # 可修改
car2 = Car(car2x0, car2y0, yaw=math.pi, step=sim_step)

############# 改动 ###########
V=2.0
############# 改动 ###########

#开始运动
for t in range(10000):
    #直接朝向目标行进的进攻方
    vx, vy = getvel(car1.x, car1.y, car1goal[0], car1goal[1], V)
    car1.move(vx, vy)
    #直接朝向进攻方行进的防御方
    vx, vy = getvel(car2.x, car2.y, car1.x, car1.y,2*V)
    car2.move(vx,vy)
    #判断当前状态
    carstate = env.carstate(car1.x,car1.y,car2.x,car2.y)
    print("car1:",car1.x,car1.y)
    print("car2:",car2.x,car2.y)
    print("carstate",carstate)
    #满足条件时停止运动
    if env.stopsim :
        break