---
source_url: https://docs.aws.amazon.com/solutions/retrieving-data-using-natural-language-queries-on-aws/index.html
---

# Guidance for Retrieving Data Using Natural Language Queries on AWS

## Overview

This Guidance demonstrates how to efficiently retrieve data by using the agent-driven framework of Amazon Bedrock to convert natural language queries (NLQ) into SQL queries. The agent-driven approach allows the Amazon Bedrock Agents to interpret your natural language input, break down complex queries, and delegate specific actions to the appropriate large language models (LLMs) and services. The agents orchestrate the entire process in an automated and coordinated manner, eliminating the need for you to manually construct database queries. By using Amazon Bedrock Agents to handle the complex task of NLQ-to-SQL conversion, you can access and analyze data more efficiently and accurately.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/retrieving-data-using-natural-language-queries-on-aws.pdf)

![Architecture diagram](/images/solutions/retrieving-data-using-natural-language-queries-on-aws/images/retrieving-data-using-natural-language-queries-on-aws-1.png)

1. **Step 1**: Company data is loaded into Amazon Simple Storage Service (Amazon S3), which serves as the data source for AWS Glue.
1. **Step 2**: Amazon Athena is a serverless query service that analyzes Amazon S3 data using standard SQL with AWS Glue managing the data catalog. AWS Glue reads unstructured data from Amazon S3, creates queryable tables for Athena, and stores query results back in Amazon S3. This integration, supported by crawlers and the AWS Glue Data Catalog, streamlines data management and analysis.
1. **Step 3**: The AWS Lambda function acts as the execution engine, processing the SQL query and interfacing with Athena. Proper configuration of resource policies and permissions is critical for secure and efficient operations, maintaining the integrity of the serverless compute environment.
1. **Step 4**: The main purpose of an action group in an Amazon Bedrock agent is to provide a structured way to perform multiple actions in response to a user's input or request. This allows the agent to take a series of coordinated steps to address the user's needs, rather than just performing a single action. This action group includes an OpenAPI schema. The schema is needed so that the Amazon Bedrock agent knows the format structure and parameters for the action group to interact with the compute layer. In this case, the compute layer is a Lambda function.
1. **Step 5**: An instruction prompt is provided to the Amazon Bedrock agent to help with orchestration. The Amazon Bedrock agent orchestrates the tasks by interpreting the input prompt and delegating specific actions to the LLM.
1. **Step 6**: Collaboration with the task orchestrator in the previous step enables the LLM to process complex queries and generate outputs that align with the user's objectives. The chain of thought mechanism ensures that each step in the process is logically connected, leading to precise action execution. The model processes the user's natural language input, translating it into actionable SQL queries, which are then used to interact with data services.
1. **Step 7**: The Amazon Bedrock agent endpoint serves as the bridge between the user's application that runs on an Amazon Elastic Compute Cloud (Amazon EC2) instance on AWS and the Amazon Bedrock agent, facilitating the transfer of input data in real-time. This setup is essential for capturing inputs that trigger the agent driven process. Natural language is used to query data and return the response back to the user through the user interface. The results from the Athena query are returned to the user from the Lambda function through the Amazon Bedrock agent endpoint.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-retrieving-data-using-natural-language-queries-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon S3 provides scalable and durable storage for source data, making it readily accessible and manageable. AWS Glue automates the data cataloging process by running crawlers and creating tables, streamlining the data integration workflow. Athena enables efficient querying of the data using standard SQL, and Lambda functions integrate with Athena to execute the SQL queries generated by the Amazon Bedrock Agent, facilitating real-time data processing. These services work together to automate data ingestion, cataloging, and querying, enabling quick responses to user queries and streamlining the management of data workflows. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Shield Standard can be integrated to provide protection against distributed denial-of-service (DDoS) attacks. Amazon Bedrock Guardrails offers additional safeguards you can customize. This feature adds another layer of safeguards regardless of the underlying foundation model (FM). It evaluates user inputs and FM responses based on specific policies to detect and block undesirable topics. Moreover, Amazon Bedrock Guardrails filters harmful content, redacts sensitive information, blocks inappropriate content with custom word filters, and detects hallucinations in model responses. AWS Identity and Access Management (IAM) limits unauthorized access by enforcing minimum permissions, and Amazon CloudFront secures data transmission and access so only authorized users can interact with the application. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The services used were designed to provide high availability, automated recovery, and consistent performance. Amazon S3 offers high availability and durability of the stored data. AWS Glue automates data processing tasks, reducing the risk of human error and enabling consistent data handling. Athena allows for reliable and efficient querying of the data. Lambda performs the execution of queries and other tasks without downtime. These services allow your system to quickly adapt to changing demands and recover from potential failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon S3 and AWS Glue optimize data storage and processing for efficient data management. Athena provides quick and efficient data querying capabilities. The use of Lambda allows for the execution of tasks in a serverless environment, further optimizing resource usage. These services provide scalability, optimized resource usage, and the ability to experiment and optimize based on your user data and requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The cost efficiencies are underpinned by the storage, processing, analytics, and compute capabilities of the services. Amazon S3 provides tiered storage options for cost-optimized data retention. AWS Glue automates data processing tasks, eliminating the need for manual interventions. Athena enables cost-efficient analysis of large datasets, without the overhead of dedicated database infrastructure. The use of Lambda functions contributes to cost optimization by providing a serverless execution environment. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3 supports sustainable storage practices by enabling lifecycle policies and tiered storage options, optimizing resource utilization. AWS Glue automates data processing tasks, reducing the need for continuous resource usage. Athena provides efficient data querying capabilities, minimizing the computational resources required. The Lambda functions offer a serverless execution model so that resources are only consumed when necessary. By optimizing resource utilization, reducing waste, and minimizing the environmental impact, these services help you build more sustainable workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
