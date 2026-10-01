---
source_url: https://docs.aws.amazon.com/solutions/secure-access-to-external-package-repositories-on-aws/index.html
---

---
title: 'Guidance for Secure Access to External Package Repositories on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/secure-access-to-external-package-repositories-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Secure Access to External Package Repositories on AWS

## Overview

This Guidance helps organizations provide their data scientists with external package repository access while maintaining information security (infosec) compliance. Data scientists must commonly install open-source packages residing in public repositories, but this introduces security risks. By using an automated orchestration pipeline on AWS, organizations can make sure that all public packages undergo comprehensive security scans before entering data scientists’ private Jupyter notebook environments. InfoSec governance controls are seamlessly integrated, providing a smooth data science workflow experience without disruptions. With this Guidance, organizations can strike a balance between empowering data scientists with agility and maintaining robust security measures for operational harmony.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/secure-access-to-external-package-repositories-on-aws.pdf)

![Architecture diagram](/images/solutions/secure-access-to-external-package-repositories-on-aws/images/secure-access-to-external-package-repositories-on-aws-1.png)

1. **Step 1**: Your data scientist pulls the external package dependency request file from a GitHub Enterprise private repository, appends the external package repository names and ZIP URLs, and then pushes the updated request file into the private repository.
1. **Step 2**: The request file check-in invokes an AWS CodePipeline orchestration, which is secured by a personal access token (PAT) in AWS Secrets Manager and accessed using an Amazon Virtual Private Cloud (Amazon VPC) endpoint.
1. **Step 3**: The CodePipeline build stage includes an AWS CodeBuild project that parses the request file and downloads the external package repositories. The external packages are stored as a build-stage output artifacts in Amazon Simple Storage Service (Amazon S3).
1. **Step 4**: Centralized inbound and outbound internet traffic occurs through a NAT gateway attached to the output virtual private cloud (VPC) in your networking account.
1. **Step 5**: Amazon CodeGuru Security performs security scans on the downloaded external package repositories.
1. **Step 6**: If the security scans return lower than medium severity, the build stage creates a new private AWS CodeArtifact package version asset in your data science account.
1. **Step 7**: Amazon Simple Notification Service (Amazon SNS) emails the results, positive or negative, to your requesting data scientist.
1. **Step 8**: Your data scientist authenticates to the Amazon SageMaker Studio domain through the AWS Identity and Access Management (IAM) or AWS IAM Identity Center mode. A SageMaker Studio notebook installs the InfoSec-validated external packages using the corresponding private CodeArtifact package version assets (for example, aws codeartifact get-package-version-asset).
1. **Step 9**: A SageMaker Studio elastic network interface (ENI) deployed in the VPC that you manage uses the VPC endpoint for private network access to CodeArtifact.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-secure-access-to-external-package-repositories-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses AWS managed services that support Amazon CloudWatch or AWS CloudTrail logging for incident and event response. You can view the CodePipeline implementation state through a console or a command line interface, and you can monitor each CodeBuild project individually. An automated deployment script monitors the AWS CloudFormation stack status and makes it visible to the user deploying this Guidance. Additionally, CloudTrail captures all API calls for CodeArtifact as events, including calls from package manager clients. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses Amazon VPC networking and VPC endpoints to establish a private data perimeter. Secrets Manager securely stores sensitive credentials, like a GitHub PAT and email, and the GitHub PAT authenticates the private repository webhook. The cfn-nag tool validates the CloudFormation template to make sure that IAM rules and security groups are not overly permissive, that access logs and encryption are enabled, and that there are no password literals. Additionally, CodePipeline uses an encrypted Amazon S3 artifact repository, encrypted by AWS Key Management System (AWS KMS), for its assets. CodeArtifact packages are published using a SHA256 hash that is calculated by the caller and provided with the request. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses services managed by AWS that natively provide high availability and resilience. For example, SageMaker provides low latency, high throughput, and highly redundant networking. This Guidance is designed to be deployed in one AWS Region, but you can easily adapt its infrastructure as code to launch an identical stack in a secondary disaster recovery Region. Providing more availability, AWS Lambda runs your function in multiple Availability Zones (AZs) so that it can still process events in the case of a service interruption in a single AZ. Providing resiliency, CodePipeline and CodeBuild can retry failed stage actions either automatically or manually. Additionally, the CloudFormation template enables you to quickly launch new versions of the resource stack, and you can use CloudTrail and CloudWatch to access stack logs of resource provisioning and errors. Finally, Amazon QuickSight will email your account administrators when significant events occur. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses higher-abstraction services managed by AWS and chosen for their operational benefits. For example, these services natively provide a minimum of 40 Gbps burstable throughput based on VPC endpoint quota limitations. For any service used, the minimum request quota—which can be increased—is 200 emails per day using Amazon Simple Email Service (Amazon SES). At that level, the Guidance scales to 1,000 CodePipeline implementations. It also integrates with various third-party source repositories, like GitHub, and you can simply plug a third-party security scanning software into the automation pipeline as a custom CodeBuild project. Additionally, you can use the SageMaker Studio system terminal to pull, edit, and push file copies between local and remote repositories. Alternatively, you can implement Git commands from their local system terminal or from another notebook environment. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance provisions services in the same Region to reduce data transfer charges. As managed serverless services, they reduce your maintenance overhead and infrastructure cost. Additionally, these services follow the pay-as-you-go model, and with high efficiency, they are not required to run for an extended period of time and can scale down when not in use. NAT gateways in Amazon VPC are charged per database of processed data, support 5 Gbps of bandwidth, and automatically scale up to 100 Gbps. Internet gateways in Amazon VPC, which are horizontally scaled, redundant, and highly available, impose no bandwidth constraints. And each VPC endpoint supports a bandwidth of up to 10 Gbps per AZ and bursts of up to 40 Gbps. Additionally, CodePipeline and CodeBuild project implementations provide a unique instance for each run with no reported concurrency limits. Furthermore, Secrets Manager supports 10,000 DescribeSecret and GetSecretValue API requests per second. Finally, SageMaker Studio lets you automatically shut down idle resources, and CloudFormation lets you create and delete stacks as needed, avoiding static provisioning costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The services used in the Guidance that are managed by AWS scale based on demand and are serverless, so they do not need to be statically provisioned. For example, CodePipeline, CodeBuild, and Lambda all use the elasticity of the cloud to scale infrastructure dynamically, matching the supply of cloud resources to demand, avoiding overprovisioned capacity. Additionally, CloudFormation enables stack deprovisioning so that you can terminate resources that are no longer needed. By reducing overprovisioned compute and storage resources, you can minimize the environmental impact of your workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
