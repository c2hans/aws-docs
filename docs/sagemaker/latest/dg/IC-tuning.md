---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/IC-tuning.html
---

# Tune an Image Classification Model
<a name="IC-tuning"></a>

*Automatic model tuning*, also known as hyperparameter tuning, finds the best version of a model by running many jobs that test a range of hyperparameters on your dataset. You choose the tunable hyperparameters, a range of values for each, and an objective metric. You choose the objective metric from the metrics that the algorithm computes. Automatic model tuning searches the hyperparameters chosen to find the combination of values that result in the model that optimizes the objective metric.

For more information about model tuning, see [Automatic model tuning with SageMaker AI](automatic-model-tuning.md).

## Metrics Computed by the Image Classification Algorithm
<a name="IC-metrics"></a>

The image classification algorithm is a supervised algorithm. It reports an accuracy metric that is computed during training. When tuning the model, choose this metric as the objective metric.

| Metric Name | Description | Optimization Direction |
| --- | --- | --- |
| validation:accuracy | The ratio of the number of correct predictions to the total number of predictions made. | Maximize |

## Tunable Image Classification Hyperparameters
<a name="IC-tunable-hyperparameters"></a>

Tune an image classification model with the following hyperparameters. The hyperparameters that have the greatest impact on image classification objective metrics are: `mini_batch_size`, `learning_rate`, and `optimizer`. Tune the optimizer-related hyperparameters, such as `momentum`, `weight_decay`, `beta_1`, `beta_2`, `eps`, and `gamma`, based on the selected `optimizer`. For example, use `beta_1` and `beta_2` only when `adam` is the `optimizer`.

For more information about which hyperparameters are used in each optimizer, see [Image Classification Hyperparameters](IC-Hyperparameter.md).

| Parameter Name | Parameter Type | Recommended Ranges |
| --- | --- | --- |
| beta\_1 | ContinuousParameterRanges | MinValue: 1e-6, MaxValue: 0.999 |
| beta\_2 | ContinuousParameterRanges | MinValue: 1e-6, MaxValue: 0.999 |
| eps | ContinuousParameterRanges | MinValue: 1e-8, MaxValue: 1.0 |
| gamma | ContinuousParameterRanges | MinValue: 1e-8, MaxValue: 0.999 |
| learning\_rate | ContinuousParameterRanges | MinValue: 1e-6, MaxValue: 0.5 |
| mini\_batch\_size | IntegerParameterRanges | MinValue: 8, MaxValue: 512 |
| momentum | ContinuousParameterRanges | MinValue: 0.0, MaxValue: 0.999 |
| optimizer | CategoricalParameterRanges | ['sgd', ‘adam’, ‘rmsprop’, 'nag'] |
| weight\_decay | ContinuousParameterRanges | MinValue: 0.0, MaxValue: 0.999 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
