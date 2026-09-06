---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-03.html
---

# ACCT.03 Configure console access for each user
<a name="acct-03"></a>

AWS recommends using temporary credentials to grant access to AWS accounts and resources. *Temporary credentials* have a limited lifetime, so you do not have to rotate them or explicitly revoke them when they're no longer needed. For more information, see [Temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the IAM documentation.

For human users, AWS recommends using federated identities from a centralized identity provider (IdP), such as AWS IAM Identity Center, Okta, Active Directory, or Ping Identity. Federating users allows you to define identities in a single, central location, and users can securely authenticate to multiple applications and websites, including AWS, by using a single set of credentials. For more information, see [Identity federation in AWS](https://aws.amazon.com/identity/federation/) and [IAM Identity Center](https://aws.amazon.com/single-sign-on/).

**Note**
Identity federation can complicate the transition from a single-account architecture to a multi-account architecture. It is common for startups to delay implementing identity federation until they have established a multi-account architecture managed in AWS Organizations.

**To set up identity federation using IAM Identity Center**

1. See [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the IAM Identity Center documentation.

1. Make sure that your IdP enforces multi-factor authentication (MFA).

1. Apply permissions according to [ACCT.04 Assign permissions](acct-04.md).

If you are using an external or third-party IdP, see [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) in the IAM documentation.

If your startup is not yet ready to configure identity federation, you can create IAM users directly as a starting point. Creating IAM users with long-term credentials is not a security best practice. Long-term credentials do not expire automatically, which increases the risk of credential exposure if they are not rotated regularly. When your startup is ready to transition to a multi-account architecture managed in AWS Organizations, migrating from IAM users to federated identities will require additional planning.

As a baseline, create an IAM user with a username, password, and multi-factor authentication (MFA) for each human operator. Do not share credentials across users, and rotate long-term credentials on a regular schedule.

**To create an IAM user**

1. Follow the steps in [Create an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console) in the IAM documentation.

1. Apply permissions according to [ACCT.04 Assign permissions](acct-04.md).

**Warning**
IAM users have long-term credentials, which presents a security risk. To help mitigate this risk, provide these users with only the permissions they require to perform their tasks and remove these users when they are no longer needed. Avoid creating long-lived access keys for IAM users. Instead, use temporary credentials through `aws login` to access the AWS CLI and SDKs, even when using IAM user credentials. This provides the same secure authentication while eliminating the risks associated with long-lived credentials. For more information about CLI and SDK access methods, see [ACCT.13 Use short-lived credentials for access to your AWS resources](acct-13.md).
