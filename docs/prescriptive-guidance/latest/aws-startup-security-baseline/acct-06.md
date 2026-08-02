---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-06.html
---

# ACCT.06 Enforce a password policy
<a name="acct-06"></a>

Users sign in to the AWS Management Console by providing sign-in credentials. AWS recommends requiring MFA for all users. Require that passwords adhere to a strong password policy to help prevent discovery through brute force or social engineering. For more information about password policy recommendations, see the [Password policy guide](https://www.cisecurity.org/insights/white-papers/cis-password-policy-guide) on the Center for Internet Security (CIS) website.

**Note**
For a benchmark-aligned minimum password length, see [AWS Security Hub control IAM.15](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-15), which references the CIS AWS Foundations Benchmark recommendation.

For IAM users, configure password requirements by creating a custom IAM password policy. For more information, see [Set an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the IAM documentation.

**To create a custom password policy**

1. Open the [IAM console](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Account settings**.

1. In the **Password policy** section, choose **Edit**.

1. Choose **Custom** to use a custom password policy.

1. Select the options that you want to apply to your password policy and choose **Save changes**.

1. Confirm that you want to set a custom password policy by choosing **Set custom**.
