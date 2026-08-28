---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin-email.html
---

# Re-Sending Welcome Email in Amazon WorkSpaces Applications
<a name="user-pool-admin-email"></a>

You can re-send the welcome email with connection instructions to users in the user pool. Unused passwords expire after seven days. To provide a new temporary password, you must re-send the welcome email. This option is only available until users set their permanent password. If they've already set their password and forgotten it, they can set a new one. For more information, see [Resetting a Forgotten Password in Amazon WorkSpaces Applications](user-pool-end-user-reset-password.md).

**To resend the welcome email for a user**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. In the left navigation pane, choose **User Pool** and select the user you want.

1. For **User Details**, choose **Resend welcome email**.

1. Confirm that the success message displays at the top of the User Pool dashboard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
