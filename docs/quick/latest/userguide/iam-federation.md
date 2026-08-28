---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/iam-federation.html
---

# IAM federation
<a name="iam-federation"></a>

|  |
| --- |
|    Applies to: Enterprise Edition and Standard Edition  |

|  |
| --- |
|    Intended audience:  System administrators  |

**Important**
Amazon Quick recommends that you integrate new Amazon Quick subscriptions with IAM Identity Center for identity management. This IAM identity federation user guide is provided as a reference for existing account configurations. For more information on integrating your Amazon Quick account with IAM Identity Center, see [Configure your Amazon Quick account with IAM Identity Center](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html).

**Note**
IAM identity federation doesn't support syncing identity provider groups with Amazon Quick.

Amazon Quick supports identity federation in both Standard and Enterprise editions. When you use federated users, you can manage users with your enterprise identity provider (IdP) and use AWS Identity and Access Management (IAM) to authenticate users when they sign in to Quick. You can use a third-party identity provider that supports Security Assertion Markup Language 2.0 (SAML 2.0) to provide an onboarding flow for your Amazon Quick users. Such identity providers include Microsoft Active Directory Federation Services, Okta, and Ping One Federation Server. With identity federation, your users get one-click access to their Amazon Quick applications using their existing identity credentials. You also have the security benefit of identity authentication by your identity provider. You can control which users have access to Amazon Quick using your existing identity provider.

**Topics**
+ [Initiating sign-on from the identity provider (IdP)](federated-identities-idp-to-sp.md)
+ [Setting up IdP federation using IAM and Amazon Quick](external-identity-providers-setting-up-saml.md)
+ [Initiating sign-on from Quick](federated-identities-sp-to-idp.md)
+ [Setting up service provider–initiated federation with Quick Enterprise edition](setup-quicksight-to-idp.md)
+ [Configuring email syncing for federated users in Quick](jit-email-syncing.md)
+ [Tutorial: Amazon Quick and IAM identity federation](tutorial-okta-quicksight.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
