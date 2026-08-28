---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-automations-edit-batch.html
---

# Edit your automatic batch prediction configuration
<a name="canvas-manage-automations-edit-batch"></a>

When you edit a batch prediction configuration, you can change the target dataset but not the frequency (since automatic batch predictions occur whenever the dataset is updated).

To make changes to your automatic batch predictions configuration, do the following:

1. In the left navigation pane of Canvas, choose **ML Ops**.

1. Choose the **Automations** tab.

1. Choose the **Configuration** tab.

1. For your auto update configuration, choose the **More options** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/more-options-icon.png)).

1. In the dropdown menu, choose **Update configuration**. You are taken to the **Auto updates** tab of the dataset.

1. The **Automate batch prediction** dialog box opens. You can select another dataset and choose **Set up** to save your changes.

Your automatic batch predictions configuration is now updated.

To pause your automatic batch predictions, turn off your automatic configuration. Use the following procedure to turn off your configuration:

1. In the left navigation pane of Canvas, choose **ML Ops**.

1. Choose the **Automations** tab.

1. Choose the ** Configuration** tab.

1. Find your configuration from the list and turn off the **Auto update** toggle.

Automatic batch predictions for your dataset are now paused. You can turn this toggle back on at any time to resume the update schedule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
