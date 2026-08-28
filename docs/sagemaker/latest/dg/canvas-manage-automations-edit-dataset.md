---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-automations-edit-dataset.html
---

# Edit your automatic dataset update configuration
<a name="canvas-manage-automations-edit-dataset"></a>

You might want to make changes to your auto update configuration for a dataset, such as changing the frequency of the updates. You might also want to turn off your automatic update configuration to pause the updates to your dataset.

To make changes to your auto update configuration for a dataset, do the following:

1. In the left navigation pane of Canvas, choose **ML Ops**.

1. Choose the **Automations** tab.

1. Choose the **Configuration** tab.

1. For your auto update configuration, choose the **More options** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/more-options-icon.png)).

1. In the dropdown menu, choose **Update configuration**. You are taken to the **Auto updates** tab of the dataset.

1. Make your changes to the configuration. When you’re done making changes, choose **Save**.

To pause your dataset updates, turn off your automatic configuration. One way to turn off auto updates is by doing the following:

1. In the left navigation pane of Canvas, choose **ML Ops**.

1. Choose the **Automations** tab.

1. Choose the ** Configuration** tab.

1. Find your configuration from the list and turn off the **Auto update** toggle.

Automatic updates for your dataset are now paused. You can turn this toggle back on at any time to resume the update schedule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
