---
source_url: https://docs.aws.amazon.com//solutions/modern-data-architecture-accelerator//index.html
---

# Modern Data Architecture Accelerator

Rapidly deploy and manage sophisticated data foundation on AWS

- **Version**: 1.7.0
- **Released**: 7/2026
- **Author**: AWS
- **Estimated cost**: [See details](/solutions/latest/modern-data-architecture-accelerator/cost.html)

## Overview

Modern Data Architecture Accelerator (MDAA) accelerates the implementation of a secure and compliant data environment on AWS. This AWS Solution helps organizations of all sizes maintain high assurance of security compliance, freeing up time to focus on data-driven business outcomes. Use MDAA to rapidly solve complex data challenges through both traditional analytics and the latest technology, such as generative AI.

## Benefits

### Secure your data instantly

Implement comprehensive data governance with built-in security, privacy, and compliance controls configured to best practices.

### Power your analytics workloads

Access pre-configured analytics services and data processing pipelines designed for both traditional and generative AI-powered analytics.

### Optimize costs automatically

Manage spending efficiently with data lifecycle features and built-in cost optimization tools.

### Deploy in weeks, not months

Launch a production-ready modern data environment in weeks with pre-built templates and automated infrastructure deployment.

## How it works

You can automatically deploy this architecture using the implementation guide and the accompanying AWS CloudFormation template.

[Open implementation guide](/solutions/latest/modern-data-architecture-accelerator/solution-overview.html)

![Architecture diagram](/images/solutions/modern-data-architecture-accelerator/images/modern-data-architecture-accelerator-1.png)

1. **Step 1**: You use AWS CloudFormation to install MDAA into your environment. Your environment must meet prerequisites before deploying the solution. (See [PREDEPLOYMENT](https://github.com/aws/modern-data-architecture-accelerator/blob/main/PREDEPLOYMENT.md) .) The provided CloudFormation template deploys an AWS CodePipeline that contains the MDAA installation engine for building analytics platforms.
1. **Step 2**: The Modern Data Architecture (Lake House) framework functions as the core architecture pattern. This way, you can establish a flexible, scalable foundation for solving virtually any data problem—using analytics, data science, or AI/ML—on AWS. The architecture remains fully open and interoperable with data capabilities both inside and outside of AWS.
1. **Step 3**: An S3-based data lake serves as the core component, wrapped with a unified data governance layer. The solution deploys AWS Glue and AWS Lake Formation to provide comprehensive data cataloging and access controls. Additionally, the solution implements a DataOps layer to facilitate seamless data movement between the core data lake and purpose-built analytics services on the perimeter.
1. **Step 4**: The solution deploys purpose-built analytics services that you can select based on specific use cases. These services support various analytical workloads including traditional BI, data science, and machine learning. The solution maintains flexibility to add or modify analytics services as requirements evolve.
1. **Step 5**: For organizations requiring distributed data architecture, MDAA supports deployment of Data Mesh patterns. Each business unit can operate an autonomous data mesh node, typically implementing an individual Lake House architecture. The solution enables producer/consumer relationships between nodes while maintaining unified governance.
## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/modern-data-architecture-accelerator/solution-overview.html?target=_blank)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[Launch in the AWS Console](https://console.aws.amazon.com/cloudformation/home#/stacks/new?&templateURL=https://solutions-reference.s3.amazonaws.com/modern-data-architecture-accelerator/latest/MdaaInstallerStack.template&redirectId=SolutionWeb&target=_blank)

## Deployment options

- **Download implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](/pdfs/solutions/latest/modern-data-architecture-accelerator/modern-data-architecture-accelerator.pdf?target=_blank)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws/modern-data-architecture-accelerator?target=_blank)

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download template](https://s3.amazonaws.com/solutions-reference/modern-data-architecture-accelerator/latest/MdaaInstallerStack.template)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/modern-data-architecture-accelerator/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/modern-data-architecture-accelerator/latest/rss.xml)
