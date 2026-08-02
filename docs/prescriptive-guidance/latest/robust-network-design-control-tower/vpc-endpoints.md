---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/vpc-endpoints.html
---

# Configuring the VPC endpoints
<a name="vpc-endpoints"></a>

VPC endpoints are created in only the outbound VPC, which acts as the source for all VPCs in the organization to reach AWS services securely. This helps with managing the VPC endpoints. It also helps with cost optimization, because there is only a single endpoint source instead of multiple endpoints in individual VPCs.

## Gateway endpoint
<a name="gateway-endpoint"></a>

Gateway VPC endpoints provide reliable connectivity to Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB without requiring an internet gateway or a NAT gateway for your VPC. Unlike other types of VPC endpoints, gateway endpoints don't use AWS PrivateLink. Gateway endpoints are offered at no charge. It's good to use them in case you need access for Amazon S3 and DynamoDB from the spoke VPCs through a secure channel.

## Interface endpoint
<a name="interface-endpoint"></a>

Interface endpoints are helpful for establishing a private communication between services on AWS and endpoints over AWS PrivateLink.

In the outbound VPC, create the required VPC endpoints. For Amazon S3 and DynamoDB, create gateway endpoints in the individual VPCs. Commonly used VPC endpoints include the following:
+ Amazon S3 Control
+ DynamoDB
+ AWS Systems Manager

## Architecture
<a name="architecture"></a>

The following diagram shows how applications hosted on EC2 instances or other services in other AWS accounts reach AWS services by using centralized VPC endpoints. In this architecture, the EC2 instance in another account in VPC B can resolve Systems Manager sessions by using VPC endpoints created in VPC A.

![The architecture includes private subnets and a security group in account A.](http://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/images/guide-img/734c65f3-3001-4321-a428-6ffbda3b44b0/images/a43f69dd-8b2e-4bbe-92e6-b3a63b1a9622.png)

This helps in cost savings because VPC endpoints are hosted in the single centralized network account that you can use across organizations. You can create and manage VPC endpoints from a single account.
