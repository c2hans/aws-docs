---
source_url: https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html
---

# Sign in to the AWS Management Console
<a name="how-to-sign-in"></a>

When you sign in to the AWS Management Console from the main AWS sign-in URL ([https://console.aws.amazon.com/](https://console.aws.amazon.com/)) you must choose your user type, either **Root user** or **IAM user**. If you're not sure what kind of user you are, see [Determine your user type](user-types-list.md).

 The [root user](https://docs.aws.amazon.com/signin/latest/userguide/account-root-user-type.html) has unrestricted account access and is associated with the person who created the AWS account. The root user then creates other types of users, such as IAM users and users in AWS IAM Identity Center, and assigns them access credentials.

An [IAM user](https://docs.aws.amazon.com/signin/latest/userguide/iam-user-type.html) is an identity within your AWS account that has specific custom permissions. When an IAM user signs in, they can use a sign-in URL that includes their AWS account or alias, such as ` https://{{account_alias_or_id}}.signin.aws.amazon.com/console/` instead of the main AWS sign in URL `[https://console.aws.amazon.com/](https://console.aws.amazon.com/)`.

You can sign in to up to 5 different identities simultaneously in a single browser in the AWS Management Console. These can be a combination of root users, IAM users, or federated roles in different accounts or in the same account. For details, see [Signing in to multiple accounts](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/multisession.html) in the *AWS Management Console Getting Started Guide*.

**Topics**
+ [Sign in to the AWS Management Console as the root user](introduction-to-root-user-sign-in-tutorial.md)
+ [Sign in to the AWS Management Console as an IAM user](introduction-to-iam-user-sign-in-tutorial.md)

If you're not sure what kind of user you are, see [Determine your user type](user-types-list.md).

**Tutorials**
+ [Sign in to the AWS Management Console as the root user](introduction-to-root-user-sign-in-tutorial.md)
+ [Sign in to the AWS Management Console as an IAM user](introduction-to-iam-user-sign-in-tutorial.md)
