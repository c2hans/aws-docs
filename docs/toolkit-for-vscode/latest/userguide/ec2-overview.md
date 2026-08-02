---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/ec2-overview.html
---

# Working with Amazon Elastic Compute Cloud
<a name="ec2-overview"></a>

The following sections describe how to work with Amazon Elastic Compute Cloud in the AWS Toolkit for Visual Studio Code.

## Prerequisites
<a name="w2aac17c31b9b5"></a>

The features described in this user guide topic have been tested on Amazon EC2 instances with the following operating systems:
+ Windows 2016\+
**Note**
This OS only works when connecting a VS Code terminal. It doesn't work when connecting a full VS Code remote instance. For additional information about VS Code terminals and remote instances, see the [Getting started with the terminal](https://code.visualstudio.com/docs/terminal/getting-started) and [VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview) topics in the VS Code documentation.
+ Amazon Linux 2023
+ Ubuntu, 22.04

A locally installed **SSH** is required to open a remote connection to an Amazon EC2 instance, but is not required to open a terminal to an Amazon EC2 instance.

Your Amazon EC2 instance profile must include the following AWS Identity and Access Management (IAM) permissions.

```
"ssmmessages:CreateControlChannel",
"ssmmessages:CreateDataChannel",
"ssmmessages:OpenControlChannel",
"ssmmessages:OpenDataChannel",
"ssm:DescribeAssociation",
"ssm:ListAssociations",
"ssm:UpdateInstanceInformation
```

**Note**
The required permissions are included in the following AWS managed policy.
`AmazonSSMManagedInstanceCore`
`AmazonSSMManagedEC2InstanceDefaultPolicy`

## Viewing existing Amazon EC2 instances
<a name="w2aac17c31b9b7"></a>

To view your existing Amazon EC2 instances from the AWS Toolkit, complete the following steps.

1. From the AWS Toolkit, expand the AWS Toolkit Explorer.

1. Expand the region that contains the Amazon EC2 instances that you want to view.

1. Expand the **EC2** heading to display your existing Amazon EC2 instances.

## Launching a new Amazon EC2 instance
<a name="w2aac17c31b9b9"></a>

There are 3 ways to create a new Amazon EC2 instance with the AWS Toolkit.

