---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-time-series.html
---

# Built-in SageMaker AI Algorithms for Time-Series Data
<a name="algorithms-time-series"></a>

SageMaker AI provides algorithms that are tailored to the analysis of time-series data for forecasting product demand, server loads, webpage requests, and more.
+ [Use the SageMaker AI DeepAR forecasting algorithm](deepar.md)—a supervised learning algorithm for forecasting scalar (one-dimensional) time series using recurrent neural networks (RNN).

| Algorithm name | Channel name | Training input mode | File type | Instance class | Parallelizable |
| --- | --- | --- | --- | --- | --- |
| DeepAR Forecasting | train and (optionally) test | File | JSON Lines or Parquet | GPU or CPU | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
