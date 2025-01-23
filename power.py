import platform
import os
def shutdown():
     if(platform.system()=="Windows"):
        os.system('shutdown /s /t 0')
     elif(platform.system=="Darwin"or platform.sytem=="Linux"):
        os.system('shutdown now')
     else:
        print("system is not supported")
def restart():
     if(platform.system=="Windows"):
        os.system('shutdown /r /t 0')
     elif(platform.system=="Darwin" or platform.system=="Linux"):
         os.system('reboot now')
     else:
         print("system not supported")
cmd=input("Enter the \'s for shutdown and \'r for restart system")
if(cmd=='s'):
    shutdown()
elif(cmd=='r'):
   restart()
else:
   print('enter the valid cmd')