---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/add-sagemaker-as-trusted-service-associate.html
---

# Add Amazon SageMaker as a trusted service in the associated AWS account
<a name="add-sagemaker-as-trusted-service-associate"></a>

If you've enabled the Amazon SageMaker blueprint, you must also add SageMaker as one of the trusted services within Amazon DataZone. To do this, complete the following procedure:

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and sign in with your account credentials.

1. Choose **View domains** and then choose the domain that contains the enabled SageMaker blueprint.

1. Choose the **Trusted services**, then choose the **Amazon SageMaker**, and then choose **Enable**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
