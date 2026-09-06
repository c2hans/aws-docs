---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/getting-started-prerequisites.html
---

# Prerequisites
<a name="getting-started-prerequisites"></a>

To complete this getting started tutorial, you need the following:
+ An AWS account. If you don't have one, see [Step 2: Set up your environment](getting-started-set-up-environment.md).
+ <a name="requirement-supported-region"></a>The use of an [AWS Region](https://en.wikipedia.org/wiki/Amazon_Web_Services#Availability_and_topology) that supports AWS IoT Greengrass V2. For the list of supported Regions, see [AWS IoT Greengrass V2 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/greengrassv2.html) in the *AWS General Reference*.
+ An AWS Identity and Access Management (IAM) user with administrator permissions.
+ A device to set up as a Greengrass core device, such as a Raspberry Pi with [Raspberry Pi OS](https://www.raspberrypi.org/downloads/) (previously called Raspbian), or a Windows 10 device. You must have administrator permissions on this device, or the ability to acquire administrator privileges, such as through `sudo`. This device must have an internet connection.

  You can also choose to use a different device that meets the requirements to install and run the AWS IoT Greengrass Core software.

  If your development computer meets these requirements, you can set it up as your Greengrass core device in this tutorial.
+ [Python](https://www.python.org/downloads/) 3.5 or later installed for all users on the device and added to the `PATH` environment variable. On Windows, you must also have the Python Launcher for Windows installed for all users.
**Important**  <a name="windows-core-device-python-installation"></a>
In Windows, Python doesn't install for all users by default. When you install Python, you must customize the installation to configure it for the AWS IoT Greengrass Core software to run Python scripts. For example, if you use the graphical Python installer, do the following:
Select **Install launcher for all users (recommended)**.
Choose **Customize installation**.
Choose **Next**.
Select **Install for all users**.
Select **Add Python to environment variables**.
Choose **Install**.
For more information, see [Using Python on Windows](https://docs.python.org/3/using/windows.html) in the *Python 3 documentation*.
+ AWS Command Line Interface (AWS CLI) installed and configured with credentials on your development computer and on your device. Make sure you use the same AWS Region to configure the AWS CLI on your development computer and on your device. To use AWS IoT Greengrass V2 with the AWS CLI, you must have one of the following versions or later:<a name="minimum-aws-cli-versions"></a>
  + Minimum AWS CLI V1 version: v1.18.197
  + Minimum AWS CLI V2 version: v2.1.11
**Tip**  <a name="tip-check-aws-cli-version"></a>
You can run the following command to check the version of the AWS CLI that you have.

  ```
  aws --version
  ```

  For more information, see [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *AWS Command Line Interface User Guide*.
**Note**
If you use a 32-bit ARM device, such as a Raspberry Pi with a 32-bit operating system, install AWS CLI V1. AWS CLI V2 isn't available for 32-bit ARM devices. For more information, see [Installing, updating, and uninstalling the AWS CLI version 1](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html).
