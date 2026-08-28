---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/aws-accounts-for-multi-account-environments.html
---

# AWS accounts for multi-account environments
<a name="aws-accounts-for-multi-account-environments"></a>

To deploy a multi-account environment, we recommend the following AWS account guidelines for each stack:
+  **Hub stack** - Deploy to a member account in your AWS Organization, preferably where you have an existing transit gateway or plan to create a new one, or in a dedicated [network account](concepts-and-definitions.md) where you plan to create a new transit gateway. It can’t be the Organizations management account.
+  **Spoke stack** - Deploy to all the member accounts in your AWS Organization that have a VPC that you plan to attach to the transit gateway hub account. You must deploy it in the hub account if you want to attach VPCs in the hub account.
+  **Organization role stack** - Optionally deploy in the Organizations management account to allow the solution to add Organizational Unit paths in the attachment name to help you identify the VPC location.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
