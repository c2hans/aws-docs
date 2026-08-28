---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-manage-automations.html
---

# How to manage automations
<a name="canvas-manage-automations"></a>

In SageMaker Canvas, you can create automations that update your dataset or generate predictions from your model on a schedule. For example, you might receive new shipping data on a daily basis. You can set up an automatic update for your dataset and automatic batch predictions that run whenever the dataset is updated. Using these features, you can set up an automated workflow and reduce the amount of time you spend manually updating datasets and making predictions.

**Note**
You can only set up a maximum of 20 automatic configurations in your Canvas application. Automations are only active while you’re logged in to the Canvas application. If you log out of Canvas, your automatic jobs pause until you log back in.

The following sections describe how to view, edit, and delete configurations for existing automations. To learn how to set up automations, see the following topics:
+ To set up automatic dataset updates, see [Update a dataset](canvas-update-dataset.md).
+ To set up automatic batch predictions, see [Batch predictions in SageMaker Canvas](canvas-make-predictions-batch.md).

**Topics**
+ [View your automations](canvas-manage-automations-view.md)
+ [Edit your automatic configurations](canvas-manage-automations-edit.md)
+ [Delete an automatic configuration](canvas-manage-automations-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
