import pybullet as p # ...
import numpy as n
import pandas as pd
import time as t


def move(grasshopper, times, t_sleep):

    lrt = 0
    lrc = 1
    lmj = 3
    lmt = 4
    lmc = 5
    lfj = 7
    lft = 8
    lfc = 9
    rrt = 11
    rrc = 12
    rmj = 14
    rmt = 15
    rmc = 16
    rfj = 18
    rft = 19
    rfc = 20

    lr = pd.read_excel('theta_lr_stage0.xlsx', header=None)
    lr = n.array(lr)
    lm = pd.read_excel('theta_lm_stage0.xlsx', header=None)
    lm = n.array(lm)
    lf = pd.read_excel('theta_lf_stage0.xlsx', header=None)
    lf = n.array(lf)
    rr = pd.read_excel('theta_rr_stage0.xlsx', header=None)
    rr = n.array(rr)
    rm = pd.read_excel('theta_rm_stage0.xlsx', header=None)
    rm = n.array(rm)
    rf = pd.read_excel('theta_rf_stage0.xlsx', header=None)
    rf = n.array(rf)

    lr1 = pd.read_excel('theta_lr_stage1.xlsx', header=None)
    lr1 = n.array(lr1)
    lm1 = pd.read_excel('theta_lm_stage1.xlsx', header=None)
    lm1 = n.array(lm1)
    lf1 = pd.read_excel('theta_lf_stage1.xlsx', header=None)
    lf1 = n.array(lf1)
    rr1 = pd.read_excel('theta_rr_stage1.xlsx', header=None)
    rr1 = n.array(rr1)
    rm1 = pd.read_excel('theta_rm_stage1.xlsx', header=None)
    rm1 = n.array(rm1)
    rf1 = pd.read_excel('theta_rf_stage1.xlsx', header=None)
    rf1 = n.array(rf1)

    lr2 = pd.read_excel('theta_lr_stage2.xlsx', header=None)
    lr2 = n.array(lr2)
    lm2 = pd.read_excel('theta_lm_stage2.xlsx', header=None)
    lm2 = n.array(lm2)
    lf2 = pd.read_excel('theta_lf_stage2.xlsx', header=None)
    lf2 = n.array(lf2)
    rr2 = pd.read_excel('theta_rr_stage2.xlsx', header=None)
    rr2 = n.array(rr2)
    rm2 = pd.read_excel('theta_rm_stage2.xlsx', header=None)
    rm2 = n.array(rm2)
    rf2 = pd.read_excel('theta_rf_stage2.xlsx', header=None)
    rf2 = n.array(rf2)

    i = 0
    j = 1
    k = 0
    tt = 0

    while tt <= 10000000000:

        while j <= 960:
            j += 1
            p.stepSimulation()

        j = 0

        while i <= 98:

            if t_sleep == 1:

                t.sleep(0.001)

            lrtp = lr[i, 0]
            lrcp = lr[i, 1]
            lmjp = lm[i, 0]
            lmtp = -lm[i, 1]
            lmcp = lm[i, 2]
            lfjp = lf[i, 0]
            lftp = -lf[i, 1]
            lfcp = lf[i, 2]
            rrtp = -rr[i, 0]
            rrcp = rr[i, 1]
            rmjp = rm[i, 0]
            rmtp = -rm[i, 1]
            rmcp = rm[i, 2]
            rfjp = rf[i, 0]
            rftp = -rf[i, 1]
            rfcp = rf[i, 2]
            i += 1
            p.setJointMotorControl2(grasshopper, lrt, p.POSITION_CONTROL, targetPosition=lrtp)
            p.setJointMotorControl2(grasshopper, lrc, p.POSITION_CONTROL, targetPosition=lrcp)
            p.setJointMotorControl2(grasshopper, lmj, p.POSITION_CONTROL, targetPosition=lmjp)
            p.setJointMotorControl2(grasshopper, lmt, p.POSITION_CONTROL, targetPosition=lmtp)
            p.setJointMotorControl2(grasshopper, lmc, p.POSITION_CONTROL, targetPosition=lmcp)
            p.setJointMotorControl2(grasshopper, lfj, p.POSITION_CONTROL, targetPosition=lfjp)
            p.setJointMotorControl2(grasshopper, lft, p.POSITION_CONTROL, targetPosition=lftp)
            p.setJointMotorControl2(grasshopper, lfc, p.POSITION_CONTROL, targetPosition=lfcp)
            p.setJointMotorControl2(grasshopper, rrt, p.POSITION_CONTROL, targetPosition=rrtp)
            p.setJointMotorControl2(grasshopper, rrc, p.POSITION_CONTROL, targetPosition=rrcp)
            p.setJointMotorControl2(grasshopper, rmj, p.POSITION_CONTROL, targetPosition=rmjp)
            p.setJointMotorControl2(grasshopper, rmt, p.POSITION_CONTROL, targetPosition=rmtp)
            p.setJointMotorControl2(grasshopper, rmc, p.POSITION_CONTROL, targetPosition=rmcp)
            p.setJointMotorControl2(grasshopper, rfj, p.POSITION_CONTROL, targetPosition=rfjp)
            p.setJointMotorControl2(grasshopper, rft, p.POSITION_CONTROL, targetPosition=rftp)
            p.setJointMotorControl2(grasshopper, rfc, p.POSITION_CONTROL, targetPosition=rfcp)
            p.stepSimulation()

        while j <= 120:
            j += 1
            p.stepSimulation()

        j = 0

        while k <= times:

            i = 0

            while i <= 97:

                if t_sleep == 1:

                    t.sleep(0.001)

                lrtp1 = lr1[i, 0]
                lrcp1 = lr1[i, 1]
                lmjp1 = lm1[i, 0]
                lmtp1 = -lm1[i, 1]
                lmcp1 = lm1[i, 2]
                lfjp1 = lf1[i, 0]
                lftp1 = -lf1[i, 1]
                lfcp1 = lf1[i, 2]
                rrtp1 = -rr1[i, 0]
                rrcp1 = rr1[i, 1]
                rmjp1 = rm1[i, 0]
                rmtp1 = -rm1[i, 1]
                rmcp1 = rm1[i, 2]
                rfjp1 = rf1[i, 0]
                rftp1 = -rf1[i, 1]
                rfcp1 = rf1[i, 2]
                i += 1
                p.setJointMotorControl2(grasshopper, lrt, p.POSITION_CONTROL, targetPosition=lrtp1)
                p.setJointMotorControl2(grasshopper, lrc, p.POSITION_CONTROL, targetPosition=lrcp1)
                p.setJointMotorControl2(grasshopper, lmj, p.POSITION_CONTROL, targetPosition=lmjp1)
                p.setJointMotorControl2(grasshopper, lmt, p.POSITION_CONTROL, targetPosition=lmtp1)
                p.setJointMotorControl2(grasshopper, lmc, p.POSITION_CONTROL, targetPosition=lmcp1)
                p.setJointMotorControl2(grasshopper, lfj, p.POSITION_CONTROL, targetPosition=lfjp1)
                p.setJointMotorControl2(grasshopper, lft, p.POSITION_CONTROL, targetPosition=lftp1)
                p.setJointMotorControl2(grasshopper, lfc, p.POSITION_CONTROL, targetPosition=lfcp1)
                p.setJointMotorControl2(grasshopper, rrt, p.POSITION_CONTROL, targetPosition=rrtp1)
                p.setJointMotorControl2(grasshopper, rrc, p.POSITION_CONTROL, targetPosition=rrcp1)
                p.setJointMotorControl2(grasshopper, rmj, p.POSITION_CONTROL, targetPosition=rmjp1)
                p.setJointMotorControl2(grasshopper, rmt, p.POSITION_CONTROL, targetPosition=rmtp1)
                p.setJointMotorControl2(grasshopper, rmc, p.POSITION_CONTROL, targetPosition=rmcp1)
                p.setJointMotorControl2(grasshopper, rfj, p.POSITION_CONTROL, targetPosition=rfjp1)
                p.setJointMotorControl2(grasshopper, rft, p.POSITION_CONTROL, targetPosition=rftp1)
                p.setJointMotorControl2(grasshopper, rfc, p.POSITION_CONTROL, targetPosition=rfcp1)
                p.stepSimulation()

            while j <= 120:
                j += 1
                p.stepSimulation()

            j = 0

            ######################################

            i = 0

            while i <= 97:

                if t_sleep == 1:

                    t.sleep(0.001)

                lrtp2 = lr2[i, 0]
                lrcp2 = lr2[i, 1]
                lmjp2 = lm2[i, 0]
                lmtp2 = -lm2[i, 1]
                lmcp2 = lm2[i, 2]
                lfjp2 = lf2[i, 0]
                lftp2 = -lf2[i, 1]
                lfcp2 = lf2[i, 2]
                rrtp2 = -rr2[i, 0]
                rrcp2 = rr2[i, 1]
                rmjp2 = rm2[i, 0]
                rmtp2 = -rm2[i, 1]
                rmcp2 = rm2[i, 2]
                rfjp2 = rf2[i, 0]
                rftp2 = -rf2[i, 1]
                rfcp2 = rf2[i, 2]
                i += 1
                p.setJointMotorControl2(grasshopper, lrt, p.POSITION_CONTROL, targetPosition=lrtp2)
                p.setJointMotorControl2(grasshopper, lrc, p.POSITION_CONTROL, targetPosition=lrcp2)
                p.setJointMotorControl2(grasshopper, lmj, p.POSITION_CONTROL, targetPosition=lmjp2)
                p.setJointMotorControl2(grasshopper, lmt, p.POSITION_CONTROL, targetPosition=lmtp2)
                p.setJointMotorControl2(grasshopper, lmc, p.POSITION_CONTROL, targetPosition=lmcp2)
                p.setJointMotorControl2(grasshopper, lfj, p.POSITION_CONTROL, targetPosition=lfjp2)
                p.setJointMotorControl2(grasshopper, lft, p.POSITION_CONTROL, targetPosition=lftp2)
                p.setJointMotorControl2(grasshopper, lfc, p.POSITION_CONTROL, targetPosition=lfcp2)
                p.setJointMotorControl2(grasshopper, rrt, p.POSITION_CONTROL, targetPosition=rrtp2)
                p.setJointMotorControl2(grasshopper, rrc, p.POSITION_CONTROL, targetPosition=rrcp2)
                p.setJointMotorControl2(grasshopper, rmj, p.POSITION_CONTROL, targetPosition=rmjp2)
                p.setJointMotorControl2(grasshopper, rmt, p.POSITION_CONTROL, targetPosition=rmtp2)
                p.setJointMotorControl2(grasshopper, rmc, p.POSITION_CONTROL, targetPosition=rmcp2)
                p.setJointMotorControl2(grasshopper, rfj, p.POSITION_CONTROL, targetPosition=rfjp2)
                p.setJointMotorControl2(grasshopper, rft, p.POSITION_CONTROL, targetPosition=rftp2)
                p.setJointMotorControl2(grasshopper, rfc, p.POSITION_CONTROL, targetPosition=rfcp2)
                p.stepSimulation()

            while j <= 120:

                j += 1
                p.stepSimulation()

            j = 0

            k += 1

        p.stepSimulation()
        tt += 1
