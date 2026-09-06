---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/ec2-troubleshoot.html
---

# Troubleshooting Amazon Elastic Compute Cloud
<a name="ec2-troubleshoot"></a>

The following sections describe how to troubleshoot known issues that can occur when working with Amazon Elastic Compute Cloud in the AWS Toolkit for Visual Studio Code. For detailed information about troubleshooting issues specific to the Amazon EC2 service, see the [Troubleshoot issues with Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.html) topic in the *Amazon Elastic Compute Cloud* User Guide.

## General Debugging
<a name="w2aac17c31c11b5"></a>

If you encounter a remote connection issue for any reason, start by checking to see if an AWS Systems Manager connection can be established from the AWS Console.

To connect to an Amazon EC2 instance through Systems Manager from the AWS Console, complete the following steps.

1. From your web browser, navigate to the [AWS Console](https://console.aws.amazon.com/ec2/).

1. Complete authentication to proceed to the AWS Console EC2 landing.

1. From the Amazon EC2 navigation pane, choose **Instances**.

1. Select the box located next to the instance that you want to connect to.

1. Choose the **Connect** button to open the **Connect to instance** screen in a new browser tab.
**Note**
You can only connect to an instance if it's running. If you're not able to select the **Connect** button, check to make sure that your instance is running.

1. From the **Connect to instance** screen, choose the **Session Manager** tab, then choose the **Connect** button to open the Systems Manager connection in your current browser tab.
**Note**
If you recently started your instance and the option isn't available for you to connect the Systems Manager, you may need to wait a few additional minutes before the option becomes available.

## Target instance is not running
<a name="w2aac17c31c11b7"></a>

To connect to an Amazon EC2 instance from the terminal or a remote connection, the instance must be running. Before you attempt to connect to your instance from the AWS Toolkit, start it from the AWS Explorer, AWS Management Console, or AWS Command Line Interface.

## Target instance doesn't have an IAM role or has an IAM role with improper permissions
<a name="w2aac17c31c11b9"></a>

To connect to your Amazon EC2 instance, it must have an IAM role with the correct permissions attached. If you attempt to connect to an instance that doesn't have an IAM role attached, you're notified by VS Code.

If you attempt to connect to an instance that has an IAM role but lacks necessary permissions, you're prompted to add the minimum necessary actions as an inline policy to the existing IAM role. After updating the inline policy, you're connected to your instance. For detailed information about IAM roles, permissions, and attaching a role to an instance, see the [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) topic in the *Amazon Elastic Compute Cloud* User Guide and the [Step 2: Verify or add instance permissions for Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-instance-profile.html) topic in the *AWS Systems Manager* User Guide.

The following example contains the minimum-necessary actions.

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
`AmazonSSMManagedEC2InstanceDefaultPolicy`
`AmazonSSMManagedInstanceCore`

## Target instance doesn't have a Systems Manager agent running
<a name="w2aac17c31c11c11"></a>

You may encounter this issue for a number of different reasons. To fix the issue, start by rebooting the instance and making another connection attempt. Or, manually start an initial connection through a non-ssm connection method. For more detailed information about Systems Manager, see the [Working with Systems Manager Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) topic in the *AWS Systems Manager*.

## On start-up, Amazon EC2 status indicates it's running, but connections aren't going through
<a name="w2aac17c31c11c13"></a>

If you recently started or created a new IAM role for an instance and are unable to establish a connection, wait a few additional minutes before making another attempt to establish a connection.
