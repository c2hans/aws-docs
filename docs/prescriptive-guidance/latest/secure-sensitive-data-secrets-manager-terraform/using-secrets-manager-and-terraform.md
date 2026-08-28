---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/using-secrets-manager-and-terraform.html
---

# Using Secrets Manager and Terraform
<a name="using-secrets-manager-and-terraform"></a>

## AWS Secrets Manager
<a name="secrets-manager"></a>

[AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) is a service for securely encrypting, storing, and rotating credentials for databases and other services. It helps you replace hardcoded credentials in your code, including passwords, with an API call to retrieve the secret programmatically. In Secrets Manager, a *secret* consists of credentials information (which is the *secret value*) and its metadata. The secret value can be binary, a single string, or multiple strings. For more information, see [Secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_secret).

Secrets Manager uses 256-bit Advanced Encryption Standard (AES) symmetric data keys to encrypt secret values. For more information, see [Secret encryption and decryption in AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html).

You can access and work with Secrets Manager by using any of the following approaches:
+ Secrets Manager console
+ Command line tools
+ AWS SDKs
+ HTTPS Query API, also called the *Secrets Manager API*
+ AWS Secrets Manager endpoints

## Terraform
<a name="terraform"></a>

[Terraform](https://developer.hashicorp.com/terraform/intro) is an IaC tool from HashiCorp that helps you create and manage cloud and on-premises resources. You can use Terraform to deploy resources and infrastructure in the AWS Cloud.

Terraform stores information about your managed AWS infrastructure and its configurations. This information is called the *state*. By default, the state is stored in a local file named `terraform.tfstate`. This file is in JSON format, and Terraform might store sensitive data in this state file in plain text. This poses a risk to the sensitive data because any user with access to the state file can access the sensitive data.

This guide provides best practices and recommendations to help you protect sensitive data when using Terraform to manage your AWS resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
