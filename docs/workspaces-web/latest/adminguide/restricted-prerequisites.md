---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/restricted-prerequisites.html
---

# Restricted internet browsing prerequisites for Amazon WorkSpaces Secure Browser
<a name="restricted-prerequisites"></a>

Before you get started, make sure that you meet the following prerequisites:
+ You need an already deployed VPC, with public and private subnets spreading over several Availability Zones (AZs). For more information about how to set up your VPC environment, see [Default VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html).
+ You need one single proxy endpoint that is accessible from private subnets, where WorkSpaces Secure Browser sessions live (for example, the network load balancer DNS name). If you want to use your existing proxy, make sure it also has a single endpoint that is accessible from your private subnets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
