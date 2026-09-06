---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/defer-component-updates-tutorial-prerequisites.html
---

# Prerequisites
<a name="defer-component-updates-tutorial-prerequisites"></a>

To complete this tutorial, you need the following:
+ An AWS account. If you don't have one, see [Set up an AWS account](setting-up.md#set-up-aws-account).
+ An AWS Identity and Access Management (IAM) user with administrator permissions.
+ A Greengrass core device with an internet connection. For more information about how to set up a core device, see [Setting up AWS IoT Greengrass core devices](setting-up.md).
  + [Python](https://www.python.org/downloads/) 3.6 or later installed for all users on the core device and added to the `PATH` environment variable. On Windows, you must also have the Python Launcher for Windows installed for all users.
**Important**  <a name="windows-core-device-python-installation"></a>
In Windows, Python doesn't install for all users by default. When you install Python, you must customize the installation to configure it for the AWS IoT Greengrass Core software to run Python scripts. For example, if you use the graphical Python installer, do the following:
Select **Install launcher for all users (recommended)**.
Choose **Customize installation**.
Choose **Next**.
Select **Install for all users**.
Select **Add Python to environment variables**.
Choose **Install**.
For more information, see [Using Python on Windows](https://docs.python.org/3/using/windows.html) in the *Python 3 documentation*.
+ A Windows, macOS, or Unix-like development computer with an internet connection.
  + [Python](https://www.python.org/downloads/) 3.6 or later installed on your development computer.
  + [Git](https://git-scm.com/) installed on your development computer.
  + <a name="development-component-aws-cli-prerequisite"></a>AWS Command Line Interface (AWS CLI) installed and configured with credentials on your development computer. For more information, see [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *AWS Command Line Interface User Guide*.
**Note**
If you use a Raspberry Pi or another 32-bit ARM device, install AWS CLI V1. AWS CLI V2 isn't available for 32-bit ARM devices. For more information, see [Installing, updating, and uninstalling the AWS CLI version 1](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html).
