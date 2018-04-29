# Securing Docker on the Cheap
## Part 2 - Vulnerabilities


### Setting up Falco
1. Install Falco as a service
```
curl -s https://s3.amazonaws.com/download.draios.com/stable/install-falco | sudo bash

```
Note: this is the quick method; make sure you understand the installer script before running!
__This step may take a while.___


2. Setup syslog rules (10-falco.conf)
```
cp 10-falco.conf /etc/rsyslog.d/
service rsyslog restart
```
Falco messages will now go to /var/log/falco/falco.log

3. Enable/Start falco service
systemd
```
systemctl enable falco && systemctl start falco
```
