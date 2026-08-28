---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/resources.html
---

# Resources
<a name="resources"></a>

## References
<a name="references.9e4ccc7f-fbe8-5a0a-b685-c9f30bfc0d2c"></a>

The following links provide additional reading material for the Terraform AWS Provider and using Terraform for IaC on AWS.
+ [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) (HashiCorp documentation)
+ [Terraform modules for AWS services](https://registry.terraform.io/namespaces/terraform-aws-modules) (Terraform Registry)
+ [The AWS and HashiCorp Partnership](https://www.hashicorp.com/blog/hashicorp-at-aws-re-invent-2020) (HashiCorp blog post)
+ [Dynamic Credentials with the AWS Provider](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/dynamic-provider-credentials/aws-configuration) (HCP Terraform documentation)
+ [DynamoDB State Locking](https://developer.hashicorp.com/terraform/language/settings/backends/s3#dynamodb-state-locking) (Terraform documentation)
+ [Enforce Policy with Sentinel](https://developer.hashicorp.com/terraform/tutorials/policy) (Terraform documentation)

## Tools
<a name="tools.7c5b848b-f0ed-51a7-bcd8-fb4b8bf88f12"></a>

The following tools help improve code quality and automation of Terraform configurations on AWS, as recommended in this best practices guide.

Code quality:
+ [Checkov](https://www.checkov.io/): Scans Terraform code to identify misconfigurations before deployment.
+ [TFLint](https://github.com/terraform-linters/tflint): Identifies possible errors, deprecated syntax, and unused declarations. This linter can also enforce AWS best practices and naming conventions.
+ [terraform-docs](https://github.com/terraform-docs/terraform-docs): Generates documentation from Terraform modules in various output formats.

Automation tools:
+ [HCP Terraform](https://www.terraform.io/cloud): Helps teams version, collaborate, and build Terraform workflows with policy checks and approval gates.
+ [Atlantis:](https://www.runatlantis.io/) An open source Terraform pull request automation tool for validating code changes.
+ [CDK for Terraform](https://developer.hashicorp.com/terraform/cdktf): A framework that lets you use familiar languages such as TypeScript, Python, Java, C\#, and Go instead of HashiCorp Configuration Language (HCL) to define, provision, and test your Terraform infrastructure as code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
