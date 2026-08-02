---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/getting-started-set-up-environment.html
---

# Step 2: Set up your environment
<a name="getting-started-set-up-environment"></a>

**Note**
These steps do not apply to nucleus lite.

Follow the steps in this section to set up a Linux or Windows device to use as your AWS IoT Greengrass core device.

## Set up a Linux device (Raspberry Pi)
<a name="getting-started-set-up-raspberry-pi"></a>

These steps assume that you use a Raspberry Pi with Raspberry Pi OS. If you use a different device or operating system, consult the relevant documentation for your device.

**To set up a Raspberry Pi for AWS IoT Greengrass V2**

1. Enable SSH on your Raspberry Pi to remotely connect to it. For more information, see [SSH (Secure shell)](https://www.raspberrypi.com/documentation/computers/remote-access.html#ssh) in the *Raspberry Pi Documentation*.

1. Find the IP address of your Raspberry Pi to connect to it with SSH. To do so, you can run the following command on your Raspberry Pi.

   ```
   hostname -I
   ```

1. Connect to your Raspberry Pi with SSH.

   On your development computer, run the following command. Replace {{username}} with the name of the user to sign in, and replace {{pi-ip-address}} with the IP address that you found in the previous step.

   ```
   ssh {{username}}@{{pi-ip-address}}
   ```
**Important**
If your development computer uses an earlier version of Windows, you might not have the `ssh` command, or you might have `ssh` but can't connect to your Raspberry Pi. To connect to your Raspberry Pi, you can install and configure [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), which is a no-cost, open source SSH client. Consult the [PuTTY documentation](https://tartarus.org/~simon/putty-snapshots/htmldoc/Chapter2.html#gs) to connect to your Raspberry Pi.

1. Install the Java runtime, which AWS IoT Greengrass Core software requires to run. On your Raspberry Pi, use the following commands to install Java 11.

   ```
   sudo apt install default-jdk
   ```

   When the installation completes, run the following command to verify that Java runs on your Raspberry Pi.

   ```
   java -version
   ```

   The command prints the version of Java that runs on the device. The output might look similar to the following example.

   ```
   openjdk version "11.0.9.1" 2020-11-04
   OpenJDK Runtime Environment (build 11.0.9.1+1-post-Debian-1deb10u2)
   OpenJDK 64-Bit Server VM (build 11.0.9.1+1-post-Debian-1deb10u2, mixed mode)
   ```

**Tip: Set kernel parameters on a Raspberry Pi**
If your device is a Raspberry Pi, you can complete the following steps to view and update its Linux kernel parameters:
Open the `/boot/cmdline.txt` file. This file specifies Linux kernel parameters to apply when the Raspberry Pi boots.
For example, on a Linux-based system, you can run the following command to use GNU nano to open the file.

   ```
   sudo nano /boot/cmdline.txt
   ```
Verify that the `/boot/cmdline.txt` file contains the following kernel parameters. The `systemd.unified_cgroup_hierarchy=0` parameter specifies to use cgroups v1 instead of cgroups v2.

   ```
   cgroup_enable=memory cgroup_memory=1 systemd.unified_cgroup_hierarchy=0
   ```
If the `/boot/cmdline.txt` file doesn't contain these parameters, or it contains these parameters with different values, update the file to contain these parameters and values.
If you updated the `/boot/cmdline.txt` file, reboot the Raspberry Pi to apply the changes.

   ```
   sudo reboot
   ```

## Set up a Linux device (other)
<a name="getting-started-set-up-linux"></a><a name="set-up-linux-device-environment-procedure"></a>

**To set up a Linux device for AWS IoT Greengrass V2**

1. Install the Java runtime, which AWS IoT Greengrass Core software requires to run. We recommend that you use [Amazon Corretto](https://aws.amazon.com/corretto/) or [OpenJDK](https://openjdk.java.net/) long-term support versions. Version 8 or higher is required. The following commands show you how to install OpenJDK on your device.
   + For Debian-based or Ubuntu-based distributions:

     ```
     sudo apt install default-jdk
     ```
   + For Red Hat-based distributions:

     ```
     sudo yum install java-11-openjdk-devel
     ```
   + For Amazon Linux 2:

     ```
     sudo amazon-linux-extras install java-openjdk11
     ```
   + For Amazon Linux 2023:

     ```
     sudo dnf install java-11-amazon-corretto -y
     ```

   When the installation completes, run the following command to verify that Java runs on your Linux device.

   ```
   java -version
   ```

   The command prints the version of Java that runs on the device. For example, on a Debian-based distribution, the output might look similar to the following sample.

   ```
   openjdk version "11.0.9.1" 2020-11-04
   OpenJDK Runtime Environment (build 11.0.9.1+1-post-Debian-1deb10u2)
   OpenJDK 64-Bit Server VM (build 11.0.9.1+1-post-Debian-1deb10u2, mixed mode)
   ```

1. (Optional) Create the default system user and group that runs components on the device. You can also choose to let the AWS IoT Greengrass Core software installer create this user and group during installation with the `--component-default-user` installer argument. For more information, see [Installer arguments](configure-installer.md).

   ```
   sudo useradd --system --create-home ggc_user
   sudo groupadd --system ggc_group
   ```

1. Verify that the user that runs the AWS IoT Greengrass Core software (typically `root`), has permission to run `sudo` with any user and any group.

   1. Run the following command to open the `/etc/sudoers` file.

      ```
      sudo visudo
      ```

   1. Verify that the permission for the user looks like the following example.

      ```
      root    ALL=(ALL:ALL) ALL
      ```

1. (Optional) To [run containerized Lambda functions](run-lambda-functions.md), you must enable [cgroups](https://en.wikipedia.org/wiki/Cgroups) v1, and you must enable and mount the *memory* and *devices* cgroups. If you don't plan to run containerized Lambda functions, you can skip this step.

   To enable these cgroups options, boot the device with the following Linux kernel parameters.

   ```
   cgroup_enable=memory cgroup_memory=1 systemd.unified_cgroup_hierarchy=0
   ```

   For information about viewing and setting kernel parameters for your device, see the documentation for your operating system and boot loader. Follow the instructions to permanently set the kernel parameters.

1. Install all other required dependencies on your device as indicated by the list of requirements in [Device requirements](greengrass-nucleus-component.md#greengrass-v2-requirements).

## Set up a Windows device
<a name="getting-started-set-up-windows"></a><a name="set-up-windows-device-environment-procedure"></a>

**To set up a Windows device for AWS IoT Greengrass V2**

1. Install the Java runtime, which AWS IoT Greengrass Core software requires to run. We recommend that you use [Amazon Corretto](https://aws.amazon.com/corretto/) or [OpenJDK](https://openjdk.java.net/) long-term support versions. Version 8 or higher is required.

1. Check whether Java is available on the [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) system variable, and add it if not. The LocalSystem account runs the AWS IoT Greengrass Core software, so you must add Java to the PATH system variable instead of the PATH user variable for your user. Do the following:

   1. Press the Windows key to open the start menu.

   1. Type **environment variables** to search for the system options from the start menu.

   1. In the start menu search results, choose **Edit the system environment variables** to open the **System properties** window.

   1. Choose **Environment variables...** to open the **Environment Variables** window.

   1. Under **System variables**, select **Path**, and then choose **Edit**. In the **Edit environment variable** window, you can view each path on a separate line.

   1. Check if the path to the Java installation's `bin` folder is present. The path might look similar to the following example.

      ```
      C:\\Program Files\\Amazon Corretto\\jdk11.0.13_8\\bin
      ```

   1. If the Java installation's `bin` folder is missing from **Path**, choose **New** to add it, and then choose **OK**.

1. <a name="set-up-windows-device-environment-open-cmd"></a>Open the Windows Command Prompt (`cmd.exe`) as an administrator.

1. <a name="set-up-windows-device-environment-create"></a>Create the default user in the LocalSystem account on the Windows device. Replace {{password}} with a secure password.

   ```
   net user /add ggc_user {{password}}
   ```
**Tip**  <a name="windows-password-expiration-tip"></a>
Depending on your Windows configuration, the user's password might be set to expire at a date in the future. To ensure your Greengrass applications continue to operate, track when the password expires, and update it before it expires. You can also set the user's password to never expire.
To check when a user and its password expire, run the following command.

     ```
     net user {{ggc_user}} | findstr /C:expires
     ```
To set a user's password to never expire, run the following command.

     ```
     wmic UserAccount where "Name='{{ggc_user}}'" set PasswordExpires=False
     ```
If you’re using Windows 10 or later where the [`wmic` command is deprecated](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmic), run the following PowerShell command.

     ```
     Get-CimInstance -Query "SELECT * from Win32_UserAccount WHERE name = '{{ggc_user}}'" | Set-CimInstance -Property @{PasswordExpires="False"}
     ```

1. <a name="set-up-windows-device-psexec"></a>Download and install the [PsExec utility](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec) from Microsoft on the device.

1. <a name="set-up-windows-device-credentials"></a>Use the PsExec utility to store the user name and password for the default user in the Credential Manager instance for the LocalSystem account. Replace {{password}} with the user's password that you set earlier.

   ```
   psexec -s cmd /c cmdkey /generic:ggc_user /user:ggc_user /pass:{{password}}
   ```

   If the **PsExec License Agreement** opens, choose **Accept** to agree to the license and run the command.
**Note**
On Windows devices, the LocalSystem account runs the Greengrass nucleus, and you must use the PsExec utility to store the default user information in the LocalSystem account. Using the Credential Manager application stores this information in the Windows account of the currently logged on user, instead of the LocalSystem account.
