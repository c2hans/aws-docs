---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-your-first-auto-scaling-group.html
---

# Tutorial: Create your first Auto Scaling group
<a name="create-your-first-auto-scaling-group"></a>

This tutorial provides a hands-on introduction to Amazon EC2 Auto Scaling through the AWS Management Console. You'll create a launch template that defines your EC2 instances and an Auto Scaling group with a single instance in it. After launching your Auto Scaling group, you'll terminate the instance and verify that the instance was removed from service and replaced. To maintain a constant number of instances, Amazon EC2 Auto Scaling detects and responds to Amazon EC2 health and reachability checks automatically.

When you sign up for AWS, you can get started with Amazon EC2 Auto Scaling for free using the [AWS Free Tier](https://aws.amazon.com/free/). You can use the free tier to launch and use a `t2.micro` instance for free for 12 months (in Regions where `t2.micro` is unavailable, you can use a `t3.micro` instance under the free tier). If you launch an instance that is not within the free tier, you incur the standard Amazon EC2 usage fees for the instance. For more information, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/).

**Topics**
+ [Prepare for the walkthrough](#gs-preparing-for-walkthrough)
+ [Step 1: Create a launch template](#gs-create-lt)
+ [Step 2: Create a single-instance Auto Scaling group](#gs-create-asg)
+ [Step 3: Verify your Auto Scaling group](#gs-verify-asg)
+ [Step 4: Terminate an instance in your Auto Scaling group](#gs-asg-terminate-instance)
+ [Step 5: Next steps](#gs-tutorial-next-steps)
+ [Step 6: Clean up](#gs-delete-asg)

## Prepare for the walkthrough
<a name="gs-preparing-for-walkthrough"></a>

This walkthrough assumes that you are familiar with launching EC2 instances and that you have already created a key pair and a security group.

To get started using Amazon EC2 Auto Scaling, you can use the *default* VPC for your AWS account. The default VPC includes a default public subnet in each Availability Zone and an internet gateway that is attached to your VPC. You can view your VPCs on the [Your VPCs page](https://console.aws.amazon.com/vpc/home?/#vpcs) of the Amazon Virtual Private Cloud (Amazon VPC) console.

## Step 1: Create a launch template
<a name="gs-create-lt"></a>

In this step, you create a launch template that specifies the type of EC2 instance that Amazon EC2 Auto Scaling creates for you. Include information such as the ID of the Amazon Machine Image (AMI) to use, the instance type, the key pair, and security groups.

**To create a launch template**

1. Open the Amazon EC2 console and go to the [Launch templates page](https://console.aws.amazon.com/ec2/v2/#LaunchTemplates).

1. On the top navigation bar, select an AWS Region. The launch template and Auto Scaling group that you create are tied to the Region that you specify.

1. Choose **Create launch template**.

1. For **Launch template name**, enter **my-template-for-auto-scaling**.

1. Under **Auto Scaling guidance**, select the check box.

1. For **Application and OS Images (Amazon Machine Image)**, choose a version of Amazon Linux 2 (HVM) from the **Quick Start** list. The AMI serves as a basic configuration template for your instances.

1. For **Instance type**, choose a hardware configuration that is compatible with the AMI that you specified.

1. (Optional) For **Key pair (login)**, choose an existing key pair. You use key pairs to connect to an Amazon EC2 instance with SSH. Connecting to an instance is not included as part of this tutorial. Therefore, you don't need to specify a key pair unless you intend to connect to your instance using SSH.

1. For **Network settings**, expand **Advanced network configuration** and do the following:

   1. Choose **Add network interface** to configure the primary network interface.

   1. For **Auto-assign public IP**, specify whether your instance receives a public IPv4 address. By default, Amazon EC2 assigns a public IPv4 address if the EC2 instance is launched into a default subnet or if the instance is launched into a subnet that's been configured to automatically assign a public IPv4 address. If you don't need to connect to your instance, choose **Disable**.

   1. For **Security group ID**, choose a security group in the same VPC that you plan to use as the VPC for your Auto Scaling group. If you don't specify a security group, your instance is automatically associated with the default security group for the VPC.

   1. For **Delete on termination**, choose **Yes** to delete the network interface when the instance is deleted.

1. Choose **Create launch template**.

1. On the confirmation page, choose **Create Auto Scaling group**.

## Step 2: Create a single-instance Auto Scaling group
<a name="gs-create-asg"></a>

Use the following procedure to continue where you left off after creating a launch template.

**To create an Auto Scaling group**

1. On the **Choose launch template or configuration** page, for **Auto Scaling group name**, enter **my-first-asg**.

1. Choose **Next**.

   The **Choose instance launch options** page appears, allowing you to choose the VPC network settings you want the Auto Scaling group to use and giving you options for launching On-Demand and Spot Instances.

1. In the **Network** section, keep **VPC** set to the default VPC for your chosen AWS Region, or select your own VPC. The default VPC is automatically configured to provide internet connectivity to your instance. This VPC includes a public subnet in each Availability Zone in the Region.

1. For **Availability Zones and subnets**, choose a subnet from each Availability Zone that you want to include. Use subnets in multiple Availability Zones for high availability. For more information, see [Considerations when choosing VPC subnets](asg-in-vpc.md#as-vpc-considerations).

1. In the **Instance type requirements** section, use the default setting to simplify this step. (Do not override the launch template.) For this tutorial, you will launch only one On-Demand Instance using the instance type specified in your launch template.

1. Keep the rest of the defaults for this tutorial and choose **Skip to review**.
**Note**
The initial size of the group is determined by its desired capacity. The default value is `1` instance.

1. On the **Review** page, review the information for the group, and then choose **Create Auto Scaling group**.

## Step 3: Verify your Auto Scaling group
<a name="gs-verify-asg"></a>

Now that you have created an Auto Scaling group, you are ready to verify that the group has launched an EC2 instance.

**Tip**
In the following procedure, you look at the **Activity history** and **Instances** sections for the Auto Scaling group. In both, the named columns should already be displayed. To display hidden columns or change the number of rows shown, choose the gear icon on the top right corner of each section to open the preferences modal, update the settings as needed, and choose **Confirm**.

**To verify that your Auto Scaling group has launched an EC2 instance**

1. Open the [Auto Scaling groups page](https://console.aws.amazon.com/ec2/v2/home?#AutoScalingGroups) of the Amazon EC2 console.

1. Select the check box next to the Auto Scaling group that you just created.

   A split pane opens up in the bottom of the **Auto Scaling groups** page. The first tab available is the **Details** tab, showing information about the Auto Scaling group.

1. Choose the second tab, **Activity**. Under **Activity history**, you can view the progress of activities that are associated with the Auto Scaling group. The **Status** column shows the current status of your instance. While your instance is launching, the status column shows `Not yet in service`. The status changes to `Successful` after the instance is launched. You can also use the refresh button to see the current status of your instance.

1. On the **Instance management** tab, under **Instances**, you can view the status of the instance.

1. Verify that your instance launched successfully. It takes a short time for an instance to launch.
   + The **Lifecycle** column shows the state of your instance. Initially, your instance is in the `Pending` state. After an instance is ready to receive traffic, its state is `InService`.
   + The **Health status** column shows the result of the Amazon EC2 Auto Scaling health checks on your instance.

## Step 4: Terminate an instance in your Auto Scaling group
<a name="gs-asg-terminate-instance"></a>

Use these steps to learn more about how Amazon EC2 Auto Scaling works, specifically, how it launches new instances when necessary. The minimum size for the Auto Scaling group that you created in this tutorial is one instance. Therefore, if you terminate that running instance, Amazon EC2 Auto Scaling must launch a new instance to replace it.

1. Open the [Auto Scaling groups page](https://console.aws.amazon.com/ec2/v2/home?#AutoScalingGroups) of the Amazon EC2 console.

1. Select the check box next to your Auto Scaling group.

1. On the **Instance management** tab, under **Instances**, select the ID of the instance.

   This takes you to the **Instances** page of the Amazon EC2 console, where you can terminate the instance.

1. Choose **Actions**, **Instance State**, **Terminate**. When prompted for confirmation, choose **Yes, Terminate**.

1. On the navigation pane, under **Auto Scaling**, choose **Auto Scaling Groups**. Select your Auto Scaling group and choose the **Activity** tab.

   When you terminate an instance from the **Instances** page, it takes a minute or two after you terminate the instance before a new instance launches. In the activity history, when the scaling activity starts, you see an entry for the termination of the first instance and an entry for the launch of a new instance. Use the refresh button until you see the new entries.

1. On the **Instance management** tab, the **Instances** section shows the new instance only.

1. On the navigation pane, under **Instances**, choose **Instances**. This page shows both the terminated instance and the new running instance.

## Step 5: Next steps
<a name="gs-tutorial-next-steps"></a>

Go to the next step if you would like to delete the basic infrastructure that you just created. Otherwise, you can use this infrastructure as your base and try one or more of the following:
+ Connect to your Linux instance using Session Manager or SSH. For more information, see [Connect to your EC2 instance using Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-with-systems-manager-session-manager.html) and [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) in the *Amazon EC2 User Guide*.
+ Configure an Amazon SNS notification to notify you whenever your Auto Scaling group launches or terminates instances. For more information, see [Amazon SNS notification options](ec2-auto-scaling-sns-notifications.md).
+ Manually scale your Auto Scaling group to test the SNS notification. For more information, see [Change the desired capacity of your Auto Scaling group](ec2-auto-scaling-scaling-manually.md#change-desired-capacity).

You can also start familiarizing yourself with auto scaling concepts by reading about [Target tracking scaling policies](as-scaling-target-tracking.md). If the load on your application changes, your Auto Scaling group can scale out (add instances) and scale in (run fewer instances) automatically by adjusting the desired capacity of the group between the minimum and maximum capacity limits. For more information about setting these limits, see [Set scaling limits for your Auto Scaling group](asg-capacity-limits.md).

## Step 6: Clean up
<a name="gs-delete-asg"></a>

You can either delete your scaling infrastructure or delete just your Auto Scaling group and keep your launch template to use later.

If you launched an instance that is not within the [AWS Free Tier](https://aws.amazon.com/free/), you should terminate your instance to prevent additional charges. When you terminate the instance, the data associated with it will also be deleted.

**To delete your Auto Scaling group**

1. Open the [Auto Scaling groups page](https://console.aws.amazon.com/ec2/v2/home?#AutoScalingGroups) of the Amazon EC2 console.

1. Select the check box next to your Auto Scaling group (`my-first-asg`).

1. Choose **Delete**.

1. When prompted for confirmation, type **delete** to confirm deleting the specified Auto Scaling group and then choose **Delete**.

   A loading icon in the **Name** column indicates that the Auto Scaling group is being deleted. When the deletion has occurred, the **Desired**, **Min**, and **Max** columns show `0` instances for the Auto Scaling group. It takes a few minutes to terminate the instance and delete the group. Refresh the list to see the current state.

Skip the following procedure if you would like to keep your launch template.

**To delete your launch template**

1. Open the [Launch templates page](https://console.aws.amazon.com/ec2/v2/#LaunchTemplates) of the Amazon EC2 console.

1. Select your launch template (`my-template-for-auto-scaling`).

1. Choose **Actions**, **Delete template**.

1. When prompted for confirmation, type **Delete** to confirm deleting the specified launch template and then choose **Delete**.
