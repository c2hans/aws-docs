---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-configure-mfa-types.html
---

# Choose MFA types for user authentication
<a name="how-to-configure-mfa-types"></a>

Use the following procedure to choose the device types your users can authenticate with when prompted for multi-factor authentication (MFA) in the AWS access portal.

**To configure MFA types for your users**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. In the left navigation pane, choose **Settings**.

1. On the **Settings** page, choose the **Authentication** tab.

1. In the **Multi-factor authentication** section, choose **Configure**.

1. On the **Configure multi-factor authentication** page, under **Users can authenticate with these MFA types** choose one of the following MFA types based on your business needs. For more information, see [Available MFA types for IAM Identity Center](mfa-types.md).
   + **Security keys and built-in authenticators**
   + **Authenticator apps**

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
