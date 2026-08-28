---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/introduction.html
---

# Securing sensitive data by using AWS Secrets Manager and HashiCorp Terraform
<a name="introduction"></a>

*Chintamani Aphale, T.V.R.L.Phani Kumar Dadi, Pratap Kumar Nanda, Pradip kumar Pandey, Aarti Rajput, and Mayuri Shinde, Amazon Web Services*

Management of sensitive data, including credentials, secret strings, and passwords, is a recognized pillar of infrastructure management and application development and deployment. To help protect your organization, adopt best practices for managing sensitive data in the cloud. Protection of sensitive data is a prerequisite for security and compliance. [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) can help secure sensitive data in your environment as *secrets*.

This guide reviews best practices for secrets, such as how to get secrets from Secrets Manager and how to use AWS Lambda to automatically rotate secrets for sensitive data. It also provides recommendations for how to manage and govern secrets by using hierarchical names. Finally, it helps you manage use of and access to secrets, such as centralization, Terraform integration, and networking considerations.

HashiCorp Terraform has been broadly adopted as an infrastructure as code (IaC) solution in the industry. However, Terraform shows sensitive data as plain text in its [state](https://developer.hashicorp.com/terraform/language/state) file. This guide contains best practices for using Terraform to manage sensitive data and to create and use Secrets Manager secrets.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for organizations that want to use Terraform as an IaC solution. The best practices in this guide are designed to help database architects, infrastructure teams, and application developers. Familiarity with Terraform is a prerequisite for this guide.

## Objectives
<a name="targeted-business-outcomes"></a>

The following are the business outcomes you can expect to achieve after implementing the recommendations in this guide:
+ Innovate faster  by automating the process of managing of secrets.
+ Improve your organization's security posture in the AWS Cloud.

The following are the technical outcomes you can expect to achieve after implementing the recommendations in this guide:
+ Use Secrets Manager to help prevent exposure of sensitive data in the Terraform state file.
+ Centralize management of secrets and sensitive data in order to improve governance and achieve compliance.
+ Enforce security best practices in your organization's processes for deploying cloud infrastructure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
