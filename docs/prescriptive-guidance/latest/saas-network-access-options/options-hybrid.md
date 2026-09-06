---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/options-hybrid.html
---

# Supporting hybrid environments
<a name="options-hybrid"></a>

It's common for consumers to come from different environments, each with its own technical and security constraints. Some customers may operate entirely from on-premises data centers that require secure connectivity over the Internet or through dedicated network links. Others might already be running workloads within AWS and expect low-latency, private network paths. A third group might rely on other CSPs, where connectivity must bridge different cloud networks.

Regardless, you should aim for standardized network access to your SaaS application to simplify your architecture and reduce operational complexity. Two of the previously presented approaches—[public internet access](options-onprem.md#options-onprem-internet) and [transit VPCs](options-onprem.md#options-onprem-transit-vpc)—work well across these scenarios. Public internet access offers the fastest onboarding path with minimal setup for your customers. Transit VPCs offer more controlled and private access, often using AWS PrivateLink.

When designing your SaaS offering, you can adopt a single network access model or combine multiple approaches into a tiered offering. For example, you might offer a public access deployment tier for customers who prioritize ease of connection and rapid onboarding, and you might offer a private access deployment tier for customers who have strict compliance or security control requirements. These tiers come with different cost, performance and risk profiles. It is also possible to combine both approaches into a single architecture. In that case, make sure that you have strong security measures so that public and private paths remain isolated.

The following diagram shows a hybrid access approach, where consumers have the option to connect privately from their data center or CSP, publicly, or directly through AWS PrivateLink (if they have workloads in the AWS Cloud).

![Hybrid connection for access from on premises, through the internet, or through the AWS Cloud.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/004bd0bb-328f-4e79-9267-37a9a312ab1d.png)
