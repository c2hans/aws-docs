---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/aws-inference-stack.html
---

# AWS inference stack
<a name="aws-inference-stack"></a>

*AI inference* is the process of using a trained machine learning (ML) model to make predictions based on input data. Traditional ML inference typically involves relatively small models with modest compute requirements. However, generative AI (gen AI) inference has introduced new requirements in terms of compute, specialized hardware, and system optimizations.

As shown in the following diagram, AWS provides a multi-layer AI inference stack to address customers' diverse inference needs.

![Layers of the AWS inference stack: Serverless, managed inference, and self-managed inference.](http://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/images/guide-img/1e4a4636-9247-4346-9ab7-62170783f8a2/images/d89acc58-5709-48ab-8210-65d21c503fef.png)

Following are descriptions of each layer of the AI inference stack.

## Serverless inference layer
<a name="serverless-inference-layer.c4ff9191-fa37-55f7-9854-6202273af41d"></a>

Following are key capabilities of the serverless inference layer, which is the top layer of the AI inference stack:
+ Powered by [Amazon Bedrock](https://aws.amazon.com/bedrock/) which offers a wide choice of industry leading foundation models (FMs) along with a broad set of capabilities to build generative AI applications.
+ Supports importing custom models with popular architectures such as Llama, Mistral, and Qwen.
+ Abstracts infrastructure management completely including high availability, scaling, and performance tuning.
+ Pay-as-you-go pricing by using tokens or capacity units. For more information, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).
+ Ideal for organizations who want to minimize operational and development effort.

### Managed inference layer
<a name="managed-inference-layer.160ef1cf-1a16-5791-8e83-a8f03876a975"></a>

Following are key capabilities of the managed inference layer, which is the middle layer of the AI inference stack:
+ Powered by [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/) which provides a broad set of tools to enable high-performance, low-cost ML for building, training and deploying AI models at scale. It provides all these capabilities in one integrated development environment (IDE).
+ Enables serving pre-trained or custom models on managed infrastructure.
+ Balances control with simplicity and with flexibility in choosing inference engines, scaling policies, and instance types.
+ Suitable for organizations who want more control over deployment configuration, scaling behavior, and cost optimization while maintaining operational simplicity.

### Self-managed inference layer
<a name="self-managed-inference-layer.ef07e6ac-25e9-5993-862e-2bc610c72d87"></a>

Following are key capabilities of the self-managed inference layer, which is the bottom layer of the AI inference stack:
+ Powered by [Amazon EC2 instances](https://aws.amazon.com/ec2/) with [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) and [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/) chips, AWS and NVIDIA [GPUs](https://aws.amazon.com/nvidia/), and CPUs. Offers broad and deep compute capabilities with over 1,000 instances and choice of the latest processor, storage, networking, operating system, and purchase model.
+ Can operate through services like [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) or [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS).
+ Offers maximum flexibility and control of their infrastructure and software.
+ Ideal for organizations who require complete control over their infrastructure.
