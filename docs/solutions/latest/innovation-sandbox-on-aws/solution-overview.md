---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/solution-overview.html
---

# Create temporary sandbox environments with configurable security and spend monitoring controls
<a name="solution-overview"></a>

Publication date: *May 2025. For updates, refer to [CHANGELOG.md](https://github.com/aws-solutions/innovation-sandbox-on-aws/blob/main/CHANGELOG.md) file in the GitHub repository.*

The Innovation Sandbox on AWS solution allows cloud administrators to set up and recycle temporary sandbox environments by automating the implementation of security and governance policies, spend management mechanisms, and account recycling preferences through a web user interface (UI). Using the solution, customers can empower their teams to experiment, learn, and innovate with AWS services in production-isolated AWS accounts that are recycled after use.

**Note**
The solution does not create any new, or close existing AWS accounts; it only allows you to manage existing AWS accounts for sandbox experiments, and recycles accounts to promote reuse.

The solution automates the setup of a sandbox Organizational Unit (OU) structure that comes preconfigured with best practices for workload isolation, by automatically deploying a standard set of policies, guardrails, and controls across sandbox accounts. The solution:

1. Enables cost optimization by sending alerts and initiating automated actions when spend reaches budget threshold limits.

1. Enables account recycling by providing the ability to use accounts for a predefined duration or spend threshold, and cleaning up the account at the end of its sandbox use.

1. Limits and controls excessively expensive, or sensitive actions within sandbox accounts.

This implementation guide provides an overview of the Innovation Sandbox on AWS solution, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the solution to the AWS Cloud. It is intended for solution architects, DevOps engineers, AWS account administrators, and cloud professionals who want to implement Innovation Sandbox on AWS in their environment.

Use this navigation table to find answers to these common questions:

| If you want to …​ | Read …​ |
| --- | --- |
| Know the cost for running this solution.<br />The average estimated cost for running this solution in the US East (N. Virginia) Region is **USD $65.25 per month**. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security-1.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know which AWS Regions support this solution. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View the instructions to automatically deploy the infrastructure resources (the "stacks") for this solution. |  [Deploy the solution](deploy-the-solution.md)  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
