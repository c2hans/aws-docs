---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-text-classification.html
---

# Text classification for model evaluation in Amazon Bedrock
<a name="model-evaluation-text-classification"></a>

Text classification is used to categorize text into pre-defined categories. Applications that use text classification include content recommendation, spam detection, language identification and trend analysis on social media. Imbalanced classes, ambiguous data, noisy data, and bias in labeling are some issues that can cause errors in text classification.

**Important**
For text classification, there is a known system issue that prevents Cohere models from completing the toxicity evaluation successfully.

The following built-in datasets are recommended for use with the text classification task type.

**Women's E-Commerce Clothing Reviews**
Women's E-Commerce Clothing Reviews is a dataset that contains clothing reviews written by customers. This dataset is used in text classification tasks.

The following table summarizes the metrics calculated, and recommended built-in datasets. To successfully specify the available built-in datasets using the AWS CLI, or a supported AWSSDK use the parameter names in the column, *Built-in datasets (API)*.

**Available built-in datasets in Amazon Bedrock**

- **Text classification**
  - **Metric:** Accuracy  / **Built-in datasets (console):** [Women's Ecommerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews) / **Built-in datasets (API):** Builtin.WomensEcommerceClothingBoolQ / **Computed metric:** Accuracy (Binary Accuracy from classification\_accuracy\_score)
  - **Metric:** Robustness  / **Built-in datasets (console):** [Women's Ecommerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews) / **Built-in datasets (API):** Builtin.WomensEcommerceClothingBoolQ / **Computed metric:** classification\_accuracy\_score and delta\_classification\_accuracy\_score

To learn more about how the computed metric for each built-in dataset is calculated, see [Review model evaluation job reports and metrics in Amazon Bedrock](model-evaluation-report.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
