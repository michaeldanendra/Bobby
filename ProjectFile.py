import vrep
import time
import math
#--------------------------START SIMULATION----------------------------#
vrep.simxFinish(-1)
# Connect to V-REP (raise exception on failure)
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
if clientID == -1:
	raise Exception('Failed connecting to remote API server')
print('Simulation Begins')

# Get "handle" to the base of robot
result, base_handle = vrep.simxGetObjectHandle(clientID, 'UR3_link1_visible', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for base frame')
    
# Get "handle" to the all joints of robot
result, joint_one_handle = vrep.simxGetObjectHandle(clientID, 'UR3_joint1', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for first joint')
result, joint_two_handle = vrep.simxGetObjectHandle(clientID, 'UR3_joint2', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for second joint')
result, joint_three_handle = vrep.simxGetObjectHandle(clientID, 'UR3_joint3', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for third joint')
result, joint_four_handle = vrep.simxGetObjectHandle(clientID, 'UR3_joint4', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for fourth joint')
result, joint_five_handle = vrep.simxGetObjectHandle(clientID, 'UR3_joint5', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for fifth joint')
result, joint_six_handle = vrep.simxGetObjectHandle(clientID, 'UR3_joint6', vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for sixth joint')

position = [[math.pi*(2/6),0.5,1.875,-0.9,-1.875,-1.875],[math.pi*(4/6),0.5,1.875,-0.9,-1.875,-1.875], [math.pi,0.5,1.875,-0.9,-1.875,-1.875], [math.pi*(8/6),0.5,1.875,-0.9,-1.875,-1.875],[math.pi*(10/6),0.5,1.875,-0.9,-1.875,-1.875],[math.pi*2,0.5,1.875,-0.9,-1.875,-1.875]]
for i in range(6):
                theta = position[i]
                vrep.simxSetJointPosition(clientID, joint_one_handle, theta[0], vrep.simx_opmode_oneshot)
                time.sleep(0.5)
                vrep.simxSetJointPosition(clientID, joint_two_handle, theta[1], vrep.simx_opmode_oneshot)
                time.sleep(0.5)
                vrep.simxSetJointPosition(clientID, joint_three_handle, theta[2], vrep.simx_opmode_oneshot)
                time.sleep(0.5)
                vrep.simxSetJointPosition(clientID, joint_four_handle, theta[3], vrep.simx_opmode_oneshot)
                time.sleep(0.5)
                vrep.simxSetJointPosition(clientID, joint_five_handle, theta[4], vrep.simx_opmode_oneshot)
                time.sleep(0.5)
                vrep.simxSetJointPosition(clientID, joint_six_handle, theta[5], vrep.simx_opmode_oneshot)
                time.sleep(0.5)
                time.sleep(3)


# Stop simulation
vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
# Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
vrep.simxGetPingTime(clientID)
# Close the connection to V-REP
vrep.simxFinish(clientID)
print('Simulation Finished')
#----------------------FINISH SIMULATION------------------------------#
