---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/nova-model-bedrock-inference.html
---

# Amazon Bedrock inference
<a name="nova-model-bedrock-inference"></a>

Once you've trained and tested your Amazon Nova model, you can deploy it to Amazon Bedrock for production-scale inference. The deployment process involves creating an Amazon Bedrock model with the CreateCustomModel API, exporting your model artifacts to it from a managed Amazon S3 bucket, and then once the model is ACTIVE configuring an endpoint with on-demand or provisioned-throughput inference.

You can also use the Amazon Nova Forge SDK to deploy customized Amazon Nova models. The Amazon Nova Forge SDK provides a streamlined experience for extracting the relevant information from a training job or S3 model checkpoint and publishing it to Amazon Bedrock. For more information, see [Amazon Nova Forge SDK](nova-forge-sdk.md).

For detailed steps to set up Amazon Bedrock inference for a custom model, see the following section.
