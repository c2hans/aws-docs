---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/how-ai-inference-works.html
---

# How AI Inference works
<a name="how-ai-inference-works"></a>

AI inference is the process of using a trained model to generate predictions or outputs from new input data. Inputs can be text, images, audio, video, or structured data — and outputs span generated text, images, audio, embeddings, classifications, or any combination of these. A single inference request can involve **multiple stages or even multiple models** working together to produce the final output. For example, a voice assistant may chain an automatic speech recognition (ASR) model, a large language model, and a text-to-speech (TTS) model in sequence. A [retrieval-augmented generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/) pipeline combines an [embedding model](https://aws.amazon.com/what-is/embeddings-in-machine-learning/), a [re-ranker](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html), and an LLM. An image generation workflow may pass through a text encoder, a diffusion model, and a super-resolution model.

Understanding how inference works at the model and the system level — what computations occur, where bottlenecks emerge, and what resources are consumed — is essential for making informed decisions about hardware selection, deployment architecture, and optimization strategy.

## The transformer architecture
<a name="the-transformer-architecture"></a>

The [transformer](https://aws.amazon.com/what-is/transformers-in-artificial-intelligence/) architecture, introduced in 2017, is the foundation behind the vast majority of modern AI models used in production inference today. Understanding how transformers work — and how different model families use them — is essential for reasoning about inference performance and optimization.

### Core components
<a name="core-components.f4002433-4343-5fd9-8f1c-d1e5926397ff"></a>

At its heart, a transformer is built from a stack of identical **layers**, each containing several components working together:

1. **Attention mechanism**: Allows the model to weigh the importance of different parts of the input when processing each element. For example, when processing the word "it" in a sentence, attention determines which previous words "it" refers to.

1. **Feed-forward network**: A neural network that processes each position independently after attention has mixed information across positions.

1. **Residual connections and normalization** ("Add & Norm"): After each attention and feed-forward step, the original input to that step is added back (residual connection), and the result is normalized. This helps training stability and allows information to flow through many layers.

Additionally, transformers use **embeddings** to convert input tokens (words, sub-words, or pixels) into numerical vectors, and **positional encoding** to inject information about the order of elements in the sequence (since attention itself has no inherent sense of position).

Each layer transforms its input (a set of vectors representing the data) and passes it to the next layer. The final layer's output is used to produce predictions — whether that's the next word, an embedding vector, or a classification score.

### Encoder, decoder, and hybrid architectures
<a name="encoder--decoder--and-hybrid-architectures.9866b825-4010-5672-9ab0-70846e5c497e"></a>

Transformers can be organized in different ways depending on the task. The diagram below shows the original transformer architecture from the 2017 ["Attention Is All You Need" paper](https://arxiv.org/abs/1706.03762), which combines an **encoder** (left) and **decoder** (right):

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/f5c783c8-26d0-43b9-a990-34dd842f8ca5.png)

The key architectural patterns are:
+ **Encoder-only**: Uses just the left side. Processes the entire input at once using **multi-head attention** (bidirectional — each token can attend to all others). Produces a fixed output like an embedding vector or classification score. Examples: BERT, embedding models.
+ **Decoder-only**: Uses just the right side. Processes input and generates output one element at a time using **masked multi-head attention** (causal — each position can only attend to previous positions, not future ones). This enables autoregressive generation. Examples: GPT, Llama, Qwen.
+ **Encoder-decoder**: Combines both sides. The encoder processes the input bidirectionally, then the decoder generates output autoregressively while using **cross-attention** to access the encoder's output at each step. Examples: T5, BART, the original Transformer used for translation.

### Model families and inference patterns
<a name="model-families-and-inference-patterns.27678822-ee69-54e3-b203-f37bdc67b24b"></a>

Different model families use these architectural patterns in different ways, resulting in fundamentally different inference characteristics:

|
|
| Model Family | Architecture | Inference Pattern | Examples |
| --- |--- |--- |--- |
| **Embedding models** | Encoder-only | Single forward pass (vector output) | BERT, E5, GTE |
| **Re-ranker models** | Encoder-only or cross-encoder | Single forward pass (scoring) | BGE Reranker |
| **Large Language Models (LLMs)** | Decoder-only | Context processing \+ sequential generation | GPT, Llama, Mistral |
| **Encoder-decoder models** | Full transformer | Encode input \+ generate output | T5, BART, Whisper |
| **Vision-Language Models (VLMs)** | Vision encoder \+ decoder LLM | Encode image \+ process context \+ generate | Qwen-VL, Gemma3 |
| **Diffusion models** | Transformer-based (DiT) or U-Net | Iterative refinement (denoising) | Stable Diffusion 3, Qwen-Image |

Understanding this taxonomy matters because the inference characteristics — and therefore the optimization strategies — differ fundamentally based on which pattern a model follows. **The rest of this guide focuses on Large Language Models (decoder-only transformers)**, which are the most common and resource-intensive models deployed for inference today.

## LLM inference: Prefill and decode
<a name="llm-inference-prefill-and-decode"></a>

As established above, Large Language Models mostly use a decoder-only transformer architecture. This architectural choice means LLMs operate in two fundamentally different phases: **prefill** (processing the input context) and **decode** (generating output tokens one at a time). These two phases have completely different performance characteristics.

### The prefill phase (context encoding)
<a name="the-prefill-phase--context-encoding-.55630580-78da-5f5a-b396-480073f626d2"></a>

When a request arrives, the LLM first processes the entire input prompt in a single forward pass. This phase takes the input tensor (tokenized prompt) and the model weights, moves them from **GPU high-bandwidth memory (HBM) into the tensor cores**, and processes all input tokens in parallel through every transformer layer.

This phase computes and caches attention states for all input tokens, enabling efficient generation in the next phase.

|
|
| Property | Detail |
| --- |--- |
| **Data movement** | Model weights \+ input tensor loaded from memory to compute cores**once** |
| **Parallelism** | High — all input tokens processed simultaneously |
| **Performance constraint** | **Compute-bound**(massive parallel matrix multiplications) |
| **Output** | Cached attention states for all input tokens \+ first output token |
| **Metric impacted** | **Time to First Token (TTFT)** |

The decode phase (token generation)

After prefill, the model switches to **autoregressive decode**: generating output tokens one at a time. Each decode step involves reading the model weights and the accumulated attention state from HBM back into the tensor cores — to produce just a single token.

|
|
| Property | Detail |
| --- |--- |
| **Data movement** | Model weights \+ entire attention state moved from memory to compute cores **per token** |
| **Parallelism** | Low — each token depends on the previous |
| **Performance constraint** | **Memory-bandwidth-bound**(massive data movement for minimal compute) |
| **Output** | One token per step, with attention state updated |
| **Metric impacted** | **Time Per Output Token (TPOT)**,**Tokens Per Second (TPS)** |

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/0f2d5c74-e45a-49e4-9078-a075626c061f.png)

The distinction between prefill and decode is fundamentally about **arithmetic intensity** — the ratio of compute operations (FLOPs) to memory accesses (bytes moved):
+ **Prefill** has **high arithmetic intensity**: weights and inputs are loaded once, then many operations are performed across all tokens. The compute (FLOPS) is the bottleneck.
+ **Decode** has **very low arithmetic intensity**: the entire KV cache and weights are loaded from memory for each step, but only enough compute to produce a single token is performed. The **memory bandwidth** (GB/s) is the bottleneck.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/a64bc279-8323-4b5e-b599-6f258fecfbc3.png)

