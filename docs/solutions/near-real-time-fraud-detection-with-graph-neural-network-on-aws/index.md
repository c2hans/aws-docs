---
source_url: https://docs.aws.amazon.com/solutions/near-real-time-fraud-detection-with-graph-neural-network-on-aws/index.html
---

# Guidance for Near Real-Time Fraud Detection with Graph Neural Network on AWS

## Overview

This Guidance demonstrates an end-to-end, near real-time anti-fraud system based on deep learning graph neural networks. This blueprint architecture uses Deep Graph Library (DGL) to construct a heterogeneous graph from tabular data and train a Graph Neural Network (GNN) model to detect fraudulent transactions.

## How it works

### Near Real-Time Fraud Detection

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/near-real-time-fraud-detection-with-graph-neural-network-on-aws.pdf#page=1)Step 1Use Amazon API Gateway to host HTTP APIs for near real-time fraud detection services.Step 2Use AWS Lambda functions as an HTTP API backend. The functions process the new transactions as graph data then store them in a graph database such as Amazon Neptune.Step 3Query the sub-graph of the requested transactions from Amazon Neptune.Step 4Use an Amazon SageMaker endpoint to predict the fraudulent possibility of transactions with pre-trained GNN models.Step 5Send the predicated results to Amazon Simple Queue Service (Amazon SQS) to be consumed by business analysis systems.Step 6Use AWS Lambda functions to poll the predicated results from Amazon SQS, then store them in Amazon DocumentDB.Step 7Business analysts access the business dashboard, which uses Amazon CloudFront and Amazon Simple Storage Service (Amazon S3) to host a static website, and AWS AppSync and AWS Lambda as a backend.Step 8Use AWS Lambda functions as an AWS AppSync resolver to fetch the data from Amazon DocumentDB.Step 9Amazon CloudFront uses origin access identity (OAI) to securely access the static web files on Amazon S3.### Offline Model Training

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/near-real-time-fraud-detection-with-graph-neural-network-on-aws.pdf#page=2)Step 1System operations or a periodic system task initiates the model training workflow.Step 2Use Lambda function to ingest the raw dataset to Amazon S3.Step 3Use AWS Glue crawler to crawl the raw dataset to populate the Data Catalog.Step 4Use AWS Glue extract, transform, load (ETL) job to transform the tabular dataset to a heterogeneous graph dataset, then save it to Amazon S3.Step 5Use the SageMaker training job to train the Graph Neural Network (GNN)-based fraud detection model with Deep Graph Library (DGL).Step 6Use AWS Fargate with Amazon Elastic Container Service (Amazon ECS) to load the graph dataset from Amazon S3 into fully-managed graph database service, Neptune.Step 7Use Lambda to package the GNN model and custom code as the model in SageMaker.Step 8Create an endpoint configuration of SageMaker.Step 9Create or update an endpoint using the endpoint configuration in SageMaker.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses AWS Serverless services like AWS Glue, SageMaker, AWS Fargate, Lambda as compute resources for processing data, training models, serving the API functionalities, and keeping billing to pay-as-you-go pricing. One of the data stores is designed using Amazon S3, providing a low total cost of ownership for storing and retrieving data. The business dashboard uses CloudFront, Amazon S3 and AWS AppSync, Lambda to implement the web application. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

API Gateway and Lambda provide a protection layer when invoking Lambda functions through an outbound API. All the proposed services support integration with AWS Identity and Access Management (IAM), which can be used to control access to resources and data. All traffic in the VPC between services are controlled by security groups. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

API Gateway, Lambda, AWS Step Functions, AWS Glue, Amazon S3, Neptune, Amazon DocumentDB, and AWS AppSync provide high availability within a Region. Customers can deploy SageMaker endpoints in a highly available manner. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

All the services used in the design provide cloud watch metrics that can be used to monitor individual components of the design. MLOps pipelines orchestrated by Step Functions helps to continuously iterate the model. API Gateway and Lambda allow publishing of new versions through an automated pipeline. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance requires GNN model training for fraud detection. The performance requirements for batch processing range from minutes to hours; AWS Glue and SageMaker training jobs are designed to meet them. Neptune is a purpose-built, high-performance graph database engine. Neptune efficiently stores and navigates graph data, and uses a scale-up, in-memory optimized architecture for fast query evaluation over large graphs. Provisioned concurrency in Lambda and the HTTP API in API Gateway can support a latency requirement of less than 10 ms. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses the scaling behaviors of Lambda and API Gateway to reduce over-provisioning resources. It uses AWS Managed Services to maximize resource utilization and to reduce the amount of energy needed to run a given workload. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Build a GNN-based real-time fraud detection solution using Amazon SageMaker, Amazon Neptune, and the Deep Graph Library**: This blog post demonstrates how many techniques have been used to detect fraudsters—rule-based filters, anomaly detection, and machine learning (ML) models, to name a few.

[Learn more](https://aws.amazon.com/cn/blogs/machine-learning/build-a-gnn-based-real-time-fraud-detection-solution-using-amazon-sagemaker-amazon-neptune-and-the-deep-graph-library/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
