---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/train-smart-sifting-apply-to-script.html
---

# SageMaker smart sifting within your training script
<a name="train-smart-sifting-apply-to-script"></a>

The SageMaker smart sifting library is packaged in the [SageMaker AI framework DLCs](train-smart-sifting-what-is-supported.md#train-smart-sifting-supported-frameworks) as a complementary library. It provides a filtering logic against training samples that have relatively lower impact on model training, and your model can reach the desired model accuracy with fewer training samples when compared to the model training with full data samples.

To learn how to implement the smart sifting tool into your training script, choose one of the following based on the framework you use.

**Topics**
+ [Apply SageMaker smart sifting to your PyTorch script](train-smart-sifting-apply-to-pytorch-script.md)
+ [Apply SageMaker smart sifting to your Hugging Face Transformers script](train-smart-sifting-apply-to-hugging-face-transformers-script.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
