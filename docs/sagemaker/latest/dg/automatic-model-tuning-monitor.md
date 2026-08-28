---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-monitor.html
---

# Monitor the Progress of a Hyperparameter Tuning Job
<a name="automatic-model-tuning-monitor"></a>

To monitor the progress of a hyperparameter tuning job and the training jobs that it launches, use the Amazon SageMaker AI console.

**Topics**
+ [View the Status of the Hyperparameter Tuning Job](#automatic-model-tuning-monitor-tuning)

## View the Status of the Hyperparameter Tuning Job
<a name="automatic-model-tuning-monitor-tuning"></a>

**To view the status of the hyperparameter tuning job**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. Choose **Hyperparameter tuning jobs**.
![Hyperparameter tuning job console.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/console-tuning-jobs.png)

1. In the list of hyperparameter tuning jobs, check the status of the hyperparameter tuning job you launched. A tuning job can be:
   + `Completed`—The hyperparameter tuning job successfully completed.
   + `InProgress`—The hyperparameter tuning job is in progress. One or more training jobs are still running.
   + `Failed`—The hyperparameter tuning job failed.
   + `Stopped`—The hyperparameter tuning job was manually stopped before it completed. All training jobs that the hyperparameter tuning job launched are stopped.
   + `Stopping`—The hyperparameter tuning job is in the process of stopping.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
