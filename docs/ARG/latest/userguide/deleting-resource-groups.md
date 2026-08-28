---
source_url: https://docs.aws.amazon.com/ARG/latest/userguide/deleting-resource-groups.html
---

# Deleting resource groups from AWS Resource Groups
<a name="deleting-resource-groups"></a>

You can use the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups) or the AWS CLI to delete resource groups from AWS Resource Groups. Deleting a resource group does not delete the resources that are members of the group or tags on member resources. It deletes only the group structure and any group-level tags.

------
#### [ Console ]

**To delete resource groups**

1. Sign in to the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups).

1. In the navigation pane, choose **[Saved Resource Groups](https://console.aws.amazon.com/resource-groups/groups)**.

1. Choose the name of the resource group that you want to delete, and then choose **View details**.

1. On the group's detail page, choose **Delete** in the top right corner.

1. When you are prompted to confirm the deletion, choose **Delete**.

------
#### [ AWS CLI & AWS SDKs ]

**To delete resource groups**

1. Run the following command, replacing {{resource\_group\_name}} with the name of your group.

   ```
   $ aws resource-groups delete-group \
       --group-name {{resource_group_name}}
   ```

1. When you are prompted to confirm the deletion, type `yes`, and then press **Enter**.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
