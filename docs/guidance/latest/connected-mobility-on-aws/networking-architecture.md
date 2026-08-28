---
source_url: https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/networking-architecture.html
---

# Networking architecture
<a name="networking-architecture"></a>

The solution uses a single Amazon VPC with the following configuration:
+  **Public Subnets** – Host NAT Gateway for outbound internet access
+  **Private Subnets** – Host MSK cluster and ElastiCache for security
+  **Security Groups** – Restrict traffic between components following least-privilege principles
+  **VPC Endpoints** – Enable private connectivity to AWS services where applicable

The networking architecture supports both public internet access and private network configurations through VPC peering or AWS Transit Gateway.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Connected Mobility on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
