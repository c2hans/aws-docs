---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/scalability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scalability
<a name="scalability"></a>

## Definition
<a name="definition-sca"></a>

 Scalability refers to the ability of your connectivity solution to grow and evolve over time as your requirements change.

 When designing a solution, you need to consider the current size, as well as the anticipated growth. This growth can be organic growth, or might be related to rapid expansion, such as in merger and acquisition type of scenarios.

 Note: depending on the targeted solution architecture, not all the preceding elements might need to be taken into consideration. However, they can serve as the foundational elements to identify the scalability requirements of most common hybrid network solutions. This whitepaper focuses on the hybrid connectivity selection and design. It is recommended that you also consider the scale of hybrid connectivity with respect to the VPC networking architecture. For more information, see the [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) whitepaper.

## Key questions
<a name="key-questions-sca"></a>
+  What is the current and anticipated number of VPCs which require connectivity to on-premises site or sites?
+  Are VPCs deployed in a single AWS Region or multiple Regions?
+  How many on-premises sites need to be connected to AWS?
+  How many customer gateway devices (typically routers or firewalls) do you have per site that need to connect to AWS?
+  How many routes are expected to be advertised to Amazon VPCs and what is the number of expected routes to be received from the AWS side?
+  Is there a requirement to increase bandwidth to AWS over time?

## Capabilities to consider
<a name="capabilities-to-consider-sca"></a>

 Scale is an important factor in hybrid connectivity design. To that point, the subsequent section will incorporate scale as a part of the targeted connectivity model design.

 The following are recommended best practices to minimize scale complexity of hybrid network connectivity design:
+  Route summarization should be used to reduce the number of routes advertised to and received from AWS. Thus, the IP addressing scheme needs designed to maximize the use of route summarization. Traffic engineering is a key overall consideration. For more information about traffic engineering, refer to the Traffic engineering subsection in the [Reliability](reliability.md) section.
+  Minimize your number of BGP peering sessions by using DXGW with VGW or AWS Transit Gateway, where a single BGP session can provide connectivity to multiple VPCs.
+  Consider Cloud WAN when multiple AWS Regions and on-premises sites need to be connected together.
