#!/bin/bash

line=$(head -n 1 nagios_led.raw);
echo $line;
IFS=, read -a array <<< "$line"; 
hosts_tt=${array[0]};
hosts_up=${array[1]};
hosts_dn=${array[2]};
srv_tt=${array[3]};
srv_ok=${array[4]};
srv_ct=${array[5]};

echo $hosts_up;
echo $srv_ok;


