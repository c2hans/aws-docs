---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin-disabling.html
---

# Disabling Users in Amazon WorkSpaces Applications
<a name="user-pool-admin-disabling"></a>

You can disable one or more users in the user pool, one at a time. After they are disabled, users can no longer log in to WorkSpaces Applications until they are re-enabled. This action does not delete users. If users are connected when you disable them, their sessions remain active until the session cookie expires (about one hour). Stack assignments for the users are retained. If the users are re-enabled, their stack assignments become active again.

**To disable a user**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. In the left navigation pane, choose **User Pool** and select the user you want.

1. Choose **Actions**, **Disable user**.

1. Confirm that the correct user is specified, and choose **Disable User**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
