---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/terraform-state-file.html
---

# Protecting sensitive data in the Terraform state file
<a name="terraform-state-file"></a>

This section discusses obfuscation of the secrets and pointers to handle the sensitive data in the Terraform state file, called `tfstate`. Typically, this is a plain text file that contains data about Terraform deployments, and it includes any sensitive and non-sensitive data about the deployed infrastructure. Sensitive data is visible in plain text in the Terraform state file. To help protect sensitive data, do the following:
+ When ingesting a secret, choose to immediately rotate the secret. For more information, see [Rotate an AWS Secrets Manager secret immediately](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_now.html) in the Secrets Manager documentation.
+ Store the Terraform state file in the centralized AWS account where you operate Secrets Manager. Store the file in an Amazon Simple Storage Service (Amazon S3) bucket, and configure policies that restrict access to it. For more information, see [Bucket policies and user policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-iam-policies.html) in the Amazon S3 documentation.
+ You can lock the Terraform state in order to help prevent corruption. For more information about locking the state and protecting the state file, see [Amazon S3 backend](https://developer.hashicorp.com/terraform/language/settings/backends/s3) in the Terraform documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
