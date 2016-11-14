from subprocess import call

call(["nagios3stats", "-m", "--data=NUMHOSTS,NUMHSTUP,NUMHSTDOWN,NUMSERVICES,NUMSVCOK,NUMSVCCRIT", "-D,"])
