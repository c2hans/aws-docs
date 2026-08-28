---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/create-new-ou.html
---

# Create a new OU
<a name="create-new-ou"></a>

Here's how to create an OU or a nested OU in AWS Control Tower.

**To create a new OU in AWS Control Tower**

1.  Navigate to the **Organization** page.

1. Select **Create organizational unit** from the **Create resources** dropdown menu in the upper right.

1. Specify a name in the **OU name** field.

1. In the **Parent OU** dropdown, you can see the hierarchy of registered OUs. Select a parent OU for the new OU you’re creating.

1. Choose **Add**.

**Tip**
To add a nested OU in fewer steps, select the name of the parent OU shown in the table on the **Organization** page, view the **OU** page for that parent OU, and then choose **Add an OU** from the **Actions** dropdown menu in the upper right. The new OU is created as a nested OU under your selected OU, automatically.

**Note**
If your landing zone is not up to date, you will see a flat list instead of a hierarchy in the dropdown menu. Even if your landing zone includes nested OUs, you will not see L5 OU’s in the dropdown, because you cannot create a new OU beneath a L5 OU. For more information about nested OUs in AWS Control Tower, see [Nested OUs in AWS Control Tower](nested-ous.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
