---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/resources.html
---

# Resources
<a name="resources"></a>

## References
<a name="references.cdbf27af-1fae-5c4c-9359-7e467975f06c"></a>

The following links provide additional reading material for the Terraform AWS Provider and using Terraform for IaC on AWS.
+ [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) (HashiCorp documentation)
+ [AWS Provider version 6 upgrade guide](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/version-6-upgrade) (HashiCorp documentation)
+ [Terraform modules for AWS services](https://registry.terraform.io/namespaces/terraform-aws-modules) (Terraform Registry)
+ [Dynamic credentials with the AWS Provider](https://developer.hashicorp.com/terraform/cloud-docs/dynamic-provider-credentials/aws-configuration) (HCP Terraform documentation)
+ [S3 backend](https://developer.hashicorp.com/terraform/language/backend/s3) (Terraform documentation)
+ [Policy enforcement](https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement) (HCP Terraform documentation)
+ [Getting started with Terraform: Guidance for AWS CDK and AWS CloudFormation experts](https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/introduction.html) (AWS Prescriptive Guidance)
+ [Securing sensitive data by using AWS Secrets Manager and HashiCorp Terraform](https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/introduction.html) (AWS Prescriptive Guidance)
+ [Working around Terraform data source limitations on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-data-limitations/introduction.html) (AWS Prescriptive Guidance)

## Tools
<a name="tools.98bcf4dc-8484-5f3a-8505-bbd3366a8082"></a>

The following tools help improve code quality and automation of Terraform configurations on AWS, as recommended in this best practices guide.

Code quality:
+ [Checkov](https://www.checkov.io/): Scans Terraform code to identify misconfigurations before deployment.
+ [Trivy](https://trivy.dev/docs/latest/scanner/misconfiguration/): Scans Terraform code for misconfigurations with `trivy config`.
+ [TFLint](https://github.com/terraform-linters/tflint): Identifies possible errors, deprecated syntax, and unused declarations. This linter can also enforce AWS best practices and naming conventions.
+ [terraform-docs](https://github.com/terraform-docs/terraform-docs): Generates documentation from Terraform modules in various output formats.

Automation tools:
+ [HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs): Helps teams version, collaborate, and build Terraform workflows with policy checks and approval gates.
+ [Atlantis](https://www.runatlantis.io/): An open-source Terraform pull request automation tool for validating code changes.
