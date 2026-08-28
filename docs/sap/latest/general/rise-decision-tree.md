---
source_url: https://docs.aws.amazon.com/sap/latest/general/rise-decision-tree.html
---

# Decision tree on connectivity to RISE
<a name="rise-decision-tree"></a>

You must establish required connectivity to proceed with RISE with SAP on AWS. The following are a few connectivity patterns described in the preceding sections:
+ direct to RISE VPC, supported with Site-to-Site VPN (up to 1.25 Gbps per tunnel)
+ connectivity through Customer’s own account or Landing Zone, supported with Site-to-Site VPN large bandwidth option (up to 5 Gbps)
+ connectivity through Customer’s own account or Landing Zone, supported with Site-to-Site VPN large bandwidth option and ECMP (above 5 Gbps)
+ direct to RISE VPC, supported with Direct Connect
+ direct to RISE VPC, supported with VPN over Direct Connect (for in-built traffic encryption)
+ connectivity through your AWS account via VPC Peering
+ connectivity through Transit Gateway from your owned AWS account in the same Region
+ connectivity through SAP-managed Transit Gateway in RISE to connect to your TGW in another Region
+ connectivity through AWS Cloud WAN from your owned AWS account for global multi-region deployments

You must also consider if you want to connect:
+ directly to an AWS Region where the RISE with SAP VPC is going to be deployed
+ or through AWS Local Zone (nearest AWS Direct Connect POP) to benefit from lower setup and running costs, with the same or lower network latency to connect to your RISE with SAP VPC

The decision tree displayed in the following diagram helps you decide which connectivity is suitable based on your requirements, such as future plan of additional AWS or RISE accounts, dedicated private connectivity (security, performance), bandwidth needs, and global multi-region deployments.

![Decision tree for choosing RISE with SAP connectivity options based on bandwidth](http://docs.aws.amazon.com/sap/latest/general/images/rise-decision-tree.png)

**Note**
ECMP requires Transit Gateway for S2S VPN.
Direct Connect Gateway is recommended to connect to multiple AWS regions. This simplifies the connectivity setup and avoids TGW peering between AWS regions.
 AWS Cloud WAN is recommended for customers planning global multi-region deployments from their owned AWS account to connect to RISE VPC.
Landing Zone implementation is recommended when connecting through your owned AWS account with multiple VPCs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
