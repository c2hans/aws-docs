---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/vnc-configuration-al2023.html
---

# Tutorial: Configure TigerVNC server on AL2023
<a name="vnc-configuration-al2023"></a>

The following procedures help you set up VNC server on your AL2023 instance. VNC allows you to remotely access and interact with the graphical desktop environment over a secure network connection.

**Topics**
+ [Prerequisites](#installing-vnc-prereqs-2023)
+ [Step 1: Installation](#install-vnc-server-2023)
+ [Step 2: Configuration](#start-vnc-server-2023)
+ [Step 3: Connect using a VNC client](#connect-vnc-server-2023)
+ [(Optional) Start service at boot](#optional-services-vnc-2023)
+ [(Optional) Disable the idle lockscreen](#optional-lockscreen-vnc-2023)
+ [Related topics](#vnc-more-info-2023)

## Prerequisites
<a name="installing-vnc-prereqs-2023"></a>
+ This tutorial assumes you have already installed the GNOME desktop environment on your AL2023 instance. For more information, see the [Tutorial: Install the GNOME desktop environment on AL2023](installing-gnome-al2023.md) page.
+ This tutorial uses SSH port forwarding to access the VNC server. For more information about setting up your key pair, See [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) in the *Amazon EC2 User Guide*.
+  The following procedure does not guide you through the process of installing a VNC client. You must have a VNC client installed on your local machine to be able to connect to and interact with the desktop environment.

## Step 1: Installation
<a name="install-vnc-server-2023"></a>

1. Connect to your instance. For more information, see [Connecting to AL2023 instances](connecting-to-instances.md).

1. Install the TigerVNC server package for AL2023.

   The `-y` option installs the package without asking for confirmation. If you would like to examine the package before installing, you can omit this option.

   ```
   [ec2-user ~]$ sudo dnf install -y tigervnc-server
   ```

## Step 2: Configuration
<a name="start-vnc-server-2023"></a>

1. Ensure the user has configured a VNC password.

   ```
   [ec2-user ~]$ vncpasswd
   ```

1. Assign a display number to the user.

   ```
   [ec2-user ~]$ sudo vi /etc/tigervnc/vncserver.users
   ```

   Add the following configuration:

   ```
   :1=ec2-user
   ```
**Note**
You can assign any display number to the user. We are using display ` :1` for the sake of this example.

1. Edit the VNC server configuration file.

   ```
   [ec2-user ~]$ sudo vi /etc/tigervnc/vncserver-config-defaults
   ```

   Add the following configuration:

   ```
   session=gnome
   securitytypes=vncauth,tlsvnc
   geometry=1920x1080
   localhost
   alwaysshared
   ```
**Note**
You can change the resolution of the display using the `geometry` parameter. We are using `1920x1080` for the sake of this example.

1. Start the VNC server. This process needs to be repeated every time you restart your instace. If you would like to automate the process of starting this service, see the optional section below.

   ```
   [ec2-user ~]$ sudo systemctl start vncserver@:1
   ```
**Important**
When starting the `vncserver` service, the part after the ` @` must match the display number set for the user in the ` /etc/tigervnc/vncserver.users` file.

   After performing this step, you may create the SSH tunnel from your local machine and connect using your VNC client.

## Step 3: Connect using a VNC client
<a name="connect-vnc-server-2023"></a>

The VNC server exposes a TCP socket for client connections. While you could expose the VNC port directly through your security group, this tutorial demonstrates using SSH tunneling as a more secure approach by encrypting the connection between your local machine and the EC2 instance. Once connected through the tunnel, you'll authenticate to the VNC server using the password you configured in the previous step. For more information about security groups, see [Change the security groups for your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html) in the *Amazon EC2 User Guide*.

1. Create an SSH tunnel from your local machine.

   ```
   $ ssh -i <keypair> -L 5901:localhost:5901 ec2-user@<address>
   ```
**Note**
Replace `<keypair>` with the path to your SSH key and ` <address>` with your instance's public IP or DNS name. The port changes based on the display number that was used to start the ` vncserver`. For example, display `:1` uses port `5901`, display `:2` uses port `5902`, etc.

1. Use your VNC client to connect to `localhost:5901` or ` 127.0.0.1:5901` with the previously set VNC password.
**Important**
 Keep the SSH tunnel open while using VNC. If the SSH tunnel isn't open, you will not be able to use your VNC client to view and interact with the desktop environment.

## (Optional) Start service at boot
<a name="optional-services-vnc-2023"></a>

 If you plan to use VNC regularly, you may want to configure the VNC server to start automatically when your instance boots. This eliminates the need to manually start the VNC server each time you restart your instance. This configuration ensures that your graphical desktop environment is ready and accessible as soon as your instance completes its startup process.
+ Configure the service to start at boot.

  ```
  [ec2-user ~]$ sudo systemctl enable vncserver@:1
  ```
**Important**
When enabling the `vncserver` service, the part after the ` @` must match the display number set for the user in the ` /etc/tigervnc/vncserver.users` file. Additionally, you can pass the ` --now` argument after `enable` to start the service immediately.

  After performing this step, you will no longer need to start ` vncserver` every time you reboot your instance.

## (Optional) Disable the idle lockscreen
<a name="optional-lockscreen-vnc-2023"></a>
+ Set the idle delay to zero in order to disable the lockscreen when the user has been inactive for a longer period of time.

  ```
  [ec2-user ~]$ gsettings set org.gnome.desktop.session idle-delay 0
  ```

## Related topics
<a name="vnc-more-info-2023"></a>

For more information about the graphical desktop environment, see the following documentation:
+  [Tutorial: Install the GNOME desktop environment on AL2023](installing-gnome-al2023.md)
+ [What Is Amazon DCV?](https://docs.aws.amazon.com/dcv/latest/adminguide/what-is-dcv.html) in the * Amazon DCV Administrator Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
