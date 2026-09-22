---
source_url: https://docs.aws.amazon.com/solutions/building-an-automotive-technician-with-multimodal-agentic-ai-on-aws/index.html
---

---
title: 'Guidance for Building an Automotive Technician with Multimodal Agentic AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-an-automotive-technician-with-multimodal-agentic-ai-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Building an Automotive Technician with Multimodal Agentic AI on AWS

## Overview

This Guidance demonstrates how a service technician assistant leverages advanced AI collaboration through AWS services to revolutionize vehicle and machine repairs. By integrating multiple AI agents, knowledge bases, and large language models (LLMs), the system provides real-time, expert-level diagnostic support while continuously learning from successful repairs. The assistant seamlessly orchestrates internal and external data sources, enabling technicians of all experience levels to access comprehensive information about warranties, claims, parts, and service history. This unified approach enhances repair accuracy, boosts technician confidence, and streamlines related administrative processes, creating a more efficient service operation.

## Benefits

### Enhance service information access

Unify technical documentation, service history, and parts data through an intelligent interface. Make informed repair decisions with comprehensive vehicle insights.

### Streamline technician onboarding

Provide instant access to expert-level support and step-by-step repair strategies. Bridge the skills gap between entry-level and experienced technicians.

### Accelerate repair diagnostics

Enable technicians to quickly diagnose complex vehicle issues through AI-powered visual and voice assistance. Reduce repair wait times while improving diagnostic accuracy.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-an-automotive-technician-with-multimodal-agentic-ai-on-aws.pdf)

![Architecture diagram](/images/solutions/building-an-automotive-technician-with-multimodal-agentic-ai-on-aws/images/building-an-automotive-technician-with-multimodal-agentic-ai-on-aws-1.png)

1. **Step 1**: Technician interacts with the solution by text or voice, through React UI, hosted on AWS Amplify, a managed and scalable multi-system hosting service, alongside Amazon Cognito for user login and AWS WAF as public traffic firewall.
1. **Step 2**: The Amazon Bedrock supervisor agent receives input, uses instructions to understand the input, and manages and delegates tasks required to the group of Amazon Bedrock collaborator agents.
1. **Step 3**: Multimodal data sources, such as OEM manuals and parts specification, that are used by the service technician are ingested using Amazon Bedrock Data Automation. Embeddings are stored in vector databases, provided by Amazon OpenSearch.
1. **Step 4**: The group of Amazon Bedrock collaborator agents, including vehicle recall agent, service history agent, diagnostic agent, parts agent, service summary agent, and warranty claim agent, receive tasks from the supervisor agent in parallel and as supervisor agent's predictions require.
1. **Step 4a**: The group of collaborator agents invoke AWS Lambda actions, such as vehicle recall action Lambda, service history action Lambda, and parts action Lambda, as agents' predictions require.
1. **Step 4b**: The group of collaborator agents invoke LLM models, such as Claude Sonnet 3.5 and Amazon Nova (Pro and Sonic) as needed.
1. **Step 4c**: The group of collaborator agents query Amazon Bedrock Knowledge Bases for Automotive, based on agents' predictions.
1. **Step 5**: Collaborator agents use Lambda actions to enable integrations with automotive data sources and perform reads and writes to data sources in realtime. These data sources include Amazon DynamoDB that provides vehicle and parts records, Amazon S3 that stores service notes, and more.
1. **Step 6**: Service supervisor accesses files uploaded through React UI using the web portal provided by AWS Transfer Family Web Apps, a no-code, fully managed app for file access to Amazon Simple Storage Service (Amazon S3).
[Read usage guidelines](/solutions/guidance-disclaimers/)
