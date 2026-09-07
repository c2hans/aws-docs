---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/workforce-iam-federation.html
---

# IAM federation
<a name="workforce-iam-federation"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

**Note**
If you already have a central user directory for managing users and groups, we recommend that you use IAM Identity Center as your primary workforce access service. If any of the design considerations discussed later in this section prevent you from using IAM Identity Center, use IAM federation instead of creating separate IAM users in AWS.

IAM federation establishes a trust system between two parties for the purpose of authenticating users and sharing the information needed to authorize their access to resources. This system requires an identity provider (IdP) that's connected to your user directory and a service provider (SP) that is managed in IAM. The IdP is responsible for authenticating users and supplying relevant authorization context data to IAM, and IAM controls access to resources in AWS accounts and environments.

IAM federation supports commonly used standards such as SAML 2.0 and OpenID Connect (OIDC). SAML-based federation is supported by many IdPs and enables federated single sign-on access for users to sign in to the AWS Management Console or call an AWS API without having to create IAM users. You can create user identities in AWS by using IAM or connect to your existing IdP (for example, Microsoft Active Directory, Okta, Ping Identity, or Microsoft Entra ID). Alternatively, you can use an IAM OIDC identity provider when you want to establish trust between an OIDC-compatible IdP and your AWS account.

There are two design patterns for IAM federation: multi-account federation or single-account federation.

## Multi-account IAM federation
<a name="workforce-iam-federation-multi"></a>

In this multi-account IAM pattern, you establish a separate SAML-trust relationship between the IdP and all AWS accounts that need to be integrated. The permissions are mapped and provisioned on an individual account basis. This design pattern provides a distributed approach to managing roles and policies, and gives you the flexibility to enable a separate SAML or OIDC IdP for each account and use federated user attributes for access control.

Multi-account IAM federation provides these benefits:
+ Provides central access to all your AWS accounts and lets you manage permissions in a distributed way for each AWS account.
+ Achieves scalability in a multi-account setup.
+ Meets compliance requirements.
+ Lets you manage identities from a central location.

The design is particularly helpful if you want to manage permissions in a distributed manner, separated by AWS accounts. It also helps in scenarios where you do not have repeatable IAM permissions across Active Directory users in their AWS accounts. For example, it supports network administrators who might provide resource access with slight variations across accounts.

SAML providers have to be created separately in each account, so each AWS account requires processes to manage the creation, update, and deletion of IAM roles and their permissions. This means that you can define precise and distinct IAM role permissions for AWS accounts with different levels of sensitivity for the same job function.

The following diagram illustrates the multi-account IAM federation pattern.

![Multi-account IAM federation pattern.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/87d24665-c238-4bcb-adbb-bf567003d972.png)

## Single-account IAM federation (hub-and-spoke model)
<a name="workforce-iam-federation-single"></a>

**Note**
Use this design pattern for the specific scenarios described in this section. For most scenarios, IAM Identity Center-based federation or multi-account IAM federation is the recommended approach. For questions, contact [AWS Support](https://aws.amazon.com/contact-us/).

In the single-account federation pattern, the SAML trust relationship is established between the IdP and a single AWS account (the identity account). The permissions are mapped and provisioned through the centralized identity account. This design pattern provides simplicity and efficiency. The identity provider provides SAML assertions that are mapped to specific IAM roles (and permissions) in the identity account. Federated users can then assume cross-account-roles to access other AWS accounts from the identity account. The following diagram illustrates the single-account IAM federation pattern.

![Single-account IAM federation pattern.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/7c326c0a-b48b-44ff-aadf-e1e3a9b57009.png)

**Use cases: **
+ Companies that have a single AWS account, but sometimes need to create short-lived AWS accounts for isolated sandbox or testing.
+ Educational institutions that maintain their production services in a main account but provide temporary, project-based student accounts.
**Note**
These use cases require strong governance and time-bound recycling processes to ensure that production data doesn't pass into the federated accounts and to remove potential security risks. The auditing process is also difficult in these scenarios.

**Design considerations for choosing between IAM federation and IAM Identity Center:**
+ IAM Identity Center supports connecting accounts to only one directory at a time. If you use multiple directories or want to manage permissions based on user attributes, consider using IAM federation as a design alternative. You should have an IdP that supports the SAML 2.0 protocol, such as Microsoft Active Directory Federation Service (AD FS), Okta, or Microsoft Entra ID. You can establish two-way trust by exchanging IdP and SP metadata, and configuring SAML assertions to map IAM roles to corporate directory groups and users.
+ If you use an IAM OIDC identity provider to establish trust between an OIDC-compatible IdP and your AWS account, consider using IAM federation. When you use the IAM console to create an OIDC identity provider, the console attempts to fetch the thumbprint for you. We recommend that you also obtain the thumbprint for your OIDC IdP manually and verify that the console fetched the correct thumbprint. For more information, see [Create an OIDC identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) in the IAM documentation.
+ Use IAM federation if your corporate directory users don't have repeatable permissions for a job function. For example, different network or database administrators might needs customized IAM role permissions in AWS accounts. To achieve this in IAM Identity Center, you can create separate customer managed policies and reference them in your permission sets. For more information, see the AWS blog post [How to use customer managed policies in AWS IAM Identity Center for advanced use cases](https://aws.amazon.com/blogs/security/how-to-use-customer-managed-policies-in-aws-single-sign-on-for-advanced-use-cases/).
+ If you are using a distributed permissions model, where each account manages their own permissions, or a centralized permissions model through AWS CloudFormation StackSets, consider using IAM federation. If you are using a hybrid model that involves both centralized and distributed permissions, consider using IAM Identity Center. For more information, see [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) in the IAMdocumentation.
+ Services and features such as Amazon Q Developer Professional and AWS CLI version 2 have built-in support for IAM Identity Center. However, some of those capabilities aren't supported with IAM federation.
+ IAM Access Analyzer currently doesn't support the analysis of IAM Identity Center users actions.
