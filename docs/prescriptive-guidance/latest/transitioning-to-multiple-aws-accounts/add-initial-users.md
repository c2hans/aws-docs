---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/add-initial-users.html
---

# Add initial users
<a name="add-initial-users"></a>

There are two ways to grant people access to AWS accounts:
+ IAM identities, such as users, groups, and roles
+ Identity federation, such as by using AWS IAM Identity Center

In smaller companies and single-account environments, it is common for administrators to create an IAM user when a new person joins the company. The access key and secret key credentials associated to an IAM user are known as *long-term credentials* because they don't expire. However, this isn't a recommended security best practice because if an attacker compromised those credentials, you would have to generate a new set of credentials for the user. Another approach for accessing AWS accounts is through [IAM roles](https://aws.amazon.com/blogs/startups/how-setting-up-iam-users-and-iam-roles-can-help-keep-your-startup-secure/). You can also use AWS Security Token Service (AWS STS) to temporarily request *short-term credentials*, which expire after a configurable amount of time.

You can manage people access into your AWS accounts through [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). You can create individual user accounts for each of your employees or contractors, they can manage their own passwords and multi-factor authentication (MFA) solutions, and you can group them to manage access. When configuring MFA, you can use software tokens, such as authenticator applications, or you can use hardware tokens, such as YubiKey devices.

IAM Identity Center also supports federation from external identity providers (IdPs) such as Okta, JumpCloud, and Ping Identity. For more information, see [Supported identity providers](https://docs.aws.amazon.com/singlesignon/latest/userguide/supported-idps.html) (IAM Identity Center documentation). By federating with an external IdP, you can manage user authentication across applications and then use IAM Identity Center to authorize access to specific AWS accounts.

## Best practices
<a name="users-best-practices"></a>
+ Adhere to the [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) (IAM documentation) for configuring user access.
+ Manage account access by groups instead of by individual users. In IAM Identity Center, create new groups that represent each of your business functions. For example, you might create groups for engineering, finance, sales, and product management.
+ Often, groups are defined by separating those who need access to all AWS accounts (often read-only access) and those who need access to a single AWS account. We recommend that you use the following naming convention for groups so that it is easy to identify the AWS account and permissions associated with the group.

  `<prefix>-<account name>-<permission set>`

  For example, for the group `AWS-A-dev-nonprod-DeveloperAccess`, `AWS-A` is a prefix that indicates access to a single account, `dev-nonprod` is the name of the account, and `DeveloperAccess` is the permission set assigned to the group. For the group `AWS-O-BillingAccess`, the `AWS-O` prefix indicates access to the entire organization, and `BillingAccess` indicates the permission set for the group. In this example, because the group has access to the entire organization, an account name isn't represented in the group name.
+ If you are using IAM Identity Center with an external SAML-based IdP and want to require MFA, you can use attribute-based access control (ABAC) to pass the authentication method from the IdP to IAM Identity Center. The attributes are sent through the SAML assertions. For more information, see [Enable and configure attributes for access control](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-abac.html) (IAM Identity Center documentation).

  Many IdPs, such as Microsoft Azure Active Directory and Okta, can use the Authentication Method Reference (`amr`) claim inside a SAML assertion to pass the user's MFA status to IAM Identity Center. The claim used to assert MFA status and its format varies by IdP. For more information, see the documentation for your IdP.

  In IAM Identity Center, you can then create permission set policies that determine who can access your AWS resources. When you enable ABAC and specify attributes, IAM Identity Center passes the attribute value of the authenticated user to IAM for use in policy evaluation. For more information, see [Create permission policies for ABAC](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-abac-policies.html) (IAM Identity Center documentation). As shown in the following example, you use the `aws:PrincipalTag` condition key to create an access control rule for MFA.

  ```
  "Condition": {
    "StringLike": { "aws:PrincipalTag/amr": "mfa" }
  }
  ```
