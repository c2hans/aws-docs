---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/introduction.html
---

# AWS Security Reference Architecture (AWS SRA) – AI security

*Avik Mukherjee, Amazon Web Services*

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This guide provides architectural patterns for securing AI workloads on AWS. It extends the [AWS SRA – core architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html). The core architecture establishes the account, network, identity, and security monitoring foundation. This guide explains how to apply that foundation to models, knowledge bases, AI applications, and agents. The targeted business outcome is to help you adopt AI capabilities at scale with confidence in your security posture through reduced data exposure, auditable model releases, authorized agent actions, and faster security reviews.

The guidance follows the [AWS AI Security Framework](https://aws.amazon.com/blogs/security/the-aws-ai-security-framework-securing-ai-with-the-right-controls-at-the-right-layers-at-the-right-phases/)'s three use cases: AI that answers, AI that connects, and AI that acts. Each use case adds controls for the data and operations available to the application. The [framework reference](https://dp8l2mfblnx2f.cloudfront.net/framework/) organizes controls by security layer and implementation phase, from prototype development through production deployment and ongoing improvement. The guide covers [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html), and models and agents on compute you operate.

## Intended audience
<a name="intended-audience.aeb68b00-f764-578a-8783-b87797d9dfca"></a>

This guidance is for security architects, platform teams, application developers, and AI/ML teams responsible for designing, implementing, or reviewing the security of AI workloads on AWS. It assumes familiarity with AWS accounts and [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html). The [related AWS SRA guides](https://dp8l2mfblnx2f.cloudfront.net/about-sra-library/) explain the shared security foundation.

### Start with your workload
<a name="start-with-your-workload"></a>

Use [Account and trust boundaries](https://dp8l2mfblnx2f.cloudfront.net/architecture/) to separate development from production inference and protected training. Select guidance for what the workload can do: generate responses, retrieve information, or use tools and take actions.
+ [**AI that answers: models**](https://dp8l2mfblnx2f.cloudfront.net/answers/)**.** Apply model inference controls. Include customization controls if you train or adapt a model. Bedrock and Amazon SageMaker AI have separate recommendations.
+ [**AI that connects: knowledge bases**](https://dp8l2mfblnx2f.cloudfront.net/connects/)**.** Add controls for applications that retrieve information from enterprise data sources to ground model responses.
+ [**AI that acts: agentic AI and actions**](https://dp8l2mfblnx2f.cloudfront.net/acts/)**.** Add authorization, execution, and recovery controls for agents that choose tools, delegate tasks, or take actions.

A workload can combine these capabilities. An agent that retrieves documents and updates tickets needs all three sets of controls. Agent tool use belongs to **AI that acts**, including read-only tools. Limit each tool's data access and apply approval and recovery controls when it can change systems.

Most AI workload type sections include the following information:
+ **Security considerations** describes risks specific to the capability.
+ **Remediations** reviews the AWS services and features that address the risks, grouped by infrastructure security, identity and data security, and AI application security.
+ **Design considerations** describes additional design decision points.

[AI application access](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/) covers user access across all three use cases. It covers custom applications and managed products, including [Kiro](https://kiro.dev/docs/enterprise/identity-provider/) and [AWS Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/setting-up-sso.html).

### How to use this guide
<a name="how-to-use-this-guide"></a>

Follow these four steps for both an architecture review and an implementation.

![A structured approach to use the SRA AI security guide to break down your work into phased approach.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/d81bbe6b-02a8-4815-82fa-e01b1fc0dfd8.png)

***Fig 1: A structured approach to build your implementation plan based on this guide***

1. **Establish account boundaries and choose a path.** Identify the accounts, data access, and owners. Select the guidance above for the models, knowledge bases, and agents in the workload.

1. **Threat model the workload.** Create a workload data-flow diagram showing assets and trust boundaries. Identify plausible attacks using the [generative AI threat modeling guidance](https://aws.amazon.com/blogs/security/threat-modeling-your-generative-ai-workload-to-evaluate-security-risk/). Record the owner and planned mitigations for each boundary.

1. **Apply the relevant controls.** Use the threat model to select controls for the services and data paths in the workload. The detailed guidance uses the framework's [three security layers](references.md#review-three-security-layers): infrastructure security, identity and data security, and AI application security. Keep the applicable model and retrieval controls when adding an agent.

1. **Verify and record decisions.** Use the "Verification and next steps" section of the guide to test allowed and denied behavior, collect evidence, and assign owners to remaining risks. Repeat the review when models, data, tools, permissions, or deployment choices change.

If you need a prioritized set of minimum baseline controls before you start building your architecture, focus on

When AI decisions can affect individuals or communities, assess those impacts alongside security risks. Record affected stakeholders, potential harms, and mitigations in the workload's [responsible AI risk assessment](https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr03-bp04.html). Apply the impact assessment requirements that are relevant to your use case and obligations.

### AWS AI Services
<a name="aws-ai-services"></a>

#### Amazon Bedrock
<a name="amazon-bedrock.54bfd037-ae2d-5501-b508-eae7537f8fce"></a>

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) helps you build and scale generative AI applications with foundation models (FMs). As a fully managed service, it provides access to FMs from a broad set of providers through a [single API](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html). For the current list of supported model providers, see [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html). You can experiment with pre-trained models, customize them with your data, and deploy them into your applications without training models from scratch or managing specialized infrastructure.

Amazon Bedrock helps you protect your data through the following security capabilities:
+ **Data protection** – Amazon Bedrock isolates your content by user, encrypts it at rest in your AWS Region, and encrypts it in transit using Transport Layer Security (TLS) 1.2 or higher.

For more information, see the [AWS secure approach to generative AI](https://aws.amazon.com/ai/generative-ai/security/).

#### Amazon Bedrock model evaluation
<a name="amazon-bedrock-model-evaluation.b9e15f14-cabc-57c8-bfb4-bf22e87fb085"></a>

Model evaluation helps you compare FM outputs and select the model that fits your application requirements. Amazon Bedrock supports both automatic evaluation using prompt datasets and human evaluation with subject matter experts.

*Automatic evaluation* jobs assess model performance using either custom prompt datasets or built-in datasets. This approach provides quantitative metrics for comparing models at scale. For more information, see [Creating an automatic model evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-automatic.html) and [Use prompt datasets for model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-prompt-datasets.html) in the Amazon Bedrock documentation.

*Human evaluation* jobs incorporate input from employees or subject matter experts to assess model quality, relevance, and safety. You organize evaluators into work teams managed through Amazon SageMaker Ground Truth. Create and manage work teams during job setup in Amazon Bedrock, or use the Amazon Cognito or [Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html) consoles for ongoing management.

##### Security
<a name="security.80825c02-37a8-5002-8714-2c7422eab623"></a>

We recommend that you run model evaluation in development environments, not production. For information about multi-account strategies, see the [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/ou-structure-for-non-production-environments.html) whitepaper. Both evaluation types require IAM service roles with the following permissions:
+ Automatic evaluation jobs require permissions to access Amazon Simple Storage Service (Amazon S3) datasets and write results.
+ Human evaluation jobs require additional permissions for Amazon SageMaker Ground Truth integration.
+ Custom prompt datasets require cross-origin resource sharing (CORS) configuration on Amazon S3 buckets.

For more information, see [Service role requirements for automatic model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/automatic-service-roles.html) and [Service role requirements for human-based model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-eval-service-roles.html) in the Amazon Bedrock documentation.

Amazon Bedrock creates a temporary copy of your evaluation data during the job and deletes it after completion. By default, Amazon Bedrock encrypts this data with an AWS managed key. We recommend that you use a customer managed key in AWS KMS for enhanced control over data access. For more information, see [Data management and encryption in Amazon Bedrock evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-data-management.html) in the Amazon Bedrock documentation.

#### Amazon Bedrock AgentCore
<a name="amazon-bedrock-agentcore.2be07ca3-dc3e-5829-a0c4-45011b6e2709"></a>

[Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) provides infrastructure and controls for deploying AI agents securely at scale. AgentCore consists of the following modular services that work together or independently:
+ **AgentCore Runtime** – Serverless execution environment with session isolation
+ **AgentCore Identity** – Authentication and credential management for agents and tools
+ **AgentCore Memory** – Persistent storage for conversation history and context
+ **AgentCore Gateway** – Centralized API integration and tool access through a unified endpoint
+ **AgentCore Policy** – Policy-based governance for agent actions
+ **AgentCore Observability** – Trace, debug, and monitor agent performance
+ **AgentCore Evaluations** – Assess agent quality through online and on-demand testing
+ **AgentCore Code Interpreter** – Enables agents to write and run code securely in sandbox environments, improving accuracy and helping them solve complex end-to-end tasks
+ **AgentCore Browser** – Cloud-based browser runtime that enables agents to interact with websites and carry out web-based workflows at scale
+ **AgentCore Optimization** – Turns production traces into continuous agent improvement through a structured loop: identify problems, generate data-driven fixes, validate them before deployment, and verify that they work
+ **AgentCore Registry** – A single place to discover, reuse, and govern AI agents, tools, and agent skills across your organization
+ **AgentCore Payments** – Helps AI agents autonomously access and pay for resources they need, such as APIs, Model Context Protocol (MCP) servers, web content, and other agents, without requiring you to build payment logic from scratch

AgentCore works with popular agent frameworks (for example, CrewAI, LangGraph, LlamaIndex, and Strands Agents) and with FMs. AgentCore provides security capabilities including session isolation through dedicated micro virtual machines (microVMs), encrypted credential storage, namespace-based memory isolation, and audit logging.

#### Amazon SageMaker AI
<a name="amazon-sagemaker-ai.b4602ca9-6b46-58f2-953a-08f14dad92ba"></a>

Amazon SageMaker AI is a fully managed service that brings together a broad set of tools to enable machine learning (ML) for a wide range of use cases. With SageMaker AI, you can build, train, and deploy ML models at scale using tools like notebooks, debuggers, profilers, pipelines, MLOps, and more, all in one integrated development environment (IDE). SageMaker AI supports governance requirements with simplified access control and transparency over your ML projects. In addition, you can build your own FMs, which are large models trained on massive datasets, with purpose-built tools to fine-tune, experiment, retrain, and deploy FMs. SageMaker AI also offers access to hundreds of pretrained models, including publicly available FMs, that you can deploy in a few steps.

SageMaker AI stores code in ML storage volumes, which you can control with security groups and optionally encrypt at rest. SageMaker AI encrypts ML model artifacts and other system artifacts in transit and at rest. SageMaker AI API and console requests use a secure TLS connection. You pass [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html?refid=cc991d8b-c588-45ae-9eed-6d677245de05) to SageMaker AI to provide permissions to access resources on your behalf for training and deployment. You can use encrypted Amazon S3 buckets for model artifacts and data, and you can pass an AWS KMS key to SageMaker AI notebooks, training jobs, and endpoints to encrypt the attached ML storage volume. SageMaker AI also supports Amazon VPC and AWS PrivateLink. SageMaker AI doesn't use or share customer models, training data, or algorithms.

#### AWS Continuum
<a name="aws-continuum.a70ff356-f690-575d-a432-98565f488eb3"></a>

[AWS Continuum](https://docs.aws.amazon.com/continuum/latest/userguide/what-is-continuum.html) helps you discover, prioritize, validate, and remediate security risks across the software lifecycle, within the guardrails you define. Before code ships, it helps identify risks in your designs and code. After your systems are running, it helps determine which risks matter to your business, validates which are exploitable, and helps you fix them.

AWS Continuum offers a frontier agent that helps secure your applications throughout the software development lifecycle. It conducts automated security reviews tailored to your organizational requirements and delivers context-aware penetration testing on demand. By continuously validating security from design to deployment, it helps you identify vulnerabilities early in development.

AWS Continuum for code vulnerabilities addresses the lifecycle of a code vulnerability, from discovery through remediation. It analyzes your environment, confirms which findings are valid, and helps you resolve them. It is model-agnostic, using multiple frontier models for the tasks they perform well, and is designed to incorporate new models as they become available.
