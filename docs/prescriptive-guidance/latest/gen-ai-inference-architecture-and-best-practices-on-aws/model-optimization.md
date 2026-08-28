---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/model-optimization.html
---

# Model optimization techniques
<a name="model-optimization"></a>

Model optimizations focus on making the model itself faster and more compute and memory efficient — independent of the serving infrastructure. These techniques modify how the model is stored, compiled, or executed at inference time.

## Model Compression
<a name="pruning"></a>

Model compression techniques reduce memory footprint and computational requirements by removing redundant information or reducing numerical precision (quantization). These methods can be applied independently or in combination to achieve optimal efficiency.

### Quantization (Precision Reduction)
<a name="quantization--precision-reduction-.be0856e3-15c3-53f3-bf9e-38b274b26216"></a>

Quantization reduces the numerical precision of model weights (and optionally activations) from higher-precision formats (FP32, FP16/BF16) to lower-precision representations (FP8, MXFP4, [NVFP4](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/)). This directly reduces:
+ **Memory footprint** — Smaller weights mean the model fits in less GPU HBM
+ **Memory bandwidth consumption** — Less data to move from HBM → compute cores per inference step
+ **Compute latency** — Lower-precision arithmetic is faster on modern accelerators (e.g., Tensor Core FP8/INT8 throughput is 2× FP16)

The trade-off is potential quality degradation — though modern quantization techniques minimize this through calibration and mixed-precision strategies.

**Tip**
Prefer pre-quantized checkpoints where available, so scale factors are computed offline instead of at runtime.

### Precision hierarchy
<a name="precision-hierarchy.ec595485-05ca-55b3-874f-a119cd4b4a74"></a>

|
|
| Format | Bits per param | Memory (7B model) |
| --- |--- |--- |
| FP32 | 32 | \~28 GB |
| FP16 / BF16 | 16 | \~14 GB |
| FP8 (E4M3/E5M2) | 8 | \~7 GB |
| 4-bit (GPTQ/AWQ/MXFP4/NVFP4) | 4 | \~3.5 GB |

In addition to the above, newer generations of accelerated compute architectures natively support lower precisions. For example, AWS Trainium3 natively supports MXFP4 computation, and NVIDIA Blackwell's fifth-generation Tensor Cores natively support NVFP4.

### KV Cache Quantization
<a name="kv-cache-quantization.409caf06-f396-5d74-a6fd-c6b1095c3f2b"></a>

Not all compression needs to target model weights. **KV Cache optimization** specifically reduces the memory consumed by the attention cache during inference — which can dominate memory usage for long sequences and large batch sizes.

#### KV Cache Quantization
<a name="kv-cache-quantization.94fcc5ad-3a5d-538a-8eb5-381667b9b48d"></a>
+ **KV-only quantization**: Compresses the Key and Value matrices in the attention cache to FP8 or INT8 while keeping model weights at full or higher precision. This preserves model quality while dramatically reducing the memory consumed per active request
+ **Weight-only quantization**: Quantizes model weights but keeps activations and KV cache at higher precision. Reduces model loading time and static memory footprint while maintaining decode quality

**Impact on capacity**: For a model serving many concurrent requests with long contexts, KV cache often consumes more memory than the model weights themselves. Quantizing KV cache from FP16 to FP8 reduces the amount of memory necessary for KV blocks by half.

## Model compilation
<a name="model-compilation"></a>

