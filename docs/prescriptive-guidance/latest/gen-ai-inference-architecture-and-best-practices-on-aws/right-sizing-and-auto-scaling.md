---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/right-sizing-and-auto-scaling.html
---

# Right-sizing and auto-scaling an inference system
<a name="right-sizing-and-auto-scaling"></a>

Fundamental to designing an inference system is the selection and sizing of the underlying compute infrastructure and the policies for dynamically scaling it based on inference demand and inference service-level objectives (SLOs) like end-to-end latency or time to first token (TTFT). We recommend the following steps for right sizing and scaling.

## 1. Define the Workload
<a name="untitled"></a>

The first step in sizing an inference system is defining the workload requirements. Inference performance is highly dependent on the characteristics of the requests being processed. Two deployments serving the same model can require significantly different infrastructure depending on factors such as prompt length, response length, concurrency, and latency objectives.

Before selecting an accelerator or estimating instance count, gather the following workload characteristics:

### Model characteristics
<a name="model-characteristics.db8140d1-8516-5183-ab15-3fb3fe6f5cf9"></a>

The model architecture and parameter count have a significant impact on both memory requirements and computational throughput. Examples include:
+ Llama 3.3 70B
+ Mistral Small 24B
+ Qwen3 32B
+ Gemma 3 27B

In addition to model size, the numerical precision used for inference should also be identified. Common formats include FP16, FP8, INT4, and NVFP4. Lower-precision deployments can reduce memory requirements and improve throughput.

### Request characteristics
<a name="request-characteristics.15278936-dcf7-509f-9403-035b2c03acbb"></a>

Inference workloads should be described using both input and output token lengths. Key metrics include:
+ Average input tokens per request
+ Average output tokens per request
+ Peak input tokens
+ Peak output tokens

For example, a use case deploying a chatbot might observe requests averaging 500 input tokens and 200 output tokens. A document-processing workload may instead receive prompts containing several thousand input tokens with relatively short responses. Input and output token lengths directly influence latency, throughput, and memory consumption.

### Concurrency requirements
<a name="concurrency-requirements.4147bb74-b332-5566-8cd3-02c443c73c46"></a>

The number of requests processed simultaneously is one of the most important inputs for sizing an inference system. Concurrency is typically expressed as:
+ Concurrent users
+ Concurrent requests
+ Requests per second (RPS)
+ Requests per minute (RPM)

For example, an application serving 500 active users may only process a small number of concurrent requests if user interactions are infrequent. Conversely, batch-processing workloads can generate sustained high concurrency despite having relatively few users.

### Latency objectives
<a name="latency-objectives.9445fea0-95de-5f96-84e0-2012e91e44dc"></a>

Performance requirements should be defined before infrastructure selection. Common metrics include:
+ Time to First Token (TTFT)
+ End-to-end response latency (E2E)
+ Maximum acceptable queueing delay

|
|
| Metric | Target |
| --- |--- |
| TTFT | < 1 second |
| E2E | < 5 seconds |
| Queueing delay | < 500 ms |

These objectives determine the amount of infrastructure required and influence the choice of accelerator.

### Availability and scaling requirements
<a name="availability-and-scaling-requirements.35f4e275-e854-5aa7-82b6-5d0e75044a98"></a>

Workloads often exhibit varying demand throughout the day. Understanding expected traffic patterns helps determine whether static provisioning or auto scaling is appropriate.

Consider:
+ Average utilization
+ Peak utilization
+ Daily traffic patterns
+ Seasonal demand spikes
+ Recovery requirements during infrastructure failures

### Example workload definition
<a name="example-workload-definition.ad9e6fdc-8936-541f-b05e-7ecf64240b6c"></a>

The following example captures the minimum information required to begin a sizing exercise:

|  |  |
| --- |--- |
| Parameter | Value |
| Model | Mistral Small 24B |
| Precision | FP8 |
| Average input length | 2,000 tokens |
| Average output length | 500 tokens |
| TTFT target | < 1 second |
| End-to-end latency target | < 5 seconds |

Once these requirements are established, the next step is determining whether the model and associated KV memory fit within the available accelerator memory and identifying the instance types capable of meeting the required throughput and latency objectives.

## 2. Memory Sizing: Can the Model Fit?
<a name="2-memory-sizing-can-the-model-fit"></a>

After the workload requirements have been defined, the next step is determining whether the model can fit within the memory available on a given instance with one or more accelerators.

