import subprocess
import time

def is_process_running(process_name):
    cmd = f"pgrep -l {process_name}"
    try:
        output = subprocess.check_output(cmd,shell=True,text=True)
        return any(process_name in line for line in output.splitlines())
    except subprocess.CalledProcessError:
        return False


# Now keep zoom from opening
processes = ["zoom"]

while True:
    for process in processes:
        if is_process_running(process):
            #pid = subprocess.check_output(
            #    f"pgrep zoom",shell=True,text=True).replace("\n","")
            subprocess.run(f"pkill {process}",shell=True,text=True)
    time.sleep(0.5)
    