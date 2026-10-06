---
source_url: https://docs.aws.amazon.com/solutions/ai-assistants-with-amazon-q-business/index.html
---

---
title: 'Guidance for AI Assistants with Amazon Q Business'
canonical_url: https://docs.aws.amazon.com/solutions/ai-assistants-with-amazon-q-business/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for AI Assistants with Amazon Q Business

Create generative AI-powered assistants with Amazon Q Business to deliver HR support based on enterprise data sources

## Overview

This Guidance demonstrates how enterprises can unlock the value of their data through the powerful generative AI capabilities of Amazon Q Business. By connecting to various data sources and enriching content, HR teams can leverage an AI assistant to provide highly relevant and personalized information to employees. The Guidance focuses on continuously improving generated responses for high-quality, up-to-date content. Designed with security, scalability, and cost-efficiency in mind, this Guidance empowers enterprises to transform how they leverage collective knowledge and better support their workforce.

## How it works

This Guidance helps to deploy an Amazon Q application, connect it with data sources, and implement a chat with an HR application through a custom plugin.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/ai-assistants-with-amazon-q-business.pdf)

![Architecture diagram](/images/solutions/ai-assistants-with-amazon-q-business/images/ai-assistants-with-amazon-q-business-1.png)

1. **Step 1**: The DevOps user deploys the AWS CloudFormation stack to create an Amazon Q application. Using this infrastructure as code method, the stack creates all necessary resources, such as an Amazon Q index, an Amazon Q retriever, an Amazon Q data source, and Amazon Q custom plugin resources (such as AWS Lambda and Amazon DynamoDB), which are required for the custom plugin. Amazon Q Business works with an instance of AWS IAM Identity Center to provision users.
1. **Step 2**: The business user sends a query, such as query on vacation balance or time off, to the Amazon Q application.
1. **Step 3**: The business user may upload their own documents to an Amazon Simple Storage Service (Amazon S3) bucket to serve as the data source (as configured in Step 1) or use the sample documents that come uploaded with this Guidance. The Amazon Q Business application retrieves the most relevant information to the business user's query from this ingested content, for which the business user has access permissions
1. **Step 4**: Amazon Q Business sends the business user's request in addition to the retrieved information as context to the underlying large language model (LLM) within Amazon Q in the form of a prompt.
1. **Step 5**: Amazon Q returns a succinct response to the business user's query based on the context, using responses from the underlying LLM in Amazon Q.
1. **Step 6**: The custom plugin provided with this Guidance includes an HR time off request application. This application stores business user data (such as vacation balance) in a DynamoDB table. The Amazon Q plugin resource contains the OpenAPI schema for this HR application.
1. **Step 7**: The Lambda function in the plugin, invoked by Amazon API Gateway, handles business user time off requests, including checking vacation days, submitting requests, and updating time off balances. The plugin enables a seamless, interactive HR application experience directly within the Amazon Q environment.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-ai-assistants-with-amazon-q-business)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda and DynamoDB enable the creation of custom, task-oriented applications that streamline business processes and enhance user productivity. The Amazon Q index, retriever, and data source components intelligently retrieve relevant information from enterprise data sources, providing comprehensive and accurate responses to user queries. The CloudFormation stack simplifies the deployment and operation of this Guidance, reducing the burden on IT resources. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Integration with IAM Identity Center enhances the security of the Amazon Q Business application by only allowing authorized users to access the application and data, with granular control over permissions. DynamoDB and Lambda provide a secure, managed environment for storing sensitive data and running custom application logic, reducing the security burden on the user. Access control features in Amazon Q Business restrict data and functionality access based on individual or group permissions, protecting critical enterprise data and applications. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The AWS services in this Guidance help ensure that the application can handle fluctuating traffic even in the event of component failures. For example, DynamoDB offers highly available data storage, Lambda contributes resilient and scalable serverless compute, Amazon S3 provides reliable object storage, and IAM Identity Center secures and controls access. Additionally, CloudFormation enables repeatable and consistent infrastructure provisioning, empowering organizations to build robust and dependable applications. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Q provides low-latency data access and automatic scaling for increased loads, resulting in efficient retrieval and processing of relevant information for responses to user queries. The serverless nature of Lambda enables seamless scaling of the custom plugin's functionality without managing underlying infrastructure. Further, DynamoDB and Lambda support the application's performance and efficiency by automatically scaling to handle increased workloads and providing low-latency data access and processing for timely responses to user queries, even during periods of high demand. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda and DynamoDB support cost optimization for the Amazon Q application. As a serverless service, Lambda scales up and down automatically, only consuming and paying for compute resources used. DynamoDB offers pay-as-you-go pricing (meaning you only pay for resources consumed) and auto-scaling so that users only pay for the required storage and throughput. These services help avoid idle or underutilized resources, minimizing operational costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless approach of Lambda, Amazon S3, and DynamoDB helps minimize waste of computing resources and energy consumption by reducing the need for physical infrastructure and server management. Lambda enables more efficient use of computing resources, reducing the overall carbon footprint and environmental impact. These native, managed AWS services improve efficiency and sustainability, as their usage is driven by on-demand workloads—which generally consume less energy than traditional "stateful" workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
