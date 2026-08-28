---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/remove-member.html
---

# Removing members from a collaboration
<a name="remove-member"></a>

**Note**
Before you begin, note that removing a member:
Removes all of their associated datasets from the collaboration
If the [member pays for query compute costs](glossary.md#glossary-member-paying-for-query-compute), this action stops all query execution in the collaboration.
Removing a member also removes all of their associated datasets from the collaboration.

**Prerequisites**
+ You must be a collaboration creator
+ You can't remove your own account

**To remove a member from a collaboration**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Select the collaboration you want to modify.

1. Choose the **Members** tab.

1. Select the option button next to the member you want to remove.

1. Choose **Remove**.

1. In the confirmation dialog box, type **confirm** to verify the removal.

**Note**
After you remove a member, all datasets associated with their account are also removed from the collaboration.

**Important**
If you remove the member who pays for query compute costs, no further queries can run in the collaboration until you designate a new paying member.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
