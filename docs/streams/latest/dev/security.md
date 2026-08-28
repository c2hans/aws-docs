---
source_url: https://docs.aws.amazon.com/streams/latest/dev/security.html
---

# Security in Amazon Kinesis Data Streams
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Kinesis Data Streams, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your organization’s requirements, and applicable laws and regulations.

This documentation helps you understand how to apply the shared responsibility model when using Kinesis Data Streams. The following topics show you how to configure Kinesis Data Streams to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Kinesis Data Streams resources.

**Topics**
+ [Data protection in Amazon Kinesis Data Streams](server-side-encryption.md)
+ [Controlling access to Amazon Kinesis Data Streams resources using IAM](controlling-access.md)
+ [Compliance validation for Amazon Kinesis Data Streams](compliance-validation.md)
+ [Resilience in Amazon Kinesis Data Streams](disaster-recovery-resiliency.md)
+ [Infrastructure Security in Amazon Kinesis Data Streams](infrastructure-security.md)
+ [Security best practices for Kinesis Data Streams](security-best-practices.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
