---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/5g-networks-on-aws.html
---

# 5G networks on AWS
<a name="5g-networks-on-aws"></a>

The typical model of 5G network infrastructure is composed of a 4G/5G radio site, a fronthaul/midhaul/backhaul network, a core network site, and a telecom/IT data center. CSPs can use AWS Services to create a scalable, flexible 5G network infrastructure while reducing upfront investment cost. AWS can be used to implement the virtual Network Operation Center (NOC) in the Region that hosts the Operations Support System/Business Support System (OSS/BSS) and the majority of control plane core network functions.

AWS can also be leveraged. to implement the local central office (CO) or distributed data center with a fleet of [AWS Outposts](https://aws.amazon.com/outposts/) instances that host mostly user-plane functions such as UPF (user-plane function), RAN central unit (CU), and Multi-Access Edge Computing (MEC). A more detailed explanation of the reference architecture and the benefits of 5G network implementation on AWS is explained in the [*5G Network Evolution on AWS*](https://d1.awsstatic.com/whitepapers/5g-network-evolution-with-aws.pdf) whitepaper.

When it’s time to implement the 5G network on AWS, AWS CI/CD tools, which are introduced in the following sections of this whitepaper, can facilitate the full automation of deployment, upgrade, and lifecycle management of 5G network functions.

![A diagram depicting 5G network end-to-end architecture.](https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g5.png)

*5G network E2E architecture*
