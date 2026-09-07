---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/system-optimizations.html
---

# System-level optimizations
<a name="system-optimizations"></a>

System optimizations focus on **how the inference serving infrastructure is configured and orchestrated** — independent of the model itself. These techniques operate at the serving engine, cluster, and request-scheduling layers to maximize hardware utilization, reduce latency, and increase throughput.

## Inference Engine Tuning
<a name="inference-engine-tuning"></a>

Modern inference engines like [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang) implement **continuous batching** (iteration-level scheduling) — dynamically admitting and removing requests at every decode step rather than processing fixed batches. As soon as one request completes, a new one fills its slot. This eliminates padding waste and idle GPU time, but shifts tuning from "pick a batch size" to "configure scheduler guardrails" that define capacity limits, memory allocation, and fairness policies.

### Anatomy of Inference Requests
<a name="anatomy-of-inference-requests.658ba498-b895-52b7-96d6-7571d08faf4a"></a>

The diagram below shows how the scheduler works at the iteration level. Each **iteration** (column) is one forward pass processing both prefill tokens (from new requests) and decode tokens (from active requests). Sequences flow through prefill (blue) → decode (green) → complete, with overflow going to queue (gray).

![Continuous batching diagram showing iteration-level scheduling with sequences flowing through prefill (blue) and decode (green) phases, illustrating max_num_seqs concurrency cap and max_num_batched_tokens budget constraints](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/8d042c97-d551-47bb-a1c7-4759054f7687.png)

### Core Parameters and Their Implications
<a name="core-parameters-and-their-implications.a5f34a53-afa7-534a-a494-f03563368b9a"></a>

`max_model_len`** (sequence length limit)**: Sets maximum total tokens (prompt \+ output) per request. This determines per-request KV cache memory consumption. A 128K limit reserves \~256MB per request; an 8K limit reserves \~16MB — allowing 16× more concurrency from the same memory pool. Setting this too high **wastes memory** and **reduces throughput**. Too low causes **hard rejections** (HTTP 400) — the only parameter that fails requests rather than queuing them. **Context impact**: longer sequences also increase prefill/decode latency, though batching mitigates this. Tune to workload P95/P99, not theoretical max. *(vLLM: *`--max-model-len`*, SGLang: *`--context-length`*)*

`gpu_memory_utilization`** (memory allocation fraction)**: Fraction of GPU memory reserved at startup. After model weights and activations (fixed), the remainder becomes the **KV cache pool**. Higher values boost **throughput** by fitting more concurrent requests, but risk **OOM errors** if transient CUDA allocations spike. When KV memory is exhausted, the system **queues new requests** (increased TTFT) or **preempts active ones** by swapping KV cache to CPU or discarding for recomputation (10-100× latency spikes from thrashing). Start at 0.85-0.90; reduce by 0.05 if you see preemption events or OOM crashes. *(vLLM: *`--gpu-memory-utilization`*, SGLang: *`--mem-fraction-static`*)*

`max_num_seqs`** (concurrency cap)**: Maximum requests active simultaneously (prefill \+ decode). Higher values improve **throughput** and GPU utilization but increase **per-request latency** (more contention for compute) and **queuing delays**. Lower values reduce **latency variance** but may **underutilize the GPU** during bursty traffic. Long-context requests consume many KV blocks, so effective concurrency may hit memory limits before this cap. When reached, new requests **queue** (FCFS). *(vLLM: *`--max-num-seqs`*, SGLang: *`--max-running-requests`*)*

`max_num_batched_tokens`** (per-iteration budget)**: Total tokens processed per forward pass. Consumed by prefill tokens (thousands per new request) and decode tokens (1 per active sequence). Effectively a **prefill admission rate limiter**. Higher budgets improve **prefill throughput** (lower TTFT, better GPU utilization), but long prefills can monopolize the GPU and cause **decode stalls** (latency spikes for other requests). Lower budgets prevent stalls but slow prefill. Without chunked prefill, prompts exceeding the budget **queue**. With chunking, they split across iterations. Balance: 4096-8192 tokens. \*(vLLM: `--max-num-batched-tokens`)

### Enabling Chunked Prefill
<a name="enabling-chunked-prefill.b4b9419e-9a8b-56bf-aab2-f030a46a8c35"></a>

