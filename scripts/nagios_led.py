#!/usr/bin/python

with open('nagios_led.raw', 'r') as f:
  first_line = f.readline()

numbers=first_line.split(",")

hosts_tot=numbers[0]
hosts_up=numbers[1]
hosts_down=numbers[2]
srv_tot=numbers[3]
srv_ok=numbers[4]
srv_crit=numbers[5]


def color(tot,ok,nok):
	if tot == ok:
		return 'green'
	if nok == '0':
		return 'orange'
	return 'red'

print 'Hosts    :', color(hosts_tot,hosts_up,hosts_down)
print 'Services :', color(srv_tot,srv_ok,srv_crit)
