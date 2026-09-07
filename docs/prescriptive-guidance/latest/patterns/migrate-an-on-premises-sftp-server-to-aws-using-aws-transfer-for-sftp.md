---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-sftp-server-to-aws-using-aws-transfer-for-sftp.html
---

# Migrate an on-premises SFTP server to AWS using AWS Transfer for SFTP
<a name="migrate-an-on-premises-sftp-server-to-aws-using-aws-transfer-for-sftp"></a>

*Akash Kumar, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-sftp-server-to-aws-using-aws-transfer-for-sftp-summary"></a>

This pattern describes how to migrate an on-premises file transfer solution that uses the Secure Shell (SSH) File Transfer Protocol (SFTP) to the AWS Cloud by using the AWS Transfer for SFTP service. Users generally connect to an SFTP server either through its domain name or by fixed IP. This pattern covers both cases.

AWS Transfer for SFTP is a member of the AWS Transfer Family. It is a secure transfer service that you can use to transfer files into and out of AWS storage services over SFTP. You can use AWS Transfer for SFTP with Amazon Simple Storage Service (Amazon S3) or Amazon Elastic File System (Amazon EFS). This pattern uses Amazon S3 for storage.

## Prerequisites and limitations
<a name="migrate-an-on-premises-sftp-server-to-aws-using-aws-transfer-for-sftp-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An existing SFTP domain name or fixed SFTP IP.

**Limitations**
+ The largest object that you can transfer in one request is currently 5 GiB. For files that are larger than 100 MiB, consider using [Amazon S3 multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html).

## Architecture
<a name="migrate-an-on-premises-sftp-server-to-aws-using-aws-transfer-for-sftp-architecture"></a>

**Source technology stack  **
+ On-premises flat files or database dump files.

**Target technology stack  **
+ AWS Transfer for SFTP
+ Amazon S3
+ Amazon Virtual Private Cloud (Amazon VPC)
+ AWS Identity and Access Management (IAM) roles and policies
+ Elastic IP addresses
+ Security groups
+ Amazon CloudWatch Logs (optional)

**Target architecture **

![Use AWS Transfer for SFTP to migrate an on-premises SFTP server to the AWS Cloud.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/ec0a905c-edef-48ba-9b5e-ea4a4040d320/images/f42aa711-bfe0-4ac6-9f66-5c18a1dd1c7a.png)

**Automation and scale**

To automate the target architecture for this pattern, use the attached CloudFormation templates:
+ `amazon-vpc-subnets.yml` provisions a virtual private cloud (VPC) with two public and two private subnets.
+ `amazon-sftp-server.yml` provisions the SFTP server.
+ `amazon-sftp-customer.yml` adds users.

## Tools
<a name="migrate-an-on-premises-sftp-server-to-aws-using-aws-transfer-for-sftp-tools"></a>

**AWS services**
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data. This pattern uses Amazon S3 as the storage system for file transfers.
+ [AWS Transfer for SFTP](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html) helps you transfer files into and out of AWS storage services over the SFTP protocol.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

## Epics
<a name="migrate-an-on-premises-sftp-server-to-aws-using-aws-transfer-for-sftp-epics"></a>

### Create a VPC
<a name="create-a-vpc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC with subnets. | Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/). Create a virtual private cloud (VPC) with two public subnets. (The second subnet provides high availability.)<br />—or—<br />You can deploy the attached CloudFormation template, `amazon-vpc-subnets.yml`, in the [CloudFormation console](https://console.aws.amazon.com/cloudformation) to automate the tasks in this epic. | Developer, Systems administrator |
| Add an internet gateway. | Provision an internet gateway and attach it to the VPC. | Developer, Systems administrator |
| Migrate an existing IP. | Attach an existing IP to the Elastic IP address. You can create an Elastic IP address from your address pool and use it. | Developer, Systems administrator |

