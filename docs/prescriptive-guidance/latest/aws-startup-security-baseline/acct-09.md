---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-09.html
---

# ACCT.09 Delete unused VPCs, subnets, and security groups
<a name="acct-09"></a>

To reduce the opportunity for security issues, delete resources that are not being used. In a new AWS account, by default, a virtual private cloud (VPC) is created automatically in every AWS Region. This enables you to assign public IP addresses in public subnets. If these VPCs are not needed, this introduces risk of unintended exposure of resources.

If they are not in use, delete the default VPCs in each Region, including Regions where you do not plan to deploy workloads. Before you can delete a VPC, you must first delete its dependent resources in the order of their dependencies. For example, delete Amazon Elastic Compute Cloud (Amazon EC2) instances before their subnets, and delete NAT gateways and internet gateways before the VPC. Subnets and security groups are deleted when the VPC is deleted. Attempting to delete a resource that has dependent resources will result in an error.

**Note**
You can view your Regions and VPCs on the [Amazon EC2 Global View console](https://console.aws.amazon.com/ec2globalview/home). For more information, see [List and filter resources across Regions using Amazon EC2 Global View](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#global-view) in the Amazon EC2 documentation.

**To delete a default VPC and its associated resources**

1. See [Delete your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/delete-vpc.html) in the Amazon Virtual Private Cloud (Amazon VPC) documentation.

1. Repeat this process for each Region where default VPCs exist.
