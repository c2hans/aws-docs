---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/selecting-aws-service.html
---

# Selecting an AWS service for AI inference
<a name="selecting-aws-service"></a>

When selecting an AWS service for AI inference, organizations need to consider multiple factors that align with their operational requirements and technical capabilities.

Key decision criteria to consider when choosing an AWS service include the following:
+ Level of infrastructure management desired
+ Existing compute commitments
+ Pricing model preferences
+ Required model architecture support
+ Level of control needed in inference engine selection, configuration, and infrastructure

Relevant AWS services include Amazon Bedrock, Amazon SageMaker AI managed endpoints, Amazon SageMaker HyperPod, or self-managed infrastructure using Amazon EC2, Amazon EKS, and Amazon ECS.

## Amazon Bedrock
<a name="amazon-bedrock"></a>

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) provides a fully managed environment for model inference, automatically handling all infrastructure provisioning and scaling. It is optimized for seamless use of off-the-shelf foundation models, while also supporting the import of customized models for select architectures.

### Infrastructure management
<a name="infrastructure-management.fee6cdc8-6dfc-5737-a196-80f7f48a57bf"></a>

AWS manages the complete infrastructure lifecycle, including provisioning, scaling, and maintenance. This capability allows teams to focus on application development.

### Pricing model
<a name="pricing-model.bc1f525b-0a9e-5ed8-8cd9-6a392fce542a"></a>

Amazon Bedrock offers flexible pricing based on actual consumption. Organizations pay for input and output tokens processed during on-demand usage, or they can use and scale imported FMs measured in capacity units.

### Model architecture support
<a name="model-architecture-support.23deb4a0-7501-58a3-853f-1fbba38fa541"></a>

