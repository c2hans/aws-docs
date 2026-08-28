---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/sharing-analyses.html
---

# Sharing Quick Sight analyses
<a name="sharing-analyses"></a>

You can share an analysis with one or more other users by emailing them a link, making it easy to collaborate and disseminate findings. You can only share an analysis with other users in your Quick account.

After you share an analysis, you can review the other users who have access to it, and also revoke access from any user.

**Topics**
+ [Sharing an analysis](#share-an-analysis)
+ [Viewing the users that an analysis is shared with](view-users-analysis.md)
+ [Revoking access to an analysis](revoke-access-to-an-analysis.md)

## Sharing an analysis
<a name="share-an-analysis"></a>

Use the following procedure to share an analysis.

**To share an analysis**

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. Open the analysis that you want to change.

1. On the analysis page, choose **File** on the application bar, and then choose **Share**.

   You can only share analyses with users or groups who are in your Quick account.

1. Add a user or group to share with. To do this, for **Type a user name or email**, enter the first user or group that you want to share this analysis with. Then choose **Share**. Repeat this step until you have entered information for everyone you want to share the analysis with.

   To edit sharing permissions for this analysis, choose **Manage analysis permissions**.

   The **Manage analysis permissions** screen appears. On this screen, choose **Invite user** to edit permissions and add more users or groups.

1.  For **Permission**, choose the role to assign to each user or group. The role determines the permission level to grant to that user or group.

1. Choose **Share**.

   The users that you have shared the analysis with get emails with a link to the analysis. Groups don't receive invitation emails.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
