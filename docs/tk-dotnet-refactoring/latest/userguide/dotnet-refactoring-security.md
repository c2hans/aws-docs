---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/dotnet-refactoring-security.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Security in AWS Toolkit for .NET Refactoring
<a name="dotnet-refactoring-security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Toolkit for .NET Refactoring, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.

This documentation helps you understand how to apply the shared responsibility model when using Toolkit for .NET Refactoring. The following topics show you how to configure Toolkit for .NET Refactoring to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Toolkit for .NET Refactoring resources.

**Topics**
+ [AWS Identity and Access Management (IAM)](dotnet-refactoring-iam.md)
+ [EULA](eula.md)
+ [Data protection in AWS Toolkit for .NET Refactoring](data-protection.md)
+ [AWS managed policies for AWS Toolkit for .NET Refactoring](security-iam-awsmanpol.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for NET Refactoring. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tk-dotnet-refactoring` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
