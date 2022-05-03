# This script is used to adjust the orientation (position? angle) of each joint of the grasshopper

PI: float = 3.1415926535897932384626

import pybullet as p
import pybullet_data
from time import sleep # Or, use 'import time' first, and then use 'time.sleep'

p.connect(p.GUI)
p.setGravity(0, 0, -0)

initial_position_lrt: float = (180 - 147.35) / 360 * 2 * PI
initial_position_lrc: float = -(180 - 92.39) / 360 * 2 * PI
initial_position_lfj: float = 39.47 / 360 * 2 * PI
initial_position_lft: float = 15.01 / 360 * 2 * PI
initial_position_lfc: float = -62.22 / 360 * 2 * PI
initial_position_rmj: float = (180 - 155.28) / 360 * 2 * PI
initial_position_rmt: float = 19.33 / 360 * 2 * PI
initial_position_rmc: float = -74.99 / 360 * 2 * PI

angle_lrt = p.addUserDebugParameter('left_rear_thigh', -PI, PI, 0)
angle_lrc = p.addUserDebugParameter('left_rear_calf', -PI, PI, 0)
angle_lmj = p.addUserDebugParameter('left_middle_joint', -PI, PI, 0)
angle_lmt = p.addUserDebugParameter('left_middle_thigh', -PI, PI, 0)
angle_lmc = p.addUserDebugParameter('left_middle_calf', -PI, PI, 0)
angle_lfj = p.addUserDebugParameter('left_front_joint', -PI, PI, 0)
angle_lft = p.addUserDebugParameter('left_front_thigh', -PI, PI, 0)
angle_lfc = p.addUserDebugParameter('left_front_calf', -PI, PI, 0)
angle_rrt = p.addUserDebugParameter('right_rear_thigh', -PI, PI, 0)
angle_rrc = p.addUserDebugParameter('right_rear_calf', -PI, PI, 0)
angle_rmj = p.addUserDebugParameter('right_middle_joint', -PI, PI, 0)
angle_rmt = p.addUserDebugParameter('right_middle_thigh', -PI, PI, 0)
angle_rmc = p.addUserDebugParameter('right_middle_calf', -PI, PI, 0)
angle_rfj = p.addUserDebugParameter('right_front_joint', -PI, PI, 0)
angle_rft = p.addUserDebugParameter('right_front_thigh', -PI, PI, 0)
angle_rfc = p.addUserDebugParameter('right_front_calf', -PI, PI, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
plane = p.loadURDF('plane.urdf')
grasshopper = p.loadURDF('C:/Users/41725/Desktop/grasshopper_v16/urdf/'
                         'grasshopper_v16.urdf', basePosition=[0, 0, 0.1])

number_of_joint = p.getNumJoints(grasshopper)
for joint_number in range(number_of_joint):
    info = p.getJointInfo(grasshopper, joint_number)
    print(info)
    # print(info[0], ": ", info[1])

sleep(0.5)

left_rear_thigh = [0]
left_rear_calf = [1]
left_middle_joint = [3]
left_middle_thigh = [4]
left_middle_calf = [5]
left_front_joint = [7]
left_front_thigh = [8]
left_front_calf = [9]
right_rear_thigh = [11]
right_rear_calf = [12]
right_middle_joint = [14]
right_middle_thigh = [15]
right_middle_calf = [16]
right_front_joint = [18]
right_front_thigh = [19]
right_front_calf = [20]

while True:
    angle0 = p.readUserDebugParameter(angle_lrt)
    angle1 = p.readUserDebugParameter(angle_lrc)
    angle2 = p.readUserDebugParameter(angle_lmj)
    angle3 = p.readUserDebugParameter(angle_lmt)
    angle4 = p.readUserDebugParameter(angle_lmc)
    angle5 = p.readUserDebugParameter(angle_lfj)
    angle6 = p.readUserDebugParameter(angle_lft)
    angle7 = p.readUserDebugParameter(angle_lfc)
    angle8 = p.readUserDebugParameter(angle_rrt)
    angle9 = p.readUserDebugParameter(angle_rrc)
    angle10 = p.readUserDebugParameter(angle_rmj)
    angle11 = p.readUserDebugParameter(angle_rmt)
    angle12 = p.readUserDebugParameter(angle_rmc)
    angle13 = p.readUserDebugParameter(angle_rfj)
    angle14 = p.readUserDebugParameter(angle_rft)
    angle15 = p.readUserDebugParameter(angle_rfc)
    for joint_index in left_rear_thigh:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle0)
    for joint_index in left_rear_calf:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle1)
    for joint_index in left_middle_joint:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle2)
    for joint_index in left_middle_thigh:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle3)
    for joint_index in left_middle_calf:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle4)
    for joint_index in left_front_joint:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle5)
    for joint_index in left_front_thigh:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle6)
    for joint_index in left_front_calf:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle7)
    for joint_index in right_rear_thigh:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle8)
    for joint_index in right_rear_calf:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle9)
    for joint_index in right_middle_joint:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle10)
    for joint_index in right_middle_thigh:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle11)
    for joint_index in right_middle_calf:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle12)
    for joint_index in right_front_joint:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle13)
    for joint_index in right_front_thigh:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle14)
    for joint_index in right_front_calf:
        p.setJointMotorControl2(grasshopper, joint_index, p.POSITION_CONTROL, targetPosition=angle15)
    p.stepSimulation()
