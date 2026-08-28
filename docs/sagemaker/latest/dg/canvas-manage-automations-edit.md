---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-automations-edit.html
---

# Edit your automatic configurations
<a name="canvas-manage-automations-edit"></a>

After setting up a configuration, you might want to make changes to it. For automatic dataset updates, you can update the Amazon S3 location for Canvas to import data, the frequency of the updates, and the starting time. For automatic batch predictions, you can change the dataset that the configuration tracks for updates. You can also turn off the automation to temporarily pause updates until you choose to resume them.

The following sections show you how to update each type of configuration.

**Note**
You can’t change the frequency for automatic batch predictions because automatic batch predictions run every time the target dataset is updated.

**Topics**
+ [Edit your automatic dataset update configuration](canvas-manage-automations-edit-dataset.md)
+ [Edit your automatic batch prediction configuration](canvas-manage-automations-edit-batch.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
