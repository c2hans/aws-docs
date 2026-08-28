---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/mfa-configure.html
---

# Configure MFA in IAM Identity Center
<a name="mfa-configure"></a>

You can configure Multi-factor authentication (MFA) capabilities in IAM Identity Center when your identity source is configured with IAM Identity Center’s identity store, AWS Managed Microsoft AD, or AD Connector. MFA in IAM Identity Center is currently not supported for [external identity providers](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html).

The following are general MFA recommendations, depending on your IAM Identity Center settings and organizational preferences.
+ Users are encouraged to register multiple backup authenticators for all enabled MFA types. This practice can prevent loss of access in case of a broken or misplaced MFA device.
+ Don't choose the **Require Them to Provide a One-Time Password Sent by Email** option if your users must sign in to the AWS access portal to access their email. For example, your users might use Microsoft 365 in the AWS access portal to read their email. In this case, users will not be able to retrieve the verification code and would be unable to sign in to the AWS access portal. For more information, see [Configure MFA device enforcement](how-to-configure-mfa-device-enforcement.md).
+ If you are already using RADIUS MFA that you configured with Directory Service, you do not need to enable MFA within IAM Identity Center. MFA in IAM Identity Center is an alternative to RADIUS MFA for Microsoft Active Directory users of IAM Identity Center. For more information, see [RADIUS MFA](mfa-types.md#about-radius).
+ The following YouTube video provides an overview of MFA and IAM Identity Center:

[![AWS Videos](http://img.youtube.com/vi/1iFvT8shnng?si=hpMeBAd85ypC3BTR/0.jpg)](http://www.youtube.com/watch?v=1iFvT8shnng?si=hpMeBAd85ypC3BTR)

**Topics**
+ [Prompt users for MFA](mfa-getting-started.md)
+ [Choose MFA types for user authentication](how-to-configure-mfa-types.md)
+ [Configure MFA device enforcement](how-to-configure-mfa-device-enforcement.md)
+ [Allow users to register their own MFA devices](how-to-allow-user-registration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
