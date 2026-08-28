---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/aft-data-protection.html
---

# Data protection
<a name="aft-data-protection"></a>

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AFT. For data protection purposes, we recommend the following best practices for security.
+ Follow the Data Protection guidelines provided by AWS Control Tower. For details, see [Data Protection in AWS Control Tower](controltower-console-encryption.md).
+ Preserve Terraform state configuration generated at the time of AFT deployment. For details, see [Deploy AWS Control Tower Account Factory for Terraform (AFT)](aft-getting-started.md).
+ Rotate sensitive credentials periodically as directed by your organization’s security policy. Examples of secrets are Terraform tokens, `git` tokens, and so forth.

 **Encryption at rest**

AFT creates Amazon S3 buckets, Amazon SNS topics, Amazon SQS queues, and Amazon DynamoDB databases that are encrypted at rest with AWS Key Management Service keys. KMS keys created by AFT have yearly rotation enabled by default. If you choose the HCP Terraform or Terraform Enterprise distributions of Terraform, AFT includes a AWS Systems Manager SecureString parameter to store Terraform token values that are sensitive.

AFT uses AWS services described in [Component services](aft-components.md) that are, by default, encrypted at rest. For details, see the AWS documentation for each component AWS service of AFT, and learn about the data protection practices followed by each service.

 **Encryption in transit**

AFT relies upon AWS services described in [Component services](aft-components.md) that employ encryption in transit, by default. For details, see the AWS documentation for each component AWS service of AFT, and learn about the data protection practices followed by each service.

 For HCP Terraform or Terraform Enterprise distributions, AFT calls an HTTPS endpoint API for access to your Terraform organization. If you choose a third-party VCS provider supported by AWS CodeStar connections, AFT calls an HTTPS endpoint API for access to your VCS provider organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
