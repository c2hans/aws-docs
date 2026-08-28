---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-sra.html
---

# AWS SRA for AI
<a name="gen-ai-sra"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This section provides recommendations for securing AI workloads within the AWS SRA multi-account framework. It covers AWS Identity and Access Management (IAM) permissions, data protection, input/output validation, network isolation, logging, and monitoring for generative AI capabilities. This section also covers integrating these capabilities into traditional AWS workloads.

This guidance covers security for the following capabilities:
+ Capability 1. Providing developers and data scientists with secure access to generative AI FMs (model inference)
+ Capability 2. Providing secure access, usage, and implementation for generative AI model customization
+ Capability 3. Providing secure access to data and systems for generative AI
+ Capability 4. Providing secure access, usage, and implementation of tools
+ Capability 5. Providing secure access, usage, and implementation of generative AI agents
+ Capability 6. Providing secure access, usage, and implementation for AI applications

Most capability sections include the following information:
+ **Rationale** explains what the capability does and when to use it.
+ **Security considerations** describes risks that are specific to the capability.
+ **Remediations** reviews the AWS services and features that address the risks.
+ **Recommended AWS services** describes the services to build the capability securely.

All capabilities build on Capability 1 (foundation model inference) because they all invoke models. When you combine capabilities, apply security controls from each relevant section. For example, a customized model with Retrieval Augmented Generation (RAG) requires controls from capabilities 1, 2, and 3.

The following diagram shows the extension of the AWS SRA [Workloads organizational unit (OU)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/application.html) architecture with a dedicated Generative AI OU. The Generative AI OU contains two accounts that separate concerns:
+ The *Application account* hosts your traditional AWS application, which provides specific business functionality.
+ The *Generative AI account* hosts Amazon Bedrock and associated AWS services. Your application in the Application account calls Amazon Bedrock capabilities in the Generative AI account through APIs.

This account separation provides two key benefits. First, it enforces security controls through OU-specific and account-specific service control policies. Second, it simplifies implementing least-privilege access by grouping services based on application type. The reference architecture also includes foundational accounts that apply to all application types: Org Management, Security Tooling, Log Archive, Network, and Shared Services. For more information about these accounts, see [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html) in the *AWS SRA – core architecture* guide.

![AWS SRA architecture to support generative AI.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/f9f7bb45-f187-428a-bd52-a31c0929d309.png)

**Design considerations**:
+ Merge the Application and Generative AI accounts if your architecture requires consolidating both services in one account, or if your generative AI usage spans your entire organization.
+ Separate Generative AI accounts by software development lifecycle (SDLC) environment (development, test, and production) or by model and user community:
  + Use separate OUs for each SDLC environment. This approach controls team access, isolates resources, tracks costs separately, and prevents development issues from affecting production.
  + Use AWS Identity and Access Management (IAM) roles in a single account for pre-trained models. Use separate accounts when user communities have different risk levels, or when customized models contain sensitive training data.
+ Use multiple accounts when different user communities have distinct risk profiles, when customized models contain sensitive training data, or when regulatory requirements mandate data isolation.
+ Use a single account when you only use pre-trained foundation models, when users have a consistent risk profile, or when IAM roles provide sufficient access control.

**Note**
This guide assumes a single generative AI account strategy with IAM roles.

## Amazon Bedrock
<a name="bedrock"></a>

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) helps you build and scale generative AI applications with foundation models (FMs). As a fully managed service, it provides access to FMs from companies such as AI21 Labs, Anthropic, Cohere, Meta, Stability AI, and Amazon through a [single API](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html). You can experiment with pre-trained models, customize them with your data, and deploy them into your applications without training models from scratch or managing specialized infrastructure.

Amazon Bedrock protects your data through the following security capabilities:
+ **Data protection** – Amazon Bedrock isolates your content by user, encrypts it at rest in your AWS Region, and encrypts it in transit using TLS 1.2 or higher.
  + **Data privacy** – Amazon Bedrock doesn't store or log your prompts and completions. AWS doesn't use your content to train models or share it with third parties.
  + **Model customization** – When you customize a foundation model, your changes use a private copy. Your data isn't shared with model providers or used to improve base models.
  + **Abuse detection** – Amazon Bedrock uses automated detection to identify potential violations of the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).
+ **Compliance** – Amazon Bedrock meets these standards: International Organization for Standardization (ISO), System and Organization Controls (SOC), Federal Risk and Authorization Management Program (FedRAMP) Moderate, and Cloud Security Alliance (CSA) Security Trust Assurance and Risk (STAR) Level 2. Amazon Bedrock is Health Insurance Portability and Accountability Act (HIPAA) eligible and in compliance with the General Data Protection Regulation (GDPR).

