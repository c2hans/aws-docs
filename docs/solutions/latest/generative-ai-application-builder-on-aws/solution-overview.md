---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/solution-overview.html
---

# This solution facilitates the development, rapid experimentation, and deployment of generative artificial intelligence (AI) applications
<a name="solution-overview"></a>

Generative AI Application Builder on AWS facilitates the development, rapid experimentation, and deployment of generative artificial intelligence (AI) applications without requiring deep experience in AI. This AWS Solution accelerates development and streamlines experimentation by helping you:
+ Ingest your business-specific data and documents
+ Evaluate and compare the performance of large language models (LLMs)
+ Run multi-step tasks and workflows with AI agents
+ Rapidly build extensible applications, and deploy those applications with an enterprise-grade architecture

Generative AI Application Builder on AWS includes integrations with:
+ LLMs available on [Amazon Bedrock](https://aws.amazon.com/bedrock)
+ LLMs that you have deployed on [Amazon SageMaker AI](https://aws.amazon.com/sagemaker)
+  [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases) for [Retrieval-Augmented Generation](https://aws.amazon.com/what-is/retrieval-augmented-generation/) (RAG)
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) to implement safeguards and reduce hallucinations
+  [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) to build agentic workflows that can carry out task orchestrations and completion
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) to build, deploy, and manage production-ready AI agents with extended runtime support
+  [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers for enterprise data and tool integration

Additionally, this solution enables connections to your choice of model by using LangChain connectors. These connectors are available in an [AWS Lambda](https://aws.amazon.com/lambda) function that deploys with the solution. You can start with the no-code deployment wizard to build generative AI applications for conversational search, AI- generated chatbots, text generation, and text summarization.

This implementation guide provides an overview of the Generative AI Application Builder on AWS solution, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the solution to the Amazon Web Services (AWS) Cloud.

This guide is intended for solution architects, business decision makers, DevOps engineers, data scientists, and cloud professionals who want to implement Generative AI Application Builder on AWS in their environment.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution.<br />The estimated cost for running this solution varies based on the components you deploy and the number of queries.<br />The cost to run the Deployment dashboard with default parameters and 100 active users in the US East (N.Virginia) Region for one month is approximately $20.12 USD per month.<br />The cost for a Text use case deployed without RAG for 1 business user performing 100 queries per day with the LLM is approximately $12.39 USD per month.<br />The cost for a RAG-enabled use case with an Amazon Kendra index supporting 8,000 interactions per day is approximately $204.26 USD per month, plus the cost of the knowledge base. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security-1.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know which AWS Regions support this solution. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/aws-solutions/generative-ai-application-builder-on-aws)  |
