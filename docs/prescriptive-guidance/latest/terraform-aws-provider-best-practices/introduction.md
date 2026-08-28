---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/introduction.html
---

# Best practices for using the Terraform AWS Provider
<a name="introduction"></a>

*Michael Begin, Amazon Web Services*

Managing infrastructure as code (IaC) with Terraform on AWS offers important benefits such as improved consistency, security, and agility. However, as your Terraform configuration grows in size and complexity, it becomes critical to follow best practices to avoid pitfalls.

This guide provides recommended best practices for using the [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) from HashiCorp. It walks you through proper versioning, security controls, remote backends, codebase structure, and community providers to optimize Terraform on AWS. Each section dives into more details on the specifics of applying these best practices:
+ [Security](security.md)
+ [Backends](backend.md)
+ [Code base structure and organization](structure.md)
+ [AWS Provider version management](version.md)
+ [Community modules](community.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
