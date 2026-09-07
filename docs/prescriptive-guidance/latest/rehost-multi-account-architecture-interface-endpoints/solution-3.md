---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-multi-account-architecture-interface-endpoints/solution-3.html
---

# Solution 3: Sharing VPC interface endpoints
<a name="solution-3"></a>

## Use case
<a name="use-case.e4273b04-ec58-5883-a509-c93ee1d30cdc"></a>

Your applications are mapped to different business units, and you want to migrate them to different AWS target accounts in the same Region for billing and isolation purposes.

## Challenge
<a name="challenge.c576a86b-7849-5667-b656-5b145242ab0d"></a>

Multiple workload accounts increase both the administrative overhead and the cost of individual VPC interface endpoints in each account. Therefore, you might want to have fewer staging VPCs for MGN and centrally manage routing for the staging VPCs to reduce costs and administrative overhead.

## Solution
<a name="solution.891b31fc-ecb1-53af-92f2-ffaf1b0efc79"></a>

Share VPC endpoints by using a shared staging area subnet, AWS Organizations, and AWS RAM. For more information about VPC sharing, see the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html).

## Architecture
<a name="architecture.10c9aa9a-8d0a-53f0-953f-a0b38cb33dfb"></a>

The following diagram illustrates the architecture for this solution.

![Traffic flow for rehosting multiple accounts by sharing VPC endpoints.](https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-multi-account-architecture-interface-endpoints/images/guide-img/7711a996-1484-4997-8795-d06bd903a940/images/a5129238-4cb3-40d1-b829-c528b15af832.png)

The diagram illustrates the following traffic flow:

1. The MGN replication server queries the VPC\+2 DNS to resolve the API endpoint for MGN, Amazon EC2, or Amazon S3.

2. The VPC\+2 DNS resolves the private IP of the endpoint with the help of AWS managed private hosted zones and responds to the MGN replication server.

3-6. The replication server uses that IP to connect to the AWS service API through the interface endpoint for the service.

## Implementation steps
<a name="implementation-steps.b68260cf-947d-5717-a2fc-6574084cf0e0"></a>

1. In the central networking account, create the staging VPC and subnet for MGN.

1. Create endpoints for MGN, Amazon EC2, or Amazon S3 with private DNS names enabled. This creates an AWS managed private hosted zone and associates it with the staging VPC.

1. Share the staging subnet with target application accounts in the same AWS organization and AWS Region.

1. For hybrid connectivity between AWS and your on-premises data center (not shown in the previous diagram) use Transit Gateway, Direct Connect or AWS Site-to-Site VPN with Route 53 Resolver endpoints, as shown in [solution 1](solution-1.md) and [solution 2](solution-2.md).

## Limitations
<a name="limitations.40d840d7-6b53-5eae-88e0-430a03c18a6b"></a>
+ The AWS accounts for the participant VPCs and the owner VPC have to be part of the same organization in AWS Organizations.
+ For a list of shareable resources, see the [Amazon VPC documentation](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-vpc).
+ For VPC sharing limitations, see the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html#vpc-share-limitations).

## Design considerations
<a name="design-considerations.bb0ff092-5c79-5a50-b09e-3501b79b28bc"></a>
+ To reduce your operational overhead, create a resource once, and then use AWS RAM to share that resource with other accounts. This eliminates the need to provision duplicate resources in every account and reduces operational overhead.
+ Simplify security management for your shared resources by using a single set of policies and permissions. If you create duplicate resources in your separate accounts, you have to implement identical policies and permissions and keep them synchronized across all accounts. Instead, you can manage all users who share an AWS RAM resource through a single set of policies and permissions. AWS RAM offers a consistent experience for sharing different types of AWS resources.
+ Provide visibility and auditability. View the usage details for your shared resources by integrating AWS RAM with Amazon CloudWatch and AWS CloudTrail. For more information, see [Monitoring AWS RAM using EventBridge](https://docs.aws.amazon.com/ram/latest/userguide/using-eventbridge.html) and [Logging AWS RAM API calls with AWS CloudTrail](https://docs.aws.amazon.com/ram/latest/userguide/cloudtrail-logging.html) in the AWS RAM documentation.
