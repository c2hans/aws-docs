---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/security.html
---

# Security in AWS CodeBuild
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS CodeBuild, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company's requirements, and applicable laws and regulations.

This documentation helps you understand how to apply the shared responsibility model when using CodeBuild. The following topics show you how to configure CodeBuild to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your CodeBuild resources.

**Topics**
+ [Data protection in AWS CodeBuild](data-protection.md)
+ [Identity and access management in AWS CodeBuild](auth-and-access-control.md)
+ [Compliance validation for AWS CodeBuild](compliance-validation.md)
+ [Resilience in AWS CodeBuild](codebuild-disaster-recovery-resiliency.md)
+ [Infrastructure Security in AWS CodeBuild](infrastructure-security.md)
+ [Access your source provider in CodeBuild](access-tokens.md)
+ [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
