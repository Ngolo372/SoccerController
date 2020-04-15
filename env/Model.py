#!/usr/bin/env python3

import math

#获取从当前坐标到目标之间的速度（vx，vy）
#距离小于0.5时，视为已经到达目标点
def getvel(xcurrent, ycurrent, xgoal, ygoal,v=1):
    d = ((xcurrent-xgoal)**2 + (ycurrent-ygoal)**2)**0.5
    vx = 0.0
    vy = 0.0
    
    if d > 0.5: #一处修改，考虑车体大小，8m场地中相当于间距25cm
        qx = (xgoal - xcurrent) / d
        qy = (ygoal - ycurrent) / d
        vx = qx*v
        vy = qy*v
        return vx,vy
    else:
        return vx,vy


#小车类
class Car:
    def __init__(self, x=0.0, y=0.0, yaw = 0.0, step=0.1):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.step = step
        self.count = 0
        self.wz = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.v = 0.0
        self.totaltime = 0.0

    #小车移动，线速度限制2.0，角速度限制（-pi/6，+pi/6）
    def move(self, vx, vy):
        v = (vx**2+vy**2)**0.5

        ############# 改动 ###########
        if v > 2.0:
            v = 2.0 # 最大速度加倍
        ############# 改动 ###########

        yawcmd = math.atan2(vy, vx)
        if yawcmd - self.yaw > math.pi:
            yawcmd = yawcmd - 2 * math.pi
        elif yawcmd - self.yaw < -math.pi:
            yawcmd = yawcmd + 2 * math.pi

        if math.fabs(yawcmd - self.yaw) > math.pi / 6:
            v = 0
        self.yaw = self.yaw + (yawcmd - self.yaw)*self.step
        vx = v*math.cos(self.yaw)
        vy = v*math.sin(self.yaw)
        self.x = self.x + vx * self.step
        self.y = self.y + vy * self.step
        self.vx = vx
        self.vy = vy
        self.v = v
        self.count += 1
        return self.x,self.y


class Env:
    def __init__(self, xmin=0.0, ymin=0.0, xmax=5.0, ymax=5.0):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self.A = 1.0
        self.B = 1.0
        self.stopsim = False

    def setgoal(self, A, B):
        self.A = A
        self.B = B

    #car1 为进攻方，car2 为防御方
    def carstate(self, car1x, car1y, car2x, car2y):
        
        if ((car1x-car2x)**2 + (car1y-car2y)**2)**0.5 < 0.5:
            
            self.stopsim = True
            return -1.0
        elif car1x < self.xmin or car1x > self.xmax or car1y < self.ymin or car1y > self.ymax:
            return -0.2
        elif ((car1x-self.A)**2 + (car1y-self.B)**2)**0.5 < 0.5:
            self.stopsim = True
            return 1.0
        else:
            return 0.0

    def getdistoboundary(self,x,y):
        xmin = x - self.xmin
        xmax = self.xmax - x
        ymin = y - self.ymin
        ymax = self.ymax - y
        d = ((x-self.A)**2 + (y-self.B)**2)**0.5
        return xmin,xmax,ymin,ymax,d