Memory sizing establishes the set of viable instance size options before throughput and latency considerations are evaluated. If the model and its associated runtime memory requirements exceed the available memory on an instance, that instance cannot be used regardless of its computational performance. Inference memory consumption is primarily driven by three components:
+ Model weights and activations
+ Key-value (KV) cache
+ Runtime overhead

### Model weights
<a name="model-weights.d4d4234c-5f28-549c-a243-c6d2fa281f9f"></a>

The model weights are typically the easiest component to estimate. Memory requirements depend on the model parameter count and the numerical precision used during inference.

The following table shows approximate memory requirements for storing model parameters:

|
|
| Model Size | FP16 | FP8 / INT8 | INT4 / NVFP4 |
| --- |--- |--- |--- |
| 7B | 14 GB | 7 GB | 3.5 GB |
| 13B | 26 GB | 13 GB | 6.5 GB |
| 70B | 140 GB | 70 GB | 35 GB |

As an example, a 70B parameter model deployed in FP8 requires approximately 70 GB of memory for the model weights alone, exceeding the memory available on a single L40s GPU with 48 GB of High Bandwidth Memory (HBM). Thus, we either need to shard the model across more than one GPU or choose a GPU with a larger HBM like H100 or B200.

### KV cache
<a name="kv-cache.e471526a-769b-5369-aaea-c065ef723bc1"></a>

For many production deployments, the KV cache becomes a significant — sometimes dominant — contributor to total memory consumption. The KV cache stores the **Key** and **Value** tensors from attention layers for previously processed tokens, allowing autoregressive models to generate responses efficiently without recomputing attention over the entire sequence at each step. KV cache requirements scale approximately linearly with:
+ Input context length
+ Output length
+ Concurrent requests (batch size)
+ Number of KV heads and layers
+ Head dimension (`hidden_size / num_attention_heads`)
+ KV cache precision (e.g., 2 bytes for FP16, 1 byte for FP8)

The total KV cache memory can be calculated as:

```
KV cache = 2 × kv_dtype × num_layers × num_kv_heads × head_dim × context_length × batch_size
```

As a result, two deployments serving the same model may require dramatically different memory footprints. For example, using Mistral-7B (GQA, 8 KV heads, 32 layers, head\_dim 128, bf16):

|
|
| Workload | Context Length | KV Cache (1 request) | KV Cache (4 concurrent) |
| --- |--- |--- |--- |
| Interactive chatbot | 1,000 tokens | 0.12 GB | 0.49 GB |
| Document analysis | 16,000 tokens | 1.95 GB | 7.81 GB |

Although the model weights remain identical, the second workload can require several times more memory due to KV cache growth.

### Model Sharding
<a name="model-sharding.58d3cfcc-1e52-5b77-a425-3c904ee4c71d"></a>

Many models exceed the memory capacity of a single accelerator. Sharding the model using techniques like tensor parallelism distributes model weights and KV cache across multiple GPUs within the same node, allowing larger models to be served without reducing context length or quantization precision.

Examples include:

|
|
| Model | Typical Deployment |
| --- |--- |
| Llama 8B FP16 | Single GPU |
| Mistral Small 24B FP16 | Single GPU or multi-GPU |
| Llama 70B FP16 | Multi-GPU |
| Frontier-scale models | Multi-GPU and multi-node |

The primary tradeoff is increased communication overhead between GPUs, which can impact latency and throughput depending on the interconnect technology. For more information about sharding techniques, go to the model optimization section.

### Accelerator eligibility
<a name="accelerator-eligibility.108a8384-4ae8-5e90-9e4b-797509005ac2"></a>

After estimating model weights and KV cache requirements, the total memory footprint can be compared against available instance types.

For example:

|
|
| AWS Instance Family | NVIDIA Accelerator | Memory |
| --- |--- |--- |
| g6 | L4 | 22 GB |
| g6e | L40S | 44 GB |
| g7e | RTX PRO™ 6000 Blackwell | 96 GB |
| p5 | H100 | 80 GB |
| p5en | H200 | 141 GB |
| p6-b200 | B200 | 180 GB |
| p6-b300 | B300 | 268 GB |

This step establishes the set of viable accelerator options before performance benchmarking begins. A deployment requiring 90 GB of memory immediately eliminates single-GPU g6, g6e and p5 instances as candidates, regardless of their throughput characteristics.

