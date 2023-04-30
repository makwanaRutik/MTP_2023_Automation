#To open gdb. 
from pygdbmi.gdbcontroller import GdbController
#To use gdb commands and get gdb console outputs.
from pygdbmi import gdbmiparser
#To name log files.
from datetime import datetime
#To verify gdb console outputs.
import re
# To handle arguments to the script
import sys
#To start openocd session
import os
import time
import MINITERM_MTP


if __name__ == "__main__":

	print("Starting copy to Flash\n")
	elf = "file "+ sys.argv[1]
	path_to_sdk = os.getenv("SHAKTISDK")
	if path_to_sdk == None:
		print("Set environmental variable SHAKTISDK")
		exit()
	print(path_to_sdk)

	

	#gdb = path_to_sdk+'/shakti-tools/bin/riscv32-unknown-elf-gdb'
	gdb = 'riscv64-unknown-elf-gdb'
	elf = "file "+ path_to_sdk + "/" + "software/examples/uart_applns/first/output/mybaudrate.shakti"

	gdbLocation = []
	gdbLocation.append(gdb)
	
	
	nextcommand = []
	nextcommand.append("target remote localhost:3333")
	nextcommand.append("set remotetimeout unlimited")
	nextcommand.append(elf)
	nextcommand.append("y")
	nextcommand.append("load")
	nextcommand.append("c")


	openocd_config = path_to_sdk +'/bsp/third_party/vajra/ftdi.cfg'
	runOpenOCD = '~/shakti-tool/bin/openocd -f ' + openocd_config +' &'

#create a openocd connection in background
	# print("open OCD COonnection..................................\n")
	os.system(runOpenOCD)
	time.sleep(2)
	
	# print("Creating GDB Object..................................\n")
	# gdbObject = GDB()
	# #gdbObject.gdbStart(command)

	# print("Crearing GDBController Object .......................\n")
	controllerObj = GdbController(gdbLocation , 5)

	# print("spawn_new_gdb_subprocess.............................\n")
	controllerObj.spawn_new_gdb_subprocess()

	# print("Calling Write Method ................................\n")
	controllerObj.write(nextcommand)

	# print("Checkpoint 5........................................\n")

	# for i in range(len(sys.argv)):
	# 	print()
	# 	print(i)
	# 	print(sys.argv[i])
	# 	print(type(sys.argv[i]))

	# pornName = sys
	# baudrate = int(sys.argv[3])
	MINITERM_MTP.mainOfMiniterm()


#execute commands 
	
#close gdb
	time.sleep(1)
	controllerObj.exit()
#close openocd
	os.system("pkill openocd")

