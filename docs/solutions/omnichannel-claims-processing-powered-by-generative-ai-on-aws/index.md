---
source_url: https://docs.aws.amazon.com/solutions/omnichannel-claims-processing-powered-by-generative-ai-on-aws/index.html
---

# Guidance for Omnichannel Claims Processing Powered by Generative AI on AWS

## Overview

overview

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/omnichannel-claims-processing-powered-by-generative-ai-on-aws.pdf)

![Architecture diagram](/images/solutions/omnichannel-claims-processing-powered-by-generative-ai-on-aws/images/omnichannel-claims-processing-powered-by-generative-ai-on-aws-1.png)

1. **Step 1**: Amazon CloudFront serves the Claims Processing React Web Application, including an Amazon Connect Customer chat interface. Amazon Cognito and AWS WAF protect CloudFront.
1. **Step 2**: Initiate First Notice of Loss (FNOL) communication through call, SMS, and chat using Amazon Connect Customer and Amazon Lex and webform using the Claims Processing Web Application.
1. **Step 3**: An Amazon DynamoDB table stores claims request details.
1. **Step 4**: Amazon Simple Storage Service (Amazon S3) stores claims documents through the Claims Processing Web Application. Amazon S3 events trigger an AWS Lambda function, which invokes Amazon Textract to analyze documents, such as driver's licenses. The Lambda function also invokes the Amazon Nova Pro large language model (LLM) using Amazon Bedrock to analyze images of vehicle damages. Lambda updates the generated insights, including potential costs to replace and repair the coverable to existing claims records in the DynamoDB table.
1. **Step 5**: Amazon API Gateway and Lambda integrate third-party application data to the Claims Processing Web Application.
1. **Step 6**: The adjuster leverages Amazon Bedrock Knowledge Bases to search for information using API Gateway and Lambda. Amazon S3 stores knowledge articles for the Amazon Bedrock Knowledge Bases. Amazon OpenSearch Serverless is used as the vector database.
1. **Step 7**: The adjuster reviews and adjudicates the claim request using the web application.
1. **Step 8**: The adjuster decision is sent to an Amazon Simple Queue Service (Amazon SQS) queue.
1. **Step 9**: Lambda picks the messages from Amazon SQS and notifies the claimant with the status of the claim request using Amazon Connect Customer.
1. **Step 10**: Lambda picks the messages from Amazon SQS and updates third-party applications for further downstream processing (if required).
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-omnichannel-claims-processing-powered-by-generative-ai-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda facilitates the integration of various AWS services, eliminating the need for manual infrastructure management and reducing the operational overhead associated with on-premises servers. Similarly, AWS Fargate, a serverless compute engine, abstracts away the underlying infrastructure, allowing teams to concentrate on the application logic rather than managing the foundational resources. The capabilities of Amazon Bedrock include analysis of vehicle damage images and the estimation of repair and replacement costs. Furthermore, Amazon Bedrock helps teams to proactively monitor and maintain the health and performance of their AI applications, deploy changes, as well as identify and resolve any issues that may arise. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) controls access to various services used in this Guidance through granular permissions based on roles. IAM policies have been scoped down to the minimum permissions required for the application to function properly. Furthermore, CloudFront, the content delivery network (CDN) service, improves the overall security of the web applications by providing traffic encryption, access controls, and integration with AWS Shield. Shield is a managed service that protects against distributed denial of service (DDoS) attacks, further bolstering the security of the application. Lastly, AWS WAF is integrated with CloudFront to provide an additional layer of security. AWS WAF allows teams to define custom rules to inspect web traffic and block requests that match specific patterns, such as those originating from known malicious IP addresses or exhibiting suspicious behaviour. This helps to protect the web applications from common web-based threats. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 provides the reliable and fault-tolerant storage capability for critical customer documents, owing to its highly durable and redundant storage architecture, as well as its ability to seamlessly replicate data across multiple Availability Zones (AZs). Moreover, the Application Load Balancer is employed to distribute the workload across multiple Fargate instances, thereby enhancing high availability and fault tolerance. CloudFront is used to globally distribute the frontend, caching the content closer to the geographical locations of users. Lastly, the incorporation of monitoring and observability capabilities through services such as Amazon CloudWatch enables the identification and resolution of any reliability issues that may arise. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services integrated throughout this Guidance are designed to accommodate high-volume traffic, provide low-latency responses, and scale automatically to meet the evolving performance requirements of the application. For instance, the deployment of DynamoDB in an on-demand capacity configuration enables a high-performance, low-latency database service to the application, coupled with a scalable and efficient data storage approach, thereby helping to ensure fast and reliable data access. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon Connect Customer and Amazon Lex provide a pay-as-you-use pricing model, allowing users to only pay for the resources they consume, thus optimizing costs by eliminating the need for upfront investments while also reducing licensing costs. OpenSearch Serverless is used as the vector database for the generative AI powered agent assistant. This is a fully managed and serverless search and analytics service, offering a scalable and cost-effective framework by automatically provisioning and scaling resources based on demand, reducing the overhead of infrastructure management. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses a variety of serverless services, including Amazon Lex, Lambda, Amazon S3, DynamoDB, Fargate, and OpenSearch Serverless, which are designed to only consume resources as necessary, thereby helping to reduce the carbon footprint of the user. The dynamic scaling capabilities inherent to these serverless and managed services further contribute to sustainability by helping to ensure that resources are provisioned and scale based on actual demand, thereby avoiding the need to over-provision and maintain excess capacity. In contrast, traditional contact centers that operate within on-premises data centers, with provisioned compute resources and online data stores, often have a larger carbon footprint due to their energy consumption. Finally, the Customer Carbon Footprint Tool, which enables users to measure, review, and forecast the carbon emissions generated from their AWS usage, facilitates informed decision-making and the implementation of sustainable practices. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
