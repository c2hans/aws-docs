---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard-alerts-edit.html
---

# Edit alert criteria
<a name="model-dashboard-alerts-edit"></a>

**To edit an alert in the Model Dashboard, complete the following steps:**

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/).

1. Choose **Governance** in the left panel.

1. Choose **Model Dashboard**.

1. In the **Models** section of the Model Dashboard, select the model name of the alert you want to modify.

1. Choose the radio box next to the monitor schedule of the alert you want to modify.

1. Choose **Edit Alert** in the **Monitor schedule** section.

1. (optional) Change **Datapoints to alert** if you want to change the number of failures within the **Evaluation period** that initiate an alert.

1. (optional) Change **Evaluation period** if you want to change the number of most recent monitoring executions to consider when evaluating alert status.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
