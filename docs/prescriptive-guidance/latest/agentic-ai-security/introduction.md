---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/introduction.html
---

# Security for agentic AI on AWS
<a name="introduction"></a>

*James Schafer and Melanie Li, Amazon Web Services*

While [agentic AI systems](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/new-generation.html) might be a relatively new concept, many of the security risks they present have well-known, effective controls.

This guide provides practical security recommendations for developing [hosted agentic AI systems](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/agent-hosting-considerations.html) the follow the [perceive, react, act layer](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/generative-ai-agents.html) architecture.** **Hosted agentic AI systems can support various business outcomes with differing risk tolerance levels. Due to this variance, some best practices in this guide are more applicable depending on your use case. Adoption of suitable controls can be phased in and enhanced through the [lifecycle](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-considerations-gen-ai/introduction.html) of the system based on organizational priorities. It's critical to [understand which threats ](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_threat_model.html)are relevant to your workload in order to understand which controls will be effective in achieving alignment with your risk appetite.

For any threat identified, you should implement multiple controls across more than one [security control type](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/security-control-types.html). This guide maps its best practices to the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). It also includes recommendations from multiple sources, focusing on the highest priority aspects for hosted agentic AI systems.

## Intended audience
<a name="intended-audience"></a>

This guide is for architects, developers, and technology leaders who need to safely and compliantly operate AI-driven software agents. To understand the concepts and recommendations in this guide, you should be familiar with modern cloud-native architectures and distributed systems, large language models, foundation model capabilities, DevOps, and platform engineering.

## Objectives
<a name="objectives"></a>

This guide helps you do the following:
+ Understand the design decisions that relate to securely operating hosted agentic AI systems
+ Determine how to design and operate hosted agentic AI systems in accordance with your target risk posture
+ Align functional controls with industry frameworks

## About this content series
<a name="about-series"></a>

This guide is part of a series about agentic AI on AWS. For more information and to view the other guides in this series, see [Agentic AI](https://aws.amazon.com/prescriptive-guidance/agentic-ai/) on the AWS Prescriptive Guidance website.
