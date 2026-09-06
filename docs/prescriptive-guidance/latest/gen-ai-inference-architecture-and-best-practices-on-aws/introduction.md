---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/introduction.html
---

# Generative AI inference architecture and best practices on AWS
<a name="introduction"></a>

*Oussama Kandakji, Mia Chang, Vivek Gangasani, Paco Gonzalez, Nicolas Jourdan, Christian Kamwangala, Marco Sgroi, and Hamza Usmani, Amazon Web Services*

Organizations that deploy generative AI (gen AI) models such as large language models (LLMs) and multimodal generation models face critical challenges in serving production workloads at scale. These challenges span multiple dimensions including how to:
+ Maintain consistent low-latency responses for real-time applications and user experiences.
+ Implement dynamic capacity scaling to handle unpredictable traffic patterns.
+ Optimize infrastructure costs.
+ Ensure high availability across deployments.

This guide provides comprehensive prescriptive guidance on selecting and implementing appropriate AWS inference services, designing resilient architectures, and applying proven best practices. This guidance can help organizations achieve performant, cost-effective, and reliable gen AI deployments.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for the following:
+ AI and machine learning (ML) teams who have trained gen AI models, like [LLMs](https://aws.amazon.com/what-is/large-language-model/) and multimodal generation models such as [diffusion models](https://aws.amazon.com/what-is/stable-diffusion/), and want to deploy them for production inference
+ Solution architects and technical leaders evaluating AWS inference options.
+ Organizations transitioning from model development to production deployment.
+ AWS Partners and system integrators providing inference solutions and implementation services.
+ Technical decision-makers assessing infrastructure requirements for AI model inference.

To understand the concepts and recommendations in this guide, you should have a basic understanding of ML concepts and AWS services.

## Objectives
<a name="objectives"></a>

The recommendations in this guide can help you achieve the following:
+ Understand the differences between AI training and inference workloads and their unique challenges.
+ Navigate the AWS inference stack (serverless, managed, and self-managed) and select the appropriate service based on key decision criteria.
+ Learn about model and system optimization techniques for efficient inference deployment.
+ Review recommended security controls and learn about responsible AI (RAI) practices for production inference workloads.
+ Leverage the AWS Partner Network to accelerate time-to-market and model distribution.

## Attachments
<a name="attachments-1e4a4636-9247-4346-9ab7-62170783f8a2"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
