## 修改内容

1.相比原场地8.5 * 5（范围[-0.5, 8.0, -2.5, 2.5]），整个场地扩大为17 * 10（范围[-9.0, 8.0, -5.0, 5.0]），进攻方出发点由（0，0）改为（-8，0）

2.最大车速从1.0改为2.0，最大角速度不变（仿真环境中体现为电机转速，python实现中使用velocity和omega即可）

3.达到目标的距离设置为0.5（因小车大小为0.8 * 0.6， 0.5可避免相撞，此规则距离确实有点大，我会尝试可否缩小）

## script注意

简单策略最好勿用numpy等库，为方便转换为lua脚本。对于复杂策略我会之后探索调用外部脚本的方法。
