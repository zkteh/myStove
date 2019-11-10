# Getting Vscode Insider on Guest Machine

1. Download insider version of VScode https://code.visualstudio.com/insiders/

2. Install nighty build of SSH remote extension for VCcode && \
Uninstall the current SSH extension (if have), we neeed to replace the SSH with nighty build version	https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-nightly


# Configuration

3. Press `Ctrl + P` to bring up the `Command Palette`. 
   Type: `>SSH` 
   Select: `Open Configuration File`
   
   ![ssh-config](/tutorials/remote-ssh-using-vscode/images/ssh-config.png)
   
   Configure it as following:
   Host : Your RPi IP address;
   Hostname : RPi hostname;
   User : RPi username (the one u log in to desktop).
   

# Being the remote SSH

4. Select: 'Connect to a host' \
   Choose the host you configured just now \
   Type in the RPi username's password  \
   You should see a green colour box located in the left corner, which means you are now conncted to the RPi using SSH with     VScode. \ 
   You can click `+sign`, choose `bash` if the bash terminal did not show up. Type `ls` to show the remote files 
   ![ssh-done](/tutorials/remote-ssh-using-vscode/images/ssh-config.png)
	
	You can navigate the remote folder also
	![ssh-done](/tutorials/remote-ssh-using-vscode/images/ssh-folder.png)
	
	
# Enable Port Forward for remote SSH from internet (outside LAN)
5. Note that default SSH port, 22 is not usable due to ISP blocking for security reason.
   Use this tool to scan if you have successully enabled the port forwarding. https://www.ipfingerprints.com/portscan.php

   ```
   Host is up (0.18s latency).
   PORT    STATE SERVICE
   443/tcp open  https
   ```

   Because you have change the SSH default port (22) to (443), you have to edit the config file again.

   ```
   Host 192.168.1.156 
       HostName raspberrypi
       User pi
       Port 443
   ```
   
# Enjoy! For More Info:
https://www.hanselman.com/blog/VisualStudioCodeRemoteDevelopmentOverSSHToARaspberryPiIsButter.aspx
https://github.com/microsoft/vscode-remote-release/issues/139
https://www.digitalocean.com/community/questions/how-to-access-port-22-if-isp-has-blocked-port-22
