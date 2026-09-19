---
source_url: https://docs.aws.amazon.com/solutions/machine-learning-for-near-real-time-advertising-on-aws/index.html
---

---
title: 'Guidance for Machine Learning for Near Real-Time Advertising on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/machine-learning-for-near-real-time-advertising-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Machine Learning for Near Real-Time Advertising on AWS

## Overview

This Guidance helps AdTech users build, train, and deploy machine learning models to an ad auction server application. This helps reduce unanswered bid requests by decoupling model creation and model consumption into separate environments to enable independent scale and security measures.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/machine-learning-for-near-real-time-advertising-on-aws.pdf)

![Architecture diagram](/images/solutions/machine-learning-for-near-real-time-advertising-on-aws/images/machine-learning-for-near-real-time-advertising-on-aws-1.png)

1. **Step 1**: Copy raw OpenRTB log data into an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 2**: Amazon SageMaker Studio deploys an Amazon EMR cluster to process raw OpenRTB data.
1. **Step 3**: Amazon SageMaker Pipelines is triggered by a user to launch the pre-processing and training steps.
1. **Step 4**: In the pre-processing step, the raw data is transformed in Amazon EMR and stored in another Amazon S3 bucket, with the transformation steps defined in a SageMaker preprocessing notebook.
1. **Step 5**: A machine learning (ML) training job uses the pre-processed data, and outputs trained models to the SageMaker model registry.
1. **Step 6**: Register the last version, save the trained model to an Amazon S3 bucket, and register metadata in AWS AppConfig.
1. **Step 7**: In a separate AWS environment, the ad auction server and the bid filtering applications are deployed to Amazon Elastic Container Service (Amazon ECS) as individual containers.
1. **Step 8**: The bid filtering application pulls the latest version from the model registry and then downloads the model from Amazon S3.
1. **Step 9**: The publisher issues auction requests to the ad auction server.
1. **Step 10**: The auction server calls the bid filter. The bid filter predicts demand side platform's (DSPs) likelihood of bidding.
1. **Step 11**: Bids to DSP below the threshold are filtered, eliminating the associated data transfer cost.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-samples/aws-rtb-intelligence-kit)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance is represented by two AWS Cloud Development Kit (AWS CDK) stacks. You can deploy changes to the application and infrastructure by applying the best practices from AWS CDKs. Programmatic access key, single sign-on, or federation are some of the authentication methods used in the AWS CDK CLI. An Amazon CloudWatch dashboard provides business metrics for monitoring. You can configure CloudWatch alarms to meet your operational needs. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

To improve privacy and security, Amazon Virtual Private Cloud (Amazon VPC) service endpoints are used. Managed services such as AWS Lambda and Amazon ECS are used to reduce the security maintenance tasks. Amazon S3 buckets used in this Guidance are encrypted and blocked from public access. Amazon Elastic Block Store (Amazon EBS) volumes are encrypted using the customer managed AWS Key Management Service (AWS KMS) key. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This solution uses managed services Amazon EMR, SageMaker, and Amazon ECS to minimize the operational efforts for the solutions. Amazon EMR is designed to handle large-scale data processing. The model training is done on SageMaker that provides the configuration parameters to size the infrastructure according to the demand. The data processing and model training parts of this solution are run periodically in batches. The inference part must be near real-time and run as containers in Amazon ECS, allowing for multi-Availability Zone deployment and auto-scaling to enable high availability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

For a hands-on experience, you can deploy the provided code in your account from an AWS Region of your choice. You would first use the sample data to start the data processing and machine learning process and then use a trained model to make inferences. To start tailoring this Guidance to your needs, you can incorporate your own data, modify the machine learning model training, and possibly adjust the inference part. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance is designed to support managed services that can run in any AWS region without incurring additional licensing costs. Deploy to the AWS Region that best fits your needs. The components are managed individually to incur cost only when used. Data transformation uses Amazon EMR clusters to provide the best cost to performance ratio when processing large data sets. From SageMaker studio, clusters can be created and ended to manage costs. The inference component uses container-based deployment to match resource consumption with actual demand. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance focuses on shared storage and single sources of truth to avoid data duplication and reduce the total storage requirements of your workload. Only fetch data from shared storage if necessary. Detach unused volumes in order to make more resources available. You can change the utilized compute resources based on the actual need. Adjust provisioned resources based on the actual demand. To understand utilization and the right-size of deployed resources, you can use CloudWatch metrics. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
