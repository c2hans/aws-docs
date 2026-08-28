---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/governance-network.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Governance & Network
<a name="governance-network"></a>

 Whereas a typical OSS application stack comprises of multi-vendor implementation, often with duplicated and overlapping tooling across different network domains, an OSS architecture on AWS simplifies:
+  The management and governance of OSS applications with services such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM), and [AWS Systems Manager](https://aws.amazon.com/systems-manager/).
+  Network and interconnecting of OSS, and IT and network workloads with services such as [AWS Direct Connect](https://aws.amazon.com/directconnect/) (Direct Connect), [AWS Transit Gateway](https://aws.amazon.com/transit-gateway) and [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing).

 Many of these shared capabilities can be deployed as part of a secure, multi-account [AWS Landing Zone](https://aws.amazon.com/solutions/implementations/aws-landing-zone/) that is part of the same [AWS Organization](https://aws.amazon.com/organizations) (for example, a shared security account or shared networking account). The creation, management, and governance of these landing zones is simplified and automated by leveraging [AWS Control Tower](https://aws.amazon.com/controltower). These services help you reduce the complexity inherent to managing a complex network comprised of multiple technology domains, NFx, and Independent Software Vendors (ISVs).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
