---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/autogluon-tabular-HowItWorks.html
---

# How AutoGluon-Tabular works
<a name="autogluon-tabular-HowItWorks"></a>

AutoGluon-Tabular performs advanced data processing, deep learning, and multi-layer model ensemble methods. It automatically recognizes the data type in each column for robust data preprocessing, including special handling of text fields.

AutoGluon fits various models ranging from off-the-shelf boosted trees to customized neural networks. These models are ensembled in a novel way: models are stacked in multiple layers and trained in a layer-wise manner that guarantees raw data can be translated into high-quality predictions within a given time constraint. This process mitigates overfitting by splitting the data in various ways with careful tracking of out-of-fold examples.

The AutoGluon-Tabular algorithm performs well in machine learning competitions because of its robust handling of a variety of data types, relationships, and distributions. You can use AutoGluon-Tabular for regression, classification (binary and multiclass), and ranking problems.

Refer to the following diagram illustrating how the multi-layer stacking strategy works.

![AutoGluon's multi-layer stacking strategy shown with two stacking layers.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/autogluon_tabular_illustration.png)

For more information, see *[AutoGluon-Tabular: Robust and Accurate AutoML for Structured Data](https://arxiv.org/pdf/2003.06505.pdf)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
