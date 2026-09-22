---
source_url: https://docs.aws.amazon.com/solutions/sap-generative-ai-assistant-on-aws/index.html
---

---
title: 'Guidance for SAP Generative AI Assistant on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/sap-generative-ai-assistant-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for SAP Generative AI Assistant on AWS

## Overview

This Guidance demonstrates how to improve business user productivity and the user experience by leveraging real-time data summaries, task automation, and seamless natural language interactions. It showcases the integration of Amazon Bedrock for generative AI and Amazon Lex for conversational AI assistant capabilities. The Guidance is designed to be extensible, allowing you to seamlessly extend both SAP S/4HANA native and RISE with SAP capabilities with other AWS services, enabling a more comprehensive and tailored solution for your business needs.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sap-generative-ai-assistant-on-aws.pdf)

![Architecture diagram](/images/solutions/sap-generative-ai-assistant-on-aws/images/sap-generative-ai-assistant-on-aws-1.png)

1. **Step 1**: Extract or federate data from SAP ERP or SAP Datasphere using AWS SAP data integration solutions.
1. **Step 2**: Amazon Athena uses AWS Glue Data Catalog to query the tables directly in Amazon Simple Storage Service (Amazon S3).
1. **Step 3**: The user interacts with their chat application of choice to perform tasks or answer questions.
1. **Step 4**: A natural language chatbot powered by Amazon Lex curates communication to handle the response and sends the user's question to AWS Lambda for processing.
1. **Step 5**: Lambda sends the response and message history back to the chat app through Amazon Lex. Amazon Lex stores the message history in a session.
1. **Step 6**: The Lambda function invokes an Amazon Bedrock endpoint to formulate an Athena query using LangChain framework.
1. **Step 7**: The Lambda function runs generated Athena queries and retrieves data.
1. **Step 8**: Amazon Bedrock interprets the data and generates a response for data retrieved from Athena queries to provide a human-readable response.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-sap-generative-ai-assistant-on-aws/tree/main)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch provides real-time monitoring and insights, enabling swift detection and response to performance issues, security threats, and configuration changes. Complementing this, AWS CloudTrail tracks API calls and resource modifications, offering a comprehensive audit trail for maintaining control and visibility over your infrastructure. By using these services, you can efficiently and effectively manage your systems, driving business agility and enhanced customer satisfaction. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) controls access, enforces least privilege, and manages keys to secure AWS resources. S3 bucket policies and access control lists (ACLs) restrict access to buckets and objects, enforce encryption, and block public access. Implementing these services secures AWS resources and data. When exposing SAP data through Amazon Lex, use IAM roles and Amazon S3 policies to ensure least privilege access and restrict unauthorized access to sensitive data fields. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda, Amazon Lex, Amazon Bedrock, Amazon S3, and Athena offer built-in redundancy and fault tolerance across Availability Zones, promoting high availability without manual configuration. As usage grows, reliability becomes crucial, ensuring consistent availability and performance despite failures or high traffic. Using these services to enhance reliability helps you maintain user trust, prevent revenue loss, and mitigate reputational risks. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS Lambda, Amazon Lex, Amazon Bedrock, Amazon S3, and Athena are serverless services that scale based on demand. Lambda runs your code without managing servers, automatically scaling to meet demand and ensuring efficient resource utilization. Amazon Lex enables seamless conversational interfaces that handle user queries with ease, providing a smooth user experience. Amazon Bedrock empowers you to leverage large-scale ML models, enhancing the performance and accuracy of your applications. Amazon S3 offers highly scalable and durable object storage, while Athena enables efficient data analysis using standard SQL, unlocking valuable insights. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The services in this Guidance support cost optimization through serverless architecture, charging only for resources consumed, and built-in features. For example, Amazon Lex enables cost-effective chatbot development. Lambda runs code without provisioning servers, eliminating idle resource costs. Amazon Bedrock deploys ML models efficiently. Athena allows you to analyze Amazon S3 data using SQL, eliminating complex extract, transform, load (ETL) processes and reducing data processing and storage costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon Lex helps automate customer interactions, reducing the need for energy-intensive physical infrastructure. Lambda and Amazon Bedrock enable efficient, on-demand computing and advanced AI modeling, minimizing energy consumption. Amazon S3 promotes durable and scalable data storage, while Athena facilitates data analysis without the overhead of traditional data warehousing solutions. By using these services, you can reduce your environmental impact and align with sustainable best practices. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
