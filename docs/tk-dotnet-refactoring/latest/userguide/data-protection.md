---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/data-protection.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Data protection in AWS Toolkit for .NET Refactoring
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Toolkit for .NET Refactoring. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/).

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Toolkit for .NET Refactoring or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Data collected by Toolkit for .NET Refactoring
<a name="dotnet-data-collected"></a>

If you accept the data collection option in the **Settings** menu of the Toolkit for .NET Refactoring extension, the following application data is collected:

1. Application errors generated when running assessments, porting, or when performing other functions provided by the Toolkit for .NET Refactoring extension.

1. Names and versions of public NuGet packages assessed by the Toolkit for .NET Refactoring extension.

1. Metrics for assessments run by the Toolkit for .NET Refactoring extension on public NuGet packages, such as the number of packages and solutions, and the amount of time taken to create a solution.

You can change your data collection settings at any time in the **Settings** menu of the Toolkit for .NET Refactoring extension.

Toolkit for .NET Refactoring will perform surface level analysis of your .NET Framework solution and generate a list of the following that are in use:
+ NuGet packages
+ NuGet APIs
+ .NET SDK APIs

Only the generated list is stored in the S3 bucket you provide, and your source code never leaves your local system. Toolkit for .NET Refactoring has a scalable backend that processes source code metadata ephemerally. The backend returns compatibility and recommendation information back to you. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).

You can choose whether to encrypt your source code metadata that is uploaded to Amazon S3. Toolkit for .NET Refactoring supports using your own customer managed keys in AWS Key Management Service (AWS KMS) for encryption and decryption. For more information, see [Protecting data with encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) in the *Amazon Simple Storage Service User Guide* and [AWS KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) in the *AWS Key Management Service Developer Guide*.

**Encryption at rest**
All data within Toolkit for .NET Refactoring is encrypted at rest in accordance with industry standards.

**Encryption in transit**
All requests to Toolkit for .NET Refactoring must be made over the Transport Layer Security protocol (TLS). We recommend TLS 1.2 or later.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for NET Refactoring. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tk-dotnet-refactoring` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
