---
source_url: https://docs.aws.amazon.com/solutions/deploying-harmonix-on-aws/index.html
---

---
title: 'Guidance for Deploying Harmonix on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-harmonix-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Deploying Harmonix on AWS

## Overview

This Guidance illustrates how to implement Harmonix on AWS, an enterprise-grade developer portal that bridges AWS services with your development teams. Provided as a reference implementation, Harmonix on AWS is an open-source tool that enables developers to build applications seamlessly while giving platform engineers comprehensive visibility across accounts, applications, and resources through a single interface. While the reference implementation uses specific tooling choices (such as Okta and GitLab), developers can either build upon this implementation directly, customize it for different toolsets, or implement Harmonix plugins within their existing Backstage deployment. This Guidance includes pre-built templates based on common patterns, showing how to provision an AWS account, an Amazon Elastic Container Service (Amazon ECS) environment, an Amazon Kubernetes Service (Amazon EKS) environment, and a serverless environment, helping developers efficiently deploy code, monitor logs, manage applications, and connect to shared resources.

## How it works

### Provisioning the AWS account

This architecture diagram illustrates how to provision an AWS account after cloning Harmonix from GitHub.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-harmonix-on-aws.pdf#page=1)Step 1Clone the Harmonix on AWS repository from GitHub.Step 2Follow the Installation instructions from the Harmonix website, and configure your .env file.Step 3Deploy Harmonix to your AWS account.Step 4Amazon Elastic Container Service (Amazon ECS) creates a service to run the Harmonix application.Step 5Amazon Elastic Container Registry (Amazon ECR) provides the latest Harmonix custom container image to Amazon ECS.Step 6The Backstage application starts running on an Amazon ECS task, connecting to a GitLab Community Edition (CE) instance to pull all the platform templates. The task has a reserved AWS Identity and Access Management (IAM) identity role, Platform Role.Step 7GitLab CE runs on Amazon Elastic Compute Cloud (Amazon EC2) with pre-backed templates and an identity token for Harmonix on AWS.Step 8A GitLab runner instance registers itself with a GitLab instance and is ready to execute pipelines and jobs. The instance also has a reserved IAM identity, Pipeline Role.Step 9The Harmonix on AWS environment is now accessible through the browser. Follow the Application Environment Tutorial from the Harmonix website to start provisioning resources on AWS.### Provisioning an Amazon ECS environment

This architecture diagram shows how to provision an Amazon ECS environment using Harmonix on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-harmonix-on-aws.pdf#page=2)Step 1The developer uses Harmonix on AWS to create an Amazon ECS environment using the ECS Environment provider template.Step 2Once submitted, Harmonix on AWS creates a new repository on GitLab with the desired environment provider information, including the AWS account, Region, and additional configuration.Step 3The commit to GitLab also includes a continuous integration/continuous development (CI/CD) pipeline, which automatically triggers and invokes GitLab runner to start executing the deployment of the request environment to the target account.Step 4The GitLab runner first assumes a target role with sufficient credentials to deploy the desired environment. Using these credentials, the pipeline deploys all the environment resources using infrastructure as code (IaC).Step 5The pipeline provisions resources, including Amazon Virtual Private Cloud (Amazon VPC), an Amazon Elastic Kubernetes Service (Amazon EKS) cluster, IAM roles for operations and provisioning, an Amazon CloudWatch log group, and an Amazon DynamoDB audit table.Step 6The last step of the pipeline is to update the GitLab repository with the created resource in the catalog-info.yaml file. This file is used by Backstage.io to visualize the environment entity and provide additional actions. Developers can now create apps and resources on the newly created environment. Review the Create Apps tutorial from the Harmonix website for additional information.### Provisioning an Amazon EKS environment

