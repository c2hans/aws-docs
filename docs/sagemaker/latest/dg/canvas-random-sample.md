---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-random-sample.html
---

# Random sample
<a name="canvas-random-sample"></a>

SageMaker Canvas uses the random sampling method to sample your dataset. The random sample method means that each row has an equal chance of being picked for the sample. You can choose a column in the preview to get summary statistics for the random sample, such as the mean and the mode.

By default, SageMaker Canvas uses a random sample size of 20,000 rows from your dataset for datasets with more than 20,000 rows. For datasets smaller than 20,000 rows, the default sample size is the number of rows in your dataset. You can increase or decrease the sample size by choosing **Random sample** in the **Build** tab of the SageMaker Canvas application. You can use the slider to select your desired sample size, and then choose **Update** to change the sample size. The maximum sample size you can choose for a dataset is 40,000 rows, and the minimum sample size is 500 rows. If you choose a large sample size, the dataset preview and summary statistics might take a few moments to reload.

The **Build** page shows a preview of 100 rows from your dataset. If the sample size is the same size as your dataset, then the preview uses the first 100 rows of your dataset. Otherwise, the preview uses the first 100 rows of the random sample.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
