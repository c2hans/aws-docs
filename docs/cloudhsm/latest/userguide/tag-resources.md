---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/tag-resources.html
---

# Tag AWS CloudHSM resources
<a name="tag-resources"></a>

A tag is a label that you assign to an AWS resource. You can assign tags to your AWS CloudHSM clusters. Each tag consists of a tag key and a tag value, both of which you define. For example, the tag key might be **Cost Center** and the tag value might be **12345**. Tag keys must be unique for each cluster.

You can use tags for a variety of purposes. One common use is to categorize and track your AWS costs. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services. When you add tags to your AWS resources, AWS generates a cost allocation report with usage and costs aggregated by tags. You can use this report to view your AWS CloudHSM costs in terms of projects or applications, instead of viewing all AWS CloudHSM costs as a single line item.

For more information about using tags for cost allocation, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.

You can use the [AWS CloudHSM console](https://console.aws.amazon.com/cloudhsm/) or one of the [AWS SDKs or command line tools](https://aws.amazon.com/tools/) to add, update, list, and remove tags.

**Topics**
+ [Add or update tags](add-update-tags.md)
+ [List tags](list-tags.md)
+ [Remove tags](remove-tags.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
