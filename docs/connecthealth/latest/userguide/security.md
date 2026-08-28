---
source_url: https://docs.aws.amazon.com/connecthealth/latest/userguide/security.html
---

# Security in Amazon Connect Health
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud:
+  **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](http://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Amazon Connect Health, see [AWS Services in Scope by Compliance Program](http://aws.amazon.com/compliance/services-in-scope/).
+  **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.

This documentation helps you understand how to apply the shared responsibility model when using Amazon Connect Health. The following topics show you how to configure Amazon Connect Health to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Amazon Connect Health resources.

**Topics**
+ [Security topics](#security-topics)
+ [Data protection in Amazon Connect Health](data-protection.md)
+ [Identity and access management for Amazon Connect Health](security-iam.md)
+ [Compliance validation for Amazon Connect Health](compliance-validation.md)
+ [Resilience in Amazon Connect Health](disaster-recovery-resiliency.md)
+ [Infrastructure security in Amazon Connect Health](infrastructure-security.md)

## Security topics
<a name="security-topics"></a>
+  [Data protection in Amazon Connect Health](data-protection.md) – Learn about encryption, zero-persistence architecture, and PHI handling.
+  [Identity and access management for Amazon Connect Health](security-iam.md) – Learn about IAM policies, service roles, and fine-grained permissions.
+  [Logging and monitoring in Amazon Connect Health](logging-using-cloudtrail.md) – Learn about logging Amazon Connect Health API calls with AWS CloudTrail. For more information, see [Monitoring Amazon Connect Health](monitoring-overview.md).
+  [Compliance validation for Amazon Connect Health](compliance-validation.md) – Learn about HIPAA eligibility and cross-region inference disclosure.
+  [Resilience in Amazon Connect Health](disaster-recovery-resiliency.md) – Learn about resilience and Availability Zone support.
+  [Infrastructure security in Amazon Connect Health](infrastructure-security.md) – Learn about network isolation and infrastructure protection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
