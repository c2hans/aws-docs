---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-schedule-view.html
---

# View scheduled monitors
<a name="model-dashboard-schedule-view"></a>

Use SageMaker Model Monitor to continuously monitor your machine learning models for data drift, model quality, bias, and other issues that might impact model performance. After you've set up monitoring schedules, you can view the details of these scheduled monitors through the SageMaker AI console. The following procedure outlines the steps to access and review the scheduled monitors for a particular model, including their current status:

**To view a model’s scheduled monitors**

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/).

1. Choose **Governance** in the left panel.

1. Choose **Model Dashboard**.

1. In the **Models** section of the Model Dashboard, select the model name of the scheduled monitors you want to view.

1. View the scheduled monitors in the **Monitor schedule** section. You can review the status for each monitor in the **Status schedule** column, which is one of the following values:
   + **Failed**: The monitoring schedule failed due to a problem with the configuration or settings (such as incorrect user permissions).
   + **Pending**: The monitor is in the process of becoming scheduled.
   + **Stopped**: The schedule is stopped by the user.
   + **Scheduled**: The schedule is created and runs at the frequency you specified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
