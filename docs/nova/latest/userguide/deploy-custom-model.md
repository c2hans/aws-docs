---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/deploy-custom-model.html
---

# Deploy a custom model for on-demand inference
<a name="deploy-custom-model"></a>

After you successfully create a custom model with a model customization job (fine-tuning, distillation, or continued pre-training), you can set up on-demand inference for the model.

To set up on-demand inference for a custom model, you deploy the model with a custom model deployment. After you deploy your custom model, you use the deployment's Amazon Resource Name (ARN) as the `modelId` parameter in your `InvokeModel` or `Converse` API operations. You can use the deployed model for on-demand inference with Amazon Bedrock features such as playgrounds, Agents, and Knowledge Bases.

**Topics**
+ [Supported models](#custom-model-inference-supported-models)
+ [Deploy a custom model](deploying-custom-model.md)
+ [Use a deployment for on-demand inference](use-custom-model-on-demand.md)
+ [Delete a custom model deployment](delete-custom-model-deployment.md)

## Supported models
<a name="custom-model-inference-supported-models"></a>

You can set up on-demand inference for the following models:
+ Amazon Nova Canvas
+ Amazon Nova Lite
+ Amazon Nova Micro
+ Amazon Nova Pro

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
