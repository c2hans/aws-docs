---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/userswithoutpwd.html
---

# Email one-time password to users created with API or CLI

When you create users with the [CreateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateUser.html) API operation or the `create-user` CLI command, the users do not have passwords. You can update the settings in IAM Identity Center to send these users a verification email after their first attempt to sign in, if you’ve specified an email for the user when they were created. After receiving the verification email, the user must set a password to sign in.

 If you don’t enable this setting, you must [generate a one-time password](reset-password-for-user.md) and share it with users that you create using the CreateUser API or `create-user` CLI command.

**To send an email address verification email to users created with the CreateUser API or `create-user` CLI command**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Settings**.

1. On the **Settings** page, choose the **Authentication** tab.

1. In the **Standard authentication** section, choose ** Configure**.

1. In the **Configure standard authentication** dialog box, select the **Send email OTP** check box. Then, choose **Save**. The status updates from **Disabled** to **Enabled**.

**Note**
If you use trusted identity propagation with an IAM identity provider and you turn on this setting, users can sign in to the AWS access portal with an IAM Identity Center credential. If you want your users to sign in only through your IAM identity provider, don't turn on this setting. For more information, see [Trusted identity propagation with an IAM identity provider](simplified-tip-enabling.md#tip-iam-federation).
