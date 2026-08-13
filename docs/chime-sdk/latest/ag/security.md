---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/security.html
---

# Security in Amazon Chime SDK
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to the Amazon Chime SDK, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.

This documentation helps you understand how to apply the shared responsibility model when using the Amazon Chime SDK. The following topics show you how to configure the Amazon Chime SDK to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Amazon Chime SDK resources.

**Topics**
+ [Identity and access management for the Amazon Chime SDK](security-iam.md)
+ [How the Amazon Chime SDK works with IAM](security_iam_service-with-iam.md)
+ [Using encryption with voice analytics](analytics-encryption.md)
+ [Cross-service confused deputy prevention](confused-deputy.md)
+ [Amazon Chime SDK resource-based policies](#security_iam_service-with-iam-resource-based-policies)
+ [Authorization based on Amazon Chime SDK tags](#security_iam_service-with-iam-tags)
+ [Amazon Chime SDK IAM roles](#security_iam_service-with-iam-roles)
+ [Amazon Chime SDK identity-based policy examples](security_iam_id-based-policy-examples.md)
+ [Troubleshooting Amazon Chime SDK identity and access](security_iam_troubleshoot.md)
+ [Using service-linked roles for Amazon Chime SDK](using-service-linked-roles.md)
+ [Logging and monitoring in the Amazon Chime SDK](monitoring-overview.md)
+ [Compliance validation for the Amazon Chime SDK](compliance.md)
+ [Resilience in the Amazon Chime SDK](disaster-recovery-resiliency.md)
+ [Infrastructure security in the Amazon Chime SDK](infrastructure-security.md)

## Amazon Chime SDK resource-based policies
<a name="security_iam_service-with-iam-resource-based-policies"></a>

The Amazon Chime SDK supports resource-based policies for the following [resource types](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonchime.html#amazonchime-resources-for-iam-policies).

## Authorization based on Amazon Chime SDK tags
<a name="security_iam_service-with-iam-tags"></a>

The Amazon Chime SDK supports tagging for these [resource types](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonchime.html#amazonchime-resources-for-iam-policies).

## Amazon Chime SDK IAM roles
<a name="security_iam_service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions.

### Using temporary credentials with the Amazon Chime SDK
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html).

The Amazon Chime SDK supports using temporary credentials.

### Service-linked roles
<a name="security_iam_service-with-iam-roles-service-linked"></a>

[Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) allow AWS services to access resources in other services that complete actions on your behalf. Service-linked roles appear in your IAM account, and the services own the roles. An IAM administrator can view but not edit the permissions for service-linked roles.

The Amazon Chime SDK supports service-linked roles. For details about creating or managing those roles, see [Using service-linked roles for Amazon Chime SDK](using-service-linked-roles.md).

### Service roles
<a name="security_iam_service-with-iam-roles-service"></a>

This feature allows a service to assume a [service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-role) on your behalf. This role allows the service to access resources in other services to complete an action on your behalf. Service roles appear in your IAM account and are owned by the account. This means that an IAM administrator can change the permissions for this role. However, doing so might break the functionality of the service.

The Amazon Chime SDK does not support service roles.
