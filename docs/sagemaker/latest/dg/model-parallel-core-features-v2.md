---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features-v2.html
---

# Core features of the SageMaker model parallelism library v2
<a name="model-parallel-core-features-v2"></a>

The Amazon SageMaker AI model parallelism library v2 (SMP v2) offers distribution strategies and memory-saving techniques, such as sharded data parallelism, tensor parallelism, and checkpointing. The model parallelism strategies and techniques offered by SMP v2 help distribute large models across multiple devices while optimizing training speed and memory consumption. SMP v2 also provides a Python package `torch.sagemaker` to help adapt your training script with few lines of code change.

This guide follows the basic two-step flow introduced in [Use the SageMaker model parallelism library v2](model-parallel-use-api-v2.md). To dive deep into the core features of SMP v2 and how to use them, see the following topics.

**Note**
These core features are available in SMP v2.0.0 and later and the SageMaker Python SDK v2.200.0 and later, and works for PyTorch v2.0.1 and later. To check the versions of the packages, see [Supported frameworks and AWS Regions](distributed-model-parallel-support-v2.md).

**Topics**
+ [Hybrid sharded data parallelism](model-parallel-core-features-v2-sharded-data-parallelism.md)
+ [Expert parallelism](model-parallel-core-features-v2-expert-parallelism.md)
+ [Context parallelism](model-parallel-core-features-v2-context-parallelism.md)
+ [Compatibility with the SMDDP library optimized for AWS infrastructure](model-parallel-core-features-v2-smddp-allgather.md)
+ [Mixed precision training](model-parallel-core-features-v2-mixed-precision.md)
+ [Delayed parameter initialization](model-parallel-core-features-v2-delayed-param-init.md)
+ [Activation checkpointing](model-parallel-core-features-v2-pytorch-activation-checkpointing.md)
+ [Activation offloading](model-parallel-core-features-v2-pytorch-activation-offloading.md)
+ [Tensor parallelism](model-parallel-core-features-v2-tensor-parallelism.md)
+ [Fine-tuning](model-parallel-core-features-v2-fine-tuning.md)
+ [FlashAttention](model-parallel-core-features-v2-flashattention.md)
+ [Checkpointing using SMP](model-parallel-core-features-v2-checkpoints.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
