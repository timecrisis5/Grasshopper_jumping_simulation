import time as t
import pybullet as p
import pybullet_data
import grasshopper_initial_setup
import grasshopper_jump_module
import grasshopper_move_module

g = 9.81

p.connect(p.GUI)
p.setGravity(0, 0, -g)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
plane = p.loadURDF('plane.urdf') # No need to be edited
grasshopper = p.loadURDF('C:/Users/41725/Desktop/grasshopper_v16/urdf/'
                         'grasshopper_v16.urdf', basePosition=[0, 0, 0.15])  # Don't forget to change this

setup = grasshopper_initial_setup.setup(grasshopper)

move = 114514
jump = 1919810

action_choose = jump  # can switch

# t.sleep(10)

if action_choose == move:

    move_times = 20
    t_sleep = 0

    move = grasshopper_move_module.move(grasshopper, move_times, t_sleep)

if action_choose == jump:

    j1_lmax = 0.85
    j1_final = 0.39210498
    j2_final = -2.84894699

    # j1_lmax = 0.85
    # j1_final = 0.22545029
    # j2_final = -2.9056915

    # f = 42.1875
    f = 1500
    jump = grasshopper_jump_module.jump(grasshopper, j1_lmax, j1_final, j2_final, f)

p.stepSimulation()
