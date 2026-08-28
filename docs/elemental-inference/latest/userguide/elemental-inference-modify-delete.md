---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/userguide/elemental-inference-modify-delete.html
---

# Work with existing Elemental Inference feeds
<a name="elemental-inference-modify-delete"></a>

You can make the following changes to an existing feed:
+ Revise the properties of any features (outputs) that have configuration properties. For example, you can change the callback metadata value in an event clipping output.
+ Add outputs up to the maximum allowed in one feed.
+ Remove outputs.
+ Enable or disable outputs (change the status). For information about the status of outputs, see [Status of an output](monitor-inference-feed-lifecycle.md#monitor-inference-status-output).

You can make these changes using the Elemental Inference console or the AWS CLI.

**Topics**
+ [Revising using the console](modify-delete-feed-console.md)
+ [Revising using the CLI](modify-delete-feed-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