Once viable accelerators have been identified based on memory requirements, the next step is determining whether they can meet the workload's latency and throughput objectives.

## 3. Latency and Throughput sizing for given service requirements
<a name="throughput-sizing-can-the-model-meet-the-sla"></a>

After identifying the instances capable of hosting the model, the next step is determining whether they can satisfy the workload's latency and throughput objectives. Unlike memory sizing, which determines whether a deployment is possible, throughput sizing determines whether a deployment is practical. A model may fit comfortably on an accelerator while still failing to meet the required Time to First Token (TTFT), response latency, or throughput targets.

As a result, benchmark results should always be interpreted within the context of the workload shape that produced them. As explained in the "How AI Inference works" section, large language model inference consists of two distinct phases:

1. Prefill

1. Decode

Each phase places different demands on the underlying hardware and contributes differently to overall application performance. The most common metrics used during throughput sizing include:

|
|
| Metric | Description |
| --- |--- |
| TTFT | Time to First Token |
| TPS | Generated tokens per second |
| End-to-end latency | Total request completion time |
| Concurrent requests | Requests served simultaneously |
| Requests per second (RPS) | Sustained throughput at a given workload shape |

No single metric is sufficient on its own. For example, an accelerator may deliver excellent aggregate throughput while producing unacceptable TTFT under high concurrency. Similarly, an accelerator may achieve excellent TTFT for individual requests while failing to support the required throughput.

### Benchmarking representative workloads
<a name="benchmarking-representative-workloads.b41d9002-56be-51a1-8be7-484396770ee7"></a>

Throughput sizing should always be based on workload shapes that resemble production traffic. When evaluating instance types, benchmark configurations should include:
+ Representative input lengths
+ Representative output lengths
+ Expected concurrency levels
+ Production inference backend
+ Intended quantization level

For example:

|
|
| Parameter | Value |
| --- |--- |
| Model | Mistral Small 24B |
| Precision | FP8 |
| Input Tokens per request | 2,000 |
| Output Tokens per request | 500 |

The resulting benchmark provides a realistic estimate of the latency and throughput that can be expected in production.

### From performance measurements to accelerator selection
<a name="from-performance-measurements-to-accelerator-selection.baa4d285-ee97-5bd7-97fb-3e07ddfad066"></a>

Once benchmark results are available, candidate instance types can be compared using workload-specific metrics such as TTFT, TPS, and RPS. This comparison enables selection of the accelerator that satisfies both the latency objectives and throughput requirements established in the workload definition phase. The next section discusses how to use these performance measurements to select the most appropriate accelerator and estimate the number of accelerators required to support production traffic.

## 4. Instance Selection and Sizing Framework
<a name="untitled"></a>

After confirming that a model fits within the available instance HBM and evaluating throughput requirements, the next step is selecting the accelerator that provides the required performance at the lowest practical cost. The goal is to identify the lowest-cost accelerator that satisfies the application's service-level objectives (SLOs).

### Compare cost-performance efficiency
<a name="compare-cost-performance-efficiency.7320f155-aff8-5788-b4cf-34b17f7b75e7"></a>

Multiple accelerators frequently satisfy both memory and performance requirements. In these situations, cost becomes the primary decision factor. Rather than selecting the accelerator with the highest benchmark result, compare performance relative to infrastructure cost. Example:

|
|
| NVIDIA Accelerator | Relative Throughput | Relative Cost |
| --- |--- |--- |
| L4 | 1.0x | 1.0x |
| L40S | 2.5x | 1.7x |
| H100 | 3.5x | 3.0x |
| H200 | 3.8x | 3.5x |

Although H200 may deliver the highest absolute performance, L40S may provide the best cost-performance ratio for many medium-sized models.

### Estimating accelerator count
<a name="estimating-accelerator-count.aff78e67-a6e6-5336-bb1e-e78a39fac732"></a>

Once the instance type has been selected based on memory fit and benchmark performance, the next step is determining how many instances are required to support expected production traffic. Express expected production demand using metrics such as:
+ Peak concurrent requests
+ Peak requests per second
+ Expected user growth
+ Total token throughput

Compare the measured throughput of candidate instances against expected workload demand. For example, if a workload requires approximately 3,000 tokens per second during peak periods:

|
|
| Instance | Throughput | Estimated Count |
| --- |--- |--- |
| G6e (L40S) | 800 tokens/s | 4 |
| P5 (H100) | 1,500 tokens/s | 2 |
| P5en (H200) | 1,650 tokens/s | 2 |

