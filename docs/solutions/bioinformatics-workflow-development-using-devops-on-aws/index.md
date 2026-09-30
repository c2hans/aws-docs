---
source_url: https://docs.aws.amazon.com/solutions/bioinformatics-workflow-development-using-devops-on-aws/index.html
---

---
title: 'Guidance for Bioinformatics Workflow Development Using DevOps on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/bioinformatics-workflow-development-using-devops-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Bioinformatics Workflow Development Using DevOps on AWS

Important: This Guidance requires the use of AWS CodeCommit, which is no longer available to new customers. Existing customers of AWS CodeCommit can continue using and deploying this Guidance as normal.

## Overview

This Guidance demonstrates how to set up a continuous integration and continuous delivery (CI/CD) pipeline to automate the lifecycle of your bioinformatics workflows on AWS HealthOmics. By integrating your existing workflows with source control systems like Git, the CI/CD pipeline enables efficient development, testing, version management, and deployment of workflow updates. Whenever code changes are committed, the pipeline automatically builds, tests, and deploys the new workflow version. This approach streamlines your workflow processes, reducing manual effort while maintaining data provenance and consistent, repeatable results across all versioned workflows.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/bioinformatics-workflow-development-using-devops-on-aws.pdf)

![Architecture diagram](/images/solutions/bioinformatics-workflow-development-using-devops-on-aws/images/bioinformatics-workflow-development-using-devops-on-aws-1.png)

1. **Step 1**: Workflow developers create a branch and write code for a new workflow or make changes to an existing workflow repository within AWS CodeCommit. Developers can specify major and minor versions as part of semantic versioning. Since CodeCommit supports Git, developers use git operations to push code, submit a pull request, and merge to the 'main' branch. This runs the continuous integration and continuous delivery (CI/CD) pipeline configured with AWS CodePipeline.
1. **Step 2**: Within CodePipeline, the build process starts using AWS CodeBuild, where it downloads the latest source code.
1. **Step 3**: A pre-created AWS Step Functions state machine imports public Docker images or builds new Docker images and stores them within Amazon Elastic Container Registry (Amazon ECR) repositories.
1. **Step 4**: The CodeBuild job prepares artifacts for the AWS HealthOmics workflow. It stores the artifacts in Amazon Simple Storage Service (Amazon S3) and creates a HealthOmics workflow. The workflow includes the user-defined semantic version and an auto-updated patch version.
1. **Step 5**: After a successful build, CodePipeline runs a Step Functions state machine, which tests the HealthOmics workflow with some preconfigured test data and waits for completion.
1. **Step 6**: On successful completion of the test workflow, a workflow administrator reviews the test workflow outputs in Amazon S3 and, using CodePipeline, manually approves the deployment of the workflow to a production AWS account.
1. **Step 7**: The approval action invokes a CodeBuild job that prepares the workflow artifacts and uploads them to the production account's Amazon S3 bucket.
1. **Step 8**: The CodeBuild job updates the Amazon ECR repository permissions for all applicable repositories to enable cross-account access for the production AWS account.
1. **Step 9**: The upload of workflow artifacts to the production account's Amazon S3 bucket runs an AWS Lambda function that checks for the necessary files and launches a CodeBuild job.
1. **Step 10**: The CodeBuild job creates the workflow in HealthOmics using the artifacts in Amazon S3.
1. **Step 11**: The HealthOmics workflow is now available for use in the production account.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-bioinformatics-workflow-development-using-devops-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

For efficient and effective operations, this Guidance helps you automate your build, test, and deployment processes with CodeBuild and CodePipeline. CodeCommit is another service that supports your operations; it stores code in private Git repositories for version control. You can track changes, test new versions, and roll back if necessary. You can also orchestrate your automated tests with Step Functions to validate the quality and reliability of your deployments. Finally, you can centralize the management of your workflows in HealthOmics to improve visibility and monitoring; HealthOmics is a managed service purpose-built for healthcare and life science organizations to store, query, and analyze omics data. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

CodeCommit, HealthOmics, and Amazon ECR work in tandem to protect your systems, applications, and data from potential threats. Specifically, CodeCommit provides secure storage and version control for your workflow code, with access controls, change tracking, and encryption. HealthOmics offers isolated, secure, and scalable processing of your bioinformatics workflows. Amazon ECR helps ensure secure storage and access control for your container images. Additionally, by separating your CI/CD and production environments, implementing least-privilege access, and securely managing your artifacts, you can achieve a higher level of isolation and security for your bioinformatics workflows. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Building resilient and highly available systems that can withstand failures requires services like CodePipeline, Step Functions, and HealthOmics. CodePipeline provides an automated way to build, test, and deploy new versions of your workflows. Step Functions orchestrates the various steps in your CI/CD pipeline, setting the framework for a resilient and fault-tolerant way to coordinate and automatically retry failed steps. HealthOmics manages the underlying infrastructure and resource management, supporting the reliability and availability of your workflow processing. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

You can optimize the use of computing resources while maximizing efficiency with CodeBuild, CodePipeline, Step Functions, and HealthOmics. CodeBuild is a service with capabilities to support a fully managed build and test workflow with features like cache and auto-discovery. The efficient deployment processes, powered by CodePipeline and Step Functions, minimize the risk of performance regressions. Finally, HealthOmics provides a managed service for running your bioinformatics workflows, handling the provisioning and scaling of the underlying compute resources and storage systems for optimal workflow performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By supporting cross-account deployments, this Guidance helps you maintain secure and isolated environments for development, testing, and production, reducing the risk of inadvertent resource utilization and costs. It utilizes CodeBuild, CodePipeline, Lambda, Amazon ECR, and HealthOmics to do this. For example, the automated build and deployment processes of CodeBuild and CodePipeline allow only the necessary resources to be provisioned. By using Lambda for lightweight tasks, you reduce the need for always-on compute resources. Also, storing your built container images in Amazon ECR allows for reuse across multiple workflow deployments, saving time and compute costs. Furthermore, HealthOmics, as a managed service, eliminates the need for you to manage the underlying infrastructure and configuration complexities and reduces your operational costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Minimize your carbon footprint and support responsible resource utilization with CodeBuild, Lambda, Amazon ECR, and HealthOmics. CodeBuild only provisions the necessary compute resources to perform the build and deployment tasks, scaling up and down as required, reducing energy consumption and the associated environmental impacts. Lambda avoids the need to provision and manage dedicated server infrastructure, running only when needed and shutting down when idle. Amazon ECR provides centralized, scalable, and durable storage of your container images, eliminating the need for additional container registries or storage solutions and reducing the overall hardware and energy footprint. By utilizing HealthOmics, you can use the service's scalable and serverless architecture to run your bioinformatics workflows and help lower your overall energy consumption. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
