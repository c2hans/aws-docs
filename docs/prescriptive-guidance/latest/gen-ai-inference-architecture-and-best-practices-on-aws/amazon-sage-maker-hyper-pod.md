---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/amazon-sage-maker-hyper-pod.html
---

# Amazon SageMaker HyperPod
<a name="amazon-sage-maker-hyper-pod"></a>

## Amazon SageMaker HyperPod
<a name="amazon-sagemaker-hyperpod.6a09dca9-0adf-5419-b848-26b704f20637"></a>

[Amazon SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-setup.html) with Amazon EKS orchestration enables large-scale, distributed model inference with enterprise-grade orchestration capabilities. It enables organizations to deploy, scale, and optimize foundation models with production reliability across the full model lifecycle from training to inference on a single unified compute infrastructure.

### Infrastructure management
<a name="infrastructure-management.e9c1d966-d66f-5c5d-b03d-0b9967009a82"></a>

SageMaker HyperPod manages GPU and Trainium ML instances with automatic node replacement and deep health checks, while Amazon EKS provides Kubernetes orchestration with workload scheduling and namespace isolation. The [HyperPod Inference Operator](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment.html)—installed as an EKS Add-on or via Helm—automates model deployment, autoscaling, observability, routing, and lifecycle management through two Custom Resource Definitions (CRDs): `JumpStartModel` for one-click deployment of models from SageMaker JumpStart, and `InferenceEndpointConfig` for full-control deployment of custom or fine-tuned models. Deployment interfaces include `kubectl apply` with CRD manifests, a Python SDK, Amazon SageMaker Studio UI, and the HyperPod CLI. Networking uses Elastic Fabric Adapter (EFA) with GPU-Direct RDMA for high-bandwidth, low-latency inter-node communication and Application Load Balancers (ALB) for external traffic ingestion. Enterprise capabilities include custom Kubernetes pod configuration (init containers, volumes, scheduler), custom ACM certificates for endpoints (public, Private CA, or imported), Route 53 DNS management for custom domain names, per-pod request limits (max concurrent requests, queue size, overflow status codes), multi-instance type deployment with automatic failover across prioritized instance lists, custom node affinity for granular scheduling (AZ distribution, capacity type filtering, custom labels), EKS Pod Identity, and [Multi-Instance GPU (MIG)](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment.html) support for deploying smaller models on fractional GPUs using NVIDIA MIG profiles (e.g., `mig-7g.40gb`, `mig-4g.71gb`). HyperPod also enables unifying training and inference infrastructure—the same cluster serves both workloads with [Task Governance](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks.html) to govern compute resource usage across training, inference, and notebooks, and dynamic resource reallocation based on demand.

HyperPod provides comprehensive, one-click observability through AWS Distro for OpenTelemetry (ADOT) for metrics scraping, Amazon Managed Service for Prometheus for storage and querying, Amazon Managed Grafana with pre-built dashboards (inference metrics, tasks, cluster overview, and DPD-specific monitoring), and Amazon CloudWatch Container Insights for cluster-level visibility. Key metrics tracked include time-to-first-token (TTFT), inter-token latency (ITL), end-to-end request latency, GPU utilization and memory pressure, request queue depth, cache hit rates (L1/L2), and autoscaling events. For compliance, debugging, and model monitoring, [inference data capture](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment.html) records inputs and outputs at three capture points—SageMaker AI Endpoint, Load Balancer (ALB access logs), and Model Pod—configurable via the `dataCapture` field in the CRD.

### Pricing model
<a name="pricing-model.7f3b7738-2287-5e2a-b774-84189610a3ad"></a>

