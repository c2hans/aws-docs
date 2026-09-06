---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to this solution.

 **application**

A logical group of AWS resources that you want to operate as a unit.

 **attachment**

Connection from a resource to a transit gateway. For this solution, you can attach one or more VPCs to the transit gateway.

 **CloudFormation stack**

Provisions the resources that are described in the templates.

 **CloudFormation template**

Specifies the AWS resources included in this solution and their properties.

 **hub account**

Central account where the solution is deployed and manages your central transit gateway. This is typically your network account.

 **network account**

The networking account serves as the central hub for your network on AWS. You can manage your networking resources and route traffic between accounts in your environment, your on-premises, and egress/ingress traffic to the internet.

 **route table**

A set of routing rules that controls the traffic leaving any subnet that’s associated with the route table. This includes dynamic and static routes that decide the next hop based on the destination IP address of the packet.

 **state machine**

A workflow for [AWS Step Functions](https://aws.amazon.com/step-functions/).

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).
