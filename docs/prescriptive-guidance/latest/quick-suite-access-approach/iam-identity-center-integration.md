---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/iam-identity-center-integration.html
---

# Granting Quick access through IAM Identity Center integration
<a name="iam-identity-center-integration"></a>

**Note**
This access approach is available only for the Enterprise edition of Amazon Quick. For more information, see [User management for Enterprise edition](https://docs.aws.amazon.com/quicksuite/latest/userguide/editions.html#edition-user-management-enterprise) in the Quick documentation.

![Architecture diagram of an IAM Identity Center user accessing Quick Suite.](http://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/images/guide-img/ec03a023-a3ad-4a10-93bb-22dcf4ea49a5/images/1cb0a684-be79-4d60-90f6-3c87a7dfd0eb.png)

The following are the characteristics of this architecture and access approach:
+ Users and groups are managed in AWS IAM Identity Center through one of the following identity sources:
  + An [external identity provider](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html)
  + A [Microsoft Active Directory directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-ad.html)
  + An [IAM Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html)
+ Depending on your requirements, you can either use an [organization instance](https://docs.aws.amazon.com/singlesignon/latest/userguide/organization-instances-identity-center.html) or [account instance](https://docs.aws.amazon.com/singlesignon/latest/userguide/account-instances-identity-center.html) of IAM Identity Center. For example, if external users need access to Quick but they are not available or allowed to be provisioned in the organization instance, then you can use an account instance that uses an identity source that supports both internal and external users.
+ You assign Quick admin, author, or reader access to IAM Identity Center groups.
+ Quick access is provisioned based on the mapped IAM Identity Center group memberships.
+ You cannot combine this Quick access approach with other approaches.

## Considerations and use cases
<a name="iam-identity-center-integration-considerations"></a>

It is recommended that you use IAM Identity Center to manage access to Quick. There are two approaches you can use with IAM Identity Center. Quick is an IAM Identity Center enabled application and supports native integration, which is the recommended approach. It is also possible to use SAML 2.0 federation, as described in [Configuring federated user access to Quick through IAM Identity Center](iam-identity-center-federation.md) in this guide, but this approach is not recommended for most use cases.

Native service integration between Quick and IAM Identity Center does not require setting up SAML federation between the two services. Native integration uses IAM Identity Center group memberships to manage access to Quick.

IAM Identity Center user groups are automatically synchronized with Quick. In the Quick console, administrators can map the IAM Identity Center groups to the Quick roles. Groups can be assigned the Admin, Author, Reader, Admin Pro, Author Pro, or Reader Pro roles.

This approach is useful because it does not require you to maintain the federation configuration or any permission sets. However, once this approach is implemented, you cannot switch to a different approach, such as federation, in the future without ending your Quick subscription. You also cannot combine this approach with other approaches.

For other limitations related to the use of Quick native integration with IAM Identity Center, see the [Quick documentation](https://docs.aws.amazon.com/quicksuite/latest/userguide/setting-up-sso.html). For example, the use of the [namespaces feature](https://docs.aws.amazon.com/quicksuite/latest/userguide/namespaces.html) in Quick is not supported if you use IAM Identity Center integration.

## Prerequisites
<a name="iam-identity-center-integration-prerequisites"></a>
+ An active AWS account
+ The following permissions:
  + Administrative access to the AWS account where Quick is subscribed
  + Access to the IAM Identity Center console to assign users to groups

## Configuring IAM Identity Center integration and user access
<a name="iam-identity-center-integration-access"></a>

Note the following when configuring this type of access:

1. Before subscribing to Quick, make sure you have already set up and configured IAM Identity Center. For instructions, see [Enabling AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html) and [Getting started tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html) in the IAM Identity Center documentation.

1. Follow the instructions in [Signing up for a Quick subscription](https://docs.aws.amazon.com/quicksuite/latest/userguide/signing-up.html) in the Quick documentation. Choose **Enterprise**, and then choose **Use IAM Identity Center enabled application**. Depending on which existing IAM Identity Center instances are available in your AWS account, you can select between an organization instance or account instance.

1. To assign Quick roles to IAM Identity Center groups, follow the instructions in [Managing access for IAM Identity Center users](https://docs.aws.amazon.com/quicksuite/latest/userguide/managing-user-access-idc.html) in the Quick documentation.
