---
source_url: https://docs.aws.amazon.com/solutions/natural-language-queries-of-relational-databases-on-aws/index.html
---

---
title: 'Guidance for Natural Language Queries of Relational Databases on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/natural-language-queries-of-relational-databases-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Natural Language Queries of Relational Databases on AWS

## Overview

This Guidance demonstrates how to build an application that allows users to query relational databases using natural language. The architecture uses a LangChain SQL database chain, a Streamlit frontend framework, and an Amazon SageMaker JumpStart foundation model (FM). The user's natural language query is passed to the LangChain SQL database chain, which translates it into a SQL statement using the FM. This SQL statement runs against the configured relational database, retrieving the relevant results. These database results are passed back to the FM, which generates a natural language explanation summarizing the findings in an easy-to-understand format. The natural language explanation is then presented to the user through the Streamlit frontend, providing a user-friendly interface for submitting queries and viewing results.

## How it works

This architecture diagram demonstrates how to use natural language to query an Amazon RDS for PostgreSQL database. It uses a combination of a generative artificial intelligence (AI) foundation model (FM) along with Streamlit technology integrated with LangChain to quickly build large language models (LLM). It also uses Chroma, an open-source database for embedded vector data.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/natural-language-queries-of-relational-databases-on-aws.pdf)

![Architecture diagram](/images/solutions/natural-language-queries-of-relational-databases-on-aws/images/natural-language-queries-of-relational-databases-on-aws-1.png)

1. **Step 1**: Create an Amazon Elastic Container Service (Amazon ECS) task definition for the natural language query (NLQ) application. Deploy it to Amazon ECS on AWS Fargate. The Docker image for the task is retrieved from the Amazon Elastic Container Registry (Amazon ECR).
1. **Step 2**: End-user requests are received by an Application Load Balancer (ALB) using HTTP. Access is controlled by the IP address using security group inbound (ingress) rules.*
1. **Step 3**: End-user requests are forwarded from the ALB to the NLQ application, which runs on Amazon ECS using the Fargate launch type. The NLQ application's containerized workloads expose their web-based user interface (UI), built with Streamlit, on port 8501.
1. **Step 4**: The NLQ application retrieves credentials for Amazon RDS for PostgreSQL from AWS Secrets Manager. Secrets Manager uses an AWS Key Management Service (AWS KMS) key to decrypt the credentials. Virtual private cloud (VPC) endpoints are used to keep traffic between the VPC and the services on the AWS network.
1. **Step 5**: The user enters a natural language query through the application's web interface built with Streamlit. The application, using LangChain's SQLDatabaseChain API, interacts with a large language model (LLM) like Amazon SageMaker JumpStart or Amazon Bedrock. It also interacts with the PostgreSQL database, hosted on Amazon RDS, to process the user's natural language query. To improve accuracy, LangChain uses in-context learning (also referred to as "few-shot prompting"), passing semantically similar SQL query examples to the FM. LangChain uses Chroma to perform a similarity search of relevant samples based on the end-user's question. LangChain is able to take the end-user's natural language questions, formulate a SQL query, and query the Amazon RDS database. It returns and translates the results into a natural language answer, which is returned to the end-user.
1. **Step 6**: This Guidance uses AWS CloudFormation for deploying resources. All parameters are stored either in Parameter Store, a capability of AWS Systems Manager, or Secrets Manager. The NLQ application centralizes all logs, metrics, and information from other AWS services into Amazon CloudWatch.
1. **Notes**: * AWS security best practices dictate that HTTPS should be used, as opposed to HTTP, to secure data in transit. HTTPS requires an SSL/TLS server certificate. Use AWS Certificate Manager (ACM) to manage the certificate, which is loaded onto the ALB. The ALB uses the certificate to terminate the front-end HTTPS connection and then decrypt requests from the end-user. The certificate requires a registered DNS hostname, which can be managed using Amazon Route 53.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-natural-language-queries-of-relational-databases-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The Docker images in the Amazon ECR repository and Amazon ECS task definitions use semantic versioning. Amazon ECS will automatically deploy services to Fargate based on the task definition. Both the service and underlying task can be updated and redeployed. Amazon RDS for PostgreSQL has native functionality that allows the user to perform minor and major updates to the database engine. CloudWatch captures logs and metric (telemetry) emitted from the services in the architecture, including Fargate, Amazon ECS, and Amazon RDS for PostgreSQL. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon ECR stores the Docker image containing the NLQ application. Amazon ECR image scanning helps prevent vulnerabilities. The Amazon RDS instance and the Amazon ECS cluster are both restricted to a VPC. Using AWS managed services, you can prevent direct access to compute resources through remote desktop protocol (RFP) and secure socket shell (SSH). AWS security best practices dictate that HTTPS should be used, as opposed to HTTP, to secure data in transit. HTTPS will require SSL/TLS server certificate. We recommend using ACM to manage the certificate, which is loaded onto the ALB. The ALB uses the certificate to terminate the front-end HTTPS connection and then decrypt requests from the end user. The certificate will require a registered DNS hostname, which can be managed using Amazon Route 53. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

VPC Classless Inter-Domain Routing (CIDR) block ranges are non-overlapping. We properly sized subnets CIDR block to accommodate expansion of resources, such as Amazon RDS and Amazon ECS, and you will deploy resources to two Availability Zones for high availability. While VPC and associated subnets CIDR block are sized to accommodate reasonable expansion of resources, they are not infinitely scalable. The resources are restricted to a single AWS account and Region, and as such, reliability may be impacted by outages within the Region or issues impacting account accessibility. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

We chose Amazon RDS for PostgreSQL because PostgreSQL is a widely used open-source database engine that has large community support. We configured based on the anticipated volume of requests and small size of the dataset used for the demonstration. We chose Amazon ECS on Fargate because Fargate is serverless and can scale to meet increased demand. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

You should size resources to meet your organizational requirements and priorities. In particular, properly sizing the Amazon RDS for PostgreSQL instance, the SageMaker JumpStart Foundation Model inference hosting instance, and the Amazon ECS vCPU and memory resources can provide the largest impact on cost. The Amazon RDS for PostgreSQL instance can use RDS storage auto scaling to continuously monitor actual storage consumption and automatically scale capacity based on actual utilization. You can implement optional software and hardware caching to minimize scaling requirements on Amazon RDS and the FM hosting instance. The SageMaker JumpStart Foundation Model inference endpoint can be enabled for auto-scaling if required. Amazon ECS on Fargate is serverless and can be configured to meet demand through scaling. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This architecture maximizes the available resources without wasting additional resources that would not be necessary for the core requirements of the Guidance. For example, we chose Amazon RDS for Postgre SQL over Amazon Aurora, which would have powerful but unnecessary functionality for this architecture’s purpose. We also provisioned a single SageMaker JumpStart Foundation Model endpoint instance rather than multiple instances. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