This architecture diagram shows how to provision an Amazon EKS environment using Harmonix on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-harmonix-on-aws.pdf#page=3)Step 1The developer uses Harmonix on AWS to create an Amazon EKS environment using the EKS Environment provider template.Step 2Once submitted, Harmonix on AWS creates a new repository on GitLab with the desired environment provider information, including the AWS account, Region, and additional configuration.Step 3The commit to GitLab also includes a continuous integration/continuous development (CI/CD) pipeline, which automatically triggers and invokes GitLab runner to start executing the deployment of the request environment to the target account.Step 4The GitLab runner first assumes a target role with sufficient credentials to deploy the desired environment. Using these credentials, the pipeline deploys all the environment resources using infrastructure as code (IaC).Step 5The pipeline provisions resources, including Amazon VPC, an EKS cluster, IAM roles for operations and provisioning, a CloudWatch log group, and an DynamoDB audit table. Additionally, the pipeline provisions a kubectl AWS Lambda function to access private EKS clusters which do not have an accessible control plane.Step 6The last step of the pipeline is to update the GitLab repository with the created resource in the catalog-info.yaml file. This file is used by Backstage.io to visualize the environment entity and provide additional actions. Developers can now create apps and resources on the newly created environment. Review the Create Apps tutorial from the Harmonix website for additional information.### Provisioning a serverless environment

This architecture diagram shows how to provision a serverless environment with Amazon API Gateway using Harmonix on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-harmonix-on-aws.pdf#page=4)Step 1The developer uses Harmonix on AWS to create a serverless environment using the serverless provider template.Step 2Once submitted, Harmonix on AWS creates a new repository on GitLab with the desired environment provider information, including the AWS account, Region, and additional configuration.Step 3The commit to GitLab also includes a continuous integration/continuous development (CI/CD) pipeline, which automatically triggers and invokes GitLab runner to start executing the deployment of the request environment to the target account.Step 4The GitLab runner first assumes a target role with sufficient credentials to deploy the desired environment. Using these credentials, the pipeline deploys all the environment resources using infrastructure as code (IaC).Step 5The pipeline provisions resources, including Amazon VPC, Amazon API Gateway, IAM roles for operations and provisioning, a CloudWatch log group, and an DynamoDB audit table.Step 6The last step of the pipeline is to update the GitLab repository with the created resource in the catalog-info.yaml file. This file is used by Backstage.io to visualize the environment entity and provide additional actions. Developers can now create apps and resources on the newly created environment. Review the Create Apps tutorial from the Harmonix website for additional information.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudWatch provides logs and tracing for applications and infrastructure. DynamoDB audits requests executed outside of AWS, capturing user interactions in the GitLab pipeline API. CloudFormation maintains IAC orchestration, reducing deployment overhead. These services facilitate troubleshooting, support native cloud conventions for configuration management, and enable observation of numerous apps across multiple accounts. The composition provides isolated access control and segregated auditing, improving compliance, security, and operational efficiency. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM limits permissions for infrastructure and application creation through specific roles, such as provisioning and operations. Access to environments requires assuming these roles. AWS Key Management Service (AWS KMS) provides encryption keys for each environment, used to encrypt all stored data. Appropriate roles are granted access to environment-specific keys. AWS Secrets Manager stores sensitive information using environment-specific AWS KMS keys, saving secrets with environment and application context. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

While Harmonix on AWS currently uses a single site, you can run multiple sites ( ECS clusters) with route policies for improved reliability. Elastic Load Balancing (ELB) distributes requests across multiple ECS containers, sending traffic only to healthy containers. Amazon ECS maintains application and platform lifecycles, helping ensure that apps are running, scaling as needed, and provisioning new tasks on failure. These services provide resiliency and automatic recovery for apps and the platform, with automatic monitoring, recovery, and traffic redirection to appropriate running tasks. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon ECS and Amazon EKS provide automatic scaling of desired tasks to help increase performance. Autoscaling groups, used with provisioned apps and ELB, improve performance by spinning up more app instances and distributing traffic across them. Lambda, a managed serverless compute service, offers automatic scaling when invoked through API, allowing serverless apps to benefit from performance increases during high traffic or demand. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Serverless Lambda functions operate on a pay-as-you-go model, meaning you only pay for resources used. This allows you to scale up as necessary and optimize costs by only charging for active compute time. This eliminates the need for dedicated EC2 instances that may be underutilized during off-peak hours. Amazon ECS and Amazon EKS containerized services improve infrastructure utilization by running multiple jobs and containers on shared infrastructure, maximizing throughput and scaling tasks across multiple nodes when needed. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

As managed services, Amazon ECS and Amazon EKS provide efficient application runtime environments, reducing redundant instances when no job is required. Serverless Lambda functions abstract hardware, allowing AWS to optimize existing infrastructure for more efficient runtimes instead of running underutilized hardware. By leveraging these services, you can optimize application execution, reduce costs, and decrease power consumption and emissions. This approach supports sustainability by maximizing resource utilization and minimizing idle infrastructure. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
