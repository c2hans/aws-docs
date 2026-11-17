---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/genai-guide.html
---

# Choosing a generative AI service
<a name="genai-guide"></a>

**Taking the first step**

|  |  |
| --- |--- |
|  Purpose  |  Determine which AWS generative AI services fit the needs of your organization.  |
|  Last updated  |  November 14, 2026  |
|  Covered services  |  +  **Assistants:** [Amazon Quick Suite](https://aws.amazon.com/quick/), [Kiro](https://kiro.dev/) <br />+  **Build applications and agents:** [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) (including Knowledge Bases, Guardrails, Flows, model customization, Custom Model Import, and cross-Region inference), [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html), and [Amazon Bedrock in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock.html) <br />+  **Models:** [Amazon Nova](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html), models from third-party providers in Amazon Bedrock, and open-weight models in [Amazon SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) <br />+  **Host, customize, and train models:** [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), Amazon SageMaker HyperPod, and self-managed on Amazon EC2, Amazon EKS, and Amazon ECS <br />+  **Infrastructure:** [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/), [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/), and Amazon EC2 GPU instances   |

## Introduction
<a name="introduction"></a>

Generative AI is a set of artificial intelligence (AI) systems and models that create new content, such as text, code, images, audio, and video, based on patterns learned from large amounts of data. Increasingly, organizations and businesses use generative AI to:
+  **Automate creative workflows:** Automate time-consuming creative processes such as writing, image or video creation, and graphic design.
+  **Customize and personalize content:** Generate targeted content, product recommendations, and customized offerings for an audience-specific context.
+  **Build AI agents:** Complete multistep tasks that combine reasoning, tool use, and access to your systems and data.
+  **Augment data:** Synthesize large training datasets for other ML models to unlock scenarios where human-labeled data is scarce.
+  **Experiment faster:** Test and iterate on more content variations and creative concepts than would be possible manually.

AWS offers generative AI capabilities at three layers, and many organizations use more than one:

1. **Ready-to-use AI assistants:** Applications such as Amazon Quick Suite and Kiro that you can adopt without choosing or managing a model.

1. **Services to build generative AI applications and agents:** [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) gives you serverless access to a broad selection of foundation models through a single API, plus tools for retrieval augmented generation (RAG), safeguards, and customization. Amazon Bedrock AgentCore lets you build, deploy, and operate AI agents with any framework or model.

1. **Options to host, customize, and train models yourself:** When you need a model that isn't available in Amazon Bedrock, or more control over how a model is served or trained, you can use Amazon SageMaker AI, Amazon SageMaker HyperPod, or self-managed infrastructure on Amazon EC2, Amazon EKS, or Amazon ECS.

For the third layer, the options sit on a spectrum from the least to the most operational ownership. More ownership gives you more control over performance, cost, and model choice, but it also adds operational work. A practical starting point for most inference workloads is to begin with the most managed option that meets your requirements. Move toward more control only when a specific requirement calls for it.

 This guide helps you make that decision for each of your workloads.

[![AWS Videos](https://img.youtube.com/vi/WEKTpzvJiec?si=39jHcyiMGTfiO2zB/0.jpg)](https://www.youtube.com/watch?v=WEKTpzvJiec?si=39jHcyiMGTfiO2zB)

## Understand
<a name="understand"></a>

AWS offers a range of generative AI services, applications, tools, and supporting infrastructure. Which of these you use depends on several factors:
+ What you're trying to do: use an assistant, build an application or agent, or host and customize models
+ Which foundation models you need, and whether they're available as a managed service
+ How much control you need over model serving, customization, and infrastructure
+ Where your data must be processed, and in which AWS Regions you operate
+ Your traffic patterns and cost model
+ The expertise and operational capacity of your team

![Diagram showing the AWS generative AI stack. This diagram shows the infrastructure to build and train AI models at the bottom of the stack, models and tools to build generative AI apps in the middle, and applications that use LLMs and other FMs to boost productivity, at the top.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/gen-ai-stack-dec-2024.png)

 **Generative AI assistants: Boost productivity without managing models**

These applications use foundation models behind the scenes. You don't need to choose or operate a model.

**Note**
Amazon Q Business is no longer open to new customers as of July 31, 2026. For similar capabilities, explore [Amazon Quick Suite](https://aws.amazon.com/quick/), the next evolution of Amazon Q Business. Existing Amazon Q Business customers can continue to use the service.
The Amazon Q Developer IDE plugins reach end of support on April 30, 2027, and new sign-ups ended on May 15, 2026. For similar capabilities, including agentic coding, chat, and Model Context Protocol (MCP) support, explore [Kiro](https://kiro.dev/).

------
#### [ Amazon Quick Suite ]

[Amazon Quick Suite](https://aws.amazon.com/quick/) is an AI-powered workspace that helps people find answers, create content, analyze data, and complete tasks across their enterprise data and applications. It's the next evolution of Amazon Q Business.

------
#### [ Kiro ]

[Kiro](https://kiro.dev/) is an agentic development environment that helps developers plan, build, test, and ship software, with agentic coding, chat, and Model Context Protocol (MCP) support.

------
#### [ Generative AI in other AWS services ]

Many AWS services include built-in generative AI features. For example, [Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-q-connect.html) provides AI-powered recommendations for contact center agents, and Amazon SageMaker Unified Studio includes AI assistance for writing code and SQL. If an existing AWS service already includes the capability you need, consider starting there.

------

 **Amazon Bedrock: Build and scale generative AI applications with managed foundation models**

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed, serverless service for building generative AI applications. It provides access to a broad selection of [foundation models (FMs)](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) from Amazon and leading providers, including [Amazon Nova](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html), Anthropic Claude, OpenAI, Meta Llama, Mistral AI, DeepSeek, Google Gemma, Qwen, Cohere, AI21 Labs, and Stability AI, through a single API. You don't manage any infrastructure, and with on-demand inference you pay for what you use, with no cost when your application is idle.

Because Amazon Bedrock offers model-independent API access, you can evaluate, switch, and upgrade models with minimal code changes. Supported models are updated regularly. Amazon Bedrock also provides what you need to build applications with security, privacy, and responsible AI, regardless of the model you choose.

![Diagram showing Amazon Bedrock's broad choice of models, from Amazon and other model providers.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/amazon-bedrock-models-feb-2025.jpg)

 Learn more about the key features of Amazon Bedrock:

------
#### [ Model choice and Marketplace ]

Choose from serverless models in the Amazon Bedrock catalog, or use the [Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html) to discover, test, and use more than 100 additional popular, emerging, and specialized FMs. Marketplace models are deployed to endpoints managed by Amazon SageMaker AI. Unlike the serverless catalog models, they run on instances you choose.

------
#### [ Model customization ]

[Model customization](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) can deliver differentiated experiences for your use case. Amazon Bedrock supports:
+ **Supervised fine-tuning:** Train a model on your own labeled examples to improve performance on specific tasks.
+ **Reinforcement fine-tuning:** Improve model alignment with your use case by defining reward functions (for example, with AWS Lambda or a model acting as a judge) instead of labeled input-output pairs.
+ **Distillation:** Transfer knowledge from a larger, more capable teacher model to a smaller, faster, and more cost-efficient student model.
+ **Continued pre-training:** Train a model on your own unlabeled data to make it more domain-specific.

Support varies by customization method, model, and AWS Region, and the list of supported models is updated regularly. For the current list, see [Customize your model to improve its performance for your use case](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html).

With [Amazon Bedrock Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html), you can bring custom models that you fine-tuned, adapted, or pre-trained elsewhere, such as in Amazon SageMaker AI, and run them in Amazon Bedrock with on-demand throughput. Custom Model Import supports a set of open-weight model architectures, and model weights must be in Hugging Face format. It's available in a limited set of AWS Regions and has size and context-length limits. For the supported architectures and current details, see [Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html).

------
#### [ Cross-Region inference ]

[Cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) profiles route your requests across AWS Regions to give you higher throughput and better resilience during traffic peaks. There are two types:
+ **Geographic cross-Region inference** keeps processing within a geographic boundary, such as the US, EU, or Asia Pacific. Use it when you have data residency requirements.
+ **Global cross-Region inference** can route requests to any supported commercial AWS Region worldwide. Per the [global cross-Region inference documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html), it saves approximately 10% on input and output token pricing compared to geographic cross-Region inference.

There's no additional routing cost. You pay based on the Region you call the inference profile from. Data stays on the AWS network and is encrypted in transit between Regions, and AWS CloudTrail logs each request in your source Region, including the Region where the request was processed. Provisioned Throughput isn't currently supported through inference profiles.

------
#### [ Knowledge Bases ]

[Amazon Bedrock Knowledge Bases ](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) is a fully managed capability for implementing the full retrieval augmented generation (RAG) workflow, from ingestion to retrieval and prompt augmentation, without building custom integrations to your data sources. With RAG, a model can use up-to-date information from document repositories, databases, and APIs. Amazon Bedrock Knowledge Bases stores embeddings in vector stores such as Amazon OpenSearch Service Serverless, Amazon Aurora PostgreSQL, Amazon Neptune Analytics, Amazon S3 Vectors, Pinecone, and Redis Enterprise Cloud. It also connects to business data sources such as Salesforce, Confluence, and SharePoint.

**Note**
Starting September 30, 2026, you can't create new Confluence, SharePoint, Salesforce, or Web Crawler connectors on customer-managed knowledge bases. Existing connectors keep working. For new applications that need these connectors, we recommend Amazon Bedrock Managed Knowledge Base. For more information, see [Connect to Confluence for your knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/confluence-data-source-connector.html).

------
#### [ Guardrails ]

[Amazon Bedrock Guardrails ](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) evaluates user inputs and model responses against policies specific to your use case, regardless of the underlying model. You can block denied topics, filter harmful content, redact sensitive information, and use contextual grounding checks to detect hallucinated responses in RAG and summarization applications.

------
#### [ Converse API and tool use ]

Use the [Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html) to build conversational applications with a consistent interface across models. With [tool use (function calling)](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html), a model can call tools that you define, such as APIs or databases, to generate its responses.

------
#### [ Prompt management and Flows ]

Use [prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) to create, version, and reuse prompts across workflows. Use [Amazon Bedrock Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html) (previously called Prompt Flows) to build generative AI workflows visually by linking prompts, models, knowledge bases, guardrails, and other AWS services such as AWS Lambda.

------
#### [ Model evaluation ]

Use [Amazon Bedrock model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) to compare models on your own data, with automatic metrics, human reviewers, or a model acting as a judge.

------
#### [ Amazon Bedrock in Amazon SageMaker Unified Studio ]

[Amazon Bedrock in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock.html) (previously called Amazon Bedrock IDE) lets you discover Amazon Bedrock models, try prompts in a playground, and build generative AI apps that use features such as knowledge bases and guardrails, with little or no code.

------

**Note**
Amazon Bedrock Agents is now Amazon Bedrock Agents Classic and is no longer open to new customers as of July 30, 2026. Existing customers can continue to use it. For new agent development, use Amazon Bedrock AgentCore. Your existing Amazon Bedrock models, Knowledge Bases, and Guardrails aren't affected.

 **Amazon Bedrock AgentCore: Build and operate AI agents**

Use [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) to build, deploy, and operate AI agents securely at scale, using any framework or foundation model, including models hosted outside Amazon Bedrock. AgentCore became generally available on October 13, 2025. It provides modular services that you can use together or independently. These include Harness (a managed agent loop you can call with a single API), Runtime, Memory, Gateway (for turning APIs and Lambda functions into MCP tools), Identity, Code Interpreter, Browser, and Observability.

AgentCore works with open source agent frameworks such as the Strands Agents SDK (an open source framework from AWS), LangGraph, CrewAI, and LlamaIndex, and it supports protocols such as MCP and Agent2Agent (A2A).

Consider how much agentic behavior your use case needs:
+ **Single model call:** For tasks that a model can complete in one request and response, such as content generation, summarization, or classification, call a foundation model directly through Amazon Bedrock.
+ **Single agent:** For tasks that require reasoning, tool use, or multiple steps, build an agent that can plan, call tools, and keep context. Use AgentCore to run the agent, and a framework such as Strands to define its logic.
+ **Multiple agents:** For complex workflows that benefit from specialized agents working together, use AgentCore Runtime with AgentCore Memory to share context across agents.

 **Options to host, customize, and train models**

When you need to run inference on a model that isn't available in Amazon Bedrock, or you need more control over how a model is served, customized, or trained, AWS offers options with increasing levels of control and operational ownership. Start with the most basic question about your workload: do you only need *inference on available models*, or do you need to *customize or train models* (and then run inference on them)?
+ For inference on available models, from frontier model providers or open-weight model providers, Amazon Bedrock is the default starting point. It gives you a serverless, managed experience with no infrastructure to operate.
+ Amazon SageMaker AI, Amazon SageMaker HyperPod, self-managed infrastructure, and AWS Partner solutions in AWS Marketplace are deliberate choices. You choose one because a workload needs something beyond inference on an available model, such as a model that isn't offered as a managed service, deeper control, or training and customization.

Many organizations run several models (commercial and open-weight; text, multimodal, and other modalities), each chosen for a specific workload. Make this choice for each workload individually rather than once for your whole organization.

For a detailed comparison of the managed-versus-control tradeoff, see [Amazon Bedrock or Amazon SageMaker AI?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/bedrock-or-sagemaker.html)

The following table summarizes when each hosting option fits, from the most managed experience to full control.

**Hosting options, from most managed to full control**

| **Option** | **When it fits** |
| --- | --- |
| Amazon SageMaker AI inference endpoints | Hosting open-weight or custom models in standard formats with control over the serving stack, while AWS manages instances, deployment, autoscaling, and monitoring. |
| Amazon SageMaker HyperPod | Large-scale training, one accelerator pool shared across training and inference, and advanced inference optimizations, while AWS manages cluster resiliency and node health. |
| Self-managed on Amazon EC2, Amazon EKS, or Amazon ECS | Any model format or framework with maximum control, where you manage everything above the instance. |

Use the most managed option that supports the capabilities your workload needs.

------
#### [ Amazon SageMaker AI ]

With [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) (previously called Amazon SageMaker), you can build, train, customize, and deploy machine learning models, including foundation models, at scale. Consider it when you need to host models that aren't available in Amazon Bedrock, customize models beyond what Amazon Bedrock supports, or control how models are served.

Amazon SageMaker AI provides purpose-built tools for the full ML lifecycle, including IDEs, distributed training, model evaluation, MLOps, governance, and a range of inference options with recommendations. Key features for generative AI include:
+ [Amazon SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html): An ML hub with hundreds of open-weight and proprietary foundation models. You can deploy these models in a few steps and customize them with techniques such as Parameter-Efficient Fine-Tuning (PEFT) and Low-Rank Adaptation (LoRA).
+ [Amazon SageMaker AI inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html): Deploy models to managed real-time endpoints with autoscaling, or use [Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) for intermittent traffic without managing instances. Serverless Inference doesn't support GPUs, so it suits smaller models that run on CPU. Large foundation models typically need GPU-based real-time endpoints.
+ Model evaluation, the [Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-apps.html) IDEs, and [Amazon SageMaker AI Partner AI Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps.html) that run within your Amazon SageMaker AI environment.

Amazon SageMaker AI is part of the next generation of Amazon SageMaker, which also includes Amazon SageMaker Unified Studio, a single data and AI development environment.

------
#### [ Amazon SageMaker HyperPod ]

Amazon SageMaker HyperPod provides resilient clusters for large-scale training and inference. It automatically detects and replaces unhealthy nodes, so long-running jobs can continue. HyperPod can move accelerator capacity between training and inference on the same cluster to improve utilization, and it supports advanced inference optimizations. For more information, see [Deploying models on Amazon SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment.html).

------
#### [ Self-managed on Amazon EC2, Amazon EKS, or Amazon ECS ]

Run models on infrastructure you manage when you need full control over the model format, serving framework, and operating environment, or when you've standardized on a specific platform such as Kubernetes. You're responsible for deployment, scaling, patching, monitoring, and resiliency.

------

After you've decided that you need more than Amazon Bedrock offers, use these rules to choose:
+ **Amazon SageMaker AI:** Choose it for training, customization, and inference of models in standard formats when you want the most managed experience. Use Amazon SageMaker AI inference endpoints to serve the models.
+ **Amazon SageMaker HyperPod:** Choose it for models in nonstandard formats, or when you want more control over your training and inference frameworks, while AWS still manages the underlying compute and cluster resiliency.
+ **Self-managed on Amazon EC2, Amazon EKS, or Amazon ECS:** Choose it when you need full control over the training, customization, and inference process, with nothing between your team and the instances.

You can also use generative AI solutions from AWS Partners through [AWS Marketplace](https://aws.amazon.com/marketplace/). These solutions range across the same spectrum of control. Buying through AWS Marketplace keeps the spend on your AWS bill. Before you route production traffic to a partner solution, review the partner's service level agreement (SLA), data handling, and security practices.

 **Infrastructure for training and inference**

 AWS offers accelerated compute for generative AI training and inference. You can use it through Amazon SageMaker AI, Amazon SageMaker HyperPod, or directly with Amazon EC2, Amazon EKS, Amazon ECS, and AWS Batch.
+ [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/) provides AWS-designed AI chips for training and serving models. The latest generation, [Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/ec2/instance-types/trn3/) powered by Trainium3, scales up to 144 Trainium3 chips in a single system and delivers higher performance and energy efficiency than Trn2 UltraServers for frontier-scale training and inference. Trn2 instances and UltraServers are also available.
+ [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/) provides AWS-designed AI chips for inference. [Amazon EC2 Inf2 instances](https://aws.amazon.com/ec2/instance-types/inf2/), powered by up to 12 Inferentia2 chips, are designed for high-performance, cost-efficient deep learning and generative AI inference.
+ NVIDIA GPU instances: [Amazon EC2 P6 instances and P6e UltraServers](https://aws.amazon.com/ec2/instance-types/p6/) (NVIDIA Blackwell and Blackwell Ultra) for the most demanding training and inference workloads; [P5 instances](https://aws.amazon.com/ec2/instance-types/p5/) (NVIDIA H100 and H200) for training and inference; and [G6e instances](https://aws.amazon.com/ec2/instance-types/g6e/) (NVIDIA L40S) for cost-efficient inference and graphics workloads.

AWS Trainium and AWS Inferentia use the AWS Neuron SDK, which supports PyTorch, JAX, and vLLM.

## Consider
<a name="consider"></a>

Before you consider specific services, answer these questions for each workload:

1. **What do you need to do?** Use an assistant, build an application or agent, run inference on an existing model, or customize or train a model?

1. **Which models do you need?** Are they available in Amazon Bedrock, in Amazon SageMaker JumpStart, or only as weights you own?

1. **Where must data be processed?** Which AWS Regions do you need, and do you have data residency requirements?

1. **What does your traffic look like?** Variable or spiky, or steady and predictable? What are your latency and throughput targets?

1. **What do you already have?** Existing compute commitments, a standard platform (such as Kubernetes), or MLOps tooling?

1. **Who operates it?** How much infrastructure and model-serving expertise does your team have?

The following criteria help you weigh those requirements against the generative AI options.

------
#### [ What you're building ]

**What it is:** The kind of work the service needs to support: employee productivity, a custom application or agent, or hosting and customizing models.

**Why it matters:** Employee productivity and software development assistance are served by an AI assistant such as Amazon Quick Suite or Kiro. Building your own application or agent points to Amazon Bedrock and Amazon Bedrock AgentCore. Hosting, customizing, or training models yourself points to Amazon SageMaker AI, Amazon SageMaker HyperPod, or self-managed infrastructure.

------
#### [ Model availability ]

**What it is:** Whether the foundation model you need is available as a managed, serverless model in Amazon Bedrock.

**Why it matters:** If your model is available in Amazon Bedrock, or you can bring it in with Amazon Bedrock Custom Model Import, you can use it without managing infrastructure. If the model isn't available, for example a specific open-weight model, a newer version, or a model in a nonstandard format, you'll need to host it. Use Amazon SageMaker AI or Amazon SageMaker HyperPod for models in standard formats, including those in Amazon SageMaker JumpStart. Use self-managed infrastructure for nonstandard or proprietary formats.

------
#### [ Level of control ]

**What it is:** How much control you need over the serving engine, model configuration, customization pipeline, and underlying infrastructure.

**Why it matters:** Amazon Bedrock manages model serving for you, which removes operational work but limits your control over the serving stack. If you need to tune the tradeoff between cost, latency, and throughput yourself, for example by choosing the inference engine, applying optimizations such as speculative decoding or custom quantization, or using specific accelerator types, use Amazon SageMaker AI inference, Amazon SageMaker HyperPod, or self-managed infrastructure. More control means more operational responsibility.

------
#### [ AWS Regions and data residency ]

**What it is:** Where your inference requests and data are processed, and whether the models and features you need are available there.

**Why it matters:** Model and feature availability varies by AWS Region. In Amazon Bedrock, cross-Region inference can increase available throughput:
+ If you can process data anywhere, global cross-Region inference provides the highest throughput at lower cost.
+ If you must keep processing within a geography such as the US or EU, use geographic cross-Region inference.
+ If you must keep processing within a single Region where your model isn't available in Amazon Bedrock, host the model in that Region with Amazon SageMaker AI, Amazon SageMaker HyperPod, or self-managed infrastructure.

Provisioned Throughput isn't supported through cross-Region inference profiles. A custom or imported model that runs on Provisioned Throughput can't use cross-Region inference to get more capacity. Check each model's regional availability in [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) and Amazon SageMaker AI instance availability in your target Regions before you finalize your architecture.

------
#### [ Capacity and throughput ]

**What it is:** Whether you can get enough inference throughput or accelerator capacity where you need it. Capacity can override every other criterion in this guide: the right option on paper isn't the right option if it can't get enough capacity in the Region you need.

**Why it matters:** For Amazon Bedrock, check the service quotas for your models and Region, consider cross-Region inference for higher throughput, and use Provisioned Throughput for workloads that need consistent performance. For instance-based options (Amazon SageMaker AI, Amazon SageMaker HyperPod, and self-managed), accelerator availability varies by instance type and Region. For predictable capacity, plan ahead with options such as reserved capacity. For example, [Amazon SageMaker AI training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html) let you reserve accelerator capacity for training jobs, HyperPod clusters, and inference endpoints. If a specific accelerator instance type is in short supply in a Region, it can affect Amazon SageMaker AI endpoints, HyperPod, and self-managed instances alike, so confirm capacity across all the options you're considering, not just one.

------
#### [ Cost and usage patterns ]

**What it is:** How pricing models line up with your traffic.

**Why it matters:** With Amazon Bedrock on-demand inference, you pay per token with no idle cost, which suits variable, spiky, or unpredictable traffic. Instance-based options charge for provisioned compute whether or not it's in use, so they become more cost-efficient only at sustained, high utilization, or when you can apply existing compute commitments. Compare per-token cost against the fully loaded cost of the instances you'd need, including the cost of operating them, by using your own request volumes and utilization data. Before you count on savings from an existing compute commitment, check which services and resources it covers.

------
#### [ Operational responsibility ]

**What it is:** How much infrastructure and model-serving work your team can take on.

**Why it matters:** Amazon Bedrock has the lowest operational burden. Amazon SageMaker AI manages the instances and deployment while you manage the model stack. Amazon SageMaker HyperPod handles cluster resiliency while you manage orchestration. Self-managed infrastructure gives you full control and full responsibility. Choose the most managed option that gives you the control you need.

------
#### [ Customization needs ]

**What it is:** Whether, and how deeply, you need to adapt a model to your data and tasks.

**Why it matters:** Many use cases need no customization: good prompts and RAG with Amazon Bedrock Knowledge Bases are often enough. If you need more, Amazon Bedrock supports supervised fine-tuning, reinforcement fine-tuning, distillation, and continued pre-training for supported models. For models or techniques that Amazon Bedrock doesn't support, or for full fine-tuning and training from scratch, use Amazon SageMaker AI, Amazon SageMaker HyperPod, or self-managed infrastructure.

------
#### [ Using more than one service ]

**What it is:** Combining services within one architecture.

**Why it matters:** The best answer isn't always a single service, and architectures that combine services are common and healthy. Plan for more than one service if you need to balance speed of delivery, regulatory requirements, capacity, cost per token, or a mix of open-weight and proprietary models. A common pattern is to use Amazon Bedrock for frontier and proprietary models, and Amazon SageMaker AI or Amazon SageMaker HyperPod for fine-tuned or open-weight models, with both behind a common gateway layer and consistent safeguards such as Amazon Bedrock Guardrails. Because models and service capabilities change quickly, review your choices regularly.

------
#### [ Validate before you commit ]
+ **Use your own data.** Validate routing logic, performance, and the economics of reserved capacity on your own workload and utilization data, not on published behavior or list prices.
+ **Plan constrained, multi-Region workloads early.** The hardest cases combine several constraints: residency that is required per Region, a core model that can't be imported into Amazon Bedrock, and several Regions with limited capacity. Global cross-Region inference can't help where residency must stay within a Region. Treat this as one coordinated capacity-planning exercise across all Regions from the start, rather than a series of separate platform changes made Region by Region.

------

 **Choosing a foundation model**

After you've chosen a service, choose the foundation model (FM) that gives you the best results for your use case. [Amazon Bedrock model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) and Amazon SageMaker AI model evaluation can help you compare models on your own data. Consider the following factors:
+ **Modality:** The types of input and output you need, such as text, images, video, audio, or embeddings. For example, use a text model such as Amazon Nova 2 Lite or Anthropic Claude for language tasks; an embeddings model such as Amazon Nova Multimodal Embeddings or [Amazon Titan Text Embeddings V2](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) for search and RAG; an image model such as Amazon Nova Canvas or Stability AI Stable Image for image generation; and Amazon Nova Reel or Luma AI Ray2 for video generation.
+ **Quality of response:** Accuracy, relevance, robustness, toxicity, and fairness of outputs for your tasks. This is usually the most important criterion.
+ **Inference latency:** How quickly the model responds. Smaller models are usually faster and cheaper; larger models might give more detailed responses.
+ **Context window:** How much information the model can consider in a single request, which matters for long documents and long conversations.
+ **Reasoning and tool use:** Whether the model supports multistep reasoning and calling tools, which matters for agents.
+ **Price:** The cost per token or per request compared to the value the model delivers. Smaller models can offer strong results at lower cost.
+ **Customization support:** Whether the model supports the customization method you need.
+ **Lifecycle:** How long the model version remains available. Amazon Bedrock models move through Active, Legacy, and End-of-Life states, so plan for upgrades. See [Model lifecycle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html).

If you plan to customize a model, also consider the quality and quantity of your training data. Relevance, accuracy, consistency, balance, bias, and labeling quality all directly affect results:
+ **Quality:** Use data that is relevant, accurate, and consistent. Be aware of bias and fairness, verify that any labels are high quality, and clean and preprocess the data before training.
+ **Quantity:** Larger, balanced datasets help a model learn a wider range of patterns and generalize better. If data is limited, consider data augmentation or transfer learning, and continue to monitor and update your dataset as your application evolves.

## Choose
<a name="choose"></a>

 **Quick decision path for inference**

For inference workloads, start with Amazon Bedrock. Then check the following, in order. Each one is a common reason to choose a different option:

1. **Is the model unavailable in Amazon Bedrock?** If you have access to the model (for example, an open-weight model) and it can't be brought in with Amazon Bedrock Custom Model Import, host it on Amazon SageMaker AI or Amazon SageMaker HyperPod (standard formats) or self-managed infrastructure (nonstandard or proprietary formats). If no AWS option meets your timeline, consider an AWS Partner inference provider.

1. **Do you need deeper control?** If you need to tune the inference engine, the serving stack, or the training and customization pipeline to manage cost, latency, and throughput yourself, choose Amazon SageMaker AI, Amazon SageMaker HyperPod, or self-managed infrastructure.

1. **Is the model unavailable in the Region you need?** If residency rules require a Region where the model isn't offered, and cross-Region inference doesn't meet those rules, host it in that Region on Amazon SageMaker AI, Amazon SageMaker HyperPod, or self-managed infrastructure. If no AWS option meets your timeline, consider an AWS Partner inference provider.

1. **Do you have existing compute commitments or steady, high volume?** Provisioned instances on Amazon SageMaker AI or Amazon SageMaker HyperPod can cost less than per-token pricing. Check which services your commitments cover before you rely on them.

**Capacity can override all of these.** Whatever the checks point to, confirm that the option can get enough capacity in your Regions.

 **Match needs to services**

The following table maps common needs to AWS services. For inference workloads, start at the top of the hosting options and move down only when a requirement calls for more control.

**Matching needs to AWS services**

| **Need** | **Recommended service** | **Consider instead** |
| --- | --- | --- |
| Boost employee productivity with AI across enterprise data | Amazon Quick Suite | Generative AI features built into the AWS services you already use |
| AI assistance for software development | Kiro | None |
| Build a generative AI application using leading foundation models, with no infrastructure to manage | Amazon Bedrock | Amazon SageMaker AI, if your model isn't available in Amazon Bedrock |
| Ground model responses in your own data (RAG) | Amazon Bedrock Knowledge Bases | A custom RAG pipeline on Amazon SageMaker AI or self-managed infrastructure |
| Build, deploy, and operate AI agents | Amazon Bedrock AgentCore | None |
| Apply consistent safeguards across models | Amazon Bedrock Guardrails | None |
| Customize a supported model with fine-tuning, reinforcement fine-tuning, or distillation | Amazon Bedrock model customization | Amazon SageMaker AI, for other models or techniques |
| Run inference on an open-weight or custom model that isn't in Amazon Bedrock | Amazon SageMaker AI inference endpoints (standard formats) | Amazon Bedrock Custom Model Import (supported architectures); self-managed (nonstandard formats) |
| Control the serving engine and optimize cost, latency, and throughput | Amazon SageMaker AI inference endpoints or Amazon SageMaker HyperPod | Self-managed on Amazon EC2, Amazon EKS, or Amazon ECS |
| Share accelerators between large-scale training and inference | Amazon SageMaker HyperPod | Self-managed on Amazon EKS |
| Keep processing within a geography | Amazon Bedrock with geographic cross-Region inference | In-Region hosting on Amazon SageMaker AI, if the model isn't available |
| Keep processing within a single Region where your model isn't available in Amazon Bedrock | Amazon SageMaker AI or Amazon SageMaker HyperPod in that Region | Self-managed in that Region |
| Get the highest throughput and lowest per-token cost without residency limits | Amazon Bedrock with global cross-Region inference | None |
| Run steady, high-volume inference, or use existing compute commitments | Amazon SageMaker AI or Amazon SageMaker HyperPod | Amazon Bedrock Provisioned Throughput; self-managed |
| Use any model format or framework with full control | Self-managed on Amazon EC2, Amazon EKS, or Amazon ECS | Amazon SageMaker HyperPod |
| Train or pre-train large models | Amazon SageMaker HyperPod | Amazon SageMaker AI training jobs; self-managed |
| Get the best price-performance for training and inference infrastructure | AWS Trainium and AWS Inferentia | Amazon EC2 GPU instances |
| Combine frontier and open-weight models in one architecture | Amazon Bedrock and Amazon SageMaker AI behind a common gateway | None |
| Fill a temporary model or capacity gap that no AWS option meets today | AWS Partner inference provider in AWS Marketplace, behind a large language model (LLM) gateway with Amazon Bedrock as the primary target | Hosting in the needed Region on Amazon SageMaker AI or self-managed |

 **Common scenarios**

The following scenarios are common starting points. Validate them against your own requirements.
+ **Always use the latest frontier models.** If you mainly use leading proprietary models and want to adopt new versions quickly, Amazon Bedrock is a good fit. Check model availability and throughput in your Regions.
+ **Optimize cost with a mix of models.** If you use frontier models for some tasks and a few open-weight models for others to reduce cost, use Amazon Bedrock for the frontier models and Amazon SageMaker AI for the open-weight models. Together they give you the most managed experience across both.
+ **Meet strict regulatory or long-term contractual requirements.** If you must keep a specific model version in production for a long time, even after newer models replace it, host open-weight or custom models on Amazon SageMaker AI or Amazon SageMaker HyperPod. This gives you control over the model lifecycle, and you can reserve capacity in the Regions you need.

## Use
<a name="use"></a>

Now that you've reviewed the criteria for choosing an AWS generative AI service, you can select the services that fit your needs and explore how to get started with each one.

------
#### [ Amazon Quick Suite ]

**Note**
Amazon Q Business is no longer open to new customers as of July 31, 2026. For similar capabilities, explore [Amazon Quick Suite](https://aws.amazon.com/quick/), the next evolution of Amazon Q Business. Existing customers can continue to use the service.
+ **Get started with Amazon Quick Suite**

  Learn about the AI-powered workspace that combines business intelligence, AI-assisted chat, workflow automation, and research.

  [Explore the Amazon Quick Suite getting started guide](https://docs.aws.amazon.com/quick/latest/userguide/getting-started.html)

+ **Amazon Q Business availability change**

  Learn how to migrate from Amazon Q Business to Amazon Quick Suite.

  [Explore the Amazon Q Business availability change guide](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html)

------
#### [ Kiro ]

**Note**
The Amazon Q Developer IDE plugins reach end of support on April 30, 2027, and new sign-ups ended on May 15, 2026. For similar capabilities, including agentic coding, chat, and Model Context Protocol (MCP) support, explore [Kiro on the Kiro website](https://kiro.dev/).
+ **Get started with Kiro**

  Use Kiro in the IDE, CLI, web, or mobile to plan features with specs, fix bugs, and connect tools with MCP.

  [Explore the documentation on the Kiro website](https://kiro.dev/docs/getting-started/)

+ **Migrate from Amazon Q Developer**

  Learn how to move from the Amazon Q Developer IDE plugins to Kiro.

  [Explore the Amazon Q Developer end of support guide](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html)

------
#### [ Amazon Bedrock ]
+ **What is Amazon Bedrock?**

  Learn how to use this fully managed service to access foundation models through a single API.

  [Explore the introduction to Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)

+ **Supported foundation models**

  See which models are available, with their capabilities and Regions.

  [Explore the supported foundation models guide](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)

+ **Cross-Region inference**

  Learn how to increase throughput with geographic and global cross-Region inference profiles.

  [Explore the cross-Region inference guide](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)

+ **Customize models**

  Learn about fine-tuning, reinforcement fine-tuning, distillation, and continued pre-training.

  [Explore the model customization guide](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html)

+ **Frequently asked questions about Amazon Bedrock**

  Get answers to the most commonly asked questions about Amazon Bedrock.

  [Read the FAQs](https://aws.amazon.com/bedrock/faqs/)

------
#### [ Amazon Bedrock in Amazon SageMaker Unified Studio ]

**Note**
Amazon Bedrock IDE is renamed to Amazon Bedrock in Amazon SageMaker Unified Studio.
+ **What is Amazon Bedrock in Amazon SageMaker Unified Studio?**

  Discover Amazon Bedrock models and build generative AI apps with little or no code.

  [Explore the Amazon Bedrock in Amazon SageMaker Unified Studio guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock.html)

+ **Build a chat agent app with Amazon Bedrock**

  Build a chat agent app that lets users chat with an Amazon Bedrock model through a conversational interface.

  [Explore the chat agent app tutorial](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/create-chat-app.html)

------
#### [ Amazon Bedrock AgentCore ]
+ **What is Amazon Bedrock AgentCore?**

  Learn how to build, deploy, and operate AI agents securely at scale.

  [Explore the Amazon Bedrock AgentCore guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)

+ **Get started with Amazon Bedrock AgentCore**

  Follow the steps to set up AgentCore and deploy your first agent from the command line.

  [Explore the AgentCore getting started guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-cli.html)

------
#### [ Amazon SageMaker AI ]
+ **What is Amazon SageMaker AI?**

  Learn how you can use this fully managed machine learning (ML) service to build, train, and deploy ML models into a production-ready hosted environment.

  [Explore the Amazon SageMaker AI guide](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)

+ **Get started with Amazon SageMaker JumpStart foundation models**

  Deploy and customize open-weight models.

  [Explore the Amazon SageMaker JumpStart foundation models guide](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html)

+ **Deploy models for inference**

  Learn about Amazon SageMaker AI inference options.

  [Explore the model deployment guide](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)

+ **Deploy inference endpoints with reserved GPU capacity**

  Use training plans to secure capacity for inference.

  [Read the blog post on the AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/deploy-sagemaker-ai-inference-endpoints-with-set-gpu-capacity-using-training-plans/)

------
#### [ Amazon SageMaker HyperPod ]
+ **Deploy models on Amazon SageMaker HyperPod**

  Use HyperPod for inference with autoscaling and intelligent routing.

  [Explore the HyperPod model deployment guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment.html)

+ **Best practices to run inference on Amazon SageMaker HyperPod**

  Learn recommended practices for serving models on resilient HyperPod clusters.

  [Read the inference best practices post on the AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/best-practices-to-run-inference-on-amazon-sagemaker-hyperpod/)

------
#### [ Amazon Nova ]
+ **What is Amazon Nova 2?**

  Explore the Amazon Nova 2 family of foundation models available in Amazon Bedrock.

  [Explore the Amazon Nova 2 guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html)

+ **Get started with Amazon Nova in the Amazon Bedrock console**

  Learn how to use the playgrounds in the AWS Management Console to submit a prompt to Amazon Nova models and generate a text or image response.

  [Explore the Amazon Nova getting started guide](https://docs.aws.amazon.com/nova/latest/userguide/getting-started-console.html)

------
#### [ AWS Trainium and AWS Inferentia ]
+ **Amazon EC2 Trn3 UltraServers**

  Learn about Trn3 UltraServers, powered by AWS Trainium3, for frontier-scale training and inference.

  [Explore Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/ec2/instance-types/trn3/)

+ **Amazon EC2 Inf2 instances**

  Learn how Amazon EC2 Inf2 instances, powered by AWS Inferentia2, deliver cost-efficient generative AI inference.

  [Explore Amazon EC2 Inf2 instances](https://aws.amazon.com/ec2/instance-types/inf2/)

+ **Use AWS Inferentia with Amazon EKS**

  Create an Amazon EKS cluster with nodes running Amazon EC2 Inf2 instances for machine learning inference.

  [Explore the AWS Inferentia with Amazon EKS guide](https://docs.aws.amazon.com/eks/latest/userguide/inferentia-support.html)

------
#### [ Amazon EC2 GPU instances ]
+ **Amazon EC2 P6 instances**

  Learn about P6 instances and P6e UltraServers, accelerated by NVIDIA Blackwell and Blackwell Ultra GPUs, for demanding training and inference workloads.

  [Explore Amazon EC2 P6 instances](https://aws.amazon.com/ec2/instance-types/p6/)

------

## Explore
<a name="explore"></a>
+  **Generative AI inference architecture and best practices on AWS**

   Prescriptive guidance for choosing and designing generative AI inference architectures.

   [Read the guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/amazon-bedrock.html)

+  **Architecture diagrams**

   These reference architecture diagrams show examples of AWS AI and ML services in use.

   [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23ai-ml&awsf.industries=*all&awsf.business-category=*all)

+  **Whitepapers**

   Explore whitepapers to help you get started and learn best practices in choosing and using AI and ML services.

  [ Explore whitepapers](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23ai-ml&awsf.industries=*all&awsf.business-category=*all)

+  **AWS solutions**

   Explore vetted solutions and architectural guidance for common use cases for AI and ML services.

   [ Explore solutions](https://aws.amazon.com/solutions/ai/)

+  **AWS Builder Center**

   Articles, videos, and tips from AWS and the builder community on building, deploying, and scaling AI agents and generative AI applications.

   [Explore the Builder Center](https://builder.aws.com/)

+  **Related decision guides**

   Explore related decision guides for machine learning and for choosing between Amazon Bedrock and SageMaker AI.

   [Choosing an AWS machine learning service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/ml-guide.html)

   [Amazon Bedrock or Amazon SageMaker AI?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/bedrock-or-sagemaker.html)

## Resources
<a name="resources"></a>

 **Foundation models**

Amazon Bedrock provides access to foundation models from Amazon and leading providers through a single API. The list is updated regularly. For the current list, with capabilities and Regions, see [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html). Providers currently include:
+ [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/)
+ [Anthropic Claude](https://aws.amazon.com/bedrock/claude/)
+ OpenAI
+ [Meta Llama](https://aws.amazon.com/bedrock/llama/)
+ [Mistral AI](https://aws.amazon.com/bedrock/mistral/)
+ DeepSeek
+ Google Gemma
+ Qwen
+ [Cohere Command & Embed](https://aws.amazon.com/bedrock/cohere-command-embed/)
+ [AI21 Labs](https://aws.amazon.com/bedrock/jurassic/)
+ [Stability AI](https://aws.amazon.com/bedrock/stable-diffusion/)

Use Amazon Bedrock and Amazon SageMaker AI to experiment with a variety of foundation models, and privately customize them with your data. To explore generative AI quickly, you can also use [PartyRock, an Amazon Bedrock Playground](https://partyrock.aws/). PartyRock is a generative AI app building playground where you can experiment hands-on with prompt engineering.

 **Associated blog posts**
+  [ Amazon Bedrock model evaluation is now generally available](https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/)
+  [ Fine-tune and deploy language models with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/fine-tune-and-deploy-language-models-with-amazon-sagemaker-canvas-and-amazon-bedrock/)
