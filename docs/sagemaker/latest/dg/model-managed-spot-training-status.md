---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training-status.html
---

# Managed Spot Training Lifecycle
<a name="model-managed-spot-training-status"></a>

You can monitor a training job using `TrainingJobStatus` and `SecondaryStatus` returned by [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html). The list below shows how `TrainingJobStatus` and `SecondaryStatus` values change depending on the training scenario:
+ **Spot instances acquired with no interruption during training**

  1. `InProgress`: `Starting`↠ `Downloading` ↠ `Training` ↠ `Uploading`
+ **Spot instances interrupted once. Later, enough spot instances were acquired to finish the training job.**

  1. `InProgress`: `Starting` ↠ `Downloading` ↠ `Training` ↠ `Interrupted` ↠ `Starting` ↠ `Downloading` ↠ `Training` ↠ `Uploading`
+ **Spot instances interrupted twice and `MaxWaitTimeInSeconds` exceeded.**

  1. `InProgress`: `Starting` ↠ `Downloading` ↠ `Training` ↠ `Interrupted` ↠ `Starting` ↠ `Downloading` ↠ `Training` ↠ `Interrupted` ↠ `Downloading` ↠ `Training`

  1. `Stopping`: `Stopping`

  1. `Stopped`: `MaxWaitTimeExceeded`
+ **Spot instances were never launched.**

  1. `InProgress`: `Starting`

  1. `Stopping`: `Stopping`

  1. `Stopped`: `MaxWaitTimeExceeded`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
