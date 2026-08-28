---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-predictions-batch-manual.html
---

# Make manual batch predictions
<a name="canvas-make-predictions-batch-manual"></a>

Choose one of the following procedures to make manual batch predictions based on your model type.

## Make manual batch predictions with numeric, categorical, and time series forecasting models
<a name="canvas-make-predictions-batch-numeric-categorical"></a>

To make manual batch predictions for numeric, categorical, and time series forecasting model types, do the following:

1. In the left navigation pane of the Canvas application, choose **My models**.

1. On the **My models** page, choose your model.

1. After opening your model, choose the **Predict** tab.

1. On the **Run predictions** page, choose **Batch prediction**.

1. Choose **Select dataset** to pick a dataset for generating predictions.

1. From the list of available datasets, select your dataset, and then choose **Start Predictions** to get your predictions.

After the prediction job finishes running, there is an output dataset listed on the same page in the **Predictions** section. This dataset contains your results, and if you select the **More options** icon (![Vertical ellipsis icon representing a menu or more options.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/more-options-icon.png)), you can choose **Preview** to preview the output data. You can see the input data matched to the prediction and the probability that the prediction is correct. Then, you can choose **Download prediction** to download the results as a file.

## Make manual batch predictions with image prediction models
<a name="canvas-make-predictions-batch-image"></a>

To make manual batch predictions for a single-label image prediction model, do the following:

1. In the left navigation pane of the Canvas application, choose **My models**.

1. On the **My models** page, choose your model.

1. After opening your model, choose the **Predict** tab.

1. On the **Run predictions** page, choose **Batch prediction**.

1. Choose **Select dataset** if you’ve already imported your dataset. If not, choose **Import new dataset**, and then you’ll be directed through the import data workflow.

1. From the list of available datasets, select your dataset and choose **Generate predictions** to get your predictions.

After the prediction job finishes running, on the **Run predictions** page, you see an output dataset listed under **Predictions**. This dataset contains your results, and if you select the **More options** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/more-options-icon.png)), you can choose **View prediction results** to see the output data. You can see the images along with their predicted labels and confidence scores. Then, you can choose **Download prediction** to download the results as a CSV or a ZIP file.

## Make manual batch predictions with text prediction models
<a name="canvas-make-predictions-batch-text"></a>

To make manual batch predictions for a multi-category text prediction model, do the following:

1. In the left navigation pane of the Canvas application, choose **My models**.

1. On the **My models** page, choose your model.

1. After opening your model, choose the **Predict** tab.

1. On the **Run predictions** page, choose **Batch prediction**.

1. Choose **Select dataset** if you’ve already imported your dataset. If not, choose **Import new dataset**, and then you’ll be directed through the import data workflow. The dataset you choose must have the same source column as the dataset with which you built the model.

1. From the list of available datasets, select your dataset and choose **Generate predictions** to get your predictions.

After the prediction job finishes running, on the **Run predictions** page, you see an output dataset listed under **Predictions**. This dataset contains your results, and if you select the **More options** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/canvas/more-options-icon.png)), you can choose **Preview** to see the output data. You can see the images along with their predicted labels and confidence scores. Then, you can choose **Download prediction** to download the results.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