For more information, see the [AWS secure approach to generative AI](https://aws.amazon.com/ai/generative-ai/security/).

## Amazon Bedrock Guardrails
<a name="bedrock-guardrails"></a>

[Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) help you implement safeguards that align with your use cases and responsible AI policies. You configure [filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html#guardrails-content-filters) to block harmful content, define restricted topics, and customize messages that users see when content is blocked.

Guardrails evaluate both user inputs and model outputs across multiple harmful categories (hate, insults, sexual, violence, misconduct, and prompt attacks). The system classifies each input and output into one of four confidence levels: none, low, medium, or high. You set filter strength for each category based on your risk tolerance. When you [deploy a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-deploy.html) to production, you create a versioned instance and invoke it in your application through the Amazon Bedrock API. For more information about implementation steps, see the [Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) section in the Amazon Bedrock documentation.

### Security
<a name="security.949eb760-0f6e-5b0c-bf4a-9683c707f848"></a>

By default, Amazon Bedrock encrypts guardrails with an AWS managed key in AWS Key Management Service (AWS KMS). We recommend that you use a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) to encrypt your guardrails and prevent unauthorized modifications. Combine encryption with [least-privilege IAM permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-permissions.html) to restrict who can view or modify guardrail configurations.

## Amazon Bedrock model evaluation
<a name="bedrock-model-eval"></a>

Model evaluation helps you compare FM outputs and select the model that best fits your application requirements. Amazon Bedrock supports both automatic evaluation using prompt datasets and human evaluation with subject matter experts.

*Automatic evaluation* jobs assess model performance using either custom prompt datasets or built-in datasets. This approach provides quantitative metrics for comparing models at scale. For more information, see [Creating an automatic model evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-automatic.html) and [Use prompt datasets for model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-prompt-datasets.html) in the Amazon Bedrock documentation.

*Human evaluation* jobs incorporate input from employees or subject matter experts to assess model quality, relevance, and safety. You organize evaluators into work teams managed through Amazon SageMaker Ground Truth. Create and manage work teams during job setup in Amazon Bedrock, or use the Amazon Cognito or [Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html) consoles for ongoing management.

### Security
<a name="security.2c4f0950-10fc-5711-988f-834c60de19a4"></a>

We recommend that you run model evaluation in development environments, not production. For information about multi-account strategies, see the [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/ou-structure-for-non-production-environments.html) whitepaper. Both evaluation types require IAM service roles with the following specific permissions:
+ Automatic evaluation jobs require permissions to access Amazon Simple Storage Service (Amazon S3) datasets and write results.
+ Human evaluation jobs require additional permissions for Amazon SageMaker Ground Truth integration.
+ Custom prompt datasets require cross-origin resource sharing (CORS) configuration on Amazon S3 buckets.

For more information, see [Service role requirements for automatic model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/automatic-service-roles.html) and [Service role requirements for human-based model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-eval-service-roles.html) in the Amazon Bedrock documentation.

Amazon Bedrock creates a temporary copy of your evaluation data during the job and deletes it after completion. By default, Amazon Bedrock encrypts this data with an AWS managed key. We recommend that you use a customer managed key in AWS KMS for enhanced control over data access. For more information, see [Data management and encryption in Amazon Bedrock evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-data-management.html) in the Amazon Bedrock documentation.

## Amazon Bedrock AgentCore
<a name="bedrock-agentcore"></a>

[Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) provides infrastructure and controls for deploying AI agents securely at scale. AgentCore consists of the following modular services that work together or independently:
+ **AgentCore Runtime** – Serverless execution environment with session isolation
+ **AgentCore Identity** – Authentication and credential management for agents and tools
+ **AgentCore Memory** – Persistent storage for conversation history and context
+ **AgentCore Gateway** – Centralized API integration and tool access
+ **AgentCore Policy** – Policy-based governance for agent actions
+ **AgentCore tools** – Built-in sandboxed tools (Code Interpreter, Browser)
+ **AgentCore Observability** – Trace, debug, and monitor agent performance
+ **AgentCore Evaluations** – Assess agent quality through online and on-demand testing

AgentCore works with any agent framework (for example, CrewAI, LangGraph, LlamaIndex, and Strands Agents) and any foundation model (FM). AgentCore provides security capabilities including session isolation through dedicated micro virtual machines (microVMs), encrypted credential storage, namespace-based memory isolation, and comprehensive audit logging.

For detailed security guidance, see Capability 5.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
