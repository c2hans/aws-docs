---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-python-sdk.html
---

# Use foundation models with the SageMaker Python SDK
<a name="jumpstart-foundation-models-use-python-sdk"></a>

All JumpStart foundation models are available for programmatic deployment using the SageMaker Python SDK.

To deploy publicly available foundation models, you can use their model ID. You can find the model IDs for all publicly available foundation models in the [Built-in Algorithms with pre-trained Model Table](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html). Search for the name of a foundation model in the **Search** bar. Use the **Show entries** dropdown or the pagination controls to navigate the available models.

Proprietary models must be deployed using the model package information after subscribing to the model in AWS Marketplace.

You can find the list of JumpStart available models in [Available foundation models](jumpstart-foundation-models-latest.md).

**Important**
Some foundation models require explicit acceptance of an end-user license agreement (EULA). For more information, see [EULA acceptance with the SageMaker Python SDK](jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula-python-sdk).

The following sections show how to fine-tune publicly available foundation models using the `JumpStartEstimator` class, deploy publicly available foundation models using the `JumpStartModel` class, and deploy proprietary foundation models using the`ModelPackage` class.

**Topics**
+ [Fine-tune publicly available foundation models with the `JumpStartEstimator` class](jumpstart-foundation-models-use-python-sdk-estimator-class.md)
+ [Deploy publicly available foundation models with the `JumpStartModel` class](jumpstart-foundation-models-use-python-sdk-model-class.md)
+ [Deploy proprietary foundation models with the `ModelPackage` class](jumpstart-foundation-models-use-python-sdk-proprietary.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
