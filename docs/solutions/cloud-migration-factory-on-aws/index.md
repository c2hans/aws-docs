---
source_url: https://docs.aws.amazon.com//solutions/cloud-migration-factory-on-aws//index.html
---

---
title: 'Cloud Migration Factory on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/cloud-migration-factory-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Cloud Migration Factory on AWS

Coordinate and automate large-scale wave planning and migrations to the AWS Cloud

- **Version**: 5.0.1
- **Released**: 2/2026
- **Author**: AWS
- **Est. deployment time**: 20 mins
- **Estimated cost**: [See details](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/cost.html)

## Overview

With Cloud Migration Factory on AWS, you can automate manual processes and efficiently integrate multiple migration tools. This automated AWS Solution offers a wave planning manager, orchestration platform, and predefined pipeline templates to improve performance and prevent long cutover windows throughout the migration process. The solution accelerates portfolio assessment with automated wave planning and uses AWS Transform MGN (AWS MGN) to migrate your workloads to AWS at scale. AWS Professional Services, AWS Partners, and other enterprises currently use this solution to automate large-scale migrations.

## Benefits

### Accelerate portfolio assessment and wave planning

Reduce wave planning time with automated application prioritization, dependency analysis, and built-in AWS best practices.

### Automate small, manual tasks for large migrations

Automate the small, manual tasks inherent in large migrations, so you can migrate more quickly and efficiently while reducing the opportunity for human error.

### Orchestrate migrations using a web interface and pipeline

Orchestrate migration activities through a web interface and pre-defined pipeline templates.

### Customize data schema and automation for your needs

With full flexibility by design, you can customize the data schema and develop your own automation and runbooks based on your requirements.

## How it works

You can automatically deploy this architecture using the implementation guide and the accompanying AWS CloudFormation template.

[View implementation guide](/solutions/latest/cloud-migration-factory-on-aws/welcome.html)

![Architecture diagram](/images/solutions/cloud-migration-factory-on-aws/images/cloud-migration-factory-on-aws-1.png)

1. **Step 1**: Amazon API Gateway receives migration requests from the migration automation server through RestAPIs.
1. **Step 2**: AWS Lambda functions provide the necessary services for you to log in to the web interface, perform the necessary administrative functions to manage the migration, and connect to third-party APIs to automate the migration process. - The `user` Lambda function ingests the migration metadata into an Amazon DynamoDB table. Standard HTTP status codes are returned to you through the Rest API from API Gateway. An Amazon Cognito user pool is used for user authentication to the web interface and Rest APIs, and you can optionally configure it to authenticate against external Security Assertion Markup Language (SAML) identity providers. - The `tools` Lambda function processes external Rest APIs and calls external tool functions, such as AWS Transform MGN (AWS MGN) for AWS migration. The `tools` Lambda function also calls the Amazon EC2 launching EC2 instances, and calls AWS Systems Manager to run automation scripts on the Migration Automation Server.
1. **Step 3**: The migration metadata stored in Amazon DynamoDB is routed to the AWS MGN API to initiate Rehost migration jobs and launch servers. If your migration pattern is Replatform to EC2, the `tools` Lambda function launches CloudFormation templates in the target AWS account to launch Amazon EC2 instances.
1. **Step 4**: All notifications are sent to a Notifications Event Bus. Event bridge rules set up to route UI notifications to the UI notifications lambda and Email notifications to the Email notifications lambda. The Email notifications lambda uses Amazon SNS to publish email notifications.
## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/cloud-migration-factory-on-aws/welcome.html)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[Go to the AWS Console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fcloud-migration-factory-on-aws%2Flatest%2Faws-cloud-migration-factory-solution.template&redirectId=SolutionWeb)

## Deployment options

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download template](https://solutions-reference.s3.amazonaws.com/cloud-migration-factory-on-aws/latest/aws-cloud-migration-factory-solution.template)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws-solutions/cloud-migration-factory-on-aws)

- **Implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](/pdfs/solutions/latest/cloud-migration-factory-on-aws/cloud-migration-factory-on-aws.pdf#solution-overview)

## Related content

- **Training: Using AWS Solutions: AWS Cloud Migration Factory**: In this course, you will learn about the features, benefits, and technical implementation of the solution.

[Go to course](https://skillbuilder.aws/learn/KNDJ6BDQGG/using-aws-solutions-aws-cloud-migration-factory/1XM6PZKMBF)

- **Training: Introduction to AWS Transform MGN**: In this course, you will learn key concepts, basic architecture, and implementation approaches for AWS MGN. A step-by-step walk-through guides you through the entire process of performing a migration with AWS MGN. This training is recommended if you are actively working on migration projects with the service or are assisting customers in doing so.

[Go to course](https://skillbuilder.aws/learn/5BKT7UWR9C/introduction-to-aws-application-migration-service/BGQDZQ5Y64)

- **Training: AWS Partners Only: Advanced Migrating to AWS (Technical, classroom based)**: In this course, you will learn how to migrate workloads at scale. This course also covers common migration patterns, including a hands on workshop for Cloud Migration Factory on AWS.

[Go to course](https://partnercentral.awspartner.com/LmsSsoRedirect)

## Pipeline template view

This solution offers pipeline functionality that enables complete management of your pipelines and tasks through a single visual pipeline interface. From this interface, you can manage and monitor your pipelines in real-time, without navigating to any other service or screen. Pipelines can also be composed within the web interface using a visual composer.

![Architecture diagram](/images/solutions/cloud-migration-factory-on-aws/images/cloud-migration-factory-pipeline-template-view.png)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/cloud-migration-factory-on-aws/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/cloud-migration-factory-on-aws/latest/rss.xml)