### Optional: Vision encoding phase
<a name="optional--vision-encoding-phase.10fbd910-9d43-547c-b178-1934851a5a84"></a>

**Vision-Language Models (VLMs)** extend the LLM inference pipeline with an additional encoding stage before prefill. They accept images (or video frames) alongside text and produce text outputs.

### How VLM inference works
<a name="how-vlm-inference-works.65c60590-ddb6-56d8-80ce-44215bc23f55"></a>

1. **Vision encoding**: A vision encoder (e.g., ViT, SigLIP) processes the input image into a sequence of visual tokens (patch embeddings)

1. **Projection**: Visual tokens are projected into the LLM's embedding space

1. **Prefill**: The combined sequence (visual tokens \+ text tokens) passes through the LLM backbone — this is standard prefill

1. **Decode**: Autoregressive token generation proceeds as normal

#### The KV cache
<a name="the-kv-cache.e93f7b75-5b7b-5b2c-824c-6bed605ec446"></a>

The **KV (Key-Value) cache** is the attention state stored in GPU memory that LLMs need to generate future tokens. It is one of the most critical concepts for understanding inference performance, memory consumption, and cost.

### Why the KV cache exists
<a name="why-the-kv-cache-exists.f0de690d-e471-598d-8805-ec5e66351aff"></a>

LLMs are autoregressive — each new token must attend to every previous token in the sequence. Without caching, the model would need to recompute the Key and Value projections for the entire context at every single decode step.

Since the Key and Value for a past token can be reused once computed, we can store them after computing them once. The KV cache stores these matrices so they are computed only once per token, dramatically reducing the computation required during decode.

**Why only K and V?** The Query represents "what the current token is looking for" — it's different for each new token and can't be precomputed. But the Keys and Values represent past tokens — they're fixed properties of those tokens, so we cache them.

### How it works
<a name="how-it-works.1b98d00e-9a01-55f7-ab77-00aa773cd3a4"></a>

1. During **prefill**, Key (K) and Value (V) projections are computed for every input token and stored in GPU HBM as the KV cache.

1. During **decode**, each new token:
   + Computes its own Query (Q), Key (K), and Value (V)
   + **Appends** its K and V to the cache
   + **Reads the entire cached K and V** to compute attention scores against all previous tokens
   + Uses the attention scores to create a weighted sum of cached Values

1. The cache grows linearly with sequence length — each new token adds one more K and V entry.

In the next section, we will cover the services on AWS that enable organizations to run AI inference at scale.
