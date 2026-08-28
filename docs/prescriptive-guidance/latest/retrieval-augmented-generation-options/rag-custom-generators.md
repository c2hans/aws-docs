---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-custom-generators.html
---

# Generators for RAG workflows
<a name="rag-custom-generators"></a>

[Large language models (LLMs)](https://aws.amazon.com/what-is/large-language-model/) are very large [deep learning](https://aws.amazon.com/what-is/deep-learning/) models that are pretrained on vast amounts of data. They are incredibly flexible. LLMs can perform varied tasks, such as answering questions, summarizing documents, translating languages, and completing sentences. They have the potential to disrupt content creation and the way people use search engines and virtual assistants. While not perfect, LLMs demonstrate a remarkable ability to make predictions based on a relatively small prompt or number of inputs.

LLMs are a critical component of a RAG solution. For custom RAG architectures, there are two AWS services that serve as the primary options:
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that makes LLMs from leading AI companies and Amazon available for your use through a unified API.
+ [Amazon SageMaker AI JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) is an ML hub that offers foundation models, built-in algorithms, and prebuilt ML solutions. With SageMaker AI JumpStart, you can access pretrained models, including foundation models. You can also use your own data to fine-tune the pretrained models.

## Amazon Bedrock
<a name="rag-custom-generators-bedrock"></a>

Amazon Bedrock offers industry-leading models from Anthropic, Stability AI, Meta, Cohere, AI21 Labs, Mistral AI, and Amazon. For a complete list, see [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html). Amazon Bedrock also allows you to customize models with your own data.

You can [evaluate the model performance](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) to determine which are best suited for your RAG use case. You can test the latest models and also test to see which capabilities and features provide the best results and for the best price. The Anthropic Claude Sonnet model is a common choice for RAG applications because it excels at a wide range of tasks and provides a high degree of reliability and predictability.

## SageMaker AI JumpStart
<a name="rag-custom-sm-jumpstart"></a>

SageMaker AI JumpStart provides pretrained, open source models for a wide range of problem types. You can incrementally train and fine-tune these models before deployment. You can access the pretrained models, solution templates, and examples through the SageMaker AI JumpStart landing page in [Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html) or use the [SageMaker AI Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-python-sdk.html).

SageMaker AI JumpStart offers state-of-the-art foundation models for use cases such as content writing, code generation, question answering, copywriting, summarization, classification, information retrieval, and more. Use JumpStart foundation models to build your own generative AI solutions and integrate custom solutions with additional SageMaker AI features. For more information, see [Getting started with Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/getting-started/).

SageMaker AI JumpStart onboards and maintains publicly available foundation models for you to access, customize, and integrate into your ML life cycles. For more information, see [Publicly available foundation models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-latest.html#jumpstart-foundation-models-latest-publicly-available). SageMaker AI JumpStart also includes proprietary foundation models from third-party providers. For more information, see [Proprietary foundation models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-latest.html#jumpstart-foundation-models-latest-proprietary).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
