---
source_url: https://docs.aws.amazon.com/vpc/latest/userguide/working-with-igw.html
---

# Add internet access to a subnet

**Note**
You can apply internet protection to your VPC by using automated internet firewall. A managed firewall is applied at your internet gateway to inspect all traffic that enters or leaves your VPCs, without changing your routes. For more information, see [Automated Internet Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/internet-gateway-firewall.html) in the *AWS Network Firewall Developer Guide*.

The following describes how to support internet access from a subnet in a nondefault VPC using an internet gateway. You must create the internet gateway, attach it to the VPC, and configure routing for the subnet.

After you configure internet access for your subnet, you must ensure that resources in the subnet can access the internet. For example, your EC2 instances must have a public IPv4 or IPv6 address, and the security groups for your instances must allow specific traffic to and from the internet.

Alternatively, to provide your instances with internet access without assigning them a public IP address, use a NAT device instead. For more information, see [NAT devices](vpc-nat.md).

To remove internet access, you can detach the internet gateway from your VPC and then delete it. For more information, see [Delete an internet gateway](delete-igw.md).

**Topics**
+ [Step 1: Create an internet gateway](#create-igw)
+ [Step 2: Attach the internet gateway to the VPC](#attach-igw)
+ [Step 3: Add a route to the subnet route table](#routing-igw)
+ [Add firewall inspection to your internet gateway](#igw-firewall-inspection)

## Step 1: Create an internet gateway
<a name="create-igw"></a>

Use the following procedure to create an internet gateway.

**To create an internet gateway using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Internet gateways**.

1. Choose **Create internet gateway**.

1. (Optional) Enter a name for your internet gateway.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and value.

1. Choose **Create internet gateway**.

1. (Optional) To attach the internet gateway to a VPC now, choose **Attach to a VPC** from the banner at the top of the screen, select an available VPC, and then choose **Attach internet gateway**. Otherwise, you can attach your internet gateway to a VPC at another time.

**To create an internet gateway using the command line**
+ [create-internet-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-internet-gateway.html) (AWS CLI)
+ [New-EC2InternetGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2InternetGateway.html) (AWS Tools for Windows PowerShell)

## Step 2: Attach the internet gateway to the VPC
<a name="attach-igw"></a>

To use an internet gateway, you must attach it to a VPC.

**To attach an internet gateway to a VPC using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Internet gateways**.

1. Select the check box for the internet gateway.

1. To attach it, choose **Actions**, Attach to VPC, select an available VPC, and choose **Attach internet gateway**.

1. To detach it, choose **Actions**, **Detach from VPC** and choose **Detach internet gateway**. When prompted for confirmation, choose **Detach internet gateway**.

**To attach an internet gateway to a VPC using the command line**
+ [attach-internet-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-internet-gateway.html) (AWS CLI)
+ [Add-EC2InternetGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2InternetGateway.html) (AWS Tools for Windows PowerShell)

## Step 3: Add a route to the subnet route table
<a name="routing-igw"></a>

The route table for the subnet must have a route that sends internet traffic to the internet gateway.

**To configure the subnet route table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**.

1. Select the route table for the subnet. By default, a subnet uses the main route table for the VPC. Alternatively, you can [create a route table](create-vpc-route-table.md#CustomRouteTable) and then [associate the subnet with the new route table](create-vpc-route-table.md#AssociateSubnet).

1. On the **Routes** tab, choose **Edit routes** and then choose **Add route**.

1. Enter 0.0.0.0/0 for **Destination** and select the internet gateway for **Target**.

1. Choose **Save changes**.

**To configure the subnet route table using the command line**
+ [create-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-route.html) (AWS CLI)
+ [New-EC2Route](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Route.html) (AWS Tools for Windows PowerShell)

## Add firewall inspection to your internet gateway
<a name="igw-firewall-inspection"></a>

After you create and attach an internet gateway, you can use automated internet firewall to inspect the traffic that enters and leaves your VPCs through the internet gateway, and to apply managed network address translation (NAT). You set up and manage automated internet firewall centrally in Network Security Manager, and it does not require changes to your route tables. For more information, see [Getting started with Automated Internet Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/internet-gateway-firewall-getting-started.html) in the *AWS Network Firewall Developer Guide*.

**Note**
Automated internet firewall is available in public preview in all AWS commercial Regions. During the preview, it doesn't work with Regional NAT, **noNAT** ingress routing, or ingress-only VPC Block Public Access. During the preview, it also does not perform NAT64 for IPv6 traffic that is destined for an IPv4 destination. It also does not support Amazon EC2 [Mac instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html) or the following machine learning instance types: p4d, p4de, p6-b200, p6-b300, p6e-gb200, trn2, trn2u, and g7e.
