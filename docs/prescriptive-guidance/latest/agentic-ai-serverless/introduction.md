---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html
---

# Building serverless architectures for agentic AI on AWS
<a name="introduction"></a>

*Aaron Sempf, Amazon Web Services*

The convergence of AI and serverless computing is reshaping the landscape of modern enterprise architecture. In response, organizations are striving to deliver intelligent capabilities at scale. They face increasing pressure to reduce operational overhead, accelerate innovation, and deploy applications that can adapt in real time to user behavior and system events.

Serverless AI on AWS represents a fundamental shift toward intelligent, adaptive, cloud-native systems. With the right strategy and tooling, organizations can unlock faster innovation cycles, lower costs, and greater scalability. This approach positions them at the forefront of the next generation of enterprise computing. AWS is enabling this shift through a combination of fully managed AI services and event-driven, serverless infrastructure.

This guide outlines the strategic and technical foundations for building AI-native, serverless architectures on AWS. These architectures are scalable, cost-effective, and capable of delivering real-time intelligence without the complexity of managing infrastructure.

## Intended audience
<a name="intended-audience"></a>

This guide is for architects, developers, and technology leaders seeking to harness the power of AI-driven software agents within modern cloud-native applications.

## Objectives
<a name="objectives"></a>

This guide helps you do the following:
+ Understand the AWS native services available for agentic AI solution development
+ Operationalize agentic AI with cloud-scale reliability
+ Align AI execution with business outcomes and cost models
+ Establish a framework for secure, governed AI adoption

## About this content series
<a name="content-series"></a>

This guide is part of a series about agentic AI on AWS. For more information and to view the other guides in this series, see [Agentic AI](https://aws.amazon.com/prescriptive-guidance/agentic-ai/) on the AWS Prescriptive Guidance website.

## The business case of serverless AI
<a name="business-case"></a>

Serverless computing provides an ideal foundation for modern AI workloads. AI applications often require intermittent, compute-intensive inference, especially in use cases such as fraud detection, recommendation engines, document summarization, and customer service automation. Traditional infrastructure models can be expensive and operationally complex when managing unpredictable or spiky workloads.

In contrast, serverless architectures offer significant advantages. They scale automatically, execute on-demand, reduce operational overhead, and charge only for resources used. These features make serverless architectures well-suited for embedding AI into modern cloud-native applications. AWS offers a comprehensive portfolio of services that combine serverless and AI capabilities. These services include Amazon SageMaker Serverless Inference and Amazon Bedrock, which provides access to foundation models through a fully managed, API-based interface. Amazon Bedrock AgentCore extends Amazon Bedrock beyond model access to a complete runtime for building, deploying, and managing autonomous agents.. Additionally, services like AWS Lambda and AWS Step Functions enable the development of agile, cost-aligned, and production-ready AI systems. When paired with services like Amazon Bedrock, SageMaker Serverless Inference, and AgentCore, they provide integrated reasoning, memory, and connector capabilities, allowing developers to create agents that can plan, act, and collaborate across AWS services and external systems. These tools offer powerful support for AI workloads, all within a serverless, event-driven architecture.

AI workloads, particularly inference, are often unpredictable and bursty. In traditional architectures, this leads to overprovisioned infrastructure, increased costs, and complexity in scaling. Serverless models solve these issues by offering:
+ **Elastic scalability** – Resources scale automatically based on demand.
+ **Cost optimization** – No charges for idle compute. Pay only for execution time.
+ **Reduced operational overhead** – Fewer operations, less to manage, and fewer dependencies on other technology, processes, or resources.
+ **Faster time to market** – Developers can focus on business logic and model performance instead of managing servers.
+ **High availability and built-in resilience** – AWS serverless offerings provide these capabilities by default.

These capabilities make serverless a natural fit for deploying AI models across a wide variety of use cases, from fraud detection and personalized recommendations to document analysis and conversational AI.

## AWS services powering serverless AI
<a name="aws-services-powering"></a>

AWS provides a robust suite of managed services that help teams embed intelligence into applications, orchestrate workflows, and react to events without managing infrastructure:
+ With [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), you can run event-driven compute workloads at scale without provisioning servers. It's ideal for AI pre- and post-processing and lightweight inference logic.
+ Use [Amazon SageMaker Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) to deploy machine learning (ML) models for real-time predictions with automatic scaling and no idle charges.
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) provides access to foundation models from leading AI companies like [AI21 Labs](https://aws.amazon.com/bedrock/ai21/?refid=ca65de14-f133-4047-b100-90c1bfbdfe77), [Anthropic](https://aws.amazon.com/bedrock/anthropic/?refid=ca65de14-f133-4047-b100-90c1bfbdfe77&ams%23interactive-card-vertical%23pattern-data.filter=%257B%2522filters%2522%253A%255B%255D%257D), [Cohere](https://aws.amazon.com/bedrock/cohere/?refid=ca65de14-f133-4047-b100-90c1bfbdfe77&ams%23interactive-card-vertical%23pattern-data.filter=%257B%2522filters%2522%253A%255B%255D%257D), [DeepSeek](https://aws.amazon.com/bedrock/deepseek/?refid=ca65de14-f133-4047-b100-90c1bfbdfe77), [Luma AI](https://aws.amazon.com/bedrock/luma-ai/?refid=ca65de14-f133-4047-b100-90c1bfbdfe77), [Meta](https://aws.amazon.com/bedrock/meta/), [Mistral AI](https://aws.amazon.com/bedrock/mistral/?refid=ca65de14-f133-4047-b100-90c1bfbdfe77), [poolside](https://aws.amazon.com/bedrock/poolside/) (coming soon), [Stability AI](https://aws.amazon.com/bedrock/stability-ai/?refid=ca65de14-f133-4047-b100-90c1bfbdfe77), [TwelveLabs](https://aws.amazon.com/bedrock/twelvelabs/), [Writer](https://aws.amazon.com/bedrock/writer/?refid=ca65de14-f133-4047-b100-90c1bfbdfe77), and [Amazon](https://aws.amazon.com/ai/generative-ai/nova/?refid=ca65de14-f133-4047-b100-90c1bfbdfe77) through a single API for generative AI workloads.
+ With [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html), you can build AI-driven workflows where models orchestrate function calls and reason through tasks by using natural language.
+ [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) provides the foundational runtime, memory, and connector capabilities that simplify building and scaling multi-agent systems. Integrating AgentCore into a serverless design allows developers to build adaptive, context-aware agents natively on AWS without managing custom orchestration or state handling.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) enables you to build loosely coupled, event-driven architectures that trigger AI workflows automatically.
+ Use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) to orchestrate multi-step AI pipelines and connect AWS services using visual workflows.
+ With [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) and [Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html), you can deploy models and logic at the edge for low-latency inference in IoT and global applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
