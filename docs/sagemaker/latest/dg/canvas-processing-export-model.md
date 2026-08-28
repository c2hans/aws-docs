---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-processing-export-model.html
---

# Export to create a model
<a name="canvas-processing-export-model"></a>

In just a few clicks from your data flow, you can export your transformed data and start creating an ML model in Canvas. Canvas saves your data as a Canvas dataset, and you're taken to the model build configuration page for a new model.

To create a Canvas model with your transformed data:

1. Navigate to your data flow.

1. Choose the ellipsis icon next to the node that you're exporting.

1. From the context menu, choose **Create model**.

1. In the **Export to create a model** side panel, enter a **Dataset name** for the new dataset.

1. Leave the **Process entire dataset** option selected to process and export your entire dataset before proceeding with building a model. Turn this option off to train your model using the interactive sample data you are working with in your data flow.

1. Enter a **Model name** to name the new model.

1. Select a **Problem type**, or the type of model that you want to build. For more information about the supported model types in SageMaker Canvas, see [How custom models work](canvas-build-model.md).

1. Select the **Target column**, or the value that you want the model to predict.

1. Choose **Export and create model**.

The **Build** tab for a new Canvas model should open, and you can finish configuring and training your model. For more information about how to build a model, see [Build a model](canvas-build-model-how-to.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
