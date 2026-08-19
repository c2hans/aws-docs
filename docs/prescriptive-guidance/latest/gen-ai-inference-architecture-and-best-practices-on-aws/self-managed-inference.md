---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/self-managed-inference.html
---

# Self-managed inference
<a name="self-managed-inference"></a>

Self-managed inference on Amazon EC2, Amazon EKS, or Amazon ECS provides organizations with complete control over their deployment environment and configuration.

## Infrastructure management
<a name="infrastructure-management.776f0959-1c3e-5bb7-a3c1-b18c9c4be3b6"></a>

Organizations maintain full control over infrastructure configuration and management. On Amazon EC2, teams manage instances directly. On Amazon EKS, Kubernetes provides container orchestration. On Amazon ECS, AWS manages the container orchestration layer while organizations control task and service definitions.

## Training compute reuse
<a name="training-compute-reuse.b5f514c0-47b2-5c05-9fe7-4c6f273b3355"></a>

Customers can expand or reallocate their existing Amazon EC2 capacity—currently used for non-inference tasks like training or evaluation—to support AI inference workloads.

## Pricing model
<a name="pricing-model.32b57afc-41ca-56b9-8f9d-adabc4c8e867"></a>

Customers are charged based on provisioned compute instances, storage, and networking resources. [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) provide commitment-based pricing options that deliver reduced rates and guaranteed capacity for planned workloads.

## Model architecture support
<a name="model-architecture-support.7a87fc38-489a-5e97-a0d2-dc5dc8fd7baf"></a>

The environment accommodates any model format or architecture, enabling deployment of models built with any framework, custom architectures, or proprietary implementations.

## Automatic scaling
<a name="automatic-scaling.bb1d7e80-2d22-5ebe-a0ed-7409cf4660f6"></a>

Scaling mechanisms are tailored to each AWS service's capabilities:
+ **Amazon EKS** – [Kubernetes Horizontal Pod Autoscaler (HPA)](https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html) or [KEDA](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-autoscaling.html#sagemaker-hyperpod-model-deployment-autoscaling-kubectl) adjust pod replicas based on resource utilization or custom metrics. Also, for Amazon EKS, [Karpenter](https://karpenter.sh/) dynamically provisions and scales nodes to match workload demands efficiently.
+ **Amazon ECS** – [Service autoscaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) adjusts task counts based on CloudWatch metrics, target tracking policies, or step scaling configurations.
+ **Amazon EC2** – [Autoscaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) manage instance fleets using dynamic scaling policies, predictive scaling, or scheduled actions.

All approaches can respond to built-in metrics (such as CPU, memory, and network) and to engine-specific performance indicators (such as request latency, queue depth, and throughput). They can also respond to custom metrics tailored to specific application requirements from [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html), or third-party sources.

## Inference engine choice
<a name="inference-engine-choice.654677a1-a34a-5bea-a9f7-982da432f823"></a>

You can select from [Deep Learning Container](https://github.com/aws/deep-learning-containers/blob/master/available_images.md) images that are optimized for popular frameworks and maintained by AWS. Or, they can deploy custom container images with any inference engine or specialized software stack.

## Inference configuration
<a name="inference-configuration.5f7f0f69-3b8c-5f2a-8dbf-eab6904aa58d"></a>

The environment provides complete customization of system configuration. Organizations can implement any quantization level, configure model sharding strategies, enable prompt caching mechanisms, define batching behaviors, select communication protocols, and optimize for specific performance characteristics.

## Supported clients and protocols
<a name="supported-clients-and-protocols.becab830-47e9-5fcf-9b6e-1a5adf2591e8"></a>

Inference API servers can be exposed through Application Load Balancers, Network Load Balancers, or Kubernetes ingress controllers or envoy proxies. All approaches support any protocol or client compatible with the deployed inference engine or container. This flexibility enables integration with diverse application architectures and client requirements.
