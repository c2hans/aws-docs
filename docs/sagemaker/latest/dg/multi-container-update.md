---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-update.html
---

# Update a multi-container endpoint
<a name="multi-container-update"></a>

To update an Amazon SageMaker AI multi-container endpoint, complete the following steps.

1.  Call [create\_model](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model) to create a new model with a new value for the `Mode` parameter in the `InferenceExecutionConfig` field.

1.  Call [create\_endpoint\_config](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config) to create a new endpoint config with a different name by using the new model you created in the previous step.

1.  Call [update\_endpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_endpoint) to update the endpoint with the new endpoint config you created in the previous step.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
