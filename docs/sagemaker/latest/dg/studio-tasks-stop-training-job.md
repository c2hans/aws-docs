---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-stop-training-job.html
---

# Stop a Training Job in Amazon SageMaker Studio Classic
<a name="studio-tasks-stop-training-job"></a>

**Note**
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

You can stop a training job with the Amazon SageMaker Studio Classic UI. When you stop a training job, its status changes to `Stopping` at which time billing ceases. An algorithm can delay termination in order to save model artifacts after which the job status changes to `Stopped`. For more information, see the [stop\_training\_job](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_training_job) method in the AWS SDK for Python (Boto3).

**To stop a training job**

1. Follow the [View experiments and runs](experiments-view-compare.md) procedure on this page until you open the **Describe Trial Component** tab.

1. At the upper-right side of the tab, choose **Stop training job**. The **Status** at the top left of the tab changes to **Stopped**.

1. To view the training time and billing time, choose **AWS Settings**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