Each work flow opens the **Launch an instance** wizard in the AWS console. For detailed information about launching a new Amazon EC2 instance from the **Launch an instance** wizard, see the [Launch an EC2 instance using the launch instance wizard in the console](https://docs.aws.amazon.com//AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html) topic in the *Amazon Elastic Compute Cloud* User Guide. To launch a new Amazon EC2 instance, complete one of the following procedures.

### Launching a new Amazon EC2 instance from the VS Code Command Palette
<a name="w2aac17c31b9b9b7b1"></a>

1. From VS Code, open the VS Code Command Palette by pressing **command \+ shift \+ P (Windows: ctrl \+ shift \+ P)**

1. From the VS Code Command Palette, search for the **AWS: Launch EC2** command and select it when it populates in the list to open the Launch EC2 instance **Select Region** prompt in VS Code.

1. From the Launch EC2 instance **Select Region** prompt, choose the region you want to launch your new instance in, then confirm you want to open the AWS Console in your default web browser.

1. From the AWS Console in your default web browser, complete the authentication process to proceed to the **Launch an instance** wizard.

1. From the **Launch an instance** wizard, complete the required sections, then choose the **Launch instance** button to launch your new Amazon EC2 instance.

1. The AWS Explorer updates to show your new Amazon EC2 instance.

### Launching a new Amazon EC2 instance from the AWS Explorer
<a name="w2aac17c31b9b9b7b3"></a>

1. Expand the AWS Toolkit Explorer, then expand the region you want to create the new Amazon EC2 instance in.

1. Expand or hover over the **EC2** heading, then choose the **\+ (Launch EC2 instance)** icon.

1. When prompted, confirm that you want to open the AWS Console in your default web browser.

1. From the AWS Console in your web browser, complete the authentication process to proceed to the **Launch an instance** wizard.

1. From the **Launch an instance** wizard, complete the required sections, then choose the **Launch instance** button to launch your new Amazon EC2 instance.

1. The AWS Explorer updates to show your new Amazon EC2 instance.

### Launching a new Amazon EC2 instance from the context (right-click) menu
<a name="w2aac17c31b9b9b7b5"></a>

1. Expand the AWS Toolkit Explorer, then expand the region you want to create the new Amazon EC2 instance in.

1. Right-click the **EC2** heading, then choose **Launch EC2 instance**.

1. When prompted, confirm that you want to open the AWS Console in your default web browser.

1. From the AWS Console in your web browser, complete the authentication process to proceed to the **Launch an instance** wizard.

1. From the **Launch an instance** wizard, complete the required sections, then choose the **Launch instance** button to launch your new Amazon EC2 instance.

1. The AWS Explorer updates to show your new Amazon EC2 instance.

## Connecting VS Code to an Amazon EC2 instance
<a name="w2aac17c31b9c11"></a>

There are 3 ways to connect to an Amazon EC2 instance from VS Code. To connect VS Code to your EC2 instance, complete one of the following procedures.

### Connecting VS Code to an Amazon EC2 instance from the Command Palette
<a name="w2aac17c31b9c11b5b1"></a>

1. From VS Code, open the VS Code Command Palette by pressing **command \+ shift \+ P (Windows: ctrl \+ shift \+ P)**

1. From the VS Code Command Palette, search for the **AWS: Connect VS Code to EC2 instance...** command and select it when it populates in the list to open the **Select EC2 Instance** prompt in VS Code.

1. From the **Select EC2 Instance** prompt, choose the region that contains the instance you want to connect to, then choose the instance you want to connect to.

1. VS Code displays the status while the connection is being established.

1. A new window opens to display your Amazon EC2 instance when the connection is complete.

### Connecting VS Code to an Amazon EC2 instance from the AWS Explorer.
<a name="w2aac17c31b9c11b5b3"></a>

1. Expand the AWS Toolkit Explorer, then expand the region that contains the Amazon EC2 instance you want to connect to.

1. Hover over the Amazon EC2 instance, then choose the **(Connect VS Code to EC2 instance)** icon.
**Note**
You can also choose the **(Connect VS Code to EC2 instance)** icon from the **EC2** service heading in the AWS Explorer.

1. VS Code displays the status while the connection is being established.

1. A new window opens to display your Amazon EC2 instance when the connection is complete.

### Connecting VS Code to an Amazon EC2 instance from the right-click menu
<a name="w2aac17c31b9c11b5b5"></a>

1. Expand the AWS Toolkit Explorer, then expand the region that contains the Amazon EC2 instance you want to connect to.

1. Right-click the Amazon EC2 instance you want to connect to, then choose **Connect VS Code to EC2 instance**.
**Note**
You can also right-click the **EC2** service heading in the AWS Explorer and choose the **Connect VS Code to EC2 instance**.

1. VS Code displays the status while the connection is being established.

1. A new window opens to display your Amazon EC2 instance when the connection is complete.

## Opening a terminal to an Amazon EC2 instance.
<a name="w2aac17c31b9c13"></a>

There are 3 ways to connect to an Amazon EC2 instance from the VS Code terminal.

### Connecting VS Code to an Amazon EC2 instance from the Command Palette
<a name="w2aac17c31b9c13b5b1"></a>

1. From VS Code, open the VS Code Command Palette by pressing **command \+ shift \+ P (Windows: ctrl \+ shift \+ P)**

1. From the VS Code Command Palette, search for the **AWS:Open terminal to EC2 instance...** command and select it when it populates in the list to open the **Select EC2 Instance** prompt in VS Code.

1. From the **Select EC2 Instance** prompt, choose the region containing the instance you want to open in the terminal, then choose the instance.

1. VS Code displays the status while the connection is being established.

1. The VS Code Terminal opens to display your new session when the connection is complete.

### Opening an Amazon EC2 instance in the VS Code terminal from the AWS Explorer.
<a name="w2aac17c31b9c13b5b3"></a>

1. Expand the AWS Toolkit Explorer, then expand the region that contains the Amazon EC2 instance you want to connect to.

1. Hover over the Amazon EC2 instance, then choose the **(Open terminal to EC2 instance...)** icon.
**Note**
You can also choose the **(Open terminal to EC2 instance...)** icon from the **EC2** service heading in the AWS Explorer.

1. VS Code displays the status while the connection is being established.

1. The VS Code Terminal opens to display your new session when the connection is complete.

### Opening an Amazon EC2 instance in the VS Code terminal from the right-click menu
<a name="w2aac17c31b9c13b5b5"></a>

1. Expand the AWS Toolkit Explorer, then expand the region that contains the Amazon EC2 instance you want to open in the VS Code terminal.

1. Right-click the Amazon EC2 instance you want to open in the terminal, then choose **Open terminal to EC2 instance...**.
**Note**
You can also right-click the **EC2** service heading in the AWS Explorer and choose the **Open terminal to EC2 instance...**.

1. VS Code displays the status while the connection is being established.

1. The VS Code Terminal opens to display your new session when the connection is complete.

## Starting or rebooting an Amazon EC2 instance
<a name="w2aac17c31b9c15"></a>

There are 3 ways to start or reboot an Amazon EC2 instance.

### Rebooting an Amazon EC2 instance from the Command Palette
<a name="w2aac17c31b9c15b5b1"></a>

1. From VS Code, open the VS Code Command Palette by pressing **command \+ shift \+ P (Windows: ctrl \+ shift \+ P)**

1. From the VS Code Command Palette, search for the **AWS: Reboot EC2 instance** command and select it when it populates in the list to open the **Select EC2 Instance** prompt in VS Code.
**Note**
To start an instance that isn't running, you must choose the **AWS: Start EC2 instance** command. The **AWS: Reboot EC2 instance** command only reboots instances that are currently running.

1. From the **Select EC2 Instance** prompt, choose the region that contains the instance you want to start or reboot.

1. VS Code displays the status while the instance is rebooting.

1. The AWS Explorer updates to show that your instance is running when it has finished rebooting.

### Starting or rebooting an Amazon EC2 instance from the AWS Explorer
<a name="w2aac17c31b9c15b5b3"></a>

1. Expand the AWS Toolkit Explorer, then expand the region that contains the Amazon EC2 instance you want to start or reboot.

1. Hover over the Amazon EC2 instance, then choose the **(Reboot EC2 instance)** icon.
**Note**
If the instance is stopped, then the only options is the **(Start EC2 instance)** icon

1. VS Code displays the status while the instance is rebooting.

1. The AWS Explorer updates to show that your instance is running when it has finished rebooting.

### Starting or rebooting an Amazon EC2 instance from the right-click menu
<a name="w2aac17c31b9c15b5b5"></a>

1. Expand the AWS Toolkit Explorer, then expand the region that contains the Amazon EC2 instance you want to start or reboot.

1. Right-click the Amazon EC2 instance you want to connect to, then choose **Reboot EC2 instance**.
**Note**
If the instance is stopped, then the only options is the **Start EC2 instance**.

1. VS Code displays the status while the instance is rebooting.

1. The AWS Explorer updates to show that your instance is running when it has finished rebooting.

## Stopping an Amazon EC2 instance
<a name="w2aac17c31b9c17"></a>

There are 3 ways to stop an Amazon EC2 instance.

### Stopping an Amazon EC2 instance from the Command Palette
<a name="w2aac17c31b9c17b5b1"></a>

1. From VS Code, open the VS Code Command Palette by pressing **command \+ shift \+ P (Windows: ctrl \+ shift \+ P)**

1. From the VS Code Command Palette, search for the **AWS: Stop EC2 instance** command and select it when it populates in the list to open the **Select EC2 Instance** prompt in VS Code.

1. From the **Select EC2 Instance** prompt, choose the region that contains the instance you want to stop.

1. VS Code displays the status while the instance is stopping.

1. The AWS Explorer updates to show that your instance is stopped.

### Stopping an Amazon EC2 instance from the AWS Explorer
<a name="w2aac17c31b9c17b5b3"></a>

1. Expand the AWS Toolkit Explorer, then expand the region that contains the Amazon EC2 instance you want to stop.

1. Hover over the Amazon EC2 instance, then choose the **(Stop EC2 instance)** icon.

1. VS Code displays the status while the instance is stopping.

1. The AWS Explorer updates to show that your instance has stopped.

### Stopping an Amazon EC2 instance from the right-click menu
<a name="w2aac17c31b9c17b5b5"></a>

1. Expand the AWS Toolkit Explorer, then expand the region that contains the Amazon EC2 instance you want to stop.

1. Right-click the Amazon EC2 instance you want to connect to, then choose **Reboot EC2 instance**.

1. VS Code displays the status while the instance is stopping.

1. The AWS Explorer updates to show that your instance has stopped.

## Copy Instance ID
<a name="w2aac17c31b9c19"></a>

To copy an instance ID, complete the following steps.

1. Right-click the instance your want to copy the ID from.

1. Choose **Copy Instance ID**.

1. The instance ID is copied to your local clipboard.

## Copy Name
<a name="w2aac17c31b9c21"></a>

To copy an instance name, complete the following steps.

1. Right-click the instance your want to copy the name from.

1. Choose **Copy Instance Name**.

1. The instance name is copied to your local clipboard.

## Copy ARN
<a name="w2aac17c31b9c23"></a>

To copy an instance ARN, complete the following steps.

1. Right-click the instance your want to copy the ARN from.

1. Choose **Copy Instance ARN**.

1. The instance ARN is copied to your local clipboard.
