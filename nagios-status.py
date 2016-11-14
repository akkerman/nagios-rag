#!/usr/bin/python
from subprocess import check_output

output = check_output(["nagios3stats", "-m", "--data=NUMHOSTS,NUMHSTUP,NUMHSTDOWN,NUMSERVICES,NUMSVCOK,NUMSVCCRIT", "-D,"])


hosts_tot,hosts_up,hosts_down,srv_tot,srv_ok,srv_crit,z = output.split(",")

def color(tot,ok,nok):
	if tot == ok:
		return 'green'
	if nok == '0':
		return 'amber'
	return 'red'

print 'Hosts    :', color(hosts_tot,hosts_up,hosts_down)
print 'Services :', color(srv_tot,srv_ok,srv_crit)
