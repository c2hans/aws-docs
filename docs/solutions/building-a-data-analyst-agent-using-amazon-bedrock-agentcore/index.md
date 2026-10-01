---
source_url: https://docs.aws.amazon.com/solutions/building-a-data-analyst-agent-using-amazon-bedrock-agentcore/index.html
---

---
title: 'Guidance for Building a Data Analyst Agent using Amazon Bedrock AgentCore'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-data-analyst-agent-using-amazon-bedrock-agentcore/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Building a Data Analyst Agent using Amazon Bedrock AgentCore

## Overview

This Guidance demonstrates how organizations can overcome the challenge of making structured data accessible to non-technical users by enabling natural language querying across datasets using Amazon Bedrock AgentCore with intelligent agent-based processing. The system automatically processes uploaded data files to create searchable metadata with semantic understanding, allowing users to ask business questions in plain English through a secure web interface. When queries are submitted, the AI agent discovers the most relevant datasets and generates appropriate database queries, then uses advanced language models to interpret results and create visualizations that make complex data insights immediately understandable. You can transform your organization's data accessibility by empowering business users to get instant, accurate answers from complex datasets without requiring SQL knowledge or technical expertise.

## Benefits

### Eliminate data discovery bottlenecks instantly.

Empower your analysts to find and query hundreds of datasets using natural language, replacing manual search with semantic AI-driven discovery across your entire data lake.

### Accelerate insights with automated analysis.

Reduce time-to-insight by letting an AI agent automatically generate SQL queries, interpret results, and produce visualizations — so your teams focus on decisions, not data wrangling.

### Deploy secure, scalable analytics confidently.

Protect your data lake with built-in authentication, WAF-based threat protection, and managed infrastructure, so you can scale self-service analytics without compromising governance or security.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-a-data-analyst-agent-using-amazon-bedrock-agentcore.pdf)

![Architecture diagram](/images/solutions/building-a-data-analyst-agent-using-amazon-bedrock-agentcore/images/building-a-data-analyst-agent-using-amazon-bedrock-agentcore-1.png)

1. **Step 1**: Admin uploads Parquet data files to Amazon Simple Storage Service (Amazon S3) using provided Python scripts for structured dataset storage.
1. **Step 2**: Amazon S3 PUT event triggers AWS Lambda function to read Parquet schema and create AWS Glue tables for Amazon Athena querying.
1. **Step 3**: Admin uploads JSON metadata files with dataset descriptions, dimensions, and keywords to Amazon S3 metadata bucket.
1. **Step 4**: Amazon S3 event triggers AWS Lambda to extract metadata from JSON files, generate vector embeddings via Amazon Bedrock, and index them in Amazon S3 Vectors, a purpose-built service for cost-effective vector storage and semantic search by meaning rather than exact keywords.
1. **Step 5**: User accesses static React web app hosted on Amazon S3 through an AWS Web Application Firewall (WAF)-protected Amazon CloudFront distribution with HTTPS termination and global caching.
1. **Step 6**: Amazon Cognito handles user authentication directly in the browser using Amazon Amplify libraries. After sign-in, the React app receives a token for secure API calls.
1. **Step 7**: React app sends the user's natural language query with the Amazon Cognito token directly to the to the Data Analyst Strands Agent (open-source Strands Agents SDK) on Amazon Bedrock AgentCore runtime, a purpose-built platform for deploying AI agents at scale.
1. **Step 8**: Agent searches Amazon S3 Vectors to discover datasets most semantically similar to the query.
1. **Step 9**: Agent executes SQL queries against discovered Amazon Athena tables with appropriate filters and aggregations.
1. **Step 10**: Agent passes Amazon Athena results to Amazon Bedrock, a fully managed foundation model service with security and responsible AI features, using Anthropic Claude Opus 4.5 to interpret intent, analyze results, and generate Python code for visualization.
1. **Step 11**: Response with natural language answer, optional visualizations, metrics, and dataset references displayed in web app chat interface.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-agentic-data-analyst-using-amazon-bedrock-agentcore-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
