---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-flow-edit-sampling.html
---

# Edit the data flow sampling configuration
<a name="canvas-data-flow-edit-sampling"></a>

When importing tabular data into a Data Wrangler data flow, you can opt to take a sample of your dataset to speed up the data exploration and cleaning process. Running exploratory transforms on a sample of your dataset is often faster than running transforms on your entire dataset, and when you're ready to export your dataset and build a model, you can apply the transforms to the full dataset.

Canvas supports the following sampling methods:
+ **FirstK** – Canvas selects the first *K* items from your dataset, where *K* is a number you specify. This sampling method is simple but can introduce bias if your dataset isn't randomly ordered.
+ **Random** – Canvas selects items from the dataset at random, with each item having an equal probability of being chosen. This sampling method helps ensure that the sample is representative of the entire dataset.
+ **Stratified** – Canvas divides the dataset into groups (or *strata*) based on one or more attributes (for example, age and income level). Then, a proportional number of items are randomly selected from each group. This method ensures that all relevant subgroups are adequately represented in the sample.

You can edit your sampling configuration at any time to change the size of the sample used for data exploration.

To make changes to your sampling configuration, do the following:

1. In your data flow graph, select your data source node.

1. Choose **Sampling** on the bottom navigation bar.

1. The **Sampling** dialog box opens. For the **Sampling method** dropdown, select your desired sampling method.

1. For **Maximum sample size**, enter the number of rows you want to sample.

1. Choose **Update** to save your changes.

The changes to your sampling configuration should now be applied.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
