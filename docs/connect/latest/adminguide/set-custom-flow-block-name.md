---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/set-custom-flow-block-name.html
---

# Customize the name of a flow block in Connect Customer
<a name="set-custom-flow-block-name"></a>

To help you distinguish blocks in a flow, you can customize the names of blocks. For example, when there are multiple **Play prompt** blocks, and you want to distinguish between them at a glance you can assign each block their own name.

Custom flow block names appear in CloudWatch logs under the `Identifier` field. This makes it easier for you to review the logs to diagnose issues.

**Important**
The following characters are not allowed in the block name or `Identifier` field: (% : ( \\ / ) = $ , ; [ ] { })
The following strings are not allowed in the block name or `Identifier` field: \_\_proto\_\_, constructor, \_\_defineGetter\_\_, \_\_defineSetter\_\_, toString, hasOwnProperty, isPrototypeOf, propertyIsEnumerable, toLocaleString, and valueOf.

There are two ways you can specify a custom block name:
+ On the block, choose **...**, and then choose **Add block name**, as shown in the following GIF.
![A block with a custom name.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-custom-flow-block-name-1.gif)
+ You can also customize the name of the block on the **Property** page, as shown in the following GIF.
![A block with a custom name.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-custom-flow-block-name-2.gif)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
