---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/right-sizing-and-auto-scaling.html
---

# Right-sizing and auto-scaling an inference system
<a name="right-sizing-and-auto-scaling"></a>

Fundamental to designing an inference system is the selection of the underlying compute infrastructure and the policies for dynamically scaling it based on inference demand.

## Selecting Amazon EC2 instance types and instance count
<a name="selecting-ec2-instance-types"></a>

Choosing a suitable Amazon Elastic Compute Cloud (Amazon EC2) instance type is the first step in right-sizing infrastructure for a given model. EC2 instance types provide a flexible choice of GPUs, CPUs, and custom chips like AWS Inferentia and AWS Trainium. The instance type and count on a given instance constrains the throughput compute and memory that is available for hosting the model.

Model memory requirements should be satisfied by the available high-bandwidth memory on each individual instance (for example, using multiple GPUs through tensor parallelism). Model compute requirements can be split among multiple instances that serve multiple copies of the model. These instances are fronted by an inference API server that routes requests to individual instances. An example of a compute requirement is the required Requests per Second (RPS).

Inference memory requirements are mainly driven by model parameters and key-value (KV) cache size. You can estimate the memory requirements for model parameters based on the parameter count and the numerical precision of the weights. The following table shows approximate memory requirements for model parameters at a given precision for popular model sizes.

|
|
| Model size (parameters) | 16-bit | 8-bit | 4-bit |
| --- |--- |--- |--- |
| 7B | 14 GB | 7 GB | 3.5 GB |
| 13B | 26 GB | 13 GB | 6.5 GB |
| 70B | 140 GB | 70 GB | 35 GB |

The memory requirements for KV cache scale roughly linearly with the number of tokens in the context length, the batch size (for example, multiple users), and the number of attention heads. They also depend on the numerical precision used to store the cache. If multiple users are using the same endpoint on a given GPU, this will additionally scale the memory requirements. Several calculation tools can estimate the KV cache size for open source models, for example, [Hugging Face](https://huggingface.co/spaces/gaunernst/kv-cache-calculator) and [lmcache.ai](https://lmcache.ai/kv_cache_calculator.html). As a rough rule of thumb, the KV cache can take up memory on the same order as the model weights themselves (often approximately 50% but can be higher for long contexts).

Most modern inference backends support tensor parallelism, which distributes the model parameters and KV cache across multiple GPUs on the same node. For example, a p5.48xlarge instance has 8× H100 GPUs, each with 80 GB of memory, for a total of 640 GB. This approach allows inference on models whose parameters and KV cache exceed the memory of a single GPU. The tradeoff is some synchronization overhead due to cross-GPU communication.

Inference compute requirements are mainly driven by the size and architecture of the model and the workload characteristics (for example, concurrent requests, acceptable latency, and sequence length). Primary indicators for the capability of an inference setup are Requests per Second (RPS) for throughput and Time to First Token (TTFT) for latency. Based on the use case requirements (for example, number of concurrent users), these indicators can be used to estimate the required number of GPUs and instances. Following are two main options to deduct the achievable throughput and latency based on a given model and use case:
+ If the model is a (potentially fine-tuned) popular open source model, throughput benchmark results for popular GPU and instance types are available on websites such as [artificialanalysis.ai](https://artificialanalysis.ai/benchmarks/hardware). Throughput benchmark results for several Llama, Mistral, and Falcon models are available in [Benchmark and optimize endpoint deployment in Amazon SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/benchmark-and-optimize-endpoint-deployment-in-amazon-sagemaker-jumpstart/) (AWS Blog).
+ If the model is heavily customized or the GPU choices are not included in public benchmarks, individual benchmarks can be performed using open source tools such as [LLMPerf](https://github.com/ray-project/llmperf) and the [vLLM](https://github.com/vllm-project/vllm/tree/main/benchmarks) benchmark suite.

The throughput metric RPS depends heavily on the specific requests that were used within the benchmark. Popular benchmarking datasets such as [ShareGPT](https://huggingface.co/datasets/RyokoAI/ShareGPT52K) are based on real user conversations and can approximate real-world workloads.

Although we generally recommend accelerated computing instance types (Inf, Trn, G and P [instance families](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html)) for most inference use cases, CPU-based instances can be cost-effective for inference with smaller quantized models.

## Configuring auto-scaling policies
<a name="configuring-auto-scaling-policies"></a>

After the baseline infrastructure setup is defined, auto-scaling ensures capacity adjusts dynamically with demand. This approach helps to ensure both sufficient capacity to meet latency and throughput requirements and effective resource utilization, minimizing idle infrastructure costs.

Gen AI inference systems typically use horizontal scaling (adding or removing instances) in contrast to vertical scaling (adjusting instance types or GPU utilization).

Scaling strategies can generally be classified as reactive (based on the current load on the system) and scheduled (for workloads with predictable temporal patterns). Both strategies can be combined, depending on the use case specifications.

Auto-scaling policies rely on metrics that reflect the load of the inference system. Common metrics include:
+ **Requests per Second **- Tracking RPS against the maximum tested throughput per instance type (see the previous section) helps maintain predictable performance.
+ **KV Cache Usage** - Average key-value cache utilization across instances indicates that GPUs are saturated and additional instances might be required.
+ **Request Queue Length** or **Pending Requests** – A growing request queue indicates demand is exceeding available throughput. This metric correlates directly with user-facing latency.

AWS provides multiple approaches for implementing auto-scaling, depending on the chosen inference service:
+ Amazon Bedrock provides fully managed and automatic scaling of the inference capacity for both publicly available foundation models and models imported through [Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html). No manual setup is required.
+ Amazon SageMaker [endpoint auto scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html) provides fully managed scaling based on configurable thresholds on invocation metrics as well as custom CloudWatch metrics such as CPU utilization.
+ [Amazon SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-autoscaling.html) and inference setups based on Amazon EKS can use Kubernetes-based auto scaling functionality through KEDA and Karpenter.
+ [Amazon ECS Managed Instances](https://aws.amazon.com/ecs/managed-instances/) provides flexible cost-effective auto-scaling for inference workloads.

There are two primary challenges with auto-scaling setups:
+ **Cold start latency** - Scale-out events have latency due to instance provisioning, container image pull, and model weight loading.
+ **Capacity availability** - Depending on the AWS Region, the desired instance types can experience varying levels of availability, increasing latency in scale-out events or even prohibiting them during certain periods.
