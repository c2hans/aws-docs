---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/add-member.html
---

# Adding members to a collaboration
<a name="add-member"></a>

**Prerequisites**
+ An AWS account with permissions to manage collaborations
+ The AWS account IDs of members you want to add

**To add a member to a collaboration**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Select the collaboration you want to add members to.

1. Choose the **Members** tab.

1. Choose **Edit members**.

1. Choose **Add another member** and enter the following information:
   + **Member display name**
   + **Member AWS account ID**
   + Specify whether they **can receive results**

1. Choose **Save changes**.

1. In the confirmation modal, verify that the information is correct, and choose **Submit change request**.
   + If the change request requires other members' approval, all existing members must approve the change request before the new member is added. For more information on change requests, see [Change requests in AWS Clean Rooms](change-requests.md).
   + If auto-approval change types are supported for new members with the specified abilities, then this change will take effect immediately. For more information, see [Edit collaboration auto-approval settings](change-requests.md#edit-auto-approval-settings).

1. On the collaboration detail page, under the **Members** tab, verify that the **Member status** of the added member(s) displays as **Invited**.

After completing these steps, the invited members can join the collaboration. For more information about joining a collaboration, see [Creating a membership and joining a collaboration](create-membership.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
