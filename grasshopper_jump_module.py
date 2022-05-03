import pybullet as p # ...
import numpy as n
import time as t


def jump(grasshopper, j1_lmax, j1_final, j2_final, f):

    lrt = 0
    lrc = 1
    rrt = 11
    rrc = 12
    initial_position_lrt: float = 0.69350062
    initial_position_lrc: float = -1.90503829

    pi: float = 3.1415926535897932384626
    g = 9.81

    m1 = 0.00102510748433604
    m2 = 0.000112847642201865
    m3 = 0.000139426648488346
    l1 = 0.075
    l2 = 0.06349622739
    lc1 = 0.026128698
    lc2 = 0.03111024805
    lc3 = l2 + 0.00046191062

    # true represents data for real grasshopper. SI
    k_pe_true = 8
    k_se_true = 1000
    c_true = 10
    f_max_true = 100 * 10 ** (-3)
    k_pve_true = 10 ** (-6)
    # c_pve_true = 10 ** (-6)
    r_true = 500 * 10 ** (-6)
    # l1_true = 10 * 10 ** (-3)
    # j_limb_true = 320 * 10 ** (-12)

    scl = 7.5  # scalar

    # data for robot. SI
    k_pe = k_pe_true * scl ** 2 / 10
    k_se = k_se_true * scl ** 2
    c = c_true * scl ** 2.5 / 6.565
    f_max = f_max_true * scl ** 3  # = 42.1875 N
    k_pve = k_pve_true * scl ** 4
    # c_pve = c_pve_true * scl ** 4.5  # actually in URDF this value is set to 0.00001. Higher causes bugs.
    r = r_true * scl
    # l1 = l1_true * scl
    # j_limb = j_limb_true * scl ** 5

    l_rest = 0.075
    dl_over_dt = 10 ** -4
    dt = 0.01
    ft = 0

    k_pve_initial_angle = initial_position_lrc
    l_ext_rest = n.sqrt(2 * r * r * (1 - n.cos(k_pve_initial_angle)) + l1 * l1
                        - 2 * r * l1 * n.sin(k_pve_initial_angle))
    l_flx_rest = n.sqrt(2 * r * r * (1 - n.cos(k_pve_initial_angle)) + l1 * l1
                        + 2 * r * l1 * n.sin(k_pve_initial_angle))

    i = 0
    j = 0
    k = 0
    k2 = 0
    k3 = 0
    spring_release = 0

    t.sleep(1)

    while True:

        while i <= 240:

            # t.sleep(0.0001)
            p.stepSimulation()
            i += 1

        if k <= 0:

            p.setJointMotorControl2(grasshopper, lrt, p.POSITION_CONTROL, targetPosition=initial_position_lrt, force=0)
            p.setJointMotorControl2(grasshopper, lrc, p.POSITION_CONTROL, targetPosition=initial_position_lrc, force=0)

        # -------------------------------------USE FOR TESTING STABILITY------------------------------------
        # while j <= 2400000000000000000:
        #
        #     # t.sleep(0.001)
        #     joint_lrt_state = p.getJointState(grasshopper, lrt)
        #     joint_lrc_state = p.getJointState(grasshopper, lrc)
        #     q1 = joint_lrt_state[0]
        #     q2 = joint_lrc_state[0]
        #     K1 = (q1 - 0.69350062) * 0.1
        #     K2 = (q2 - (-1.90503829)) * 0.1
        #     G1 = m1 * g * lc1 * n.cos(q1) + m2 * g * (l1 * n.cos(q1) + lc2 * n.cos(q1 + q2)) + \
        #         m3 * g * (l1 * n.cos(q1) + lc3 * n.cos(q1 + q2))
        #     G2 = m2 * g * (lc2 * n.cos(q1 + q2)) + m3 * g * (lc3 * n.cos(q1 + q2))
        #     p.setJointMotorControl2(grasshopper, lrt, p.TORQUE_CONTROL, force=G1-K1)
        #     p.setJointMotorControl2(grasshopper, lrc, p.TORQUE_CONTROL, force=G2-K2)
        #     p.stepSimulation()
        #     j += 1
        #     print(G2)
        #     print(q2)
        # ---------------------------------------------------------------------------------------------------

        while k <= 0:

            j1_fix = 0
            j2_fix = 0
            fix_status = j1_fix + j2_fix
            reach_times = 0
            j2_reach_times = 0

            # --------------

            # tension_up = 0
            # tension_down = 0
            # d_l_up = 0
            # d_l_down = 0
            #
            # tension_ext = 0
            # tension_flx = 0
            # d_l_ext = 0
            # d_l_flx = 0

            # --------------

            while fix_status <= 1.5:

                # t.sleep(0.001)
                joint_lrt_state = p.getJointState(grasshopper, lrt)
                joint_lrc_state = p.getJointState(grasshopper, lrc)
                q1 = joint_lrt_state[0]
                q2 = joint_lrc_state[0]

                # -----------------------------------------------------------------------------------

                # l_ext = n.sqrt(2 * r * r * (1 - n.cos(q2)) + l1 * l1 - 2 * r * l1 * n.sin(q2))
                # l_flx = n.sqrt(2 * r * r * (1 - n.cos(q2)) + l1 * l1 + 2 * r * l1 * n.sin(q2))
                # d_tension_ext = k_se / c * (
                #             -(1 + k_pe / k_se) * tension_ext + k_pe * (l_ext - l_ext_rest) + c * d_l_ext + f)
                # d_tension_flx = k_se / c * (
                #         -(1 + k_pe / k_se) * tension_flx + k_pe * (l_flx - l_flx_rest) + c * d_l_flx + f)
                # tension_ext += d_tension_ext * 1 / 240
                # tension_flx += d_tension_flx * 1 / 240
                # tau_ext = 0 + f * r * n.cos(pi / 2 - n.abs(q2))
                # tau_flx = 0 - f * r * n.cos(pi / 2 - n.abs(q2))
                # # print('tau_ext =', tau_ext, 'tau_flx =', tau_flx)
                # print(l_flx)

                # -------------------------------------------------------------------------------

                g1 = m1 * g * lc1 * n.cos(q1) + m2 * g * (l1 * n.cos(q1) + lc2 * n.cos(q1 + q2)) + \
                    m3 * g * (l1 * n.cos(q1) + lc3 * n.cos(q1 + q2))
                g2 = m2 * g * (lc2 * n.cos(q1 + q2)) + m3 * g * (lc3 * n.cos(q1 + q2))

                torque_spring = k_pve * (k_pve_initial_angle - q2)
                j1_torque_input_up = g1 + 0.6 / 100000 + torque_spring
                j1_torque_input_down = g1 - 0.1 / 100000 + torque_spring
                j2_torque_input_inward = g2 - 0.4 / 100000 + torque_spring
                # j2_torque_input_outward = g2 + 0.4 / 100000 + torque_spring

                fj2_in = j2_torque_input_inward / r / n.cos(-pi / 2 + n.abs(q2))
                # print('tension =', fj2_in)

                # print(torque_spring)

                if q1 < j1_lmax:

                    if reach_times <= 0:

                        p.setJointMotorControl2(grasshopper, lrt, p.TORQUE_CONTROL,
                                                force=j1_torque_input_up - torque_spring)
                        j1_fix = 0
                        # print('torque =', j1_torque_input_up - torque_spring)
                    else:

                        if q1 >= j1_final + 0.05:

                            p.setJointMotorControl2(grasshopper, lrt, p.TORQUE_CONTROL,
                                                    force=j1_torque_input_down - torque_spring)
                            j1_fix = 0
                            # print('torque =', j1_torque_input_down - torque_spring)
                        else:

                            p.setJointMotorControl2(grasshopper, lrt, p.POSITION_CONTROL, targetPosition=q1)
                            j1_fix = 1
                else:

                    reach_times += 1
                    p.setJointMotorControl2(grasshopper, lrt, p.TORQUE_CONTROL,
                                            force=j1_torque_input_down - torque_spring)
                    j1_fix = 0
                    # print('torque =', j1_torque_input_down - torque_spring)

                if j2_reach_times <= 0:

                    if q2 > j2_final:

                        p.setJointMotorControl2(grasshopper, lrc, p.TORQUE_CONTROL,
                                                force=j2_torque_input_inward - torque_spring)

                        j2_fix = 0
                        # print('torque2 =', j2_torque_input_inward - torque_spring)
                    else:

                        p.setJointMotorControl2(grasshopper, lrc, p.POSITION_CONTROL, targetPosition=q2)
                        j2_fix = 1
                        j2_reach_times += 1
                else:
                    p.setJointMotorControl2(grasshopper, lrc, p.POSITION_CONTROL, targetPosition=q2)
                    j2_fix = 1

                p.stepSimulation()
                fix_status = j1_fix + j2_fix
                # print("fix_status =", fix_status)

                # -----------------------------------

                # joint_lrc_state_2 = p.getJointState(grasshopper, lrc)
                # q2_2 = joint_lrc_state_2[0]
                # l_ext_2 = n.sqrt(2 * r * r * (1 - n.cos(q2_2)) + l1 * l1 - 2 * r * l1 * n.sin(q2_2))
                # l_flx_2 = n.sqrt(2 * r * r * (1 - n.cos(q2_2)) + l1 * l1 + 2 * r * l1 * n.sin(q2_2))
                # d_l_ext = (l_ext_2 - l_ext)
                # d_l_flx = (l_flx_2 - l_flx)
                # # print('d_l_ext =', d_l_ext, 'd_l_flx =', d_l_flx)

                # -----------------------------------

                if fix_status >= 1.5:
                    k += 1

        if k2 <= 0:
            p.setJointMotorControl2(grasshopper, rrt, p.POSITION_CONTROL, targetPosition=initial_position_lrt, force=0)
            p.setJointMotorControl2(grasshopper, rrc, p.POSITION_CONTROL, targetPosition=initial_position_lrc, force=0)

        while k2 <= 0:

            j1_fix = 0
            j2_fix = 0
            fix_status = j1_fix + j2_fix
            reach_times = 0
            j2_reach_times = 0

            while fix_status <= 1.5:

                # t.sleep(0.001)
                joint_rrt_state = p.getJointState(grasshopper, rrt)
                joint_rrc_state = p.getJointState(grasshopper, rrc)
                q1 = joint_rrt_state[0]
                q2 = joint_rrc_state[0]
                g1 = m1 * g * lc1 * n.cos(q1) + m2 * g * (l1 * n.cos(q1) + lc2 * n.cos(q1 + q2)) + \
                    m3 * g * (l1 * n.cos(q1) + lc3 * n.cos(q1 + q2))
                g2 = m2 * g * (lc2 * n.cos(q1 + q2)) + m3 * g * (lc3 * n.cos(q1 + q2))

                torque_spring = k_pve * (k_pve_initial_angle - q2)
                j1_torque_input_up = g1 + 0.6 / 100000 + torque_spring
                j1_torque_input_down = g1 - 0.1 / 100000 + torque_spring
                j2_torque_input_inward = g2 - 0.8 / 100000 + torque_spring
                # j2_torque_input_outward = g2 + 0.8 / 100000 + torque_spring

                if q1 < j1_lmax + 0.1:

                    if reach_times <= 0:

                        p.setJointMotorControl2(grasshopper, rrt, p.TORQUE_CONTROL,
                                                force=j1_torque_input_up - torque_spring)
                        j1_fix = 0
                    else:

                        if q1 >= j1_final + 0.1:

                            p.setJointMotorControl2(grasshopper, rrt, p.TORQUE_CONTROL,
                                                    force=j1_torque_input_down - torque_spring)
                            j1_fix = 0
                        else:

                            p.setJointMotorControl2(grasshopper, rrt, p.POSITION_CONTROL, targetPosition=q1)
                            j1_fix = 1
                else:

                    reach_times += 1
                    p.setJointMotorControl2(grasshopper, rrt, p.TORQUE_CONTROL,
                                            force=j1_torque_input_down - torque_spring)
                    j1_fix = 0

                if j2_reach_times <= 0:

                    if q2 > j2_final:

                        p.setJointMotorControl2(grasshopper, rrc, p.TORQUE_CONTROL,
                                                force=j2_torque_input_inward - torque_spring)
                        j2_fix = 0
                        # print('torque2 =', j2_torque_input_inward - torque_spring)
                    else:

                        p.setJointMotorControl2(grasshopper, rrc, p.POSITION_CONTROL, targetPosition=q2)
                        j2_fix = 1
                        j2_reach_times += 1
                else:
                    p.setJointMotorControl2(grasshopper, rrc, p.POSITION_CONTROL, targetPosition=q2)
                    j2_fix = 1

                p.stepSimulation()
                fix_status = j1_fix + j2_fix
                # print(q1)

                if fix_status >= 1.5:
                    k2 += 1

        t.sleep(0.5)
        joint_lrc_state = p.getJointState(grasshopper, lrc)
        q2 = joint_lrc_state[0]
        torque_spring = k_pve * (k_pve_initial_angle - q2)

        if k3 <= 0:

            p.setJointMotorControl2(grasshopper, lrc, p.POSITION_CONTROL, targetPosition=initial_position_lrc, force=0)
            p.setJointMotorControl2(grasshopper, rrc, p.POSITION_CONTROL, targetPosition=initial_position_lrc, force=0)

        position = p.getBasePositionAndOrientation(grasshopper)
        x_ini = position[0][0]
        z_max = 0
        x_final = 0

        while k3 <= 100000000000:

            if spring_release <= 0:

                if ft <= f * 1.1:

                    # dft_over_dt = k_se / c * (-(1 + k_pe / k_se) * ft + k_pe * (l1 - l_rest) + c * dl_over_dt + f)
                    # ft += (dft_over_dt * dt)
                    # l1 -= dl_over_dt * dt
                    ft = f

                torque_jump = 0 + ft * r * n.cos(-pi / 2 + n.abs(q2))
                # print(ft)
                p.setJointMotorControl2(grasshopper, lrc, p.TORQUE_CONTROL, force=torque_spring + torque_jump)
                p.setJointMotorControl2(grasshopper, rrc, p.TORQUE_CONTROL, force=torque_spring + torque_jump)
                # p.setJointMotorControl2(grasshopper, lrc, p.VELOCITY_CONTROL, targetVelocity=200)
                # p.setJointMotorControl2(grasshopper, rrc, p.VELOCITY_CONTROL, targetVelocity=200)

                if ft >= f * 0.9:

                    spring_release += 1

            # print('q2 =', q2)
            t.sleep(0.001)
            k3 += 1
            # spring_release += 1
            position = p.getBasePositionAndOrientation(grasshopper)
            v = p.getBaseVelocity(grasshopper)
            vx = n.abs(v[0][0])
            vy = n.abs(v[0][1])
            vz = n.abs(v[0][2])
            # wx = v[1][0]
            # wy = v[1][1]
            # wz = v[1][2]

            x_pre = position[0][0]
            y_pre = position[0][1]
            z_pre = position[0][2]

            if vx <= 5*10**-4 and vy <= 5*10**-4 and vz <= 5*10**-4:

                x_final = x_pre
                # y_final = y_pre
                # z_final = z_pre

                break

            print('base_position =', position)
            p.stepSimulation()

            position = p.getBasePositionAndOrientation(grasshopper)
            # x = position[0][0]
            # y = position[0][1]
            z = position[0][2]

            if z > z_pre:

                if z > z_max:

                    z_max = z

        print('jump complete')
        print('when f =', f, ',', 'z_max =', z_max)

        while j <= 10000000000:

            p.stepSimulation()
            j += 1

        p.stepSimulation()

        jump_complete = 1
        return jump_complete
