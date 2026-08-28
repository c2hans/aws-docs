---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/autogluon-tabular-tuning.html
---

# Tuning an AutoGluon-Tabular model
<a name="autogluon-tabular-tuning"></a>

Although AutoGluon-Tabular can be used with model tuning, its design can deliver good performance using stacking and ensemble methods, meaning hyperparameter optimization is not necessary. Rather than focusing on model tuning, AutoGluon-Tabular succeeds by stacking models in multiple layers and training in a layer-wise manner.

For more information about AutoGluon-Tabular hyperparameters, see [AutoGluon-Tabular hyperparameters](autogluon-tabular-hyperparameters.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
