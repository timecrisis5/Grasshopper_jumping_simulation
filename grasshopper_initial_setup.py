import pybullet as p  # ... 


def setup(grasshopper):

    lrt = 0
    lrc = 1
    lrf = 2

    lmj = 3
    lmt = 4
    lmc = 5
    lmf = 6

    lfj = 7
    lft = 8
    lfc = 9
    lff = 10

    rrt = 11
    rrc = 12
    rrf = 13

    rmj = 14
    rmt = 15
    rmc = 16
    rmf = 17

    rfj = 18
    rft = 19
    rfc = 20
    rff = 21

    initial_position_lrt: float = 0.69350062
    initial_position_lrc: float = -1.90503829
    initial_position_lmj: float = 0.62879629
    initial_position_lmt: float = 0.48494658
    initial_position_lmc: float = -1.8315209
    initial_position_lfj: float = -0.5404195
    initial_position_lft: float = 0.5269896
    initial_position_lfc: float = -2.01078018

    # initial_position_lrt: float = 0
    # initial_position_lrc: float = 0
    # initial_position_lfj: float = 0
    # initial_position_lft: float = 0
    # initial_position_lfc: float = 0
    # initial_position_rmj: float = 0
    # initial_position_rmt: float = 0
    # initial_position_rmc: float = 0

    p.setJointMotorControl2(grasshopper, lrt, p.POSITION_CONTROL, targetPosition=initial_position_lrt)
    p.setJointMotorControl2(grasshopper, lrc, p.POSITION_CONTROL, targetPosition=initial_position_lrc)
    p.setJointMotorControl2(grasshopper, lmj, p.POSITION_CONTROL, targetPosition=initial_position_lmj)
    p.setJointMotorControl2(grasshopper, lmt, p.POSITION_CONTROL, targetPosition=initial_position_lmt)
    p.setJointMotorControl2(grasshopper, lmc, p.POSITION_CONTROL, targetPosition=initial_position_lmc)
    p.setJointMotorControl2(grasshopper, lfj, p.POSITION_CONTROL, targetPosition=initial_position_lfj)
    p.setJointMotorControl2(grasshopper, lft, p.POSITION_CONTROL, targetPosition=initial_position_lft)
    p.setJointMotorControl2(grasshopper, lfc, p.POSITION_CONTROL, targetPosition=initial_position_lfc)
    p.setJointMotorControl2(grasshopper, rrt, p.POSITION_CONTROL, targetPosition=initial_position_lrt)
    p.setJointMotorControl2(grasshopper, rrc, p.POSITION_CONTROL, targetPosition=initial_position_lrc)
    p.setJointMotorControl2(grasshopper, rmj, p.POSITION_CONTROL, targetPosition=-initial_position_lmj)
    p.setJointMotorControl2(grasshopper, rmt, p.POSITION_CONTROL, targetPosition=initial_position_lmt)
    p.setJointMotorControl2(grasshopper, rmc, p.POSITION_CONTROL, targetPosition=initial_position_lmc)
    p.setJointMotorControl2(grasshopper, rfj, p.POSITION_CONTROL, targetPosition=-initial_position_lfj)
    p.setJointMotorControl2(grasshopper, rft, p.POSITION_CONTROL, targetPosition=initial_position_lft)
    p.setJointMotorControl2(grasshopper, rfc, p.POSITION_CONTROL, targetPosition=initial_position_lfc)

    p.setJointMotorControl2(grasshopper, lrf, p.POSITION_CONTROL, targetPosition=0)
    p.setJointMotorControl2(grasshopper, lmf, p.POSITION_CONTROL, targetPosition=0)
    p.setJointMotorControl2(grasshopper, lff, p.POSITION_CONTROL, targetPosition=0)
    p.setJointMotorControl2(grasshopper, rrf, p.POSITION_CONTROL, targetPosition=0)
    p.setJointMotorControl2(grasshopper, rmf, p.POSITION_CONTROL, targetPosition=0)
    p.setJointMotorControl2(grasshopper, rff, p.POSITION_CONTROL, targetPosition=0)

    setup_complete = 1
    return setup_complete
