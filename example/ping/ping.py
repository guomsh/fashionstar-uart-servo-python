'''
FashionStar Uart舵机 
> Python SDK舵机通讯检测 Example <
--------------------------------------------------
- 作者: 阿凯
- Email: xingshunkai@qq.com
- 更新时间: 2020-12-5
--------------------------------------------------
'''
# 添加uservo.py的系统路径
import sys
sys.path.append("../../src")
# 导入依赖
import time
import serial
from uservo import UartServoManager

# 参数配置
# 角度定义
SERVO_PORT_NAME =  'COM7' # 舵机串口号
SERVO_BAUDRATE = 115200 # 舵机的波特率
SERVO_ID = 0  # 舵机的ID号

# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
					 parity=serial.PARITY_NONE, stopbits=1,\
					 bytesize=8,timeout=0)
# 初始化舵机管理器
uservo = UartServoManager(uart)

# 舵机通讯检测
is_online = uservo.ping(SERVO_ID)
print("舵机ID={} 是否在线: {}".format(SERVO_ID, is_online))
