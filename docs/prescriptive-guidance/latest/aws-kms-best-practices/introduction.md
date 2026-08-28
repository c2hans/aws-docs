---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/introduction.html
---

# AWS Key Management Service best practices
<a name="introduction"></a>

*Frank Phillis, Ken Beer, Zach Miller, Peter M. O'Donnell, Patrick Palmer, Jeremy Stieglitz, and Dave Walker, Amazon Web Services*

[AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) is a managed service that makes it easy for you to create and control the cryptographic keys that are used to protect your data. This guide describes how to effectively use AWS KMS and provides best practices. It helps you compare configuration options and choose the best set for your needs.

This guide includes recommendations for how your organization can use AWS KMS to protect sensitive information and implement signing for multiple use cases. It considers current recommendations that use the following dimensions:
+ **Managing keys** – Delegation options for management and key storage choices
+ **Data protection** – Encrypting data within your own applications vs in AWS services doing it on your behalf
+ **Access management** – Using AWS KMS key policies and AWS Identity and Access Management (IAM) policies to implement role-based access control (RBAC) or attribute-based access control (ABAC).
+ **Multi-account and multi-Region architecture** – Recommendations for large scale deployments.
+ **Billing and cost management** – Understanding your cost and usage, and recommendations for ways to reduce costs.
+ **Detective controls** – Monitoring the status of your KMS keys, encryption settings, and encrypted data.
+ **Incident response** – Correcting misconfigurations that result in non-compliance with your data protection policies.

## Targeted business outcomes
<a name="outcomes"></a>

Your data is a critical and sensitive asset for your business. With AWS KMS, you manage the cryptographic keys that are used to protect and verify your data. You control how your data is used, who has access to it, and how it is encrypted. This guide is intended to help developers, system administrators, and security professionals implement encryption best practices that help you secure sensitive data that is stored or transmitted through AWS services. By understanding and implementing the recommendations in this guide, you can promote data confidentiality and integrity across your AWS environment. You can meet your data protection requirements, whether those requirements are formulated internally, or you have requirements specific to a compliance or validation program. For more information about how AWS KMS can help you secure data in your AWS environment, see [Using AWS KMS encryption with AWS services](https://docs.aws.amazon.com/kms/latest/developerguide/service-integration.html) in the AWS KMS documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
