import pybullet as p # ...
import pybullet_data
import time as t
import grasshopper_initial_setup

g = 9.81
pi: float = 3.1415926535897932384626

p.connect(p.GUI)
p.setGravity(0, 0, -g)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
plane = p.loadURDF('plane.urdf')
grasshopper = p.loadURDF('C:/Users/41725/Desktop/grasshopper_v16/urdf/'
                         'grasshopper_v16.urdf', basePosition=[0, 0, 0.15], baseOrientation=[pi/2, 0, 0, 0])

setup = grasshopper_initial_setup.setup(grasshopper)

t.sleep(2)

i = 0
j = 0
k = 0
lrt = 0
lrc = 1
rrt = 11
rrc = 12
initial_position_lrt: float = 0.69350062
initial_position_lrc: float = -1.90503829
ff = 6.5 * 10 ** -2

while True:

    while j <= 960:

        p.stepSimulation()
        j += 1

    if k <= 0:

        t.sleep(0.0001)
        p.setJointMotorControl2(grasshopper, lrt, p.POSITION_CONTROL, targetPosition=initial_position_lrt, force=0)
        p.setJointMotorControl2(grasshopper, rrt, p.POSITION_CONTROL, targetPosition=initial_position_lrc, force=0)
        k += 1

    if i <= 0:

        t.sleep(0.0001)
        p.setJointMotorControl2(grasshopper, lrt, p.TORQUE_CONTROL, force=ff)
        p.setJointMotorControl2(grasshopper, rrt, p.TORQUE_CONTROL, force=ff)
        p.stepSimulation()
        i += 1

    t.sleep(0.0001)
    p.stepSimulation()
