---
source_url: https://docs.aws.amazon.com/solutions/e-commerce-products-similarity-search-on-aws/index.html
---

---
title: 'Guidance for E-Commerce Products Similarity Search on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/e-commerce-products-similarity-search-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for E-Commerce Products Similarity Search on AWS

## Overview

This Guidance shows how to create a product catalog with a similarity search capability by integrating AWS and artificial intelligence (AI) services with the pgvector extension. As an open-source extension for PostgreSQL, pgvector adds the ability for you to store and search for points in a vector embedding and find the most similar or "nearest neighbor" to those points. The nearest neighbor search capabilities allow you to use the semantic meaning to power a variety of intelligent applications and data analysis within your PostgreSQL database. By integrating pgvector with AWS services, as shown here, you can conduct both image and text-to-image similarity searches to provide a more personalized, relevant, and efficient shopping experience for your consumers. **Important:** This Guidance requires the use of [AWS Cloud9](/cloud9/) which is no longer available to new customers. Existing customers of AWS Cloud9 can continue using and deploying this Guidance as normal.

## How it works

This architecture diagram shows how to build a product catalog with a similarity search capability. It uses artificial intelligence (AI), Amazon SageMaker, Amazon RDS for PostgreSQL, and the pgvector extension.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/e-commerce-products-similarity-search-on-aws.pdf)

![Architecture diagram](/images/solutions/e-commerce-products-similarity-search-on-aws/images/e-commerce-products-similarity-search-on-aws-1.png)

1. **Step 1**: Deploy resources in your AWS account using AWS CloudFormation. This includes deploying instances of Amazon Relational Database Service (Amazon RDS) for PostgreSQL, Amazon SageMaker, AWS Cloud9, AWS Lambda, and a Custom Resource.
1. **Step 2**: RDS for PostgreSQL stores both the product catalog and embeddings for the products using the PostgreSQL open-source extension pgvector to store and index these high-dimensional vector embeddings.
1. **Step 3**: SageMaker runs the pre-trained HuggingFace large language model (LLM) (SentenceTransformer) for real-time inference. You also have the flexibility to select other models that best fit your needs. Amazon Bedrock offers an alternative way for running diverse foundation models and conducting inference to produce text embeddings.
1. **Step 4**: The AWS Cloud9 integrated development environment (IDE) hosts a sample Streamlit application that provides product information retrieved from RDS for PostgreSQL. You have the option to replace this sample application with one of your choice. For alternative compute choices to run the application, consider deploying it on Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), AWS Fargate, or Amazon Elastic Compute Cloud (Amazon EC2).
1. **Step 5**: Custom Resources in CloudFormation run user-defined provisioning logic during stack creation, update (if the Custom Resource is modified), or deletion. When combined with a Lambda function, CloudFormation invokes and runs the function accordingly. The Custom Resource from the CloudFormation stack invokes Lambda to bootstrap RDS for PostgreSQL. During this process, the system creates the pgvector extension, initializes the Product Catalog schema, and generates embeddings using SageMaker near real-time inference. The system stores these embeddings along with product catalog metadata in RDS for PostgreSQL and indexes the embeddings using the pgvector index type hierarchical navigable small world (HNSW).
1. **Step 6**: Run the e-commerce product catalog application on AWS Cloud9 and preview the application while it's running.
1. **Step 7**: Perform a search on the product catalog in the application, which generates embeddings for the search query using the SageMaker near real-time inference endpoint.
1. **Step 8**: The application connects to RDS for PostgreSQL, runs the similarity search query on embeddings using the pgvector HNSW index, and then displays the product catalog similarity search results on the application screen.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-e-commerce-products-similarity-search-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

SageMaker simplifies machine learning model lifecycle management, allowing you to quickly adapt to changing data and user demands. RDS for PostgreSQL with the pgvector extension offers robust data storage and efficient nearest neighbor search capabilities, so you can deliver accurate and timely search results to your consumers. Together, these services streamline the deployment, monitoring, and maintenance of your search experience. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

RDS for PostgreSQL safeguards your data with industry-standard encryption protocols, while SageMaker offers built-in security controls to manage model training and deployment processes securely. We recommend you use AWS Identity and Access Management (IAM) to control access to your AWS resources, and use AWS Secrets Manager to protect sensitive credentials. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

RDS for PostgreSQL provides high availability and durability, with automatic backups, database snapshots, and multiple Availability Zone (AZ) deployments for enhanced fault tolerance. Also, SageMaker allows you to configure multiple instances across AZs for high availability and quick recovery from failures for your machine learning operations. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

SageMaker supports near real-time inference and low-latency responses to user queries. RDS for PostgreSQL with the pgvector extension enables efficient management and querying of vector embeddings, significantly speeding up the similarity searches needed to match user queries with your product catalog. We recommend you continuously monitor and optimize your system's performance by using AWS services like Amazon CloudWatch and AWS Auto Scaling so that the components in this Guidance remain responsive and cost-effective. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

SageMaker helps reduce costs by providing a managed service with pay-as-you-go pricing and instance types optimized for specific workloads. Additionally, RDS for PostgreSQL offers cost efficiency through reserved instances and scaling options that adjust resources based on your database workload, minimizing unnecessary expenses. Moreover, you can implement cost monitoring and optimization strategies, such as AWS Budgets and AWS Cost Explorer, to continuously identify and address potential cost inefficiencies. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

SageMaker and RDS for PostgreSQL are managed AWS services that optimize resource usage through efficient handling of workloads, reducing the environmental impact by minimizing the computational resources required for your workloads. And by deploying this Guidance in the AWS Cloud, you can avoid the need for physical hardware procurement, further enhancing the overall sustainability of your system. Additionally, use AWS services like AWS CloudTrail and AWS Config to monitor and enforce sustainable practices, such as resource utilization and energy efficiency. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Building AI-powered search in PostgreSQL using Amazon SageMaker and pgvector**: This blog post demonstrates how to create a product catalog similarity search solution by integrating Amazon SageMaker and Amazon Relational Database Service (Amazon RDS) for PostgreSQL with the pgvector extension.

[Read the blog](https://aws.amazon.com/blogs/database/building-ai-powered-search-in-postgresql-using-amazon-sagemaker-and-pgvector/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
