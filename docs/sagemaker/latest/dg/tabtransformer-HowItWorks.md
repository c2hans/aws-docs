---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/tabtransformer-HowItWorks.html
---

# How TabTransformer works
<a name="tabtransformer-HowItWorks"></a>

TabTransformer is a novel deep tabular data modeling architecture for supervised learning. The TabTransformer is built upon self-attention based Transformers. The Transformer layers transform the embeddings of categorical features into robust contextual embeddings to achieve higher prediction accuracy. Furthermore, the contextual embeddings learned from TabTransformer are highly robust against both missing and noisy data features, and provide better interpretability.

TabTransformer performs well in machine learning competitions because of its robust handling of a variety of data types, relationships, distributions, and the diversity of hyperparameters that you can fine-tune. You can use TabTransformer for regression, classification (binary and multiclass), and ranking problems.

The following diagram illustrates the TabTransformer architecture.

![The architecture of TabTransformer.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/tabtransformer_illustration.png)

For more information, see *[TabTransformer: Tabular Data Modeling Using Contextual Embeddings](https://arxiv.org/abs/2012.06678)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
