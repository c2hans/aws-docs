---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/model-optimization.html
---

# Model optimization techniques
<a name="model-optimization"></a>

You can apply several key optimization techniques to improve gen AI model performance and efficiency.

## Pruning
<a name="pruning"></a>

*Pruning* removes less important or redundant connections and neurons from a model, resulting in a sparser, more efficient network. This process can involve removing entire units like neurons or channels or setting individual weight parameters to zero based on various importance criteria. The goal is to reduce the model's size and computational requirements while maintaining its performance capabilities. When properly implemented, pruning can significantly decrease the resource requirements of a model without substantially impacting its accuracy. Pruning is an effective optimization technique for deployment scenarios where efficiency is crucial.

## Quantization
<a name="quantization"></a>

*Quantization *reduces both model and cache memory footprint while accelerating memory I/O and compute latency. This approach works by converting higher precision weights to lower precision formats, such as converting from FP16 to INT8. The key advantage of quantization is its ability to significantly reduce model size and improve performance while minimizing accuracy loss. Quantization is particularly effective for deployment in resource-constrained environments.

## Model compilation
<a name="model-compilation"></a>

*Model compilation* optimizes the underlying operators for specific hardware architectures. This process involves combining multiple operations for more efficient execution and eliminating redundant computations throughout the model. By creating hardware-specific optimized code paths, compilation ensures that models run as efficiently as possible on the target hardware platform. Compilation can result in improved inference speed and resource utilization.

## Speculative decoding
<a name="speculative-decoding"></a>

*Speculative decoding* is a technique to speed up the decoding process of large LLMs. It optimizes models for latency without compromising the quality of the generated text.

This technique can use a smaller but faster "draft" model to propose candidate tokens, which are then validated by the larger but slower "target" model. This is known as the draft-target approach. Alternatively, the [Extrapolation Algorithm for Greater Language-model Efficiency (EAGLE)](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-introduces-eagle-based-adaptive-speculative-decoding-to-accelerate-generative-ai-inference/) approach attaches a lightweight "EAGLE head" directly to the target model, rather than using a separate draft model. The EAGLE head generates an entire tree of potential token candidates by extrapolating from the target model's internal hidden state features. The target model can then efficiently verify and prune this draft token tree in a single parallel pass.

In either case, at each iteration, the draft or EAGLE mechanism generates multiple candidate tokens. The target model verifies the tokens, and if it finds that a particular token is not acceptable, it rejects that token and regenerates it. So, the target model both verifies tokens and generates a small amount of them.

The draft or EAGLE mechanism is significantly faster than the target model. It generates all the token candidates quickly and then sends them to the target model for parallel verification. This speeds up the final response compared to standard sequential token generation.

SageMaker AI offers a [pre-built draft model](https://aws.amazon.com/blogs/machine-learning/achieve-up-to-2x-higher-throughput-while-reducing-costs-by-50-for-generative-ai-inference-on-amazon-sagemaker-with-the-new-inference-optimization-toolkit-part-1/) that you can use, so you don't have to build your own. If you prefer to use your own custom draft model, SageMaker AI also supports this option.

## Artifact storage
<a name="artifact-storage"></a>

Efficient artifact storage maintains model weights and parameters in a ready-to-use state, enabling quick pre-loading and caching of examples. This optimization technique reduces cold-start times and streamlines the storage and retrieval of model weights. Proper artifact management is important for maintaining consistent performance in production environments, especially with large models, where checkpoints can approach hundreds of gigabytes. SageMaker AI provides [functionalities](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to facilitate artifact management.

## Applying inference optimizations in SageMaker AI
<a name="sagemaker-ai-technique"></a>

SageMaker AI leverages the techniques described earlier. With SageMaker AI, you can improve the performance of your generative AI models by applying inference optimization techniques. By optimizing your models, you can attain better cost performance for your use case. When you optimize a model, you choose which supported [optimization technique](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html) to apply, including quantization, speculative decoding, compilation, and fast model loading. After your model is optimized, you can run an evaluation to see performance metrics for latency, throughput, and price.
