#!/usr/bin/python
from subprocess import check_output


def rag(tot,ok,nok):
    if tot == ok:
        return '001' # green
    if nok == '0':
        return '010' # amber
    return '100'     # red

def nagios_rag():
    output = check_output(["nagios3stats", "-m", "--data=NUMHOSTS,NUMHSTUP,NUMHSTDOWN,NUMSERVICES,NUMSVCOK,NUMSVCCRIT", "-D,"])
    hosts_tot,hosts_up,hosts_down,srv_tot,srv_ok,srv_crit,z = output.split(",")

    host_rag = rag(hosts_tot,hosts_up,hosts_down)
    serv_rag = rag(srv_tot,srv_ok,srv_crit)
  
    return (host_rag, serv_rag)

if __name__ == "__main__": 
   print nagios_rag()