**The problem:** A 32K-token prefill processed in one iteration monopolizes the GPU for hundreds of milliseconds, severely limiting concurrent decode operations. Without chunking, decode requests can only advance by **a single token** during the entire prefill, causing decode streams to effectively pause. These **decode stalls** appear as P95/P99 TPOT spikes whenever long-context requests arrive.

**The solution:** Chunked prefill splits long prompts into smaller chunks (configurable, typically 512-8192 tokens) and **prioritizes decode requests between chunks**. Instead of one decode step during an entire prefill, there can now be as many decode steps as there are prefill chunks. In the diagram, Req D's prefill spans iterations 1-2 (4096 \+ 2904 tokens) rather than blocking iteration 1 entirely. The per-iteration token budget (`max_num_batched_tokens`) determines max chunk size: if 200 requests are decoding (200 tokens) and `max_num_batched_tokens=8192`, then 7992 tokens remain for prefill chunks that iteration.

**Why it helps:** Without chunking, long prefills cause complete decode pauses for concurrent requests. Chunking transforms this into **gradual slowdown instead of total blocking**, while maximizing GPU utilization by combining compute-bound (prefill) and memory-bound (decode) work in the same batch. Trade-off: **slight TTFT increase** (chunked prefill has some overhead vs. contiguous prefill) for **major ITL improvement** and **throughput gains** (benchmarks show \+50% token throughput improvement on concurrent workloads). The chunk size provides a tuning knob: smaller chunks prioritize decode fairness; larger chunks (>2048) prioritize throughput.

**When to enable:** Recommended as default for most production deployments with concurrent traffic. The benefits are highest when prefill and decode operations overlap. Disable only for single-user or offline batch scenarios where fairness doesn't matter. \*(vLLM: `--enable-chunked-prefill --max-num-batched-tokens 4096`, SGLang: `--chunked-prefill-size`).

## Parallelism
<a name="parallelism"></a>

Parallelism strategies determine how a model is distributed across multiple GPUs. This is the foundation of your serving architecture — all other optimizations (batching, caching, disaggregation) operate on top of your parallelism topology.

### Parallelism Strategies
<a name="parallelism-strategies.1ff2002b-54b6-5f72-9e40-4feb418edd22"></a>

