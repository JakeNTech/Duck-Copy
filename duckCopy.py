import subprocess
for i in range(0,2741768):
    filename = "/etc/d/duck"+str(i)+".png"
    process = subprocess.Popen(["cp","./ducko.png",filename], stdin=subprocess.PIPE)
    process.stdin.close()