---
source_url: https://docs.aws.amazon.com/athena/latest/ug/editing-workgroups.html
---

# Edit a workgroup
<a name="editing-workgroups"></a>

Editing a workgroup requires permissions to `UpdateWorkgroup` API operations. See [Configure access to workgroups and tags](workgroups-access.md) and [Use IAM policies to control workgroup access](workgroups-iam-policy.md). If you are adding or editing tags, you also need to have permissions to `TagResource`. See [Tag policy examples for workgroups](tags-access-control.md#tag-policy-examples-workgroups).

**To edit a workgroup in the console**

1. In the Athena console navigation pane, choose **Workgroups**.

1. On the **Workgroups** page, select the button for the workgroup that you want to edit.

1. Choose **Actions**, **Edit**.

1. Change the fields as needed. For the list of fields, see [Create workgroup](creating-workgroups.md). You can change all fields except for the workgroup's name. If you need to change the name, create another workgroup with the new name and the same settings.

1. Choose **Save changes**. The updated workgroup appears in the list on the **Workgroups** page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
