---
source_url: https://docs.aws.amazon.com/ARG/latest/userguide/updating-resource-groups.html
---

# Updating groups in AWS Resource Groups
<a name="updating-resource-groups"></a>

To update a tag-based resource group in Resource Groups, you can edit the query and tags that are the basis of your group. You can add and remove resources from your group only by applying changes to the query or tags. You cannot select specific resources to add to or remove from your group. The best way to add or remove a specific resource from a group is to edit the resource's tags. Then verify that your resource group tag query either includes or omits the tag, depending on whether you want the resource in your group.

To update an CloudFormation stack-based resource group, you can choose a different stack. You can also add or remove resource types from the stack that you want to be part of the group. To change the resources that are available in the stack, update the CloudFormation template used to create the stack, and then update the stack in CloudFormation. For more information about how to update an CloudFormation stack, see [CloudFormation stacks updates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html) in the *CloudFormation User Guide.*

In the AWS CLI, you update groups in two commands.
+ `update-group`, which you run to update a group's description.
+ `update-group-query`, which you run to update the resource query and tags that determine the group's member resources.

In the console, you cannot change an CloudFormation stack-based group to a tag-based query group, or vice versa. However, you can do this by using the Resource Groups API, including in the AWS CLI.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
