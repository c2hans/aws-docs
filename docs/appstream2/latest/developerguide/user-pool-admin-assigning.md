---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin-assigning.html
---

# Assigning Stacks to Users in Amazon WorkSpaces Applications
<a name="user-pool-admin-assigning"></a>

You can assign one or more stacks to one or more users in the user pool. After they are assigned to at least one stack, users can log in to WorkSpaces Applications and launch applications. If users are assigned to more than one stack, they are presented with a list of stacks as catalogs to choose from before launching applications.

**Note**
Stacks can't be assigned to users if the stacks are associated with a fleet that is joined to an Active Directory domain.

**To assign a stack to users**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. In the left navigation pane, choose **User Pool** and select the users you want.

1. Choose **Actions**, **Assign stack**. For more information, see [Using Active Directory with WorkSpaces Applications](active-directory.md).

1. Review the list to confirm that the correct users are specified. For **Stack**, choose the stack you want to assign.

1. By default, **Send email notification to user** is enabled. Clear this option if you do not want to send the notification email to users now.

1. Choose **Assign stack**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
