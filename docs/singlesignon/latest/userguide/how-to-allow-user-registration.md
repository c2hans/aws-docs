---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-allow-user-registration.html
---

# Allow users to register their own MFA devices
<a name="how-to-allow-user-registration"></a>

IAM Identity Center administrators can allow users to self-register their own MFA devices.

**To allow users to register their own MFA devices**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. In the left navigation pane, choose **Settings**.

1. On the **Settings** page, choose the **Authentication** tab.

1. In the **Multi-factor authentication** section, choose **Configure**.

1. On the **Configure multi-factor authentication** page, under **Who can manage MFA devices**, choose **Users can add and manage their own MFA devices**.

1. Choose **Save changes**.

**Note**
After you set up self-registration for your users, you might want to send them a link to the procedure [Registering your device for MFA](user-device-registration.md). This topic provides instructions on how to set up their own MFA devices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
