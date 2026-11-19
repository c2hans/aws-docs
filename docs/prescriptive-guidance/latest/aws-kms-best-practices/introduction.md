---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/introduction.html
---

# AWS Key Management Service best practices

*Frank Phillis, Ken Beer, Zach Miller, Aviral Nigam, Peter M. O'Donnell, Patrick Palmer, Jeremy Stieglitz, and Dave Walker, Amazon Web Services*

[AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) is a managed service that helps you create and control the cryptographic keys that protect your data. This guide describes how to use AWS KMS and provides recommended practices. It helps you compare configuration options and choose the set that meets your needs.

This guide includes recommendations for how your organization can use AWS KMS to protect sensitive information and implement signing for multiple use cases. It considers current recommendations that use the following dimensions:
+ **Managing keys** – Delegation options for management and key storage choices
+ **Data protection** – Encrypting data within your own applications versus using AWS services that encrypt data on your behalf
+ **Access management** – Using AWS KMS key policies and AWS Identity and Access Management (IAM) policies to implement role-based access control (RBAC) or attribute-based access control (ABAC)
+ **Multi-account and multi-Region architecture** – Recommendations for large-scale deployments
+ **Billing and cost management** – Understanding your cost and usage, and recommendations for ways to reduce costs
+ **Detective controls** – Monitoring the status of your KMS keys, encryption settings, and encrypted data
+ **Incident response** – Correcting misconfigurations that result in noncompliance with your data protection policies

## Targeted business outcomes
<a name="outcomes"></a>

Your data is a critical and sensitive asset for your business. With AWS KMS, you manage the cryptographic keys that protect and verify your data. You control how your data is used, who has access to it, and how it is encrypted. This guide helps developers, system administrators, and security professionals implement recommended encryption practices that help you protect sensitive data that is stored or transmitted through AWS services. By understanding and implementing the recommendations in this guide, you can help promote data confidentiality and integrity across your AWS environment. AWS KMS supports your data protection strategy. Requirements internal to your organization, compliance programs, or validation programs can drive this strategy. For more information about how AWS KMS can help you protect data in your AWS environment, see [Using AWS KMS encryption with AWS services](https://docs.aws.amazon.com/kms/latest/developerguide/service-integration.html) in the AWS KMS documentation.
