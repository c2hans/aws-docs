---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/system-optimizations.html
---

# System-level optimizations
<a name="system-optimizations"></a>

Beyond instance selection and scaling, the following system-level optimizations can improve inference efficiency, reduce latency, and increase throughput:
+ **Routing and load balancing** - Efficient request routing ensures balanced utilization across GPUs and instances. Common strategies include:
  + **Round-robin routing** for even distribution of independent requests.
  + **Session-aware routing** to keep user conversations on the same instance, preserving KV cache locality.
  + **Latency-aware routing** to send requests to the least-loaded instance for reduced queueing delay.
+ **Throughput and latency** - Batch size is one of the primary levers for tuning performance. Smaller batches favor low latency, while larger batches improve throughput. Optimal settings depend on workload characteristics (for example, interactive chat or batch inference).
+ **Prefix caching** - Caching identical prompt prefixes avoids redundant compute and decoding, significantly lowering latency for repeated queries. This approach is especially effective in applications with high overlap in user prompts. Frameworks such as vLLM (`PagedAttention`), Text Generation Inference (TGI), SGLang, and `Llama.cpp` natively support prefix caching.
+ **Chunked prefill** - Large context inputs can stall GPUs during prefill. Splitting prefill into smaller chunks reduces idle decoding cycles, improving utilization for long-sequence workloads.
+ **Continuous batching** - Continuous batching dynamically groups incoming requests, prioritizing memory I/O and compute to maximize throughput while keeping latency within acceptable bounds. This approach prevents resource underutilization when request patterns are uneven.
+ **Sequence size tuning** - Right-sizing the maximum sequence length reduces unnecessary computation for workloads that rarely need the full context window. This tuning balances memory footprint, throughput, and latency.
