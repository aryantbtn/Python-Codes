# Shutdown PC, Computer using Python
# Compile Python Program in .exe (using py2exe) and give it to somebody
# Or use this program in any shutdown application.
import os
def shutdown_PC(time):
    os.system(f"shutdown /s /t {time}")
shutdown_PC(300)