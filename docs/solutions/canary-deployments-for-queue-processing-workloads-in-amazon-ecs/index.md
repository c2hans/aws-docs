---
source_url: https://docs.aws.amazon.com/solutions/canary-deployments-for-queue-processing-workloads-in-amazon-ecs/index.html
---

---
title: 'Guidance for Canary Deployments for Queue Processing Workloads in Amazon ECS'
canonical_url: https://docs.aws.amazon.com/solutions/canary-deployments-for-queue-processing-workloads-in-amazon-ecs/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Canary Deployments for Queue Processing Workloads in Amazon ECS

Zero-downtime deployments with monitoring and instant rollbacks

## Overview

This Guidance shows how to implement canary deployments for backend or queue processing workloads without using a load balancer. By using AWS CodePipeline, you can orchestrate a workflow that first deploys the canary release to a low-capacity service instance for testing before propagating it to a high-capacity service instance to complete the deployment. Additionally, you can use AWS monitoring capabilities and alarms to automatically initiate a rollback, allowing you to better implement safe deployments when deploying new changes to your application. **Important:** This Guidance requires the use of [AWS CodeCommit](/codecommit/latest/userguide/welcome.html) , which is no longer available to new customers. Existing customers of AWS CodeCommit can continue using and deploying this Guidance as normal.

## How it works

This architecture diagram shows how to implement canary deployments for backend or queue processing workloads in Amazon Elastic Container Service (Amazon ECS) without a load balancer.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/canary-deployments-for-queue-processing-workloads-in-amazon-ecs.pdf)

![Architecture diagram](/images/solutions/canary-deployments-for-queue-processing-workloads-in-amazon-ecs/images/canary-deployments-for-queue-processing-workloads-in-amazon-ecs-1.png)

1. **Step 1**: Submit any code changes to software configuration management tools like AWS CodeCommit.
1. **Step 2**: AWS CodePipeline watches for new code changes and initiates the continuous integration and continuous delivery (CI/CD) pipeline to build the new container image using AWS CodeBuild.
1. **Step 3**: After the image is built, CodePipeline initiates the Amazon Elastic Container Service (Amazon ECS) deploy action.
1. **Step 4**: The Amazon ECS deploy action deploys the change to a low-capacity Amazon ECS service instance to start the canary process and waits for manual approval.
1. **Step 5**: The low-capacity Amazon ECS service instance will start processing messages from the Amazon Simple Queue Service (Amazon SQS) queue using the new version, while the high-capacity service instance is still using the existing version.
1. **Step 6**: Once the changes are validated, your team can manually approve the canary release to propagate the change to the high-capacity Amazon ECS service instance.
1. **Step 7**: The Amazon ECS deploy action deploys the change to the high-capacity Amazon ECS service instance to complete the deployment process.
1. **Step 8**: The new version is deployed to both the low-capacity and the high-capacity Amazon ECS service instance to process messages from the Amazon SQS queue.
1. **Step 9**: Failures in processing Amazon SQS messages are sent to the Amazon SQS dead letter queue (DLQ) so that you can monitor issues from the new code version.
1. **Step 10**: An Amazon CloudWatch alarm monitors the Amazon SQS DLQ depth and can invoke an AWS Lambda function to stop and roll back the canary release.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-ecs-canary-deployments-for-backend-workloads-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CodePipeline and CodeBuild automate the CI/CD process for building and deploying new code changes. This Guidance deploys the changes in Amazon ECS and AWS Fargate, fully managed serverless services that help you offload operational overhead tasks like upgrading, patching, and scaling various compute resources. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All the services in this Guidance use AWS Identity and Access Management (IAM) for authentication and authorization. IAM roles and policies, which can grant short-term access credentials, protect AWS resources, and manage access. By scoping IAM policies to the minimum permissions required, you can limit unauthorized access to resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance deploys Amazon ECS and Fargate tasks, Amazon SQS queues, and Lambda functions across multiple Availability Zones (AZs) by default, helping you achieve high availability. Additionally, Amazon SQS queues implement decoupling between application components, and a DLQ captures any processing failures for investigation and retry. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CodePipeline and CodeBuild implement the CI/CD process when you need to push new code changes to the CodeCommit repository. Amazon ECS uses Application Auto Scaling to automatically adjust the number of Amazon ECS and Fargate tasks running in the cluster based on the Amazon SQS queue depth. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

All the services used in this Guidance are serverless, which means you can run code without provisioning or managing servers, and you only pay for what you use. CodeBuild, which provides on-demand compute capacity, is billed for the duration of code building, and CodePipeline is billed for the number of pipelines per month. Additionally, CodeBuild is responsible for building the application code. Application Auto Scaling automatically adjusts the number of Amazon ECS and Fargate tasks running in the cluster to meet demand, thus minimizing the overall compute costs. Additionally, you can choose an ARM64 CPU architecture, spot capacity, and compute savings plans to further reduce compute costs. For example, you can use Fargate Spot if the workload tolerates interruptions. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses serverless services that let you run code without provisioning or managing servers. These services can scale based on your workloads so that you can avoid overprovisioning resources, ultimately lowering your carbon footprint. For example, Application Auto Scaling automatically adjusts the number of Amazon ECS and Fargate tasks running to meet demand, thus minimizing compute. You can also run Fargate on the ARM64 architecture to further reduce power consumption. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
