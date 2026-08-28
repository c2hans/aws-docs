---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/nova-model-bedrock-inference.html
---

# Amazon Bedrock inference
<a name="nova-model-bedrock-inference"></a>

Once you've trained and tested your Amazon Nova model, you can deploy it to Amazon Bedrock for production-scale inference. The deployment process involves creating an Amazon Bedrock model with the CreateCustomModel API, exporting your model artifacts to it from a managed Amazon S3 bucket, and then once the model is ACTIVE configuring an endpoint with on-demand or provisioned-throughput inference.

You can also use the SageMaker Python SDK to deploy customized Amazon Nova models to Amazon Bedrock On-Demand or SageMaker AI Real-time Inference endpoints. For more information, see [Customizing with SageMaker Python SDK](nova-forge-sdk.md).

For detailed steps to set up Amazon Bedrock inference for a custom model, see the following section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
