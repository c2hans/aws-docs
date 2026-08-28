---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security.html
---

# Security in AWS MCP Server
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS MCP Server, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.

The Agent Toolkit for AWS has different security characteristics depending on how you use it:
+ **AWS MCP Server** — A stateless proxy that executes AWS API calls on your behalf using your IAM credentials. Authentication and authorization for the operations it performs are governed by your IAM identity.
+ **AWS CLI (`aws agent-toolkit`)** — Commands that discover and install AWS-vended agent skills over HTTPS. These commands are unauthenticated and do not send credentials. No customer data is stored.

The topic-specific pages below cover security for both usage paths.

This documentation helps you understand how to apply the shared responsibility model when using AWS MCP Server. The following topics show you how to configure AWS MCP Server to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your AWS MCP Server resources.

**Topics**
+ [Data protection in AWS MCP Server](data-protection.md)
+ [Identity and access management for AWS MCP Server](security-iam.md)
+ [OAuth 2.1 authentication for AWS MCP Server](oauth-authentication.md)
+ [Compliance validation for AWS MCP Server](compliance-validation.md)
+ [Resilience in AWS MCP Server](disaster-recovery-resiliency.md)
+ [Data protection for the AWS CLI](data-protection-service-endpoint.md)
+ [IAM for the AWS CLI](security-iam-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Agent Toolkit for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-toolkit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
