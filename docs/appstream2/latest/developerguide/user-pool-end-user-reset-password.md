---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-end-user-reset-password.html
---

# Resetting a Forgotten Password in Amazon WorkSpaces Applications
<a name="user-pool-end-user-reset-password"></a>

If users forget their password, follow these steps to connect to the login portal link (provided in the welcome email) and choose a new password.

**To choose a new password**

1. Open the WorkSpaces Applications login portal by using the login link provided in the welcome email.

1. Choose **Forgot Password?**.

1. Type the email address that you used to create the user in the user pool, and choose **Next**.

   Your email address is case-sensitive. During login, if your email address doesn't use the same capitalization as the email address specified when your user pool account was created, a "user does not exist" error message displays.

1. Check your email for the password reset request message. If you are having difficulty finding the email, check your spam email folder. Type the verification code from the email in **Verification Code**.
**Note**
The verification code is valid for 24 hours. If a new password is not chosen within this time, request a new verification code.

1. Following the password rules shown, type and confirm your new password. Choose **Reset Password**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
