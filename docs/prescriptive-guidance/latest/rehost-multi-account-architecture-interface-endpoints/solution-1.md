---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-multi-account-architecture-interface-endpoints/solution-1.html
---

# Solution 1: Creating VPC endpoints in a central networking account for a single Region
<a name="solution-1"></a>

## Use case
<a name="use-case.78f28552-1b6c-5510-94e1-d3a1976683ff"></a>

Your applications are mapped to different business units and you want to migrate them to different AWS target accounts in the same AWS Region for billing and isolation purposes.

## Challenges
<a name="challenges.6f741941-c9c2-57db-a7fb-adf4dafafe07"></a>

To achieve this over a private network, you would have to create multiple VPC interface endpoints in every target account. This adds to administrative overhead and costs for maintaining endpoints. (See [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/).)

## Solution
<a name="solution.cf95521b-8c1a-5f56-8b38-ef2ac40f2214"></a>

Create VPC endpoints in a central AWS networking account and use Transit Gateway to connect to target application accounts.

## Architecture
<a name="architecture.ece31983-dfe9-5601-a38d-ccfba683af4a"></a>

The following diagram illustrates the architecture for this solution.

![Traffic flow for rehosting multiple accounts in the same Region.](http://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-multi-account-architecture-interface-endpoints/images/guide-img/7711a996-1484-4997-8795-d06bd903a940/images/11f6d63e-5294-4f50-9d81-949d1d283322.png)

In the diagram, the numbers represent the following traffic flow:

1. The Amazon Elastic Compute Cloud (Amazon EC2) instance or MGN replication server that needs to connect to Amazon Simple Storage Service (Amazon S3), MGN, or Amazon EC2 through an interface endpoint that's located in the central networking account VPC first needs to resolve the domain name by querying the VPC\+2 resolver. The endpoint private hosted zone is associated with the MGN staging VPC in the same Region to complete the domain resolution.
**Note**
For each private hosted zone that you associate with a VPC, the resolver creates a rule and associates it with the VPC. If you associate the private hosted zone with multiple VPCs, the resolver associates the rule with all the VPCs.

1. When the instance knows the private IP to connect to, it sends the traffic to the transit gateway ENI. The traffic is sent to the transit gateway and forwarded to the shared resource VPC, based on the transit gateway route table.

1. The transit gateway ENI in the shared resource VPC forwards the traffic to the corresponding interface endpoint.

1. The VPC endpoint sends the response back to the transit gateway ENI.

1. The traffic is forwarded to the transit gateway. As specified in the transit gateway route table, the traffic is sent to the spoke MGN staging VPC. The response is sent by the transit gateway ENI to the destination, that is, to the EC2 instance or MGN replication server.

1. A client application that's located in the corporate data center resolves a domain name in the form `<aws_service>.<aws_region>.amazonaws.com` (for example, `mgn.us-east-1.amazonaws.com`). It sends the query to its preconfigured DNS resolver. The DNS resolver in the corporate data center has a forwarding rule that points any DNS query for `amazonaws.com` domains to the Route 53 Resolver inbound endpoint. Transit Gateway forwards the query to the shared resource VPC, which forwards the DNS query at the Route 53 Resolver inbound endpoint.

   The Route 53 Resolver inbound endpoint uses the VPC\+2 resolver. The endpoint private hosted zone that's associated with the shared resource VPC holds the DNS records for `amazonaws.com`, so Route 53 Resolver can resolve the query.

1. The Route 53 Resolver outbound endpoint returns the DNS query response to the on-premises client application.

## Implementation steps
<a name="implementation-steps.391e00c3-310a-555a-8e6f-974738c10755"></a>

To set up the architecture shown in the previous diagram, follow these steps:

1. Connect your corporate data center to the central networking account on AWS through AWS Direct Connect or AWS Site-to-Site VPN.

1. In the networking account, use Transit Gateway to provide connectivity between VPCs. The transit gateway is shared between AWS accounts by using AWS RAM, and further connected to the target application account staging subnet through a VPC attachment.
**Note**
Target AWS accounts do not have to be part of the same AWS organization. For more information, see [Shareable resources](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html#shareable-vpc) in the AWS RAM documentation.

1. Create VPC interface endpoints for Amazon EC2, MGN, and Amazon S3 in the central network account **without** enabling a private DNS name.
**Note**
When you create a VPC endpoint to an AWS service, you can enable private DNS. When enabled, the setting creates a managed Route 53 private hosted zone for you. This managed zone resolves the DNS name within a VPC. However, it doesn't work outside the VPC. This is the reason for using private hosted zone sharing and Route 53 Resolver to help get unified name resolution for shared VPC endpoints.

1. Create a private hosted zone for each endpoint (MGN, Amazon EC2, Amazon S3). For example, for MGN in the `us-east-1` Region:
   + Create a private hosted zone with the domain name `mgn.us-east-1.amazonaws.com`.
   + Create a host record of type A that points the domain name to endpoint IPs.

1. Create Route 53 Resolver inbound and outbound rules to facilitate hybrid DNS resolution, and share the rules with the required AWS account in the same Region.
