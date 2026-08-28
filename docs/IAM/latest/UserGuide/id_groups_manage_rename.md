---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_rename.html
---

# Rename an IAM user group
<a name="id_groups_manage_rename"></a>

When you change a user group's name or path, the following happens:
+ Any policies attached to the user group stay with the group under the new name.
+ The user group retains all its users under the new name.
+ The unique ID for the user group remains the same. For more information about unique IDs, see [Unique identifiers](reference_identifiers.md#identifiers-unique-ids).

IAM does not automatically update policies that refer to the user group as a resource to use the new name. Therefore, you must be careful when you rename a user group. Before you rename your user group, you must manually check all of your policies to find any policies where that user group is mentioned by name. For example, let's say Bob is the manager of the testing part of the organization. Bob has a policy attached to his IAM user entity that lets him add and remove users from the Test user group. If an administrator changes the name of the user group (or changes the group path), the administrator must also update the policy attached to Bob to use the new name or path. Otherwise Bob won't be able to add and remove users from the user group.

**To find policies that refer to an IAM group as a resource:**

1. From the navigation pane of the IAM console, choose **Policies**.

1. Sort by the **Type** column to find your **Customer managed** custom policies.

1. Choose the policy name of the policy to edit.

1. Choose the **Permissions** tab, and then choose **Summary**.

1. Choose **IAM** from the list of services, if it exists.

1. Look for the name of your user group in the **Resource** column.

1. Choose **Edit** to change the name of your user group in the policy.

## To change the name of an IAM user group
<a name="id_groups_manage_rename-section-1"></a>

------
#### [ Console ]

1. In the navigation pane, select **User groups** and then select the group name.

1. Choose **Edit**. Type the new user group name and then choose **Save changes**.

------
#### [ AWS CLI ]

Run the following command:
+ [aws iam update-group](https://docs.aws.amazon.com/cli/latest/reference/iam/update-group.html)

------
#### [ API ]

Call the following operation:
+ [UpdateGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateGroup.html)

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