Model compilation optimizes how operations are executed on hardware. At inference time, the choice between **eager mode** (operation-by-operation execution) and **compiled/graph mode** (pre-optimized execution paths) significantly impacts latency and throughput. Inference engines like [vLLM](https://docs.vllm.ai/en/stable/design/cuda_graphs/), SGLang, and TensorRT-LLM leverage these compilation modes to maximize performance.

### Execution Modes: Eager vs. Graph
<a name="execution-modes--eager-vs.-graph.5f6ca87e-2699-5028-ac83-fa5783f09ab6"></a>

**Eager Mode:**
+ Operations execute immediately as called, one at a time
+ Flexible — supports dynamic shapes and easy debugging
+ Higher overhead — each operation dispatched individually from CPU to GPU

**Graph/Compiled Mode:**
+ Operations are captured into a reusable execution graph during warm-up
+ Entire graph executes in one dispatch, eliminating per-operation overhead
+ During graph capture, inference engines apply hardware-optimized kernel implementations — for example, vLLM selects specialized kernels for MoE expert computation (DeepGEMM, CUTLASS, FlashInfer), fused attention kernels (FlashAttention, PagedAttention), and quantized GEMM operations tailored to the target hardware and precision format

**Example: vLLM uses CUDA graphs by default for maximum throughput, but provides the **`--enforce-eager`** flag for flexibility.**

### Kernel Optimization During Compilation
<a name="kernel-optimization-during-compilation.b8cdec2e-1765-5eeb-9fbe-ac1ae64e73d9"></a>

When inference engines compile a model into a CUDA graph or execution plan, they replace generic operations with specialized, fused kernels optimized for the target hardware and model architecture. This kernel selection happens at graph capture time and can significantly impact performance.

**Key kernel categories applied during compilation:**
+ **MoE expert kernels**: For Mixture-of-Experts models, engines select from specialized implementations like DeepGEMM (FP8-optimized), CUTLASS (NVIDIA's high-performance GEMM library with FP4/FP8 variants), or FlashInfer (minimal memory overhead for FP4/FP8). Selection depends on quantization format, activation function, and parallelism strategy.
+ **Attention kernels**: Fused implementations like FlashAttention-2 or PagedAttention that combine multiple attention operations into single kernel launches, reducing memory bandwidth and improving arithmetic intensity.
+ **Quantized GEMM operations**: Hardware-accelerated kernels that leverage Tensor Cores for mixed-precision computation (FP8, FP4, INT8).

These optimizations leverage NVIDIA GPU capabilities like Tensor Cores for maximum throughput. While kernel selection typically happens automatically based on model configuration and hardware detection, inference frameworks expose parameters to manually enable or disable specific kernel implementations — useful for debugging performance issues or testing different backends for your workload.

### Trainium Compilation with Neuron SDK
<a name="trainium-compilation-with-neuron-sdk.0f684bc8-26bd-5082-ac8e-e9ec851d6c16"></a>

AWS Trainium leverages compilation using Neuron SDK in order to prepare and optimize the model for its execution on its purpose-built accelerator cores. Models can be compiled before deployment using different libraries like [Optimum Neuron](https://huggingface.co/docs/optimum-neuron/en/index), [NeuronX Inference](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-inference/index.html#nxdi-index) or [PyTorch](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/frameworks/torch/index.html), which all use the Neuron compiler and leverage [Neuron Kernel Interface (NKI)](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/nki/index.html) to apply custom and optimized kernels. The ecosystem is evolving rapidly — consult the [Neuron documentation](https://awsdocs-neuron.readthedocs-hosted.com/) for latest news and best practices.

## Speculative decoding
<a name="speculative-decoding"></a>

***Speculative decoding*** is an acceleration technique for autoregressive generation (token generation). Rather than producing one final token per expensive model step, it uses a cheaper proposal mechanism to suggest several candidate tokens, then verifies them with the target model in a single pass.

**Core principle**: decode-time generation is usually memory-bandwidth bound, so the target model can often score multiple proposed tokens with only a modest increase in cost compared with scoring one token. If proposals are cheap enough and acceptance is high, the system can return multiple tokens per target-model step, often delivering substantial speedups with no change in output quality.

All speculative decoding variants follow the same basic loop:

1. **Proposal phase**: generate candidate tokens using a fast mechanism.

1. **Verification phase**: run the target model to evaluate those candidates.

1. **Acceptance**: keep the longest left-to-right prefix that matches the target; stop at the first mismatch and continue from there.

The techniques differ in how they produce proposals, which can be grouped into three categories:

### Model-less Speculation
<a name="model-less-speculation.c89f8eb0-64e1-5d30-9e56-0dd84764d59e"></a>

**Technique**: Pattern matching against already-generated text — no separate model needed.

**How it works**: Builds a suffix tree or n-gram statistics from generated text and the prompt, then proposes continuations from matching patterns when similar contexts reappear. The target model verifies these pattern-based candidates.

**Best for**:
+ Structured outputs (JSON, YAML, tool calls)
+ Code generation with repetitive patterns
+ Agentic workflows with repeated actions

**Advantages**:
+ Zero memory overhead — no additional model
+ Zero setup — works with any model out of the box
+ Effective for constrained or repetitive generation

**Example:** Suffix-based speculative decoding uses a **suffix tree** built from the prompt tokens to speculatively predict future tokens (matching repeated patterns/suffixes in the input), configured in vLLM via `--speculative-config '{"method": "suffix",...`

### Draft Model Speculation
<a name="draft-model-speculation.a7dd806e-80b9-5f41-bb3b-c9bfea304e02"></a>

**Technique**: Use a smaller, faster model to generate candidate tokens.

**How it works**: A small draft model generates K tokens autoregressively, then the target model validates all candidates in one pass. Tokens are accepted until the first disagreement, where the target model's prediction replaces the rejected token.

**Best for**: General-purpose generation when a compatible draft model is available (shared vocabulary and training distribution)

**Advantages**:
+ Proven approach with broad applicability
+ Works across diverse content types
+ Draft model can be reused across workloads

**Trade-offs**:
+ Requires loading a separate draft model (additional memory)
+ Acceptance rate depends on draft-target alignment

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/7212304c-d3d5-45ac-ab15-a3db2b23f3e1.png)

**Configuration example (vLLM):**

```
vllm serve meta-llama/Llama-3.1-70B-Instruct \
  --speculative-config '{"model": "meta-llama/Llama-3.2-1B-Instruct", "num_speculative_tokens": 5}'
```

### Decoding Head Speculation
<a name="decoding-head-speculation.d80e066e-43d8-53d4-b9b6-c98d5649462b"></a>

**Technique**: Train and/or use a lightweight "draft head" that predicts tokens using the target model's internal hidden states.

**How it works**: A small neural network (1–2 transformer layers) is trained to predict next-token distributions from the target model's latent features. At inference, the EAGLE or Medusa head generates candidates using the target model's own representations from the previous step, achieving higher acceptance rates than independent draft models.

**Best for**: Maximum speedup when a trained head is available for your target model

**Advantages**:
+ Higher acceptance rates than draft models (leverages target's internal representations)
+ Minimal memory overhead (\~1% of target model size)
+ Better prediction alignment with target model behavior

**Trade-offs**:
+ Requires training a speculator head for each target model if one is not already available
+ More complex setup than other approaches

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/b1a1b55d-348f-47f4-88c6-fe4f4557fa43.png)

**Configuration examples**

In SageMaker AI, you can [train EAGLE3 speculative decoder heads with SageMaker-curated datasets or with your own data](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-introduces-eagle-based-adaptive-speculative-decoding-to-accelerate-generative-ai-inference/). You can also leverage EAGLE3 speculative decoding using [SageMaker AI optimized generative AI inference recommendations](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-now-supports-optimized-generative-ai-inference-recommendations/). In addition, the following configuration shows how to use EAGLE3 and NVFP4 quantization in vLLM.

```
vllm serve nvidia/Kimi-K2.6-NVFP4 \
  --trust-remote-code \
  --tensor-parallel-size 4 \
  --tool-call-parser kimi_k2 \
  --enable-auto-tool-choice \
  --reasoning-parser kimi_k2 \
  --attention-backend tokenspeed_mla \
  --speculative-config '{"model":"lightseekorg/kimi-k2.6-eagle3.1-mla","method":"eagle3","num_speculative_tokens":3}' \
  --language-model-only
```

## Multi-LoRA Serving
<a name="artifact-storage"></a>

**Multi-LoRA serving** enables a single base model to serve multiple LoRA (Low-Rank Adaptation) adapters simultaneously, allowing different requests to use different fine-tuned variants without maintaining separate model deployments. LoRA adapters are small weight matrices (typically <1% of base model size) that modify specific layers to specialize model behavior for particular domains, tasks, or users.

### How Multi-LoRA Serving Works
<a name="how-multi-lora-serving-works.d8793129-efc2-53bc-8598-0069f39a2742"></a>

Rather than deploying N separate fine-tuned models, multi-LoRA serving loads one base model in GPU memory and keeps multiple lightweight LoRA adapters available. Incoming requests specify which adapter to use via API parameter, and the inference engine dynamically applies the appropriate adapter weights during forward pass.

**Key characteristics:**
+ **Shared base model**: One copy of base weights (\~14GB for a 7B FP16 model) serves all adapters
+ **Lightweight adapters**: Each LoRA adapter is typically 10-100MB depending on rank and target modules
+ **Dynamic switching**: Different concurrent requests can use different adapters in the same batch
+ **Automatic management**: Engine handles adapter loading/unloading based on memory constraints and request patterns

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/1f06ecc6-6043-448f-a88c-937fb170f08c.png)

### Memory and Performance Impact
<a name="memory-and-performance-impact.3a283487-c3a4-514f-ab4e-b039b3f34786"></a>

Multi-LoRA serving trades a small amount of compute overhead (applying adapter weights) for dramatic memory savings compared to deploying separate models:
+ **Memory**: Base model (14GB) \+ N adapters (50MB each) vs. N full models (14GB each) — enabling 100\+ adapters where only 7-8 full models would fit
+ **Latency**: Minimal overhead per request (\~5-10% compared to base model) when adapters are cached in GPU memory. Higher latency if adapter needs loading from CPU/disk
+ **Resource Utilization**: Higher as it prevents replicating base-model weights for each separate task-specific model

### When to Use Multi-LoRA Serving
<a name="when-to-use-multi-lora-serving.4be318ab-4333-5502-8989-3b70ca71fca8"></a>

Multi-LoRA serving is most valuable when you need to serve many variants of a base model:
+ **Multi-tenant deployments**: Different customers or teams with domain-specific fine-tunes sharing infrastructure
+ **Task specialization**: Single endpoint serving adapters for different capabilities (summarization, extraction, code generation)
+ **Personalization**: User-specific or group-specific adapters for customized behavior
+ **A/B testing**: Concurrent evaluation of multiple fine-tune candidates against production traffic
+ **Domain adaptation**: Industry-specific variants (legal, medical, finance) without separate deployments

### Configuration Examples
<a name="configuration-examples.6dbe83e4-db23-54d0-a3ce-6f4f5474f6a2"></a>

In SageMaker AI, you can leverage the efficient multi-adapter inference as a native feature. More details in [this blog post](https://aws.amazon.com/blogs/machine-learning/easily-deploy-and-manage-hundreds-of-lora-adapters-with-sagemaker-efficient-multi-adapter-inference/). In addition, the following configuration shows how to use multi-adapter LLM inference natively in vLLM.

```
# Start server with multi-LoRA support
vllm serve Qwen/Qwen3.6-35B-A3B \
    --enable-lora \
    --enable-mixed-moe-lora-format \
    --tensor-parallel-size 4 \
    --enable-expert-parallel \
    --lora-modules \
        '{"name": "lora-2d", "path": "jeeejeee/qwen36-35ba3b-2d-weights-poken-lora", "is_3d_lora_weight": false}' \
        '{"name": "lora-3d", "path": "jeeejeee/qwen36-35ba3b-moe-all-linear-poken-lora", "is_3d_lora_weight": true}'

# Request with specific LoRA adapter
curl -X POST http://localhost:8000/v1/load_lora_adapter \
-H "Content-Type: application/json" \
-d '{
    "lora_name": "lora-3d",
    "lora_path": "/path/to/3d-format-lora",
    "is_3d_lora_weight": true
}'
```

## Applying inference optimizations in SageMaker AI
<a name="sagemaker-ai-technique"></a>

SageMaker AI leverages the techniques described earlier. With SageMaker AI, you can improve the performance of your generative AI models by applying inference optimization techniques. By optimizing your models, you can attain better cost performance for your use case. When you optimize a model, you choose which supported [optimization technique](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html) to apply, including quantization, speculative decoding, compilation, and fast model loading. After your model is optimized, you can run an evaluation to see performance metrics for latency, throughput, and price.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
