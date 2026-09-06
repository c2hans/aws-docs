---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

 This section provides a reference implementation architecture diagram for the components deployed with this guidance.

## Architecture diagram
<a name="architecture-diagram"></a>

 Deploying this guidance with the default parameters deploys the following components in your AWS account.

![Guidance architecture diagram. Details are provided in the text that follows.](http://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/images/cross-network-traffic-inspection-with-aws-network-firewall.png)

**Note**
 [AWS CloudFormation](https://aws.amazon.com/cloudformation/) resources are created from [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) (AWS CDK) constructs.

 The high-level process flow for the guidance components deployed with the CloudFormation template is as follows:

1.  The AWS CloudFormation template deploys an [inspection virtual private cloud (VPC)](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/) with four subnets in randomly-selected Availability Zones within the Region where the guidance is deployed.

   1.  The guidance uses two of the subnets to create [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) attachments for your VPCs if you provide an existing transit gateway ID.

   1.  The guidance uses the other two subnets to create [AWS Network Firewall](https://aws.amazon.com/network-firewall/) endpoints in two randomly-selected Availability Zones within the Region where the guidance is deployed.

1.  The **CloudFormation** template creates an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket with a default network firewall configuration that allows all traffic. This initiates [AWS CodePipeline](https://aws.amazon.com/codepipeline/) to run the following stages:
**Note**
 The template also includes a set of examples to help you create new rule groups. You can modify the configuration package in the S3 bucket.

   1.  **Validation stage**: The guidance validates the **Network Firewall** configuration by using **Network Firewall** application programming interfaces (APIs) with dry run mode enabled. This allows you to find unexpected issues before attempting an actual change. This stage also checks whether all the referenced files in the configuration exist in the JSON file structure.

   1.  **Deployment stage**: The guidance creates a new [firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewalls.html), [firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policies.html), and [rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups.html). If any of the resources already exist, the guidance updates the resources. This stage also helps with detecting any changes and remediates by applying the latest configuration from the **S3** bucket.

   1.  The rule group changes roll back to the original state if one of the rule group changes fails. The appliance mode activates for the attachment from **Transit Gateway** to [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/) to avoid asymmetric traffic. For more information, refer to [Appliance in a shared services VPC](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-appliance-scenario.html).

1.  The guidance creates **Amazon VPC** route tables for each Availability Zone. The default route destination target for each is the **Amazon VPC** endpoint for **Network Firewall**.

1.  The guidance creates a shared route table with firewall subnets. The default route destination target is the transit gateway ID. This route is only created if the transit gateway ID is provided in the **CloudFormation** input parameters.
