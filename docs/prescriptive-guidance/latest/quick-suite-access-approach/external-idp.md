---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/external-idp.html
---

# Configuring federated user access to Quick through IAM and an external IdP
<a name="external-idp"></a>

![Architecture diagram of a federated user from an external IdP accessing Quick Suite through an IAM role.](https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/images/guide-img/ec03a023-a3ad-4a10-93bb-22dcf4ea49a5/images/6625c4f2-1107-426a-8688-6d06ea70c908.png)

The following are the characteristics of this architecture:
+ The Amazon Quick user record is linked to an AWS Identity and Access Management (IAM) role and the username in the IdP, such as `QuickSightReader/DiegoRamirez@example.com`.
+ Users can self-provision access.
+ Users log in to their external identity provider.
+ If email synchronization is disabled, users can provide their preferred email address when they sign into Quick. If email synchronization is enabled, Quick uses the email address defined in the enterprise IdP. For more information, see [Quick email synchronization for federated users](email-synchronization-federated-users.md) in this guide.
+ The IAM role contains a trust policy that allows only federated users from your external IdP to assume the role.

## Considerations and use cases
<a name="external-idp-considerations"></a>

If you already use identity federation to access your AWS accounts, you can use this existing configuration to also extend access to Quick. For Quick access, you can reuse the same processes that you have in place for provisioning and reviewing access to AWS accounts.

## Prerequisites
<a name="external-idp-prereqs"></a>
+ Administrative permissions in Quick.
+ Your organization is already using an external identity provider, such as Okta or Ping.

## Configuring access
<a name="external-idp-configuration"></a>

For instructions, see [Setting up IdP federation using IAM and Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/external-identity-providers-setting-up-saml.html) in the Quick documentation. For more information about configuring the permissions policy for Quick, see [Configuring IAM policies](configuring-iam-policies.md) in this guide.