Customers are charged based on instance-based [pricing](https://aws.amazon.com/sagemaker/ai/pricing/) covering compute and storage. [SageMaker Training Plans](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-training-plans.html) offer commitment-based pricing with reduced rates and guaranteed capacity. With scale-to-zero, organizations pay nothing during idle periods when Karpenter removes all nodes. Unified infrastructure eliminates the need for duplicate clusters for training versus inference workloads.

### Model architecture support
<a name="model-architecture-support.74608146-695f-5dcd-914c-91e8c74a8e9f"></a>

SageMaker HyperPod provides access to foundation models through [Amazon SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html), including open-weight and gated models, which can be deployed with a single `JumpStartModel` CRD. For custom or fine-tuned models, the `InferenceEndpointConfig` CRD supports loading from Amazon S3 buckets, Amazon FSx for Lustre, Hugging Face Hub, or local NVMe storage for reduced cold-start latency.

### Automatic scaling
<a name="automatic-scaling.f652e9c6-1540-5ac4-86db-f617c9156240"></a>

HyperPod implements a dual-layer autoscaling architecture. At the pod layer, [KEDA (Kubernetes Event-Driven Autoscaling)](https://keda.sh/) is automatically installed with the Inference Operator and scales inference pods based on request queue length, CloudWatch metrics, latency, Prometheus metrics, or custom metrics—including support for scale-to-zero that eliminates compute costs during idle periods. At the node layer, [Karpenter](https://karpenter.sh/) runs in the EKS control plane and dynamically provisions or removes compute nodes based on pending pod requirements, with intelligent instance type selection based on pod resource requests. Together, ADOT Collector scrapes metrics from inference pods and pushes them to Amazon Managed Prometheus or CloudWatch; KEDA evaluates metrics against thresholds and triggers HPA to create or remove pods; if new pods are pending due to insufficient capacity, Karpenter provisions nodes with appropriate GPU configurations; and when demand decreases, KEDA scales down pods while Karpenter consolidates workloads and removes underutilized nodes. The result is that organizations only pay for compute resources when actively serving inference requests.

### Inference engine choice
<a name="inference-engine-choice.e82b3813-d623-5ed7-abe0-a8520bfd9fda"></a>

Teams can choose [AWS Deep Learning Containers](https://github.com/aws/deep-learning-containers) optimized for generative AI serving engines, including vLLM, TGI, and SGLang. Alternatively, teams can bring custom container images with any inference framework or specialized dependencies.

### Inference optimizations and configurations
<a name="inference-optimizations-and-configurations.37fd43a7-c3b2-5153-9e6b-48f4e495138c"></a>

The service enables advanced inference optimizations through managed tiered KV caching, intelligent request routing, and disaggregated prefill and decode:
+ [**Managed Tiered KV Cache**](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-caching-routing.html) — A two-tier caching architecture stores intermediate attention computations from previous tokens. L1 cache uses CPU memory for low-latency local reuse on the same node. L2 cache offers two backend options: Redis for scalable node-level cache sharing across instances, or inbuilt SageMaker Managed Tiered Storage for higher performance in high-throughput LLM workloads. Performance gains include up to 40% reduction in latency, 25% improvement in throughput, and 25% cost savings versus baseline without these optimizations.
+ [**Intelligent routing strategies**](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-caching-routing.html) — Routes requests based on configurable strategies: `prefixaware` routes requests with the same prompt prefix to the same instance (ideal for system prompts and shared contexts); `kvaware` routes to the instance with the highest KV cache hit rate (for mixed workloads with prefix overlap); `session` routes the same user session to the same instance (for multi-turn conversations); and `roundrobin` provides even distribution without state (for stateless or uniform traffic).
+ [**Disaggregated Prefill and Decode (DPD)**](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-dpd.html) — Separates the compute-bound prefill phase (processing the entire input prompt in parallel to generate the initial KV cache) from the memory-bandwidth-bound decode phase (generating tokens one at a time) onto dedicated GPU pools, removing interference that causes per-token latency spikes when colocated. The intelligent router tokenizes prompts and applies a configurable routing threshold to direct long prompts to prefiller pods and short prompts directly to decoder pods. KV cache transfer uses LMCache PD → NIXL → libfabric → EFA (GPU-Direct RDMA), with transfer costs of approximately single-digit milliseconds for 8,000 tokens on 3,200 Gbps EFA. Configuration is specified via a `pdSpec` field in the `InferenceEndpointConfig` CRD, with configurable routing threshold, independent prefill/decode replica scaling, per-role vLLM args, and intelligent routing strategy for multiple prefillers. Performance benchmarks with Llama 3.3 70B on P5 instances show 22–66% improvement in per-token latency (TPOT) on H100, 28–48% on H200; up to 35% improvement in output throughput on H100, up to 64% on H200; and 14–32% improvement in end-to-end P50 latency on H100, 29–41% on H200. Prerequisites include EFA-capable instances with RDMA read/write in the same Availability Zone (P5, P5e, P5en, P6 families).
+ **Multi-Instance GPU (MIG)** — Partitions large GPUs into isolated instances, deploying models on specific NVIDIA MIG profiles to improve GPU utilization for smaller models, compatible with all other Inference Operator features.

### Supported clients and protocols
<a name="supported-clients-and-protocols.9acf7aaa-92f2-53e4-ac00-8bd1d6982c7b"></a>

Deployed inference workloads can be accessed through Application Load Balancers (ALB) over HTTPS, the Amazon SageMaker Runtime API, the AWS SDK, the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/), any OpenAI-compatible client (vLLM exposes `/v1/chat/completions`), or custom Route 53 DNS endpoints with ACM certificates.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
