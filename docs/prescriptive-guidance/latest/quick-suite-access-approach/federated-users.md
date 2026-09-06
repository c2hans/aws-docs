---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/federated-users.html
---

# Granting Quick access to federated users
<a name="federated-users"></a>

When you use federated identities, you can manage users with an external identity provider (IdP) to authenticate users when they sign in to Amazon Quick. Quick supports identity federation with SAML 2.0. Many external IdPs, such as Okta and Ping, use this standard. You can also use AWS IAM Identity Center as your external IdP for a SAML 2.0 federation approach to Quick access. However, we recommend the built-in service integration discussed in [IAM Identity Center integration](iam-identity-center-integration.md) in this guide instead of the federated user approach. If you use IAM Identity Center, the federated user approach is only recommended if you cannot use IAM Identity Center integration due to current feature limitations.

Federated users have a single sign-on (SSO) experience, and you can grant access to Quick without creating an AWS Identity and Access Management (IAM) user or Quick local user for each person in your organization. In addition, federation provides users with temporary credentials, which is a [security best practice](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp). For more information about identity federation and its benefits and use cases, see [Identity federation in AWS](https://aws.amazon.com/identity/federation/).

When configuring access to Quick for federated users, you can use one of the following approaches:
+ [Configuring federated user access to Quick through IAM and an external IdP](external-idp.md)
+ [Configuring federated user access to Quick through IAM Identity Center](iam-identity-center-federation.md)

Both of these approaches allow federated users to self-provision access to Quick. The approaches vary based on the architecture and services used for federation. However, in both solutions, the federated user then assumes an IAM role that determines which permissions they have in Quick.

When you use Quick Enterprise edition, you can force users who are self-provisioning their access to sign in to Quick by using the email address defined in the identity provider. For more information, see [Quick email synchronization for federated users](email-synchronization-federated-users.md).
