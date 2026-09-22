---
source_url: https://docs.aws.amazon.com/solutions/multi-account-machine-learning-model-governance-on-aws/index.html
---

---
title: 'Guidance for Multi-Account Machine Learning Model Governance on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/multi-account-machine-learning-model-governance-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Multi-Account Machine Learning Model Governance on AWS

## Overview

This Guidance shows how to implement a centralized multi-account machine learning (ML) model governance strategy on AWS. With a centralized model governance approach, you can establish a single, authoritative repository for registering, versioning, and sharing ML models. By serving as the primary control point for the entire lifecycle of your ML models, from development to deployment and monitoring, the centralized approach facilitates consistent model management, streamlined model sharing and deployment, and improved visibility and control. Consequently, this approach enhances compliance and mitigates risk exposure through streamlined monitoring and approval workflows.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/multi-account-machine-learning-model-governance-on-aws.pdf)

![Architecture diagram](/images/solutions/multi-account-machine-learning-model-governance-on-aws/images/multi-account-machine-learning-model-governance-on-aws-1.png)

1. **Step 1**: The stakeholder, specifically the Data Scientist (DS) team lead, receives a request from the business leader to develop an AI use case, such as a credit risk model.
1. **Step 1a**: The Machine Learning Engineer (MLE) is notified to establish a model group for the development of a new model. The MLE then creates the necessary infrastructure pipeline to set up the new model package group.
1. **Step 2**: The MLE sets up the pipeline to share the model group with the necessary permissions (create, describe, update model version) to the ML project team's development account. Optionally, the package group can also be shared with the test and production accounts if local account access to model versions is required.
1. **Step 3**: The DS uses MLflow, an open-source platform for managing the end-to-end machine learning lifecycle. MLflow is used within Amazon SageMaker Studio to construct model experiments, select a candidate model, and register the model version within the shared model group in the local Amazon SageMaker Model Registry.
1. **Step 4**: Since this is a shared model group, the model version metadata will be recorded in the Centralized Model Registry, and a corresponding link will be maintained in the development account. The MLE can set up Amazon Simple Storage Service (Amazon S3) and Amazon Elastic Container Registry (Amazon ECR) in the shared account, allowing the DS to store the model artifacts from the development account. The DS is granted the necessary permissions to access the model artifacts in Amazon S3 and Amazon ECR within the shared services account.
1. **Step 5**: The Centralized Model Registry triggers an Amazon EventBridge rule, which in turn invokes an AWS Lambda function that writes the relevant data to an Amazon DynamoDB table. The model versions are synchronized with the Model Stage Governance table using DynamoDB, which records attributes such as Model Group, Model Version, Model Stage (for example: Dev, Test, Prod), Model Status (pending, approved, rejected), and Model Metrics. DynamoDB provides storage for registering models from diverse sources beyond Amazon SageMaker, enabling a consolidated view of all enterprise models and metadata. The DynamoDB table is the central model governance system that integrates with both use case and model lifecycle stages. It also augments metadata and approvals along with SageMaker model registry attributes, and centralizes model governance and performance metrics from production inference endpoints.
1. **Step 6**: The model version is approved for deployment into the testing stage and is subsequently deployed into the test account. It's deployed with the necessary infrastructure for invoking the model, such as Amazon API Gateway and Lambda.
1. **Step 7**: The model undergoes integration testing in the test environment, and the quality assurance (QA) model evaluation metrics are updated in the Centralized Model Registry, which are then written to the DynamoDB table using a Lambda function.
1. **Step 8**: The model test results are validated, and the model version is approved for deployment into the production stage. The model is then deployed into the production account, along with the necessary infrastructure for invoking the model, such as API Gateway and Lambda.
1. **Step 9**: The model undergoes A/B testing in the production environment, and the model production metrics are updated in the DynamoDB (Model Stage Governance) table. Once satisfactory production results are achieved, the model version is promoted in the production environment. Additionally, model monitoring is enabled at the model endpoint.
1. **Step 10**: The Model Governance or Compliance Officer uses the Governance dashboard within Amazon QuickSight to execute model governance functions, including reviewing the model for compliance validation and monitoring for risk mitigation.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-multi-account-machine-learning-model-governance-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The services used throughout this Guidance collectively provide a comprehensive, automated, and scalable infrastructure for the entire ML lifecycle. Specifically, SageMaker offers a fully managed ML environment, streamlining workflows from data preparation to deployment and monitoring. Lambda and EventBridge enable serverless compute and event-driven automation, reducing manual intervention and potential errors. DynamoDB provides a flexible database for model metadata, while QuickSight offers dashboarding capabilities for monitoring and governance. Amazon S3 and Amazon ECR provide scalable storage offerings for model artifacts and container images, helping ensure consistent performance as demands grow. Lastly, API Gateway manages API creation and management for model invocation, facilitating smooth integration with other systems. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

By providing mechanisms for access control, data protection, and secure artifact storage, the services used in this Guidance work in tandem to protect your information and systems. For example, SageMaker offers built-in security features for ML workflows, including isolation of notebook instances and model endpoints. AWS Identity and Access Management (IAM) enables fine-grained access control and permission management across AWS services. Amazon S3 provides secure object storage with encryption capabilities for model artifacts. And lastly, Amazon ECR offers secure storage for container images with access controls and encryption in transit. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The services selected for this Guidance are designed to handle varying workloads and potential failures gracefully. For instance, the managed infrastructure of SageMaker reduces the operational burden of maintaining ML environments. The serverless nature of Lambda helps ensure that compute resources are always available without manual scaling. The distributed architecture of DynamoDB provides high availability for model metadata storage. Moreover, Amazon S3 is designed for 99.999999999% (11 nines) durability, protecting your critical model artifacts. Finally, Amazon ECR helps ensure that container images are always accessible for deployment and API Gateway handles traffic spikes with consistent model access. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

SageMaker offers a high-performance infrastructure for model training and inference with the ability to automatically select the most efficient instance types. Lambda enables rapid execution of functions with near-instantaneous scaling. DynamoDB provides single-digit millisecond latency for data retrieval at any scale. Amazon S3 offers high-throughput access to model artifacts. Amazon ECR ensures fast and consistent deployment of container images. And API Gateway provides low-latency API management for model invocation. These services collectively offer optimized, scalable, and low-latency approaches for various aspects of the ML pipeline. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using serverless and managed services, your organization can avoid the capital expenses associated with owning and maintaining physical infrastructure. One example of such a service is SageMaker that provides automatic scaling so resources are used efficiently during model training and inference. Lambda offers a serverless model, meaning you don’t pay for idle compute time, which is particularly beneficial for intermittent workloads in the ML pipeline. Additionally, DynamoDB includeson-demand capacity mode where the database automatically scales up and down, optimizing costs for unpredictable workloads. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Efficient, scalable, and serverless computing options allow you to optimize resource usage, minimizing the environmental impacts of running cloud workloads. SageMaker offers managed ML infrastructure that can automatically scale resources based on demand, reducing idle capacity. Lambda provides serverless compute that only consumes resources when functions are executed. Finally, DynamoDB is a serverless database that scales automatically, ensuring efficient use of resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
