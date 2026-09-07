---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/connecting-to-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Connecting to AWS
<a name="connecting-to-aws"></a>

 When moving workflows to AWS, the first step is to determine how to best connect on-premises systems to AWS. The on-premises connections can range from simple thin clients, to entire legacy enterprise infrastructure that require many levels of authentication and user access. Minimally, we suggest that you use an [Site-to-Site VPN](https://aws.amazon.com/vpn/) connection to ensure a secure environment. That said, even though Site-to-Site VPN provides basic connectivity, using [AWS Direct Connect](https://aws.amazon.com/directconnect/) can both solve security requirements and data transfer issues as well. That is, as you move data in to AWS, having a robust connection can establish a foundation for hybrid environments and allow for straightforward inbound and outbound data for the entire workflow.

![This diagram shows the services used to connect to AWS: AWS Direct Connect and AWS Site-to-Site VPN.](https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-connecting-to-aws.png)

**Connecting to AWS**

 The preceding figure shows initial connectivity recommended to customers when first moving workflows. These connections are used for running workflows and data movement. Once you have a secure, robust connection to AWS you can start thinking about what data will be required to run your first workload.
