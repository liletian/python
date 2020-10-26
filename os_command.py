#python -c "import os, sys; print(os.path.dirname(sys.executable))"#

import os
os.chdir(path)
print("Current Working Directory " , os.getcwd())
os.chdir("/home/varun/temp")


try:
    # Change the current working Directory    
    os.chdir("/home/varun/temp")
    print("Directory changed")
except OSError:
    print("Can't change the Current Working Directory") 
    
    
# Check if New path exists
if os.path.exists("/home/varun/temp") :
    # Change the current working Directory    
    os.chdir("/home/varun/temp")
else:
    print("Can't change the Current Working Directory")  
