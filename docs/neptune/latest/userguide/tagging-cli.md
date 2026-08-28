---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/tagging-cli.html
---

# Tagging in Neptune using the AWS CLI
<a name="tagging-cli"></a>

You can add, list, or remove tags for a DB instance in Neptune using the AWS CLI.
+ To add one or more tags to a Neptune resource, use the AWS CLI command [`add-tags-to-resource`](https://docs.aws.amazon.com/cli/latest/reference/neptune/add-tags-to-resource.html).
+ To list the tags on a Neptune resource, use the AWS CLI command [`list-tags-for-resource`](https://docs.aws.amazon.com/cli/latest/reference/neptune/list-tags-for-resource.html).
+ To remove one or more tags from a Neptune resource, use the AWS CLI command [`remove-tags-from-resource`](https://docs.aws.amazon.com/cli/latest/reference/neptune/remove-tags-from-resource.html).

To learn more about how to construct the required Amazon Resource Name (ARN), see [Constructing an ARN for Neptune](tagging-arns-constructing.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