Amazon Bedrock provides access to a wide selection of [foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html), including Amazon Nova, Anthropic Claude, Mistral, Meta Llama, and Qwen. With the Custom Model Import feature, you can use custom models that align with [supported architectures](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html#model-customization-import-model-architecture), enabling deployment of fine-tuned models.

### Automatic scaling
<a name="automatic-scaling.98f89747-e6fb-5618-9f82-f368df7d21b9"></a>

AWS automatically adjusts capacity based on demand patterns, which helps to provide consistent performance during traffic fluctuations.

### Inference engine choice
<a name="inference-engine-choice.d8569f84-58fe-56fa-88dc-3ab6b8d65932"></a>

Amazon Bedrock provides a fully managed inference engine optimized for the supported model architectures, with AWS handling all engine configuration and optimization.

### Inference configuration
<a name="inference-configuration.aae2a526-bcdb-589a-a7cc-c50775fb22b2"></a>

You can control model behavior through model-specific request [parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html). This capability allows customization of generation characteristics such as temperature, top-p sampling, and maximum token length for each inference request.

### Supported clients and protocols
<a name="supported-clients-and-protocols.8c79d725-1ddf-5ece-8f3d-af53d5c6c176"></a>

Applications can access models in Amazon Bedrock through the [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) or [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) API actions over HTTPS or integrate using the [AWS SDK](https://aws.amazon.com/what-is/sdk/). This approach provides straightforward integration paths for various application architectures. You can also use third-party open source libraries like [Strands Agents](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/) or [Crew AI](https://docs.crewai.com/en/concepts/llms#aws-bedrock) to interact with Amazon Bedrock.

## Amazon SageMaker AI inference
<a name="sagemaker-ai-inference"></a>

SageMaker AI Inference endpoints deliver a managed inference environment specifically designed for deploying ML models at scale.

### Infrastructure management
<a name="infrastructure-management.cf848c70-5629-5e1c-a236-6cbfdbd6750d"></a>

SageMaker AI manages the underlying ML instances while providing organizations with control over instance types and configurations. The service handles instance provisioning, health monitoring, and infrastructure maintenance. With these capabilities, teams can focus on model deployment configuration with containers maintained by AWS or custom containers and create inference pipelines for multi-model workflows.

### Pricing model
<a name="pricing-model.baad5453-bbb7-5064-a2d3-3352246bb11d"></a>

Customers are charged based on the instance types deployed, with costs covering both compute resources and storage. This instance-based [pricing model](https://aws.amazon.com/sagemaker/ai/pricing/) enables accurate cost forecasting based on instance selection and deployment duration.

### Model architecture support
<a name="model-architecture-support.09e88346-fd51-58d1-9d76-aaad893bab5d"></a>

SageMaker AI accommodates any compatible model framework or architecture, providing flexibility to deploy models built with TensorFlow, PyTorch, Hugging Face, scikit-learn, XGBoost, or custom frameworks.

### Automatic scaling
<a name="automatic-scaling.9788e73c-b85c-5210-946b-612d65fdf034"></a>

You can configure automatic scaling policies that adjust the number of instances or replicas based on multiple factors. For example, factors include time schedules, built-in Amazon CloudWatch metrics such as invocation rates, concurrent requests, resource utilization, or custom metrics tailored to specific application requirements.

### Inference engine choice
<a name="inference-engine-choice.b555dfba-cf46-5d4d-821c-516e6fd79c6f"></a>

Teams can choose [AWS Deep Learning Containers](https://github.com/aws/deep-learning-containers) images that are optimized for popular frameworks and maintained by AWS. Or, teams can bring custom container images that include specialized inference engines or dependencies.

### Inference configuration
<a name="inference-configuration.94719608-a23e-5806-afe6-43852bcde9f0"></a>

The service enables flexible configuration of both model parameters and system-level settings, including the following:
+ Model's precision, such as FP16, FP8, or INT4
+ Engine-specific optimization strategies like prefix caching and speculative decoding to improve performance
+ Model sharding techniques for distributing large models across multiple GPUs or Trainium [NeuronCores](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/index.html#neuroncore-architecture)

### Supported clients and protocols
<a name="supported-clients-and-protocols.b955b019-11d0-52fd-ac27-e13406a97ab1"></a>

Applications can invoke endpoints through the Amazon SageMaker Runtime [API actions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_Runtime.html) over HTTPS, integrate using the AWS SDK, or leverage the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/) for streamlined Python-based interactions.

## Amazon SageMaker HyperPod
<a name="sagemaker-hyperpod"></a>

[Amazon SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-setup.html) with Amazon EKS orchestration enables large-scale, distributed model inference with enterprise-grade orchestration capabilities. For more information, see [Orchestrating SageMaker HyperPod clusters with Amazon EKS](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks.html) in the Amazon SageMaker AI documentation.

### Infrastructure management
<a name="infrastructure-management.2ae7cfa2-e640-5c87-96df-6f51a016507e"></a>

SageMaker HyperPod provides managed ML instances that AWS automatically provisions and monitors as part of the HyperPod cluster. Kubernetes orchestration through Amazon EKS enables sophisticated workload management and scheduling.

### Training compute reuse
<a name="training-compute-reuse.4b36dfb3-c00a-5266-8994-ad3f93a87fa0"></a>

With SageMaker HyperPod, you can use the same compute resources for both training and inference workloads, maximizing infrastructure efficiency. Additionally, you can govern the usage of compute resources across different types of workloads by using [SageMakerHyperPod task governance](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance.html).

### Pricing model
<a name="pricing-model.0f2baf9a-1e26-5067-884e-c1440ca2e8ba"></a>

Customers are charged based on provisioned instances covering compute and storage resources. [SageMaker training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html) are flexible and offer commitment-based pricing that provides reduced rates and guaranteed capacity for predictable workloads.

### Model architecture support
<a name="model-architecture-support.f64f1313-baae-590d-83b0-69660ccc9839"></a>

The service accommodates any model format or architecture, with full customization of model frameworks and deployment configurations. This flexibility supports diverse use cases from standard transformer models to custom architectures with specialized requirements.

### Automatic scaling
<a name="automatic-scaling.afed6258-1cf1-5f40-8607-dec7e27f33e8"></a>

Pod scaling operates through [Kubernetes Event-driven Autoscaling (KEDA)](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-autoscaling.html#sagemaker-hyperpod-model-deployment-autoscaling-kubectl) and [Karpenter](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-autoscaling-cluster.html) for node scaling, responding to built-in Amazon CloudWatch metrics, engine-specific performance indicators, or custom metrics defined by your organization. SageMaker HyperPod provides comprehensive observability over cluster resources and software components with [Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html), [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html), and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html).

### Inference engine choice
<a name="inference-engine-choice.44e0fe9a-7a54-5581-8b6f-21c5ca568fe1"></a>

You can select from [Deep Learning Container](https://github.com/aws/deep-learning-containers/blob/master/available_images.md) images that are optimized for various frameworks and maintained by AWS. Or, you can deploy custom container images with specialized inference engines, which supports diverse deployment scenarios.

### Inference configuration
<a name="inference-configuration.15b17f6f-1d31-57ef-8f20-95fba9769b9e"></a>

The platform provides comprehensive configuration flexibility for both model and system parameters. Organizations can do the following:
+ Define precision levels.
+ Implement prompt caching strategies.
+ Configure model sharding across GPUs, Trainium NeuronCores, or even nodes.
+ Select quantization approaches.
+ Enable multi-node deployments.
+ Choose communication protocols.
+ Support various client types through the runtime and container configuration.

### Supported clients and protocols
<a name="supported-clients-and-protocols.d8c6c29a-f7ae-5323-957f-68b5b3186b50"></a>

Deployed inference workloads can be accessed by any of the following approaches, providing maximum integration flexibility:
+ Directly over Application Load Balancers over HTTPS
+ Through the [Amazon SageMaker Runtime API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_Runtime.html)
+ By using the AWS SDK
+ By using the SageMaker SDK
+ Through any protocol or client compatible with the chosen inference engine

## Self-managed inference
<a name="self-managed-inference"></a>

Self-managed inference on Amazon EC2, Amazon EKS, or Amazon ECS provides organizations with complete control over their deployment environment and configuration.

### Infrastructure management
<a name="infrastructure-management.776f0959-1c3e-5bb7-a3c1-b18c9c4be3b6"></a>

Organizations maintain full control over infrastructure configuration and management. On Amazon EC2, teams manage instances directly. On Amazon EKS, Kubernetes provides container orchestration. On Amazon ECS, AWS manages the container orchestration layer while organizations control task and service definitions.

### Training compute reuse
<a name="training-compute-reuse.b5f514c0-47b2-5c05-9fe7-4c6f273b3355"></a>

Customers can expand or reallocate their existing Amazon EC2 capacity—currently used for non-inference tasks like training or evaluation—to support AI inference workloads.

### Pricing model
<a name="pricing-model.32b57afc-41ca-56b9-8f9d-adabc4c8e867"></a>

Customers are charged based on provisioned compute instances, storage, and networking resources. [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) provide commitment-based pricing options that deliver reduced rates and guaranteed capacity for planned workloads.

### Model architecture support
<a name="model-architecture-support.7a87fc38-489a-5e97-a0d2-dc5dc8fd7baf"></a>

The environment accommodates any model format or architecture, enabling deployment of models built with any framework, custom architectures, or proprietary implementations.

### Automatic scaling
<a name="automatic-scaling.bb1d7e80-2d22-5ebe-a0ed-7409cf4660f6"></a>

Scaling mechanisms are tailored to each AWS service's capabilities:
+ **Amazon EKS** – [Kubernetes Horizontal Pod Autoscaler (HPA)](https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html) or [KEDA](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-autoscaling.html#sagemaker-hyperpod-model-deployment-autoscaling-kubectl) adjust pod replicas based on resource utilization or custom metrics. Also, for Amazon EKS, [Karpenter](https://karpenter.sh/) dynamically provisions and scales nodes to match workload demands efficiently.
+ **Amazon ECS** – [Service autoscaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) adjusts task counts based on CloudWatch metrics, target tracking policies, or step scaling configurations.
+ **Amazon EC2** – [Autoscaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) manage instance fleets using dynamic scaling policies, predictive scaling, or scheduled actions.

All approaches can respond to built-in metrics (such as CPU, memory, and network) and to engine-specific performance indicators (such as request latency, queue depth, and throughput). They can also respond to custom metrics tailored to specific application requirements from [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html), or third-party sources.

### Inference engine choice
<a name="inference-engine-choice.654677a1-a34a-5bea-a9f7-982da432f823"></a>

You can select from [Deep Learning Container](https://github.com/aws/deep-learning-containers/blob/master/available_images.md) images that are optimized for popular frameworks and maintained by AWS. Or, they can deploy custom container images with any inference engine or specialized software stack.

### Inference configuration
<a name="inference-configuration.5f7f0f69-3b8c-5f2a-8dbf-eab6904aa58d"></a>

The environment provides complete customization of system configuration. Organizations can implement any quantization level, configure model sharding strategies, enable prompt caching mechanisms, define batching behaviors, select communication protocols, and optimize for specific performance characteristics.

### Supported clients and protocols
<a name="supported-clients-and-protocols.4ffe6415-92c5-58a1-916a-702a716445e0"></a>

Inference API servers can be exposed through Application Load Balancers, Network Load Balancers, or Kubernetes ingress controllers. All approaches support any protocol or client compatible with the deployed inference engine or container. This flexibility enables integration with diverse application architectures and client requirements.
