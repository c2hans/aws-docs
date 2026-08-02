---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/setting-up-sso.html
---

# Using IAM Identity Center
<a name="setting-up-sso"></a>

|  |
| --- |
|    Applies to: Enterprise Edition and Standard Edition  |

|  |
| --- |
|    Intended audience:  System administrators and Amazon Quick administrators  |

Amazon Quick Enterprise edition integrates with your existing directories, using either Microsoft Active Directory or single sign-on (IAM Identity Center) using Security Assertion Markup Language (SAML). You can use AWS Identity and Access Management (IAM) to further enhance your security, or for custom options such as embedding dashboards.

In Quick Standard edition, you can manage users entirely within Quick. If you prefer, you can integrate with your existing users, groups, and roles in IAM.

You can use the following tools for identity and access to Amazon Quick:
+ [IAM Identity Center](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) (Enterprise edition only)
+ [IAM federation](https://docs.aws.amazon.com/quicksuite/latest/userguide/iam-federation.html) (Standard and Enterprise editions)
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) (Enterprise edition only)
+ [SAML-based single sign-on](https://docs.aws.amazon.com/quicksight/latest/user/external-identity-providers.html) (Standard and Enterprise edition)
+ [Multifactor authentication (MFA)](https://docs.aws.amazon.com/quicksight/latest/user/using-multi-factor-authentication-mfa.html) (Standard and Enterprise edition)

**Note**
In the regions listed below, Amazon Quick accounts can only use [IAM Identity Center](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) for identity and access management.
`af-south-1` Africa (Cape Town)
`ap-southeast-3` Asia Pacific (Jakarta)
`ap-southeast-5` Asia Pacific (Malaysia)
`eu-south-1` Europe (Milan)
`eu-south-2` Europe (Spain)
`eu-central-2` Europe (Zurich)
`il-central-1` Israel (Tel Aviv)
`me-central-1` Middle East (UAE)

IAM Identity Center helps you securely create or connect your workforce identities and manage their access across AWS accounts and applications.

Before you integrate your Amazon Quick account with IAM Identity Center, set up IAM Identity Center in your AWS account. If you haven't set up IAM Identity Center in your AWS organization, see [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the *AWS IAM Identity Center User Guide*.

If you want to configure an external identity provider with IAM Identity Center, see [Supported identity providers](https://docs.aws.amazon.com/singlesignon/latest/userguide/supported-idps.html) to view a list of supported identity providers' configuration steps.

**Topics**
+ [Configure your Amazon Quick account with IAM Identity Center](#sec-identity-management-identity-center)

## Configure your Amazon Quick account with IAM Identity Center
<a name="sec-identity-management-identity-center"></a>

|  |
| --- |
|  Applies to:  Enterprise Edition  |

|  |
| --- |
|    Intended audience:  System administrators  |

IAM Identity Center helps you securely create or configure your existing workforce identities and manage their access across AWS accounts and applications. IAM Identity Center is the recommended approach for workforce authentication and authorization on AWS for organizations of any size and type. To learn more about IAM Identity Center, see [AWS IAM Identity Center](https://aws.amazon.com//iam/identity-center/).

Configure Amazon Quick and IAM Identity Center so that you can sign up for a new Amazon Quick account with an IAM Identity Center configured identity source. With IAM Identity Center, you can configure your external identity provider as an identity source. You can also use IAM Identity Center as an identity store if you don't want to use a third-party identity provider with Amazon Quick. Identity methods can't be changed after your account is created.

When you integrate your Amazon Quick account with IAM Identity Center, Amazon Quick account administrators can create a new Amazon Quick account that automatically has the identity provider's groups available. This simplifies asset sharing at scale in Amazon Quick.

Access to some sections of the Amazon Quick administration console is restricted by IAM permissions. The following table summarizes the admin actions that you can perform in Amazon Quick based on the access type that you choose.

To learn more how to sign up for an Amazon Quick account with IAM Identity Center, see [Signing up for an Amazon Quick subscription](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html).

The following table lists admin actions and whether they require IAM permissions.

| Admin action | IAM permissions required |
| --- | --- |
| **Account settings** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Manage assets** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Amazon Q** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Manage subscriptions** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No |
| **SPICE capacity** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No |
| **Index capacity** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Manage users (view)** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No |
| **Manage users > Role groups** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Manage domains** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No |
| **Mobile settings** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No |
| **Manage IP/VPC restrictions** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Manage VPC connections** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Manage OAuth client applications** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **KMS keys** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **AWS resources** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Default access policy** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **IAM policy assignments** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **AWS actions** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Extension access** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Custom permissions** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Configure SageMaker** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Brand customization** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Agent customization** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Email customization** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |
| **Quick Usage Metrics** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes |

If you have the Amazon Quick admin role, you can perform actions that do not require IAM permissions. To perform actions that require IAM permissions, sign in to the AWS Management Console as an IAM principal with the appropriate `quicksight:*` permissions. You can also perform some admin actions programmatically through the Amazon Quick API. For a list of available API operations, see the [Amazon Quick API Reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).

### Considerations
<a name="idc-considerations"></a>

**Irreversible actions**
The following actions permanently prevent all users from signing in to your Amazon Quick account. You cannot undo these actions.
+ Disabling or deleting the Amazon Quick application in the IAM Identity Center console. If you want to delete your Amazon Quick account, see [Closing your Amazon Quick account](https://docs.aws.amazon.com/quicksight/latest/user/closing-account.html).
+ Migrating the Amazon Quick account that contains your IAM Identity Center configuration to an AWS Organization that does not contain the IAM Identity Center instance that your Amazon Quick account is configured to.
+ Deleting the IAM Identity Center instance that is configured to your Amazon Quick account.
+ Editing IAM Identity Center application attributes, for example the **requires assignment** attribute.
