---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-tags-cli.html
---

# Tag or untag resources
<a name="nw-monitor-tags-cli"></a>

You can work with resource tags in Network Synthetic Monitor, to add or remove tags.

You can update tags by updating monitors or probes in the console. Or, you can work with tags programmatically, for example, by using the AWS Command Line Interface.

**To update monitor tags by using the CLI**
+ To list resource tags, use [list-tags-for-resources](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/list-tags-for-resources.html).
+ To tag a resource, use [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/tag-resource.html).
+ To untag a resource, use [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/untag-resource.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
