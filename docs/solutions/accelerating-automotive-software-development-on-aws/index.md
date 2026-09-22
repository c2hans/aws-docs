---
source_url: https://docs.aws.amazon.com/solutions/accelerating-automotive-software-development-on-aws/index.html
---

---
title: 'Guidance for Accelerating Automotive Software Development on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/accelerating-automotive-software-development-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Accelerating Automotive Software Development on AWS

## Overview

This Guidance demonstrates how automotive OEMs can accelerate their software-defined vehicle (SDV) development while maintaining control over their architecture and brand experience through a curated collection of AWS Marketplace products and services from AWS and industry partners. The solution described in this guidance combines these offerings for developers with an integrated development environment running on Amazon EC2 instances, providing virtual testing environments and development tools. This Guidance features pre-integrated build pipelines and a Backstage.io-based Internal Developer Portal that centralizes technical documentation, API specs, service catalogs, and infrastructure guides while providing streamlined resource access. This approach helps OEMs reduce time-to-market for their SDV solution delivery through streamlined development workflows.

## Benefits

### Accelerate software development cycles

Deploy a comprehensive development environment and virtual targets that are hosted on AWS. Automotive manufacturers, suppliers, and ISVs can use these tools to help speed up their software-defined vehicle development process, reducing time-to-market while maintaining their quality standards.

### Simplify evaluation and testing

Access AWS Partner offerings and trials through AWS Marketplace. This helps automotive manufacturers, suppliers, and ISVs more easily evaluate solutions before deployment, helping reduce procurement complexity and implementation risks.

### Enhance developer productivity

Access a unified developer experience through the Backstage.io-based Internal Developer Portal with integrated CI/CD pipelines. Developers gain a single access point to documentation, tools, and virtual targets, helping teams collaborate more effectively and focus on innovation.

## How it works

### SDV Accelerator Overview

This architecture diagram shows a high-level overview of the SDV Accelerator, an initiative that combines AWS Marketplace offerings with validated AWS Partner tools to help automotive OEMs accelerate their SDV development.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/accelerating-automotive-software-development-on-aws.pdf)Step 1Access to AWS Partner offerings via AWS Marketplace, including trial and evaluation access, to these development tools and virtual targets allowing automotive OEM customers to more easily evaluate and test these offerings before customers engage in full deployment.Step 2SDV Accelerator Workbench is an integrated development environment with tools and virtual targets running on Amazon Elastic Compute Cloud (Amazon EC2) instances designed to help support OEMs develop automotive software.Step 3Continuous integration and deployment using pre-integrated build pipelines for helping OEMs accelerate their software development workflow.Step 4Deploy and test software applications in virtual environments that replicate production conditions.Step 5SDV Accelerator helps automotive OEM developers and testers to speed up their software development cycle, accelerating time-to-market for their vehicle solutions.Step 6SDV Accelerator Internal Developer Portal based on Backstage.io, providing a single pane of glass to documentation, tools and virtual targets.Step 7Amplitude tracks user behavior to guide product development decisions.Step 8Customize in-car voice controls with Alexa Custom Assistant.### Internal Developer Portal Deployment Overview

This architecture diagram shows the deployment overview of an SDV Accelerator Internal Developer Portal (IDP) using AWS services.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/accelerating-automotive-software-development-on-aws.pdf)Step 1SDV Accelerator Solution Guidance users access Backstage.io based IDP (Internal Developer Portal).Step 2Amazon CloudFront caches IDP content globally, improving speed and reducing server load.Step 3Amazon Route 53 provides DNS services, health checks, and intelligent traffic routing.Step 4AWS Web Application Firewall (AWS WAF) protects CloudFront-distributed content from web attacks and malicious traffic.Step 5Application Load Balancer distributes incoming traffic across AWS Fargate containers to ensure high availability and scalability.Step 6A Backstage-based IDP container runs on AWS Fargate using container images stored in Amazon Elastic Container Registry (Amazon ECR). Amazon Relational Database Service (Amazon RDS) stores backend data.Step 7Implement and maintain centralized version control, collaboration features, and CI/CD pipeline integration for software development and deployment with a GitLab repository.Step 8Configure GitLab Runners to automate workflows triggered by GitLab repository events.Step 9SDV Accelerator Environments deploy in private subnets.Step 10Amazon Cognito provides secure authentication and authorization for portal access.Step 11AWS Secrets Manager provides sensitive credentials management, such as license keys, for portal services.Step 12Amazon Simple Storage Service (Amazon S3) provides durable data storage for Solution Guidance artifacts.[Read usage guidelines](/solutions/guidance-disclaimers/)