[**Tensor Parallelism**](https://docs.vllm.ai/en/latest/serving/distributed_serving.html#tensor-parallelism)** (TP)**: Splits each model layer across multiple GPUs. All GPUs work on the same request simultaneously.
+ **Why**: Fits large models in memory, reduces per-request latency
+ **Trade-off**: Requires high-bandwidth interconnects (NVLink/NVSwitch/EFA). More GPUs = more communication overhead.
+ **When**: Model doesn't fit on a single GPU, or you need lower per-request latency
+ **vLLM config**: `--tensor-parallel-size=4` (splits across 4 GPUs)

[**Expert Parallelism**](https://docs.vllm.ai/en/latest/serving/expert_parallel_deployment/)** (EP)**: For Mixture-of-Experts (MoE) models, distributes experts across GPUs.
+ **Why**: MoE models have too many experts to fit all on one GPU
+ **Trade-off**: Only active experts for each token require communication
+ **When**: Serving MoE models (Mixtral, DeepSeek, Qwen MoE)
+ **vLLM config**: `--enable-expert-parallel` (by default, expert layers form a TP group of size DP × TP without this flag)

[**Data Parallelism**](https://docs.vllm.ai/en/latest/serving/data_parallel_deployment/)** (DP)**: Replicates the entire model (or TP/EP group) across multiple independent serving groups. Each DP replica processes its own batch of requests with its own KV cache.
+ **Why**: Scale throughput linearly without affecting per-request latency
+ **Trade-off**: Uses more total GPUs. For dense models, replicas are fully independent (no communication). For MoE models with EP enabled, replicas communicate via AllToAll for expert dispatch/combine.
+ **When**: Single TP/EP group cannot handle your throughput requirements
+ **vLLM config**: `--data-parallel-size=4` (creates 4 independent replicas)

**Combining parallelism strategies**: DP can be layered with TP or EP. Example: `--tensor-parallel-size=2 --data-parallel-size=4` requires 8 GPUs total (4 replicas × 2 GPUs per replica).

**Key insight**: With EP enabled, `EP_SIZE = TP × DP` determines how many GPUs participate in distributing experts. Whole experts are distributed across the EP grid. Attention layer behavior depends on TP: replicated when TP=1, sharded when TP>1. The router/gating network is always replicated (cheap computation, runs independently on each GPU to compute routing decisions before AllToAll). For a detailed comparison of TP vs DP\+EP trade-offs for MoE models, see the [AMD ROCm MoE Playbook](https://rocm.blogs.amd.com/software-tools-optimization/vllm-moe-guide/README.html).

**Example topologies:**
+ **Single-node dense model**: TP=8, DP=1 (8× GPUs in one node)
+ **MoE model (EP only)**: TP=1, DP=8, EP enabled (8× GPU, experts distributed across all 8, attention replicated)
+ **MoE model (EP \+ TP)**: TP=2, DP=4, EP enabled (8× GPU, 4 TP groups of 2 GPUs, experts distributed across all 8, attention sharded within TP groups)
+ **Massive MoE**: TP=1, DP=16, EP enabled (16× GPUs across 2 nodes, experts distributed across all 16, attention replicated)

## KV Cache Management
<a name="kv-cache-management"></a>

The KV cache stores attention key and value tensors for each token processed during inference. As context length grows, KV cache becomes the **dominant variable memory consumer** — often exceeding model weight size. After model weights and activation buffers are allocated (see [Engine Tuning: ](#inference-engine-tuning)`gpu_memory_utilization`), the remainder of GPU memory becomes the **KV cache pool**. How this pool is managed determines how many concurrent requests an endpoint can serve, how efficiently repeated prefixes are handled, and whether long-context workloads fit in memory at all.

This section covers three KV cache optimization strategies:

1. **Prefix caching** — Reuse KV blocks for repeated prompt prefixes

1. **Tiered caching** — Extend cache capacity beyond GPU memory using CPU/disk/remote storage

1. **Cache-aware routing** — Direct requests to instances that already hold relevant KV blocks

### Prefix Caching
<a name="prefix-caching.b1d048ca-f6b0-52dd-817c-a80899bc2130"></a>

Many LLM workloads share prompt prefixes across requests. System prompts, few-shot examples, retrieved documents in RAG pipelines, and conversation histories create repeated prefixes that would otherwise be recomputed for every request.

**Prefix caching** retains KV cache blocks after a request completes and reuses them for subsequent requests with matching prefixes:

1. When a request completes, its KV cache blocks remain in GPU memory instead of being freed

1. New requests are matched against cached prefixes via hash-based lookup

1. If a prefix match is found, the engine skips **prefill** for the matched portion and loads cached KV blocks directly

1. Only the novel suffix (tokens beyond the cached prefix) goes through prefill, which in turn reduces TTFT and improves throughput

**When prefix caching helps most:**
+ RAG pipelines with shared retrieved documents
+ Multi-turn chat with accumulating conversation history
+ Agentic workflows with repeated system prompts and tool definitions
+ Batch evaluation with the same base prompt and different user inputs

**Framework configuration:**

|
|
| Framework | Configuration |
| --- |--- |
| vLLM | `vllm serve model --enable-prefix-caching` |
| SGLang | `python -m sglang.launch_server --enable-prefix-caching` |

**Design consideration:** Prefix caching trades GPU memory (cached KV blocks persist) for compute (skip redundant prefill). In memory-constrained scenarios, cached blocks may be evicted to make room for new requests. Eviction policies are typically LRU (least recently used). The next section addresses this limitation.

### Tiered KV Cache (Offloading Beyond Local GPU Memory)
<a name="tiered-kv-cache--offloading-beyond-local-gpu-memory-.a6dc35e0-6bda-5779-832e-adb4a4d5874c"></a>

GPU memory is finite. Once the KV cache pool is full, the system must evict cached prefixes (reduced cache hit rate). **Tiered caching** extends effective cache capacity by offloading KV blocks elsewhere, such as slower, larger storage tiers:

**How tiered caching works:**
+ **Automatic tiering**: Hot blocks (frequently accessed) stay in GPU memory; warm blocks move to CPU; cold blocks to disk or remote storage based on access patterns
+ **Prefetch hot KV blocks**: The system prefetches the next layer's KV blocks from slower tiers, hiding latency
+ **Cross-request persistence**: KV blocks survive beyond a single request's lifecycle — cached prefixes remain available even after GPU memory is reclaimed for new requests
+ **Cross-worker sharing**: Separate inference engine replicas can share or exchange KV blocks, enabling prefix reuse across instances

**Performance impact:**
+ **Throughput**: improvement for high-reuse workloads (multi-round Q&A, document analysis)
+ **TTFT**: reduction compared to recomputing shared prefixes from scratch
+ **Scale**: Enables caching 100K\+ unique prefixes across CPU/SSD tiers

**Framework integration**

Several tools provide tiered caching capabilities. [LMCache](https://github.com/LMCache/LMCache) is one of them, an open-source library that works with vLLM and SGLang, while NVIDIA Dynamo includes KVBM (KV Block Manager) which is tightly integrated with its disaggregation features (covered in the next section). These capabilities sit between the inference engine and storage tiers, coordinating KV block movement and cross-engine sharing:

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/17f7ea45-bbea-4dbe-8a6f-9bf69d7c53a6.png)

**Deployment example (LMCache with vLLM):**

```
vllm serve Qwen/Qwen3-8B \
    --port 8000 --kv-transfer-config \
    '{"kv_connector":"LMCacheMPConnector", "kv_role":"kv_both"}'
```

**When to use tiered caching:**
+ Long-context workloads where GPU memory cannot hold all active KV caches
+ Multi-replica deployments where cache sharing across instances improves hit rates
+ High-reuse workloads (agentic, multi-turn) where cached prefixes are valuable but expire too quickly from GPU-only storage
+ As a building block for prefill-decode disaggregation (see next section)

**Design trade-off:** Tiered caching adds latency when fetching KV blocks from slower storage (CPU: \~10ms, SSD: \~100ms). I/O pipelining and batched operations reduce this overhead. For workloads with low prefix reuse, the latency cost may outweigh throughput gains.

### Cache-aware Request Routing
<a name="cache-aware-request-routing.de9fd72d-5eef-5c17-b848-208ae2c9205e"></a>

In multi-replica deployments, naive routing strategies (round-robin, least-loaded, least-requests) ignore KV cache locality. Requests with shared prefixes may land on different replicas, causing cache misses and redundant prefill computation. **Cache-aware routing** directs requests to instances that already hold relevant KV blocks.

**How it works:**

1. The router maintains metadata about which KV blocks reside on which instances

1. Incoming requests are hashed based on their prefix

1. Requests are routed to instances that already hold their prefix KV blocks, also taking into account GPU load.

**Performance impact:**

In workloads with high prefix reuse (e.g., same system prompt across thousands of requests), cache-aware routing increases effective cache hit rates translating to TTFT reductions.

**Framework support:**

|
|
| Framework/Service | Support |
| --- |--- |
| Amazon SageMaker Hyperpod | Managed [Tiered KV Cache and Intelligent Routing](https://aws.amazon.com/blogs/machine-learning/managed-tiered-kv-cache-and-intelligent-routing-for-amazon-sagemaker-hyperpod/) using HyperPod's Inference Operator |
| NVIDIA Dynamo | Cache-aware routing (considers KV locality and GPU load in scheduling) |
| llm-d | Native cache-aware routing via intelligent scheduler |
| LMCache | Exposes APIs for custom routers to query KV block locations across replicas |

**Design consideration:** Cache-aware routing works best when request distributions are non-uniform. If all requests are unique, routing overhead adds latency without benefit. Monitor cache hit rates before deploying.

## Prefill-Decode Disaggregation
<a name="prefill-decode-disaggregation"></a>

LLM inference consists of two phases with opposing resource profiles: **prefill** (compute-bound, parallel processing of the input prompt) and **decode** (memory-bandwidth-bound, sequential token generation). In traditional colocated serving, both phases share the same GPU, causing interference — large prefills block decode steps for other requests, while decode underutilizes compute capacity. **Disaggregation** separates prefill and decode into independent pools, each optimized for its phase's resource profile.

### Phase Characteristics
<a name="phase-characteristics.23d4b5f9-0303-58a9-8859-ecd13b5dd7a6"></a>

|
|
| Phase | Bottleneck | Resource need | Duration | Behavior |
| --- |--- |--- |--- |--- |
| **Prefill** | Compute-bound | High FLOPS (tensor cores) | Short burst per request | Parallel, bursty |
| **Decode** | Memory-bandwidth-bound | High memory bandwidth | Long tail (one token at a time) | Sequential, sustained |

In colocated serving, this mismatch creates decode stalls (prefill blocks other requests), compute underutilization (decode cannot saturate tensor cores), and inability to scale each phase independently.

### When to Use Disaggregation
<a name="when-to-use-disaggregation.25fadfb9-93a2-5eb8-a6e8-bf7f5b2c9ca9"></a>

Disaggregation adds architectural complexity (separate pools, KV transfer overhead, routing logic) and typically doubles GPU count. Use this decision framework:

|
|
| Factor | Use Disaggregation |
| --- |--- |
| **Model size** | Large models (70B\+) where prefill causes noticeable decode stalls |
| **I/O ratio** | Imbalanced (reasoning/code gen with long outputs, or RAG with long input) |
| **Latency requirements** | Cannot tolerate decode latency spikes from concurrent prefills |
| **Concurrency** | High concurrency where interference is severe |

How Disaggregation Works

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/80e3a1e5-b0e7-4fed-8457-6e2b2a3eab15.png)

**Request flow:**
+ Router directs incoming request to prefill worker (optimized for compute)
+ Prefill worker processes full prompt, generating KV cache
+ KV cache transfers to decode worker via high-speed interconnect (NVLink/NVSwitch for intra-node, RDMA over [AWS EFA ](https://aws.amazon.com/hpc/efa/)for inter-node)
+ Decode worker generates output tokens autoregressively using transferred KV cache
+ Response streams back to user from decode worker

**Encode-Prefill-Decode (EPD) disaggregation for Vision Language Models**: VLMs add a compute-intensive **encoding** phase before prefill, where vision encoders process images or video frames into embeddings. EPD (Encoder-Prefill-Decode) disaggregation extends the two-pool architecture to three specialized pools: an encoder pool processes visual inputs, transfers embeddings to the prefill pool (which combines them with text tokens to generate KV cache), then KV cache transfers to the decode pool for token generation. This isolates vision workload from text processing, enables hardware specialization (vision-optimized accelerators for encoding, LLM-optimized GPUs for text), and allows independent scaling of encoder capacity for vision-heavy workloads.

### Performance Impact
<a name="performance-impact.214abb85-14c6-5fb1-8ccd-c74776fd1f75"></a>

Disaggregation delivers several performance benefits. **Independent scaling** allows you to scale prefill and decode pools separately based on workload characteristics — add prefill capacity for long-input workloads or decode capacity for long-output scenarios without overprovisioning the other phase. **Hardware specialization** enables matching hardware to phase requirements: prefill pools use compute-optimized instances with high FLOPS (dense tensor cores), while decode pools use memory-bandwidth-optimized instances with high HBM bandwidth. **Eliminated interference** means decode latency is no longer impacted by concurrent prefill operations, delivering consistent TPOT across all active requests and substantially reducing P99 latency. **Higher utilization** comes from each pool running only the workload it's optimized for, eliminating the underutilization that occurs when a single GPU switches between compute-bound and memory-bound phases.

These gains are most pronounced when prefill and decode have very different resource profiles, such as reasoning models with long generation, long-context RAG with short outputs, or agentic workflows with high token amplification.

### KV Cache Transfer: NIXL
<a name="kv-cache-transfer--nixl.88709768-92fb-5f6e-ae97-6122396d0947"></a>

Disaggregated serving requires efficient KV cache transfer between prefill and decode pools. [**NIXL (NVIDIA Inference Xfer Library)**](https://github.com/ai-dynamo/nixl) provides zero-copy, GPU-direct transfers using high-speed interconnects:
+ **Intra-node**: NVLink/NVSwitch for GPU-to-GPU transfers within a single node
+ **Inter-node**: RDMA over high-bandwidth fabrics (AWS Elastic Fabric Adapter)

NIXL is used by frameworks like NVIDIA Dynamo and llm-d to transfer KV cache blocks without CPU involvement, minimizing latency overhead.

**Disaggregated Serving Examples:**
+ **Amazon Sagemaker HyperPod: **Managed disaggregated serving with vLLM using the HyperPod Inference Operator.
+ **NVIDIA Dynamo**: Orchestration layer above vLLM/SGLang with dynamic GPU scheduling and NIXL transport
+ **llm-d**: Kubernetes-native framework with NIXL over EFA for AWS deployments ([SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/introducing-disaggregated-inference-on-aws-powered-by-llm-d/), EKS)

For detailed deployment guides, see [NVIDIA Dynamo documentation](https://docs.nvidia.com/dynamo/v-0-7-1/design-docs/disaggregated-serving) and [Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/disaggregated-prefill-and-decode-for-llm-inference-on-sagemaker-hyperpod/).
