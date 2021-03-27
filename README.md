# CPSC4240-project
Ideas for what we want the program to do...
- List devices on the network
  - hostname -I | awk '{print $1}' # get the ip address
  - sudo nmap {ip}/24 | grep MAC # get the list of host names on the network
- Network analysis
  - speed,bandwidth,total data usage, etc.
- Most visited ip/web sites
- information abou the host device
- information about the devices on the network
- port analysis on host machine

Installed linux tools (through apt)
- nmap
- net-tools
- nload
