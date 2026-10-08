---
source_url: https://docs.aws.amazon.com/solutions/agentic-workflow-assistants-on-aws/index.html
---

---
title: 'Guidance for Agentic Workflow Assistants on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/agentic-workflow-assistants-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Agentic Workflow Assistants on AWS

## Overview

This Guidance demonstrates how to leverage generative AI to enhance operational efficiencies and drive innovation for energy organizations. It shows how to build agent-based assistants by incorporating large language model (LLM)-based agentic workflows for autonomous task execution. By analyzing diverse data points, including equipment failures, maintenance history, and supplier information, these agents can provide real-time decision support, generate actionable insights, and optimize operations

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/agentic-workflow-assistants-on-aws.pdf)

![Architecture diagram](/images/solutions/agentic-workflow-assistants-on-aws/images/agentic-workflow-assistants-on-aws.png)

1. **Step 1**: Source business documents, data files, and diagrams from shared drives such as SharePoint or the internet. Amazon Simple Storage Service (Amazon S3) stores private company data, allowing the agent to store and retrieve contextual information. Amazon Bedrock Knowledge Bases contains vectorized embeddings stored in serverless Amazon Aurora or Amazon OpenSearch Serverless.
1. **Step 2**: Users can interact with agents securely through a simple chat interface secured by Amazon Cognito. A user-selected agent is configured to use the correct LLM with persona-optimized instructions and settings.
1. **Step 3**: AWS AppSync hosts a GraphQL API, which handles sending user queries to the agents in the backend which process the request.
1. **Step 4**: Amazon Bedrock Agents automates multi-step tasks by seamlessly connecting with company systems, APIs, and data sources.
1. **Step 5**: AWS Lambda functions can be configured as Amazon Bedrock action groups to provide tool capabilities. The agent uses tools to perform deterministic real-time enterprise data queries (for example, text-to-SQL), API calls, and engineering calculations to incorporate into the user response.
1. **Step 6**: Amazon Bedrock Knowledge Bases provides Amazon Bedrock Agents with vectorized versions of business documents for fast retrieval of multimodal data. Agents can contribute to their own knowledge base to continue learning from new interactions.
1. **Step 7**: Enable existing enterprise data sources through agent tools and by periodic embeddings into knowledge bases. This solution provides both options to optimize each business use case for accuracy, performance, and cost. For example, Amazon Athena enables the LLM agent to query structured data stores by executing SQL queries.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Bedrock, Amazon Simple Storage Service (Amazon S3), Amazon Cognito, and AWS Amplify work together to improve productivity. Foundation models available on Amazon Bedrock deliver contextual information from company data sources, while Amazon S3 integrates for efficient data storage. Amazon Cognito handles secure user authentication, and Amplify streamlines deployment of resources and the web front-end. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito provides robust authentication and authorization features. This fully managed service controls secure access while integrating seamlessly with other AWS services. Amazon Cognito also integrates with existing Active Directory instances, eliminating the need for additional log-ins and allowing you to maintain your current user accounts and configurations. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon Bedrock hosts generative AI models, agents, and knowledge bases, while Amazon Cognito manages user authentication and user pools. Amazon S3 stores knowledge base artifacts reliably, and AWS Amplify hosts front-end resources. This approach removes manual infrastructure management tasks, resulting in high availability and consistent performance. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amplify drives performance efficiency in this architecture. Amplify enhances performance by providing comprehensive development tools for building and deploying web and mobile applications, offering automated enhancements and optimized resource utilization. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon Bedrock offers a pay-per-token pricing model, which reduces costs by eliminating the need for infrastructure investments or model training costs. Amazon S3 provides flexible storage categories that optimize costs based on usage patterns. These tiered storage classes and lifecycle management features automatically move data to cost-effective storage tiers. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon Bedrock and Amazon S3 minimize environmental impact through efficient resource utilization. Amazon Bedrock is a fully managed service that eliminates the need to run dedicated infrastructure for foundation models, creating a more sustainable approach than direct model hosting. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
