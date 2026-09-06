---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/architecture.html
---

# Architecture components and requirements for restricted replication
<a name="architecture"></a>

This section provides a detailed description of the most restrictive scenario, where all communication occurs over the private channel only, and includes a detailed explanation of the requirements and corresponding components to be built for each area.

## Staging subnet
<a name="staging-subnet"></a>

The [staging subnet](https://docs.aws.amazon.com/mgn/latest/ug/subnet.html) is the most important part of the replication infrastructure. This is where all AWS Transform MGN [replication servers](https://docs.aws.amazon.com/mgn/latest/ug/replication-server-settings.html) will be launched, and it contains the IP addresses the replication traffic will be directed to. For inbound private data replication, configure the [replication server settings](https://docs.aws.amazon.com/mgn/latest/ug/template-vs-server.html) for MGN with the [Use private IP option](https://docs.aws.amazon.com/mgn/latest/ug/use-private-ip.html).

For [outbound requirements](https://docs.aws.amazon.com/mgn/latest/ug/Network-Requirements.html#Communication-TCP-443-Staging), you can use the [Create public IP](https://docs.aws.amazon.com/mgn/latest/ug/use-private-ip.html#public-ip) option to choose whether replication servers will communicate with required AWS services (Amazon S3, MGN, Amazon EC2) over private or public IP. The standard options to provide outbound internet connectivity are listed in the [MGN documentation](https://docs.aws.amazon.com/mgn/latest/ug/Network-Requirements.html#Communication-TCP-443-Staging): either a public IP address with an internet gateway or a private IP address with a NAT gateway. Both options allow you to implement a simplified hybrid scenario in which data replication traffic goes over a private connection (AWS VPN or AWS Direct Connect) while replication servers communicate with AWS services over the public network.

However, having public outbound connectivity is usually prohibited in closed corporate environments, and this is the most restrictive scenario discussed in the next section. In this case, you use AWS PrivateLink and configure the following VPC endpoints in staging subnets for replication servers:
+ VPC gateway endpoint to communicate with Amazon S3
+ VPC interface endpoints to communicate with MGN and Amazon EC2

To learn more about VPC endpoints, see the [AWS PrivateLink documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html).

## Source subnet
<a name="source-subnet"></a>

The source subnet is any subnet you are replicating from. This is where your [source servers](https://docs.aws.amazon.com/mgn/latest/ug/source-servers.html) are located and where you will install AWS Replication Agent on these servers. The [network requirements](https://docs.aws.amazon.com/mgn/latest/ug/Network-Requirements.html#Source-Manager-TCP-443) for an Agent include:
+ Communicating over HTTPS/TCP port 443 with AWS services such as Amazon S3 and MGN
+ Communicating with the replication server's IP address (private or public, based on its settings)

The Agent also supports hybrid scenarios where communication with AWS services can happen over the public network (using standard HTTPS traffic) while replication data is sent over private networks to the private IP of the replication server.

This guide focuses on a more restrictive scenario where even HTTPS traffic to AWS services isn't allowed from source systems, so the following endpoints are configured in the staging subnet:
+ VPC interface endpoints for MGN and Amazon S3 (Regional interface endpoint, not the gateway endpoint that's required for replication servers)
+ An [inbound DNS resolver endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-network-to-vpc), to allow on-premises sources and DNS servers to resolve private IP addresses for VPC endpoints, located in the staging subnet.

## Target subnet
<a name="target-subnet"></a>

The target subnet is any subnet that you plan to launch your servers into, including test and cutover instances. These subnets have no network connectivity requirement at all, and could be located in any other VPC in the same AWS account and Region. This is because MGN uses Amazon EC2 APIs to create new test or cutover instances (which is why replication servers in the staging subnet require outbound HTTPS connectivity to Amazon EC2), and accesses Regional Amazon S3 snapshots created from replicated Amazon EBS volumes. None of these operations require direct network access to or from the target subnet, so this could even be a completely isolated private subnet.

However, MGN also [automatically installs](https://docs.aws.amazon.com/mgn/latest/ug/AWS-Related-FAQ.html#Which-AWS-Services-Automatically-Installed-Target) several tools, such as EC2Config or AWS Systems Manager Agents (SSM Agents) on target instances, and these activities require outbound HTTPS/TCP port 443 connectivity from target instances and subnets.
