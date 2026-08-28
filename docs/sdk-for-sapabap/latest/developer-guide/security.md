---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/security.html
---

# Security in AWS SDK for SAP ABAP
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS SDK for SAP ABAP, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.

This section covers the following topics.

**Topics**
+ [SAP system authentication on AWS](system-authentication.md)
+ [Best practices for IAM Security](best-practices.md)
+ [SAP authorizations](authorizations.md)
+ [Secure operations](secure-operations.md)
+ [Using Secret Access Key Authentication with SSF Encryption](ssf-authentication.md)
+ [Using certificates with IAM Roles Anywhere](using-iam.md)
+ [Using Source Profile for Cross-Account Access](source-profile.md)
+ [Using SAP Credential Store](credential-store.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
