---
source_url: https://docs.aws.amazon.com/awssupport/latest/user/support-devops-agent-security.html
---

# Security for AWS DevOps Agent activated from AWS Support
<a name="support-devops-agent-security"></a>

AWS DevOps Agent provides the following security controls:
+ Agent spaces are the primary security boundary. Each agent space is isolated to a single AWS account.
+ Data is encrypted at rest with AWS-managed keys and encrypted in transit.
+ Agent activity is captured in an immutable agent journal and in AWS CloudTrail (CloudTrail).
+ AWS DevOps Agent enforces account-boundary, limited-write, and prompt-injection protections.

For the full security posture, including regional processing, integration security, network connectivity, and the shared responsibility model, see [AWS DevOps Agent Security](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security.html) in the *AWS DevOps Agent User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
