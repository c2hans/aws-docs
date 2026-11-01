---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/introduction.html
---

# Best practices for using the Terraform AWS Provider
<a name="introduction"></a>

*Michael Begin, Amazon Web Services*

Managing infrastructure as code (IaC) with Terraform on AWS offers important benefits such as improved consistency, security, and agility. As your Terraform configuration grows in size and complexity, following best practices helps you avoid common pitfalls.

This guide is for organizations in situations such as these:
+ A team that started with Terraform in one account now runs it across many accounts and Regions, and needs consistent credentials, state, and guardrails.
+ A platform team publishes shared modules for application teams, and needs those modules to be safe to reuse and easy to upgrade.
+ An organization is preparing for an audit or a regulatory review, and needs to show who changed infrastructure, how changes were reviewed, and that secrets aren't stored in plain text.
+ Teams are upgrading to AWS Provider 6.x or a newer Terraform release, and want to adopt current features without breaking existing deployments.

This guide provides recommended best practices for using the [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) from HashiCorp. It covers security controls, remote backends, code base structure, testing, version management, and community modules. The examples use Terraform 1.11 or later and AWS Provider 6.x. Each section goes into the specifics of applying these best practices:
+ [Security](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/security.html)
+ [Backends](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/backend.html)
+ [Code base structure and organization](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/structure.html)
+ [Testing](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/best-practices-for-testing.html)
+ [AWS Provider version management](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/version.html)
+ [Community modules](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/community.html)
