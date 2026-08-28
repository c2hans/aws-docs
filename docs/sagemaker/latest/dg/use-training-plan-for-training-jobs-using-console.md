---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/use-training-plan-for-training-jobs-using-console.html
---

# Create a training job using the SageMaker AI console
<a name="use-training-plan-for-training-jobs-using-console"></a>

You can use a SageMaker training plans for your training jobs using the SageMaker AI UI. When creating a training job, the available plans are suggested to you if your instance choice and region matches the available plans.

To create a training job using a training plan's reserved capacity in the SageMaker console:

1. Navigate to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. In the left navigation pane, choose **Training**, and then **Training jobs**.

1. Choose the **Create training job** button.

1. When configuring the resources for your training job, look for the **Instance capacity** section. If there are plans available that match your chosen instance type and region, they are displayed here. Select a training plan that aligns with your compute capacity needs.

   If no suitable plans are available, you can either adjust your instance type or region, or proceed without using a training plan.

1. After selecting a training plan (or choosing to proceed without one), complete the rest of your training job configuration and choose **Create training job** to start the process.

![SageMaker AI console page for creating a new training job. The page displays various configuration options including job settings, algorithm options, resource configuration, training plan selection, and stopping conditions.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/training-plans/tp-create-training-job.png)

Review and launch your job. Your job starts running as soon as the training plan becomes `Active`, pending capacity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
