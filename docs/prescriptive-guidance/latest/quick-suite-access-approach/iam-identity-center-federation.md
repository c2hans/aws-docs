---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/iam-identity-center-federation.html
---

# Configuring federated user access to Quick through IAM Identity Center
<a name="iam-identity-center-federation"></a>

If your enterprise is already using AWS IAM Identity Center, you might want to use this service to authenticate federated users. You can use SAML 2.0 federation or use the built-in service integration between IAM Identity Center. For more information about the built-in service integration, see [IAM Identity Center integration](iam-identity-center-integration.md) in this guide.

When using SAML 2.0 federation with IAM Identity Center, there are two methods to configure federated user access to Quick:
+ [Configuring permissions by using permission sets](#permission-sets) – You can use this approach only if the AWS accounts for IAM Identity Center and Quick are members of same organization in AWS Organizations. A [permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) is a template that defines a collection of one or more AWS Identity and Access Management (IAM) policies. Permission sets can simplify permissions management in your organization.
+ [Configuring permissions by using IAM roles](#iam-roles) – This approach is well suited if the AWS account for Quick is not part of the same organization as IAM Identity Center. In this approach, you create the IAM roles directly in the same account with Quick.

In both of these approaches, users can self-provision their own Quick access. If email synchronization is disabled, users can provide their preferred email address when they sign into Quick. If email synchronization is enabled, Quick uses the email address defined in the enterprise IdP. For more information, see [Quick email synchronization for federated users](email-synchronization-federated-users.md) in this guide.

## Configuring permissions by using permission sets
<a name="permission-sets"></a>

![Architecture diagram of a federated user gaining Quick Suite access through a permission set in IAM Identity Center.](http://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/images/guide-img/ec03a023-a3ad-4a10-93bb-22dcf4ea49a5/images/c33b1a45-3150-4f00-8ca3-ca8cc069cf0f.png)

The following are the characteristics of this architecture and access approach:

1. The AWS accounts for IAM Identity Center and Quick are in the same organization in AWS Organizations.

1. The permission set that you define in IAM Identity Center manages and controls the IAM role.

1. Users log in through IAM Identity Center.

1. The Quick user record is linked to the IAM role managed by IAM Identity Center and the username, such as `AWSReservedSSO_QuickSightReader_7oe58cd620501f23/DiegoRamirez@example.com`.

### Prerequisites
<a name="prerequisites.94d3b4cb-745c-5ac4-8aca-76eb6dd97a87"></a>
+ An active Quick account
+ The following permissions:
  + Administrator access to the AWS account where Quick is subscribed
  + Access to the IAM Identity Center console and permissions to create permissions sets

### Configuring access
<a name="configuring-access.6b06d506-d248-5677-b4ea-b097a6e2555d"></a>

Before subscribing to Quick, make sure that you have already set up and configured IAM Identity Center. For instructions, see [Enabling AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html) and [Getting started tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html) in the IAM Identity Center documentation. After you have configured IAM Identity Center in your organization, create a custom permission set in IAM Identity Center that allows federated users to access Quick. For instructions, see [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the IAM Identity Center documentation. For more information about configuring the policies that you include in the permission set, see [Configuring IAM policies](configuring-iam-policies.md) in this guide.

After you create the permission set, provision it to the target AWS account where Quick is subscribed, and then apply it to the users and groups who require Quick access. For more information about assigning permission sets, see [Assign user access to AWS accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/useraccess.html#assignusers) in the IAM Identity Center documentation.

## Configuring permissions by using IAM roles
<a name="iam-roles"></a>

![Architecture diagram of a federated user gaining Quick Suite access through an IAM role](http://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/images/guide-img/ec03a023-a3ad-4a10-93bb-22dcf4ea49a5/images/b7fe9af9-f62e-486a-94c6-d240989c1025.png)

The following are the characteristics of this architecture and access approach:

1. The AWS accounts for IAM Identity Center and Quick are not in the same organization in AWS Organizations.

1. Users log in through IAM Identity Center or through the external IdP that you configured as an identity source in IAM Identity Center.

1. The IAM role contains a trust policy that allows only federated users from IAM Identity Center to assume the role.

1. The Quick user record is linked to an IAM role and the username in the IdP, such as `QuickSightReader/DiegoRamirez@example.com`.

### Prerequisites
<a name="prerequisites.96555d22-6672-53b9-b088-c5d876d7d4c5"></a>
+ An active Quick account.
+ The following permissions:
  + Administrator access to the AWS account where Quick is subscribed.
  + Access to the IAM Identity Center console and permissions to manage applications.
+ You have set up and configured IAM Identity Center. For instructions, see [Enabling AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html) and [Getting started tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html) in the IAM Identity Center documentation.
+ You have configured IAM Identity Center as a trusted IdP in IAM. For instructions, see [Creating IAM identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create.html) in the IAM documentation.

### Configuring access
<a name="configuring-access.8c9624cb-468d-5096-954e-d3e58d9e6c94"></a>

For instructions, see the [AWS IAM Identity Center Integration Guide for Amazon Quick](https://static.global.sso.amazonaws.com/app-b1262cec5a6d8194/instructions/index.htm). After you have configured IAM Identity Center as a trusted identity provider for the AWS account, create an IAM role that federated users can assume in order to access Quick. For instructions, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the IAM documentation. For more information about configuring the policies for Quick, see [Configuring IAM policies](configuring-iam-policies.md) in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
