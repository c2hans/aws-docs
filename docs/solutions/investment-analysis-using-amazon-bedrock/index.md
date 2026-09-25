---
source_url: https://docs.aws.amazon.com/solutions/investment-analysis-using-amazon-bedrock/index.html
---

---
title: 'Guidance for Investment Analysis Using Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/investment-analysis-using-amazon-bedrock/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Investment Analysis Using Amazon Bedrock

## Overview

This Guidance demonstrates how Amazon Bedrock, which offers a range of large language models (LLMs), can perform generative AI-powered analysis on structured and unstructured data sets to support investment analysts. Tools offered by AWS generative AI services process complex instructions, such as investment analysis and goals. The resulting analysis is presented as a text summary, referencing relevant data to support the reasoning, enabling investment analysts to actively manage investments for institutional or individual clients more effectively.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/investment-analyst-on-aws.pdf)

![Architecture diagram](/images/solutions/investment-analysis-using-amazon-bedrock/images/investment-analysis-using-amazon-bedrock-1.png)

1. **Step 1**: AWS Amplify React using Cloudscape app is hosted on Amazon Simple Storage Service (Amazon S3) and served through Amazon CloudFront, which is secured using AWS WAF.
1. **Step 2**: The user authenticates to the application through Amazon Cognito user pools. The application retrieves an API key, URL, and Amazon Cognito user pool ID from AWS Secrets Manager.
1. **Step 3**: Analysts provide a stock ticker or stock name on the app for performing fundamental income statement analysis. The app interacts with the backend through Amazon API Gateway WebSockets.
1. **Step 4**: AWS Lambda WebSocket handler retrieves financial data, and a specific prompt is sent to the Amazon Nova Pro model to perform quantitative data analysis and obtain a financials summary. View summary data in chart, tabular, and summary format in the application.
1. **Step 5**: A Lambda function is configured as a web authorizer within API Gateway. This function validates the ID token against Amazon Cognito to authenticate the user.
1. **Step 6**: The Lambda WebSocket handler stores the WebSocket connection within Amazon DynamoDB.
1. **Step 7**: Amazon Bedrock Agents invokes Lambda to obtain live news data (through AlphaVantage API). The large language model (LLM) summarizes stock ticker sentiment.
1. **Step 8**: For analyst queries, the retriever chain is executed to perform similarity search on data stored in the vector store. Results are sent along with the prompt to an Amazon Nova Pro model available on Amazon Bedrock. The LLM provides answers for queries along with citations.
1. **Step 9**: A Lambda function triggers ingestion of documents into Amazon Bedrock Knowledge Bases.
1. **Step 10**: Vector data of research documents are stored in Amazon OpenSearch Serverless.
1. **Step 11**: Amazon Bedrock Agents invokes a Lambda function, which sources news from third-party sources.
1. **Step 12**: Amazon Bedrock Guardrails are configured and used to sanitize the output from the Amazon Nova Pro models.
1. **Step 13**: CloudFront is configured with AWS WAF to protect against malicious access.
1. **Step 14**: Amazon CloudWatch and AWS CloudTrail provide logging and tracing.
1. **Step 15**: AlphaVantage, Yahoo, and FactSet provide various financial data.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Deploy this Guidance Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-investment-analyst-assistant)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Bedrock and Lambda enable your application to scale automatically based on demand, eliminating the need for manual infrastructure management. These services ensure your application can handle fluctuating user demand with ease, providing high availability and fault tolerance through managed services. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Safeguard your application and user data with Amazon Cognito, which provides secure user authentication and authorization. Secrets Manager securely stores sensitive credentials, preventing exposure in your application's code or configuration. Enhance your website's security with CloudFront, which offers traffic encryption and access controls. Use AWS Identity and Access Management (IAM) policies to scope down to the minimum permissions required, limiting unauthorized access to resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Elastic Load Balancing (ELB) routes traffic requests from the store’s mobile application to healthy Amazon Elastic Compute Cloud (Amazon EC2) instances. Distribute your Streamlit-based frontend globally with CloudFront, caching content closer to your users for improved reliability and availability. By incorporating a monitoring and observability service services like Amazon CloudWatch, you can quickly identify and resolve reliability issues. The synchronous loose coupling provided by ELB reduces the chance of application failure, so your users can browse the mobile application without encountering downtime errors. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda and Amazon Bedrock Agents handle high-volume traffic, provide low-latency responses, and scale automatically to meet your application's evolving performance needs. Additionally, CloudFront reduces latency for your users by caching content closer to them, improving the perceived performance of your application. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda functions are charged based on the number of invocations and the duration of execution, allowing your application to run without incurring fixed infrastructure costs. With Amazon Bedrock, you pay only for what you consume through input and output token pricing, without the need to manage or handle the underlying infrastructure. By using these serverless and managed services, your application can scale up and down as needed, paying only for the resources it consumes, and minimizing the overall operational costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Databse instances powered by AWS Graviton3 processors enable you to reach your sustainability innovation goals faster and with 60 percent less energy consumption than comparable Intel-based processors. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