Ideally, production deployments include additional capacity beyond the calculated minimum to accommodate traffic spikes, uneven request distribution, infrastructure failures, and future growth.

### Using public benchmarks for initial sizing
<a name="using-public-benchmarks-for-initial-sizing.d3e614f8-c3d5-57e2-a3e8-ae54d3a960e0"></a>

Benchmarking every instance configuration is often impractical during early architecture design. Public benchmarks from vendor publications, model providers, and benchmark repositories provide useful starting points for narrowing candidate instances and estimating initial capacity. However, results obtained under different workload shapes, quantization strategies, or serving frameworks are not directly comparable.

#### Benchmarking tools and datasets
<a name="benchmarking-tools-and-datasets.df9f03e2-b4d3-560f-8cc1-ee8947cac9a6"></a>

Amazon SageMaker AI supports [optimized generative AI inference recommendations](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-now-supports-optimized-generative-ai-inference-recommendations/), a capability that eliminates manual optimization and benchmarking to deliver optimal inference performance. Instead of manually testing combinations of GPU instance types, serving containers, parallelism strategies, and optimization techniques, you provide your model and workload requirements, and SageMaker AI returns validated, deployment-ready configurations with real performance metrics.

Other common tools include [vLLM benchmark suite](https://docs.vllm.ai/en/latest/benchmarking/), [LLMPerf](https://github.com/ray-project/llmperf), [NVIDIA AIPerf, ](https://github.com/ai-dynamo/aiperf)and custom load-testing frameworks ([Locust](https://locust.io/), [JMeter](https://jmeter.apache.org/)). Use synthetic workloads for repeatability and comparison, or production-derived workloads for realistic performance estimates.

#### Common benchmarking pitfalls
<a name="common-benchmarking-pitfalls.c040f9ad-a1a7-5549-8d65-6091aba1d8c6"></a>
+ Comparing benchmarks with different workload shapes
+ Evaluating only single-request performance
+ Focusing exclusively on throughput while ignoring TTFT or E2E latency
+ Assuming public benchmarks will exactly match your production performance

## 5. Auto Scaling and Capacity Management
<a name="5-auto-scaling-and-capacity-management"></a>

After determining the baseline instance count required to satisfy performance objectives, the final step is designing a strategy for handling variations in workload demand. Auto scaling enables inference capacity to adjust dynamically as traffic increases or decreases. This helps maintain latency objectives during peak demand while reducing infrastructure costs during periods of lower utilization.

### Establishing baseline capacity
<a name="establishing-baseline-capacity.2bd74451-1fee-5b0b-9dd5-baf8aa6249d6"></a>

Before configuring auto scaling, a minimum deployment size should be established.

This baseline capacity should be sufficient to:
+ Meet expected steady-state traffic
+ Maintain target latency objectives
+ Tolerate individual accelerator or instance failures
+ Absorb short-term traffic fluctuations

Auto scaling should be viewed as a mechanism for handling changes in demand rather than replacing baseline capacity planning.

### Horizontal scaling
<a name="horizontal-scaling.1d1c1d83-d3f5-5e21-a09d-bd515d2fc33f"></a>

Most inference deployments scale horizontally by adding or removing accelerator-backed instances.

Horizontal scaling offers several advantages:
+ Increased throughput capacity
+ Improved resilience
+ Simplified operational management
+ Independent scaling of inference replicas

### Selecting scaling metrics
<a name="selecting-scaling-metrics.700dbb15-5e34-54bc-8ef4-321050202562"></a>

The effectiveness of an auto-scaling strategy depends heavily on the metrics used to trigger scaling actions. Traditional infrastructure metrics such as CPU utilization often provide limited visibility into inference workload saturation. Instead, scaling decisions should be driven by metrics that more closely reflect user experience and system capacity.

Common examples include:
+ Requests per second (RPS)
+ Concurrent requests
+ Request queue length
+ Pending requests
+ Time to First Token (TTFT)
+ KV cache utilization
+ Token throughput per node

### Request queue length
<a name="request-queue-length.7ead13de-d104-57e0-a2f3-94da1c4392a9"></a>

Queue depth is often one of the most useful indicators of insufficient capacity.

When incoming traffic exceeds the system's processing capability, requests begin accumulating in a queue before inference starts.

A growing queue typically indicates:
+ Insufficient throughput capacity
+ Increasing user-facing latency
+ Need for additional accelerators

Queue-based scaling policies often provide a direct relationship between scaling actions and user experience.

### Latency-driven scaling
<a name="latency-driven-scaling.289adcb9-de41-5451-9104-265ff388db6a"></a>

For interactive applications, latency metrics may provide better scaling signals than resource utilization.

Examples include:
+ Time to First Token (TTFT)
+ End-to-end request latency
+ P95 response latency
+ P99 response latency

If latency exceeds predefined thresholds, additional capacity can be provisioned before user experience degrades significantly.

### KV cache utilization
<a name="kv-cache-utilization.1906faf8-770e-560d-af7e-50d770305660"></a>

Even though techniques like KV cache offloading and KV cache aware routing have emerged to maximize cache hits and the KV cache memory space. Inference workloads can still be scaled based on KV cache utilization when it reaches a high threshold. Monitoring KV cache utilization can help identify situations where additional replicas are required to add more HBM.

### Scaling response time considerations
<a name="scaling-response-time-considerations.e92fd675-779a-5733-add7-6deb6a86c07b"></a>

Unlike stateless web services, inference systems frequently require significant time to scale. Scale-out operations may involve:
+ Instance provisioning
+ Container startup
+ Model weight loading
+ CUDA Graph capture
+ KV cache initialization
+ Framework startup

Depending on model size and infrastructure configuration, these activities may take several minutes. Scaling policies should therefore be configured to react before capacity becomes exhausted.

### Reducing Scale-Out and Cold Start Latency
<a name="reducing-scale-out-and-cold-start-latency.fca718df-4ee6-52c6-952a-823ebd1e70fb"></a>

Auto scaling responsiveness can often be improved by reducing the time required to bring new inference replicas into service. Common techniques include:
+ Reducing container image download time through [container caching in SageMaker AI](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling/)
+ Accelerate container image pull (for example, [SOCI parallel pull and unpack on Amazon EKS](https://aws.amazon.com/blogs/containers/introducing-seekable-oci-parallel-pull-mode-for-amazon-eks/) and [Amazon ECR VPC endpoints](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html))
+ Using faster storage options for storing or caching model checkpoints and container images like local NVMe or high-performance file system like [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/)
+ Leverage model weight transfer across nodes (for example, peer-to-peer model transfer with [ModelExpress](https://github.com/ai-dynamo/modelexpress))
+ Using [Amazon S3 VPC endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) and [Run:ai Model Streamer](https://github.com/run-ai/runai-model-streamer) to accelerate model download when retrieving model artifacts over the network

### Scheduled scaling
<a name="scheduled-scaling.05134bac-2b21-57f4-8114-b8663b6e3863"></a>

Some workloads exhibit predictable demand patterns.

Examples include:
+ Business-hour traffic
+ Batch processing windows
+ Regional usage peaks
+ Periodic reporting workloads

In these situations, scheduled scaling can complement reactive scaling policies by proactively increasing capacity before demand rises.

### Capacity availability considerations
<a name="capacity-availability-considerations.793c32e7-8b46-5b32-b6cf-9efc726b5f2a"></a>

Auto scaling assumes that additional accelerator capacity can be provisioned when required.

In practice, accelerator availability may vary depending on:
+ Region and Availability Zone
+ Accelerator type
+ Account quotas for [EC2](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-quotas.html) and [SageMaker AI](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html#limits_sagemaker)
+ Purchase options (On-demand, [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html), Spot, [ML Capacity Blocks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html), [SageMaker Flexible Training Plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html), [Saving Plans](https://aws.amazon.com/savingsplans/compute-pricing/))

Workloads with strict availability requirements should consider maintaining additional baseline capacity rather than relying entirely on reactive scaling.

### Managed scaling options
<a name="managed-scaling-options.676df1a4-3ea5-5bbd-8b5f-0f9647cd3afe"></a>

AWS provides several approaches for implementing inference auto scaling.

Examples include:
+ Amazon SageMaker [endpoint auto scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)
+ Amazon EKS and SageMaker HyperPod with [KEDA](https://keda.sh/) and [Karpenter](https://karpenter.sh/)
+ Amazon EKS Auto Mode
+ Amazon ECS managed scaling and ECS Managed Instances

The appropriate option depends on the deployment architecture and operational requirements.