### Provision an SFTP server
<a name="provision-an-sftp-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an SFTP server. | Open the [AWS Transfer Family console](https://console.aws.amazon.com/transfer/). Follow the instructions in [Create an internet-facing endpoint for your server](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#create-internet-facing-endpoint) in the AWS Transfer Family documentation to create an SFTP server with an internet-facing endpoint. For **Endpoint type**, choose **VPC hosted**. For **Access**, choose **Internet Facing**. For **VPC**, choose the VPC you created in the previous epic.<br />—or—<br />You can deploy the attached CloudFormation template, `amazon-sftp-server.yml`, in the [CloudFormation console](https://console.aws.amazon.com/cloudformation) to automate the tasks in this epic. | Developer, Systems administrator |
| Migrate the domain name. | Attach the existing domain name to the custom hostname. If you're using a new domain name, use the **Amazon Route 53 DNS **alias. For an existing domain name, choose **Other DNS**. For more information, see [Working with custom hostnames](https://docs.aws.amazon.com/transfer/latest/userguide/requirements-dns.html) in the AWS Transfer Family documentation. | Developer, Systems administrator |
| Add a CloudWatch logging role. | (Optional) if you want to enable CloudWatch logging, create a `Transfer` role with the CloudWatch Logs API operations  `logs:CreateLogGroup`, `logs:CreateLogStream`,` logs:DescribeLogStreams`, and `logs:PutLogEvents`. For more information, see[ Log activity with CloudWatch](https://docs.aws.amazon.com/transfer/latest/userguide/monitoring.html#monitoring-enabling) in the AWS Transfer Family documentation. | Developer, system administrator |
| Save and submit. | Choose **Save**. For **Actions**, choose **Start **and wait for the SFTP server to be created with the status **Online**. | Developer, Systems administrator |

### Map Elastic IP addresses to the SFTP server
<a name="map-elastic-ip-addresses-to-the-sftp-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop the server so you can modify settings. | On the [AWS Transfer Family console](https://console.aws.amazon.com/transfer/), choose **Servers**, and then select the SFTP server you created. For **Actions**, choose **Stop**. When the server is offline, choose **Edit **to modify its settings. | Developer, system administrator |
| Choose Availability Zones and subnets. | In the **Availability Zones** section, choose the Availability Zones and subnets for your VPC. | Developer, Systems administrator |
| Add Elastic IP addresses. | For **IPv4 Addresses**, choose an Elastic IP address for each subnet, and then choose **Save**. | Developer, Systems administrator |

### Add users
<a name="add-users"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM role for users to access the S3 bucket. | Create a IAM role for `Transfer`** **and add` s3:ListBucket`,` s3:GetBucketLocation`, and `s3:PutObject` with the S3 bucket name as a resource. For more information, see [Create an IAM role and policy](https://docs.aws.amazon.com/transfer/latest/userguide/requirements-roles.html) in the AWS Transfer Family documentation.<br />—or—<br />You can deploy the attached CloudFormation template, `amazon-sftp-customer.yml`, in the [CloudFormation console](https://console.aws.amazon.com/cloudformation) to automate the tasks in this epic. | Developer, Systems administrator |
| Create an S3 bucket. | Create a S3 bucket for the application. | Developer, Systems administrator |
| Create optional folders. | (Optional) If you want to store files for users separately, in specific Amazon S3 folders, add folders as appropriate. | Developer, Systems administrator |
| Create an SSH public key. | To create an SSH key pair, see [Generate SSH keys](https://docs.aws.amazon.com/transfer/latest/userguide/key-management.html#sshkeygen) in the AWS Transfer Family documentation. | Developer, Systems administrator |
| Add users. | On the [AWS Transfer Family console](https://console.aws.amazon.com/transfer/), choose **Servers**, select the SFTP server you created, and then choose **Add user**. For **Home directory**, choose the S3 bucket you created. For **SSH public key**, specify the public key portion of the SSH key pair. Add users for the SFTP server, and then choose **Add**. | Developer, Systems administrator |

### Test the SFTP server
<a name="test-the-sftp-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the security group. | In the **Security Groups** section of your SFTP server, add your test machine's IP to gain SFTP access. | Developer |
| Use an SFTP client utility to test the server. | Test file transfers by using any SFTP client utility. For a list of clients and instructions, see [Transferring files using a client](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-file.html) in the AWS Transfer Family documentation. | Developer |

## Related resources
<a name="migrate-an-on-premises-sftp-server-to-aws-using-aws-transfer-for-sftp-resources"></a>
+ [AWS Transfer Family User Guide](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-for-sftp.html)
+ [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
+ [Elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) in the Amazon EC2 documentation

## Attachments
<a name="attachments-ec0a905c-edef-48ba-9b5e-ea4a4040d320"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/ec0a905c-edef-48ba-9b5e-ea4a4040d320/attachments/attachment.zip)
