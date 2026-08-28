---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-api-name.html
---

# Find your workforce name
<a name="sms-workforce-management-private-api-name"></a>

Some of the SageMaker AI workforce-related API operations require your workforce name as input. You can see your Amazon Cognito or OIDC IdP private and vendor workforce names in an AWS Region using the [`ListWorkforces`]() API operation in that AWS Region. If you created your workforce using your own OIDC IdP, you can find your workforce name in the Ground Truth area of the SageMaker AI console.

**To find your workforce name in the SageMaker AI console**

1. Go to the Ground Truth area of the SageMaker AI console: [https://console.aws.amazon.com/sagemaker/groundtruth](https://console.aws.amazon.com/sagemaker/groundtruth).

1. Select **Labeling workforces**.

1. Select **Private**.

1. In the **Private workforce summary** section, locate your workforce ARN. Your workforce name is located at the end of this ARN. For example, if the ARN is `arn:aws:sagemaker:us-east-2:111122223333:workforce/example-workforce`, the workforce name is `example-workforce`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
