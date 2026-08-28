---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-outbound-network-traffic/introduction.html
---

# Secure your VPC's outbound network traffic in the AWS Cloud
<a name="introduction"></a>

*Kirankumar Chandrashekar and Abdal Garuba, Amazon Web Services*

This guide covers best practices for securing and monitoring outbound network traffic when using Amazon Virtual Private Cloud (Amazon VPC). It also describes AWS tools that can help you monitor outbound network traffic from elastic network interfaces and virtual private clouds (VPCs) in the AWS Cloud.

**Note**
This guide doesn't cover third-party tools that can integrate with AWS to provide additional layers of security. It also assumes a cloud-only architecture. This guide doesn't apply to hybrid architectures.

The following best practices are outlined in this guide:
+ Determining your VPC's security requirements by analyzing existing traffic patterns
+ Restricting a VPC's outbound traffic by using security groups
+ Restricting a VPC's outbound traffic by using AWS Network Firewall and DNS hostnames
+ Accessing AWS resources by using VPC endpoints
+ Establishing private connectivity between internal applications by using AWS PrivateLink
+ Communicating across VPCs and AWS Regions by using VPC peering or AWS Transit Gateway

**Note**
For the best possible security posture, you can also pass outbound traffic through a dedicated path to a filtering tool, such as a firewall appliance.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This guide helps you do the following:

1. Control and monitor your VPC's outbound network traffic.

1. Make sure that traffic between your AWS resources passes through secure, private routes that are controlled by the AWS backbone network.

1. Implement AWS tools to continuously monitor outbound network traffic and stop requests to unapproved endpoints.

## Attachments
<a name="attachments-bce22483-dc0a-4eb3-b027-d2b6a2a1a92a"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
