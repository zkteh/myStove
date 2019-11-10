#Getting Vscode Insider on Guest Machine

1. Download insider version of VScode https://code.visualstudio.com/insiders/

2. Install nighty build of SSH remote extension for VCcode && Uninstall the current SSH extension (if have), we neeed to replace the SSH with nighty build version https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-nightly&WT.mc_id=-blog-scottha 


#Begin connection!

3. Press `Ctrl + P` to bring up the `Command Palette`. 
   Type: `>SSH` 
   Select: `Open Configuration File`
   
   Configure it as following:
   Host : Your RPi IP address
   Hostname : RPi hostname
   User : RPi username (the one u log in to desktop)
   
```
Host 192.168.1.156 
    HostName raspberrypi
    User pi
```
  
  d

#Enable Port Forward for remote SSH from internet (outside LAN)
-Note that default SSH port, 22 is not usable due to ISP blocking for security reason
x. Use this tool to scan if you have successully enabled the port forwarding. https://www.ipfingerprints.com/portscan.php

```
Host is up (0.18s latency).

PORT    STATE SERVICE

443/tcp open  https
```



#For More Info
https://www.hanselman.com/blog/VisualStudioCodeRemoteDevelopmentOverSSHToARaspberryPiIsButter.aspx



https://github.com/microsoft/vscode-remote-release/issues/139


https://www.digitalocean.com/community/questions/how-to-access-port-22-if-isp-has-blocked-port-22
