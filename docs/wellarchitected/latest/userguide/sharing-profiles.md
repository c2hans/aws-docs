---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/sharing-profiles.html
---

# Sharing a profile in AWS WA Tool
<a name="sharing-profiles"></a>

Profiles can be shared with users or accounts, or they can be shared with an entire organization or organizational unit.

**To share a profile**

1. Select **Profiles** in the left navigation pane.

1. Select the name of the profile you want to share.

1. Choose the **Shares** tab.

1. To share to a user or account, choose **Create** and select **Create shares to IAM users or accounts**. In the **Send invitations** box, specify the user or account IDs, and choose **Create**.

1. To share to an organization or organizational unit, choose **Create** and select **Create shares to Organizations**. To share to an entire organization select **Grant permissions to the entire Organization**. To share with an organizational unit, select **Grant permissions to individual Organization Units**, specify the organizational unit in the box, and choose **Create**.

**Important**
Before sharing a profile with an organization or organizational unit (OU), you must [enable AWS Organizations access](sharing.md#getting-started-sharing-orgs).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
