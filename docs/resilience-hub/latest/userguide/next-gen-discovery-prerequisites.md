---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-discovery-prerequisites.html
---

# Prerequisites for dependency discovery
<a name="next-gen-discovery-prerequisites"></a>

Before you enable dependency discovery, ensure the following requirements are met:
+ Your service must have compute resources (Amazon Elastic Compute Cloud instances, Amazon Elastic Container Service tasks, Amazon Elastic Kubernetes Service pods, or VPC bound Lambda functions) that make DNS queries through Route 53 resolvers.
+ The compute resources must reside in a VPC configured to use Route 53 DNS resolvers.
+ Next generation Resilience Hub discovers either Amazon Elastic Compute Cloud instances (preferred) or Amazon VPC (fallback). This can be verified by viewing the Service topology in the console.
+ No additional IAM permissions are required beyond the standard invoker role – dependency discovery uses Next generation Resilience Hub's own service credentials to access DNS query data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
