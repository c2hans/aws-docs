---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/leave-collab.html
---

# Leaving a collaboration
<a name="leave-collab"></a>

As a collaboration member, you can leave a collaboration by deleting your membership. If you are the collaboration creator, you can only leave a collaboration by [deleting the collaboration](delete-collaboration.md).

**Note**
When you delete your membership, you leave the collaboration and can't re-join it. If you are the [member paying for query compute costs](glossary.md#glossary-member-paying-for-query-compute) and you delete your membership, no more queries are allowed to run.

**To leave a collaboration**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. For **With active membership**, choose the collaboration of which you are a member.

1. Choose **Actions**.

1. Choose **Delete membership**.

1. In the dialog box, confirm the decision to leave the collaboration by typing **confirm** in the text input field, and then choose **Empty and delete membership**.

   You see a message on the console indicating that the membership was deleted.

   The collaboration creator sees the **Member status** as **Left**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
