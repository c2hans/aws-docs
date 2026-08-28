---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/bedrock-or-sagemaker.html
---

# Amazon Bedrock or Amazon SageMaker AI?
<a name="bedrock-or-sagemaker"></a>

**Understand the differences and pick the one that's right for you**

|  |  |
| --- |--- |
| **Purpose** | Understand the differences between Amazon Bedrock and Amazon SageMaker AI, and determine which service is the best fit for your needs. |
| **Last updated** | July 23, 2026 |
| **Covered services** |  +  [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) <br />+  [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)   |

## Introduction
<a name="introduction"></a>

Amazon Web Services (AWS) offers managed services to help you build AI applications and agents. For an overview of how these services work together across the generative AI stack, from custom silicon to agentic solutions, see the [generative AI decision guide](https://docs.aws.amazon.com/decision-guides/latest/generative-ai-on-aws-how-to-choose/guide.html).

The following diagram shows the AWS AI stack from silicon to agentic solutions.

![Diagram showing the AWS AI stack from silicon to agentic solutions. From bottom to top: global infrastructure (39 Regions), AI chips (Trainium, Graviton, NVIDIA GPUs), data foundation, models training and inferencing (SageMaker, Bedrock), agent development and orchestration (Bedrock AgentCore), and agentic solutions (Kiro, Quick, Connect, Marketplace). Security, governance, and agent store span the full stack.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/gen-ai-stack-dec-2024.png)

When choosing which generative AI services to use, two services are often compared:

**Amazon Bedrock**
+ Choose [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) if you need a fully managed, serverless platform to build, run, and operate AI applications and agents at production scale. Amazon Bedrock provides access to frontier models from leading AI labs, agent development paths that work with any framework, and governance controls that extend the AWS security stack to AI wherever it runs.
+ Amazon Bedrock provides [additional capabilities](https://docs.aws.amazon.com/bedrock/latest/userguide/additional-capabilities.html) to enhance your generative AI applications, including [Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for retrieval augmented generation (RAG), [Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) for implementing safeguards, [AgentCore](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html) for building, deploying, and operating AI agents at scale, [Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html) for building end-to-end workflows, [Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) for transforming unstructured data, and [Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) for constructing reusable prompts.
+ Use [ Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html) to discover, test, and use popular, emerging, and specialized foundation models (FMs).

**Amazon SageMaker AI**
+ [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) (formerly Amazon SageMaker) is a fully managed service designed to help you build, train, and deploy AI, predictive ML, and classical ML models at scale. This includes building models from scratch using tools such as notebooks, pipelines, and ModelOps solutions. Serverless MLflow supports tracking experiments and tracing agents. Consider SageMaker AI when you have use cases that can benefit from extensive training, fine-tuning, customization, and inference of open, proprietary, and custom models. Also consider SageMaker AI for deploying models when you need to manage cost, throughput, and latency tradeoffs. SageMaker AI provides managed infrastructure with native optimizations for workload-optimized inference. It can also help you through the potentially challenging task of evaluating which model is the best fit for your use case. Custom models trained on SageMaker AI can deploy to SageMaker AI endpoints for managed inference, to Amazon SageMaker HyperPod for large-scale inference, or to Amazon Bedrock for serverless inference.
+ In addition to the managed infrastructure provided by SageMaker AI training and SageMaker AI inference, Amazon SageMaker HyperPod provides resilient, scalable infrastructure for training and deploying AI models at scale with access to the orchestration layer: Kubernetes (EKS) for training and inference, or Slurm for training.

This guide is focused on understanding the differences between Amazon SageMaker AI and Amazon Bedrock. For more information about how Amazon Bedrock and SageMaker AI fit into Amazon’s generative AI services and solutions, see the [generative AI decision guide](https://docs.aws.amazon.com/decision-guides/latest/generative-ai-on-aws-how-to-choose/guide.html).

While both Amazon Bedrock and Amazon SageMaker AI enable the development of AI applications and agents, they serve different purposes. This guide helps you understand which of these services is the best fit for your needs, including scenarios in which both services can be used together to build generative AI applications.

The following is a high-level view of the key differences between these services to get you started.

|  **Category**  |  ![Amazon Bedrock service icon.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch_Amazon-Bedrock_48.png) **Amazon Bedrock**  |  ![Brain icon with interconnected nodes representing artificial intelligence or machine learning.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch_Amazon-SageMaker_48.png) **Amazon SageMaker AI**  |
| --- | --- | --- |
|  Use Cases  | Fully managed, serverless platform for building, running, and operating AI applications and agents at production scale | Optimized for convenient training, customizing, and deploying AI models with maximum user control for AI applications, predictive ML, and classical ML at production scale |
|  Target Users  | Optimized for technical decision makers, developers, and teams building AI applications and agents | Optimized for ML practitioners, ML engineers, Data Scientists, AI platform teams and developers |
|  Customization  | Automated customization with fine-tuning, distillation, and custom model import; minimal infrastructure management | Serverless customization with SFT, DPO, RLVR, and RLAIF; managed training with Training Jobs; full control with HyperPod |
|  Pricing  | Pay-as-you-go per-token pricing based on input and output tokens processed, with Priority, Flex, and Reserved service tiers available | Per-token pricing for serverless customization; usage-based pricing for compute resources with training jobs, inference, and HyperPod |
|  Integration  | Integrate pre-trained models into applications through API calls, including OpenAI-compatible endpoints | Integrate custom models into applications, with more customization options |
|  Expertise Required  | Basic level of ML expertise needed to use pre-trained models | Guided UI and AI agent-assisted workflows simplify customization; deeper ML expertise helpful for advanced training jobs |
| Management | Amazon Bedrock provides a simplified API-based approach with minimal infrastructure management. | Serverless model customization requires no infrastructure management. Inference, training jobs, and HyperPod offer full infrastructure control with extensive [monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) and [control](https://docs.aws.amazon.com/sagemaker/latest/dg/governance.html) capabilities. |
| Deployment and Hosting | Amazon Bedrock is serverless, meaning you do not have to manage infrastructure. | Serverless for model customization; custom models deploy to SageMaker AI dedicated endpoints for managed inference or Amazon Bedrock for serverless inference. Training jobs and HyperPod support train-to-serve continuity with granular node-level resource control. Endpoints scale to zero with built-in observability and operational simplicity, including serverless MLflow. |

## Differences between Amazon Bedrock and SageMaker AI
<a name="differences"></a>

The following sections examine and compare the capabilities of Amazon Bedrock and Amazon SageMaker AI.

------
#### [ Use cases ]

Amazon Bedrock and Amazon SageMaker AI address different use cases based on your specific requirements and resources.

 **Amazon Bedrock**
+ Amazon Bedrock is designed for use cases where you want to build AI applications and agents without investing heavily in custom model development. For example, a content moderation system for a social media platform could use Amazon Bedrock's pre-trained models to automatically identify and flag inappropriate text or images. Similarly, a customer support chatbot could use Amazon Bedrock's natural language processing capabilities to understand and respond to user inquiries. Amazon Bedrock is particularly useful if you have limited machine learning (ML) expertise or resources, as it helps you to benefit from AI without the need for extensive in-house development.

 **Amazon SageMaker AI**
+ SageMaker AI is a good choice for convenient training, customizing, and deploying AI, predictive ML, and classical ML models with maximum control. Choose SageMaker AI when you need to access the container or orchestration layer to directly manage cost-latency-throughput and other tradeoffs. Examples include a healthcare company developing a model to predict patient outcomes based on specific biomarkers. Another example is a financial institution creating a fraud detection system tailored to their unique data and risk factors. Another scenario is a large-scale LLM deployment where you want to maximize GPU utilization while balancing cost against desired throughput and latency metrics.

------
#### [ Target users ]

Rather than choosing one service over the other, consider what level of customization you need. A common path is to start with Amazon Bedrock and progress to SageMaker AI as your customization requirements grow.

 **Amazon Bedrock**
+ Choose Amazon Bedrock if you want to build AI applications and agents using pre-trained models, prompt engineering, and RAG — without needing deep ML expertise.

 **Amazon SageMaker AI**
+ SageMaker AI serves two audiences. If you need to change model behavior through serverless customization, the guided UI and AI agent-assisted workflow require no ML expertise. If you need full control over training workflows, model deployment, frameworks, and infrastructure, use training jobs, dedicated endpoints, and HyperPod.

------
#### [ Choice of FMs ]

 While both Amazon Bedrock and Amazon SageMaker AI offer a broad set of FMs for your applications, there are differences in the set of FMs that each service offers.

 **Amazon Bedrock**
+ Amazon Bedrock provides access to FMs including proprietary models such as Anthropic Claude and Amazon Nova, open models from Meta (Llama), Mistral AI, Qwen, and OpenAI (GPT-OSS), Stability AI models for image generation, and many others. See the [ list of available FMs](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html), which is updated frequently.
+ Use the [ Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html) to rapidly test and incorporate over 100 publicly available and proprietary FMs.
+ Amazon Bedrock provides access to certain proprietary models, including Claude, that are not available in Amazon SageMaker JumpStart.

 **Amazon SageMaker AI**
+ Amazon SageMaker JumpStart offers built-in publicly available and proprietary foundation models to customize and integrate into your generative AI, classical ML, and predictive ML workflows, with nearly 1,000 models available, including models optimized for specific use cases.
+ JumpStart offers publicly available FMs, including models from Hugging Face, Stability AI, Meta, and Amazon, and proprietary FMs from Amazon (Nova models for both customization and inference), AI21 Labs, Cohere, and LightOn. See the [ list of publicly available and proprietary FMs](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-latest.html), which is updated frequently.

------
#### [ Customization ]

Amazon Bedrock and Amazon SageMaker AI offer different levels of customization capabilities that you can tailor to your specific needs and expertise.

 **Amazon Bedrock**
+ Amazon Bedrock offers a set of models from leading providers that you can use to build generative AI applications with automated customization options. You have access to a set of API calls that you use to enter data and receive predictions from these pre-trained models. This approach simplifies the process of incorporating AI capabilities into applications. Amazon Bedrock supports fine-tuning, [model distillation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-distillation.html), reinforcement fine-tuning, and [custom model import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html), with minimal infrastructure management.

 **Amazon SageMaker AI**
+ Amazon SageMaker AI provides serverless model customization with a guided interface and AI agent-assisted workflow, offering control with guardrails while eliminating infrastructure management. The AI agent handles the full customization lifecycle — technique selection, data preparation, training, evaluation, and deployment — through natural language, so developers can complete workflows without specialized ML knowledge. SageMaker AI also supports IDE portability with VS Code, Kiro, and other development environments. SageMaker AI supports a broad set of serverless customization techniques available for open-weight models, including supervised fine-tuning (SFT), direct preference optimization (DPO), reinforcement learning with verifiable rewards (RLVR), reinforcement learning with AI feedback (RLAIF), and managed multi-turn reinforcement learning. For full infrastructure control, SageMaker AI managed training jobs, managed inference and HyperPod provide complete flexibility over the training and inferencing workflows, frameworks, and compute resources.
+ Use [ Amazon SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) to evaluate, compare, and select models based on pre-defined quality and responsibility.
+ Use [Amazon Nova customization recipes](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model.html) on SageMaker AI for comprehensive model customization, including fine-tuning and training Nova models that can be imported into Amazon Bedrock. With [Amazon Nova Forge](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-forge.html), you can build your own frontier models using Nova by starting from early model checkpoints, blending proprietary data with Amazon Nova-curated training data, and hosting custom models securely on AWS.

------
#### [ Pricing ]

 Amazon Bedrock and Amazon SageMaker AI have different pricing models that reflect their target users and the services they provide.

 **Amazon Bedrock**
+ Amazon Bedrock uses per-token [pricing](https://aws.amazon.com/bedrock/pricing/) for model inference, based on input and output tokens processed. Additional features such as Knowledge Bases, Guardrails, and Data Automation are priced separately based on usage. This pricing structure makes it efficient to estimate and control costs. Amazon Bedrock also offers service tiers for inference: Priority for latency-sensitive workloads, Flex for cost-optimized batch processing, and Reserved for committed capacity with predictable pricing. Batch inference offers up to 50% savings for non-real-time workloads, and Provisioned Throughput provides committed capacity at reduced rates. The pricing model for Amazon Bedrock is particularly well-suited for applications with predictable workloads, or for cases where you want more transparency in your AI-related expenses.

 **Amazon SageMaker AI**
+ SageMaker AI offers per-token [pricing](https://aws.amazon.com/sagemaker/pricing/) for serverless model customization, providing the same pricing simplicity as Amazon Bedrock. For managed training jobs, inference, and HyperPod, SageMaker AI follows usage-based pricing for compute resources, storage, and other services consumed during the AI development process, with prices varying depending on the instance type and size. SageMaker AI Savings Plans can reduce costs by up to 64% with 1- or 3-year commitments. SageMaker AI also supports cost-optimized hardware including AWS Trainium for training and AWS Inferentia for inference.

------
#### [ Integration ]

 Amazon Bedrock and Amazon SageMaker AI offer different approaches to integrating AI models into applications, catering to your specific needs and expertise.

 **Amazon Bedrock**
+ Amazon Bedrock simplifies the integration process by providing pre-trained models that you can access directly through API calls. Use the Amazon Bedrock SDK, REST API, or OpenAI-compatible API endpoints to send input data and receive predictions from the models without needing to manage the underlying infrastructure. The OpenAI-compatible endpoints support the Responses API and Chat Completions API. With these endpoints, you can migrate existing OpenAI applications by updating the base URL and API key. This approach significantly reduces the complexity and time required to integrate AI capabilities into applications, making it accessible to a broad range of developers.

 **Amazon SageMaker AI**
+ SageMaker AI provides a comprehensive platform for building, training, and deploying custom AI models. For managed inference on SageMaker AI endpoints, you use the SageMaker AI SDK or API to access deployed models. SageMaker AI provides tools such as GenAI inference recommendations and benchmarking to simplify instance type selection. For serverless customization, custom models can also deploy to Amazon Bedrock for serverless inference with no additional infrastructure setup.

------
#### [ Expertise required ]

 Amazon Bedrock and Amazon SageMaker AI offer different paths depending on your level of expertise and the degree of control you need.

 **Amazon Bedrock**
+ Amazon Bedrock is more accessible to a broader range of users, including developers and businesses with limited ML expertise. By providing pre-trained models that can be easily integrated into applications through API calls, Amazon Bedrock abstracts away much of the complexity associated with building and deploying AI models. For the serverless path, both Amazon Bedrock and SageMaker AI serverless customization handle data preprocessing, model selection, and infrastructure management. You can focus on integrating AI capabilities into your applications without deep ML expertise.

 **Amazon SageMaker AI**
+ SageMaker AI provides guided experiences that simplify model customization for a broad range of users. The guided UI and AI agent-assisted workflow (in preview) enable developers to complete customization workflows in a few clicks or through natural language, including technique selection, data preparation, and model evaluation. For advanced use cases such as custom training jobs and HyperPod clusters, deeper ML expertise is helpful for optimizing training workflows, frameworks, and infrastructure configurations.

------
#### [ Features ]

 Amazon Bedrock and Amazon SageMaker AI offer complementary capabilities for building AI applications and agents.

 **Amazon Bedrock**
+ Amazon Bedrock offers a suite of features to help you build and scale AI applications and agents, including model choice features (evaluation), cost and latency optimization features (prompt caching, intelligent prompt routing, service tiers), customization features (knowledge bases, model distillation, reinforcement fine-tuning), safeguards (guardrails with automated reasoning checks, organizational safeguards, image content filters, and cross-platform support for non-Amazon Bedrock models), agentic features (Amazon Bedrock AgentCore for building, deploying, and operating AI agents at scale, multi-agent collaboration, AWS Agent Registry, and framework-agnostic compatibility with LangGraph, CrewAI, and LlamaIndex), and data processing features (Amazon Bedrock Data Automation for documents, images, audio, and video). Amazon Bedrock also offers custom model import, OpenAI-compatible API endpoints, and a serverless, unified API for accessing foundation models. Prompt caching can reduce costs by up to 90% and latency by up to 85% for supported models. Intelligent prompt routing can reduce costs by up to 30% without compromising accuracy. Distilled models are up to 500% faster and up to 75% less expensive than original models, with less than 2% accuracy loss for use cases such as RAG. Guardrails with automated reasoning checks help reduce factual errors due to hallucinations to near zero.

 **Amazon SageMaker AI**
+ SageMaker AI offers a comprehensive platform for the full AI development lifecycle. Key capabilities include: serverless model customization with SFT, DPO, RLVR, and RLAIF through a guided UI and AI agent-assisted workflow; Amazon SageMaker JumpStart as a model hub with nearly 1,000 models available including open-source, proprietary, and custom models; support for predictive ML and classical ML in addition to generative AI; and IDE portability with support for VS Code, Kiro, and other development environments. Amazon SageMaker HyperPod provides an end-to-end experience for large-scale AI development, supporting training and inference on managed clusters with checkpointless training, elastic training, and task governance. HyperPod reduces training time by up to 40%, task governance reduces costs by up to 40%, and checkpointless training enables upwards of 95% training goodput. HyperPod scales across thousands of AI accelerators. SageMaker AI endpoints support scaling to zero instances to reduce costs when idle, stateful sessions for maintaining context across inference requests, and inference optimization techniques such as EAGLE-based speculative decoding for up to 2.5x throughput improvement. SageMaker AI supports advanced deployment options including heterogeneous instance clusters and cross-region inference for higher availability, A/B testing, canary deployments, blue/green deployments, and shadow testing. Inference Components reduce model deployment costs by hosting multiple models behind a single endpoint.
+ Amazon SageMaker HyperPod provides resilient, scalable infrastructure for training and deploying AI models at scale with access to the orchestration layer: Kubernetes (EKS) for training and inference, or Slurm for training. For inference, HyperPod also offers built-in capabilities such as distributed KV caching, capacity-aware inference, and intelligent routing, reducing latency by 40%.

------

The choice between Amazon Bedrock and Amazon SageMaker AI is not always mutually exclusive. You may benefit from using both services together in a progressive customization pipeline:
+ **Start with Amazon Bedrock**: Begin with prompt engineering and retrieval augmented generation (RAG) using Amazon Bedrock Knowledge Bases to quickly build and iterate on your generative AI application.
+ **Move to SageMaker AI serverless customization**: When you need to change model behavior beyond what prompting can achieve, use SageMaker AI serverless customization with techniques such as SFT and DPO to fine-tune models on your data.
+ **Advance to reinforcement learning**: For reward-signal optimization, use RLVR and RLAIF on SageMaker AI to further align model outputs with your specific quality and accuracy requirements.
+ **Deploy across both services**: Custom models trained on SageMaker AI can be deployed in SageMaker AI inference or imported to Amazon Bedrock through custom model import for serverless inference, or to SageMaker AI endpoints for managed inference with granular control over cost, throughput, and latency. You can also prototype on Amazon Bedrock serverless inference and move to SageMaker AI endpoints or HyperPod when you need production-level control over infrastructure to manage cost-latency-throughput tradeoffs.

The following table maps common use case patterns to recommended service approaches.

| **Use case pattern** | **Recommended approach** |
| --- | --- |
| Rapid FM prototyping with prompt engineering and RAG | Amazon Bedrock |
| Enterprise AI agents with security and observability | Amazon Bedrock AgentCore with Amazon Bedrock and/or SageMaker AI for inference |
| Serverless model customization (SFT, DPO, RL) | SageMaker AI serverless customization |
| Custom model training at scale | SageMaker AI training jobs or HyperPod |
| Large-scale GenAI inference | Amazon Bedrock and/or SageMaker AI depending on the need to directly manage cost-latency-throughput tradeoffs |
| Full ML lifecycle with governance | SageMaker AI |
| Production GenAI apps with cost optimization | Both services together |

Ultimately, the decision between Amazon Bedrock and Amazon SageMaker AI depends on your specific requirements. Evaluating these factors helps you choose the service that best fits your needs.

For more information about Amazon’s generative AI services and solutions, see the [generative AI decision guide](https://docs.aws.amazon.com/decision-guides/latest/generative-ai-on-aws-how-to-choose/guide.html).

## Use
<a name="use"></a>

A common approach is to follow a progressive journey: start with Amazon Bedrock for prompt engineering and RAG, then move to SageMaker AI serverless customization when you need to change model behavior, and advance to training jobs or HyperPod when you need full infrastructure control. Use the following resources to get started at any point in this journey.

------
#### [ Amazon Bedrock ]
+  **What is Amazon Bedrock?**

  Use this fully managed, serverless platform to build, run, and operate AI applications and agents at production scale.

   [Explore the guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)

+  **Frequently asked questions about Amazon Bedrock**

  Get answers to the most commonly-asked questions about Amazon Bedrock. These include how to use agents, security considerations, details about Amazon Bedrock software development kits (SDKs), retrieval augmented generation, how to use model evaluation, and billing.

   [Read the FAQs](https://aws.amazon.com/bedrock/faqs/)

+  **Guidance for generating product descriptions with Amazon Bedrock**

  Use Amazon Bedrock in your solution to automate your product review and approval process for an e-commerce marketplace or retail website.

   [Explore the solution](https://aws.amazon.com/solutions/guidance/generating-product-descriptions-with-amazon-bedrock/)

------
#### [ Amazon Bedrock IDE ]

**Note**
Amazon Bedrock Studio, renamed to Amazon Bedrock IDE, is available in Amazon SageMaker Unified Studio
+  **What is Amazon Bedrock IDE?**

   Use Amazon Bedrock IDE to discover Amazon Bedrock models, and build generative AI apps that use Amazon Bedrock models and features.

   [Explore the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock.html)

+  **Build generative AI applications with Amazon Bedrock IDE**

  This blog post describes how you can build applications using a wide array of top performing models. It then explains how to evaluate and share your generative AI apps with Amazon Bedrock IDE.

   [Read the blog](https://aws.amazon.com/blogs/machine-learning/build-generative-ai-applications-quickly-with-amazon-bedrock-ide-in-amazon-sagemaker-unified-studio/)

+  **Building a chat app with Amazon Bedrock IDE**

  Build an Amazon Bedrock IDE chat agent app that allows users to chat with an Amazon Bedrock model through a conversational interface.

   [Explore the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/create-chat-app.html)

------
#### [ Amazon SageMaker AI ]
+  **What is Amazon SageMaker AI?**

  Use this fully managed AI service to build, train, and deploy AI models into a production-ready hosted environment.

   [Explore the guide](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)

+  **Get started with Amazon SageMaker AI**

   Set up access to Amazon SageMaker AI, including quick or custom setup steps.

   [Explore the guide](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html)

+  **Get started with Amazon SageMaker JumpStart**

   Explore Amazon SageMaker JumpStart solution templates that set up infrastructure for common use cases, and executable example notebooks for AI with SageMaker AI.

   [Explore the guide](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)

+  **Model customization with Amazon SageMaker AI**

  Accelerate AI model customization with serverless reinforcement learning and an AI agent-guided workflow.

   [Explore model customization](https://aws.amazon.com/sagemaker/ai/model-customization/)

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Decision Guides. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query decision-guides` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
