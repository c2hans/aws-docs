---
source_url: https://docs.aws.amazon.com/solutions/fraud-detection-using-machine-learning-on-aws/index.html
---

---
title: 'Guidance for Fraud Detection Using Machine Learning on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/fraud-detection-using-machine-learning-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Fraud Detection Using Machine Learning on AWS

Automated real-time credit card fraud detection

## Overview

This Guidance shows you how to use machine learning (ML) to create dynamic, self-improving, and maintainable fraud detection models, tailored for central banks. As your customers increasingly use digital tools and services, fraudulent activities by bad actors necessitate advanced fraud detection solutions. This Guidance lets you run automated transaction processing that both monitors digital currency transactions in real-time and detects suspicious activities so you can take action to prevent fraud before it strikes. As a result, you can improve the security and integrity of digital currencies as you work to maintain your regulatory compliance.

## How it works

This architecture diagram shows how to use a sample credit card transaction dataset to train a self-learning ML model that can recognize fraud patterns so that you can automate fraud detection and alerts.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/fraud-detection-using-machine-learning-on-aws.pdf)

![Architecture diagram](/images/solutions/fraud-detection-using-machine-learning-on-aws/images/fraud-detection-using-machine-learning-on-aws-1.png)

1. **Step 1**: An Amazon Simple Storage Service (Amazon S3) bucket contains an example dataset of credit card transactions.
1. **Step 2**: An Amazon SageMaker notebook instance contains different ML models that will be trained on the dataset.
1. **Step 3**: An AWS Lambda function processes transactions from the example dataset and invokes two SageMaker endpoints, which assign anomaly and classification scores to incoming data points.
1. **Step 4**: An Amazon API Gateway REST API invokes predictions using signed HTTP requests.
1. **Step 5**: An Amazon Data Firehose (successor to Kinesis Data Firehose) delivery stream loads the processed transactions into another Amazon S3 results bucket for storage.
1. **Step 6**: When the transactions have been loaded into Amazon S3, you can use analytics tools and services, including Amazon QuickSight, for visualization, reporting, individual queries, and more-detailed analysis.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/fraud-detection-using-machine-learning)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

SageMaker provides fully managed ML tools that automate workflows, from data preparation to model deployment and monitoring. This removes the need for you to manage a complex ML infrastructure. Lambda lets you run code without provisioning or managing servers, further reducing your operational burden. Additionally, Amazon DynamoDB facilitates low-latency data storage and retrieval and minimizes administrative tasks. Finally, AWS Step Functions simplifies the orchestration of complex workflows and provides built-in error handling capabilities, enhancing reliability and reducing the need for manual intervention. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) lets you implement the principle of least privilege, which grants authorized users and services only the minimum permissions required to perform their intended tasks, reducing the risk of unauthorized access or accidental misuse. Amazon Virtual Private Cloud (Amazon VPC) provides a logically isolated environment for the components that make up this Guidance, allowing you to use security groups and network access control lists to control inbound and outbound traffic. Additionally, as a serverless service, Lambda enhances security by minimizing the potential attack surface. Without the need to manage and secure underlying servers, you reduce the risk of vulnerabilities associated with server misconfigurations or outdated software versions. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda automatically scales compute resources based on incoming traffic, so your application can handle fluctuations in demand without manual intervention, minimizing downtime. DynamoDB provides built-in replication across multiple Availability Zones, providing redundancy and minimizing the risk of data loss due to infrastructure failures. Finally, Step Functions helps you create robust and fault-tolerant serverless workflows. Its built-in features, like automatic retries and error handling, help tasks recover from transient failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda enables your application to scale seamlessly and handle fluctuations in traffic without compromising performance. DynamoDB supports high throughput and low-latency data access, enabling your fraud detection process to operate in real time without performance bottlenecks. Additionally, SageMaker automates and accelerates the ML model development lifecycle, enabling you to efficiently and quickly iterate and fine-tune models. This results in improved model accuracy and enhances overall solution performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda uses a serverless computing model that scales to match demand, and you only pay for the compute time you consume. This helps you avoid the costs associated with overprovisioning or underutilizing servers. DynamoDB removes the need for dedicated database administrators and the associated costs, and it automatically scales to accommodate fluctuations in traffic without manual intervention. Additionally, SageMaker provides a fully managed ML environment, reducing the costs associated with procuring and maintaining hardware and software for model development, training, and deployment. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda enables your application to scale up or down automatically based on demand, minimizing energy consumption when the application is not in use. SageMaker provides a managed ML environment, reducing the energy and resource consumption needed to set up and maintain a dedicated ML infrastructure. Finally, DynamoDB automatically scales resources based on traffic patterns, optimizing resource usage and minimizing the environmental impact of overprovisioning or underutilizing database resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
