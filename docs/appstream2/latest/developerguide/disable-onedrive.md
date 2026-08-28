---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/disable-onedrive.html
---

# Disable OneDrive for Your WorkSpaces Applications Users
<a name="disable-onedrive"></a>

You can disable OneDrive for a stack without losing user content that is already stored on OneDrive. Disabling OneDrive for a stack has the following effects:
+ Users who are connected to active streaming sessions for the stack receive an error message. They are informed that they do not have permissions to access their OneDrive.
+ Any new sessions that use the stack with OneDrive disabled do not display OneDrive.
+ Only the specific stack for which OneDrive is disabled is affected.
+ Even if OneDrive is disabled for all stacks, WorkSpaces Applications does not delete the user content stored in their OneDrive.

Follow these steps to disable OneDrive for an existing stack.

**To disable OneDrive for an existing stack**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. In the left navigation pane, choose **Stacks**, and select the stack for which to disable OneDrive.

1. Below the stacks list, choose **Storage**, and clear **Enable OneDrive for Business** option.

1. In the **Disable OneDrive for Business** dialog box, type `CONFIRM` (case-sensitive) to confirm your choice, then choose **Disable**.

   When users of the stack start their next WorkSpaces Applications streaming session, they can no longer access their OneDrive folder from within that session and future sessions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
