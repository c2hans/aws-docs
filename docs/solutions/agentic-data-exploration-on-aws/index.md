---
source_url: https://docs.aws.amazon.com/solutions/agentic-data-exploration-on-aws/index.html
---

---
title: 'Guidance for Agentic Data Exploration on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/agentic-data-exploration-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Agentic Data Exploration on AWS

## Overview

This Guidance demonstrates how to overcome data fragmentation challenges by using a team of AI agents to automate the discovery, connection, and analysis of information across siloed systems. Users interact with an Amazon Bedrock Supervisor Agent that orchestrates specialized collaborator agents to perform data exploration tasks like schema analysis and transformation. The process begins when diverse data is uploaded to Amazon S3, then processed through Amazon Bedrock Knowledge Bases, while Amazon Bedrock Prompt Flow analyzes data entities to infer relationships and store them in Amazon Neptune graph database. You gain actionable, scalable, and AI-ready insights that drive better decision-making across your organization without manual data integration efforts.

## Benefits

### Unlock insights across diverse data sources

Transform your organization's ability to derive value from both structured and unstructured data through an intelligent multi-agent system. This architecture automatically processes, analyzes, and connects information across formats, enabling comprehensive data exploration without specialized coding skills.

### Accelerate data-driven decision making

Empower business users to interact naturally with complex datasets through an intuitive chat interface backed by specialized AI agents. This approach reduces time-to-insight by automating data preparation, relationship discovery, and complex query processing across your organization's information assets.

### Scale knowledge operations with intelligent automation

Deploy a serverless, event-driven architecture that automatically processes incoming data and makes it accessible through natural language interactions. This solution eliminates manual data preparation tasks while maintaining security controls, allowing your teams to focus on extracting business value rather than managing infrastructure.

## How it works

### Data Ingestion

This architecture diagram illustrates how to effectively support agentic data exploration on AWS. It shows the key components of the data ingestion process for structured and unstructured data.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/agentic-data-exploration-on-aws.pdf#page=1)Step 1Users upload or stream diverse data, such as documents and database exports into Amazon Simple Storage Service (Amazon S3). Note: You may perform additional data preparation when data is ingested depending on the type of content.Step 2Unstructured data is loaded into Amazon Bedrock Knowledge Bases that Amazon Bedrock Agents can later access.Step 3Amazon OpenSearch Service is used to provide vector storage for Amazon Bedrock Knowledge Bases.Step 4The creation of new structured data on Amazon S3 triggers a message to Amazon Simple Queue Service (Amazon SQS).Step 5An AWS Lambda function is used to process messages in the SQS queue.Step 6An Amazon Bedrock Prompt Flow inspects incoming data by analyzing data entities and fields to infer relationships.Step 7CSV files are reformatted and stored in an openCypher compatible format on Amazon S3.Step 8An AWS Lambda function bulk loads data into an Amazon Neptune graph database.Step 9Amazon Neptune stores data nodes and relationships for later use by Amazon Bedrock Agents.### Data Exploration

This architecture diagram illustrates how to effectively support agentic data exploration on AWS. It shows the key components of the multi-agent application used to analyze, process, and search data.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/agentic-data-exploration-on-aws.pdf#page=2)Step 1Users access the front-end web application hosted on Amazon Simple Storage Service (Amazon S3), served by Amazon CloudFront, and secured by Amazon Cognito.Step 2Users interact with the Amazon Bedrock Supervisor Agent through a chat interface. Complex user tasks are divided into specific subtasks and completed by specialized collaborator agents.Step 3A set of Amazon Bedrock Collaborator Agents is used to perform specific data exploration tasks including schema analysis and data transformation as assigned by the supervisor agent.Step 4AWS Lambda functions are used by Amazon Bedrock Collaborator agents as tools analyze, load and query data.Step 5Relational data is translated from CSV to openCypher format for bulk loading into the Amazon Neptune database using AWS Lambda functions.Step 6Users can review data analysis results stored in Amazon DynamoDB tables through the frontend web application.Step 7Amazon Bedrock Knowledge Bases are used to store data that supports Retrieval-Augmented Generation (RAG) by Amazon Bedrock Collaborator Agents.Step 8Amazon Bedrock Collaborator Agents connect to external APIs for data retrieval.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-agentic-data-exploration-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
