---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/rdp-configuration-al2027.html
---

# Configure remote desktop using RDP on AL2027
<a name="rdp-configuration-al2027"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 does not include the TigerVNC server that was available in AL2023. To remotely access the graphical desktop, use the Remote Desktop Protocol (RDP) provided by GNOME Remote Desktop. GNOME Remote Desktop is included with the GNOME desktop environment. The following procedures configure the system-level RDP service. When you finish, you can connect to the graphical login screen and log in with your user account.

**Topics**
+ [Prerequisites](#rdp-prereqs-2027)
+ [Step 1: Install the desktop environment](#rdp-install-desktop-2027)
+ [Step 2: Create a TLS certificate](#rdp-tls-certificate-2027)
+ [Step 3: Configure and enable the RDP service](#rdp-configure-service-2027)
+ [Step 4: Connect using an RDP client](#rdp-connect-2027)
+ [(Optional) Start the service at boot](#rdp-optional-boot-2027)
+ [(Optional) Disable RDP access](#rdp-optional-disable-2027)
+ [(Optional) Use your own TLS certificate](#rdp-optional-own-cert-2027)
+ [Related topics](#rdp-more-info-2027)

## Prerequisites
<a name="rdp-prereqs-2027"></a>
+ You use SSH port forwarding to access the RDP server. For more information about setting up your key pair, see [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) in the *Amazon EC2 User Guide*.
+ The following procedure does not guide you through the process of installing an RDP client. You must have an RDP client installed on your local machine to be able to connect to and interact with the desktop environment.

## Step 1: Install the desktop environment
<a name="rdp-install-desktop-2027"></a>

1. Connect to your instance using SSH.

1. Install the GNOME desktop environment and the `systemd-pam` package. The `Desktop` group includes GNOME Remote Desktop, which provides the RDP service. The `systemd-pam` package is required for the graphical login session.

   ```
   [ec2-user ~]$ sudo dnf group install "Desktop"
   [ec2-user ~]$ sudo dnf install systemd-pam
   ```

## Step 2: Create a TLS certificate
<a name="rdp-tls-certificate-2027"></a>

RDP connections are always encrypted with TLS, so GNOME Remote Desktop requires a server certificate before the service can be enabled. The following steps create a self-signed certificate owned by the `gnome-remote-desktop` service user. If you want to use a certificate issued by a certificate authority instead, see the optional section at the end of this topic.

1. Create the directory that holds the certificate and key.

   ```
   [ec2-user ~]$ sudo -u gnome-remote-desktop mkdir -p ~gnome-remote-desktop/.local/share/gnome-remote-desktop
   ```

1. Generate a self-signed certificate and private key.

   ```
   [ec2-user ~]$ sudo -u gnome-remote-desktop openssl req -new -newkey rsa:4096 -days 720 -nodes -x509 \
     -subj "/C=US/ST=NONE/L=NONE/O=GNOME/CN=gnome.org" \
     -out ~gnome-remote-desktop/.local/share/gnome-remote-desktop/tls.crt \
     -keyout ~gnome-remote-desktop/.local/share/gnome-remote-desktop/tls.key
   ```
**Note**
This example command generates a certificate that is valid for 720 days, after which you need to regenerate it. Consider changing the parameters to suit your environment.
**Note**
The certificate and key must be readable by the ` gnome-remote-desktop` service user, which is why the files are created with `sudo -u gnome-remote-desktop`.

## Step 3: Configure and enable the RDP service
<a name="rdp-configure-service-2027"></a>

1. Configure the RDP service to use the certificate and key.

   ```
   [ec2-user ~]$ sudo grdctl --system rdp set-tls-key ~gnome-remote-desktop/.local/share/gnome-remote-desktop/tls.key
   [ec2-user ~]$ sudo grdctl --system rdp set-tls-cert ~gnome-remote-desktop/.local/share/gnome-remote-desktop/tls.crt
   ```

1. Set the RDP credentials. You are prompted for a username and password.

   ```
   [ec2-user ~]$ sudo grdctl --system rdp set-credentials
   ```
**Note**
These credentials are used only to authenticate the RDP connection. They are not connected to a system user account, and the username does not need to match one. After the RDP connection is established, you log in to the desktop with your system user account at the graphical login screen.

1. Make sure the system user account you use at the graphical login screen has a password you can enter. For a local account that does not have a password, set one as shown. If the account already has a password, skip this step and use its existing credentials.

   ```
   [ec2-user ~]$ sudo passwd <username>
   ```
**Note**
Replace `<username>` with the system user account you log in with (for example, `ec2-user`).

1. Enable the RDP service.

   ```
   [ec2-user ~]$ sudo grdctl --system rdp enable
   ```
**Note**
On instances without a TPM device, `grdctl` prints `Init TPM credentials failed because No TPM device found, using GKeyFile as fallback`. This message is expected. The credentials are stored in a file that is readable only by the service user.

1. Start the graphical login screen.

   ```
   [ec2-user ~]$ sudo systemctl start gdm.service
   ```

   After performing this step, you can create the SSH tunnel from your local machine and connect using your RDP client.

## Step 4: Connect using an RDP client
<a name="rdp-connect-2027"></a>

The RDP server listens on TCP port 3389. You can expose this port directly through your security group. Instead, these steps use SSH tunneling, which is more secure. The SSH tunnel authenticates the instance and encrypts the connection between your local machine and the EC2 instance, so port 3389 is never exposed to the network. For more information about security groups, see [Change the security groups for your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html) in the *Amazon EC2 User Guide*.

1. Create an SSH tunnel from your local machine.

   ```
   $ ssh -i <keypair> -L <local-port>:localhost:3389 ec2-user@<address>
   ```
**Note**
Replace `<keypair>` with the path to your SSH key and ` <address>` with your instance's public IP or DNS name. Replace ` <local-port>` with any available port on your local machine (for example, `5000`). Don't change the remote port `3389`; that is the port the RDP server listens on. On some local machines, port ` 3389` is already in use, so choosing a different local port avoids conflicts.

1. Use your RDP client to connect to `localhost:<local-port>` (for example, `localhost:5000`) with the RDP credentials you configured in the previous step.
**Note**
Your RDP client might warn that the server certificate can't be verified. You can safely accept the warning here, because the SSH tunnel already authenticates the instance and encrypts the connection. Don't ignore certificate warnings when connecting directly over the network.

1. Log in with your system user account at the graphical login screen to start the desktop session.
**Important**
Keep the SSH tunnel open while using RDP. If the SSH tunnel isn't open, your RDP client can't view or interact with the desktop environment.

## (Optional) Start the service at boot
<a name="rdp-optional-boot-2027"></a>

If you plan to use RDP regularly, configure the instance to boot into the graphical target so that the login screen and the RDP service start automatically when your instance boots.
+ To start the login screen and RDP service automatically at boot, set the default boot target.

  ```
  [ec2-user ~]$ sudo systemctl set-default graphical.target
  ```

  After performing this step, you will no longer need to start ` gdm.service` every time you reboot your instance.

## (Optional) Disable RDP access
<a name="rdp-optional-disable-2027"></a>

If you no longer need remote desktop access, disable the RDP service so the instance stops listening for connections.

1. Disable the RDP service.

   ```
   [ec2-user ~]$ sudo grdctl --system rdp disable
   ```

1. If you changed the default boot target earlier, restore it to the multi-user (non-graphical) target.

   ```
   [ec2-user ~]$ sudo systemctl set-default multi-user.target
   ```

## (Optional) Use your own TLS certificate
<a name="rdp-optional-own-cert-2027"></a>

Instead of the self-signed certificate from Step 2, you can use a certificate issued by a certificate authority that your clients trust. Register it with the same ` grdctl --system rdp set-tls-key` and `set-tls-cert` commands from Step 3. With this, your RDP client can verify the server identity, so you can connect directly to port 3389 without an SSH tunnel. If you connect directly, restrict inbound access to port 3389 in your security group to known source IP addresses. For instructions, see [Change the security groups for your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html) in the *Amazon EC2 User Guide*.

## Related topics
<a name="rdp-more-info-2027"></a>

For more information about the graphical desktop environment, see the following documentation:
+  [AL2027 graphical desktop](graphical-desktop.md)
+ [What Is Amazon DCV?](https://docs.aws.amazon.com/dcv/latest/adminguide/what-is-dcv.html) in the *Amazon DCV Administrator Guide*
