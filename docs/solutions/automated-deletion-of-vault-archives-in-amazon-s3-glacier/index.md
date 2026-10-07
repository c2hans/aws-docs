---
source_url: https://docs.aws.amazon.com/solutions/automated-deletion-of-vault-archives-in-amazon-s3-glacier/index.html
---

---
title: 'Guidance for Automated Deletion of Vault Archives in Amazon S3 Glacier'
canonical_url: https://docs.aws.amazon.com/solutions/automated-deletion-of-vault-archives-in-amazon-s3-glacier/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Automated Deletion of Vault Archives in Amazon S3 Glacier

## Overview

This Guidance shows how to automate the complex and repetitive tasks associated with deleting data stored in an Amazon S3 Glacier vault. It handles the entire process of downloading the S3 Glacier vault inventory and emptying the vault of its archives. The inventory is then downloaded, split into smaller chunks, and for each chunk, the solution submits multiple concurrent requests to delete all the archives in the list. Once all the archives have been successfully deleted, the S3 Glacier vault itself can then be deleted through a separate process. This automated approach helps to streamline the data deletion workflow, reduce the risk of human error, and help ensure that S3 Glacier vaults are properly maintained on a regular basis.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automated-deletion-of-vault-archives-in-amazon-s3-glacier.pdf)

![Architecture diagram](/images/solutions/automated-deletion-of-vault-archives-in-amazon-s3-glacier/images/automated-deletion-of-vault-archives-in-amazon-s3-glacier-1.png)

1. **Step 1**: The user deploys the template as a stack in the AWS CloudFormation console.
1. **Step 2**: CloudFormation deploys the necessary resources, including custom AWS Lambda resources.
1. **Step 3**: A custom Lambda resource function updates the Amazon S3 Glacier vault notification settings and initiates an inventory job request.
1. **Step 4**: S3 Glacier vault posts a message to an Amazon Simple Notification Service (Amazon SNS) topic when the inventory retrieval job is completed.
1. **Step 5**: The Amazon SNS topic invokes an Initiate State Machine Lambda function.
1. **Step 6**: The function initiates the AWS Step Functions workflow and passes the S3 Glacier vault inventory information as input.
1. **Step 7**: The Step Functions workflow orchestrates the process of downloading the inventory, splitting it into smaller chunks, iterating over the chunks, and deleting the archives.
1. **Step 8**: An invoked Lambda function downloads the inventory to the Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 9**: A Lambda function uses AWS Glue and Amazon Athena to query and split the large inventory manifest into smaller chunks, which are then fed into the Map state of the Step Functions workflow.
1. **Step 10**: The Map state of the Step Functions workflow iterates over each chunk of the inventory manifest. It invokes a Delete Archives AWS Lambda function to submit a delete request for each archive.
1. **Step 11**: Upon successful completion of the workflow, an email notification is sent to the email address provided by the user.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Deploy this Guidance

[Sample codeUse sample code to deploy this Guidance in your AWS account](https://github.com/aws-solutions-library-samples/guidance-for-automated-deletion-of-vault-archives-in-amazon-s3-glacier)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The detailed deployment and workflow status information provided by CloudFormation, Step Functions, Lambda, and Amazon SNS assists in the identification of potential issues and includes detailed messages to facilitate root cause analysis. For example, CloudFormation enables the deployment and visibility of all the created resources, allowing for the tracking of their deployment status. Step Functions provides visibility into the individual steps of the workflow, enabling the tracking of the Lambda function invocations and the overall performance and status of the process. Lambda also writes invocation and other operational events to Amazon CloudWatch Logs, while Amazon SNS informs the user through email of the workflow's status. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) is scoped to provide the minimum permissions required by each component of this Guidance. IAM is designed to enable fine-grained access control to AWS resources and their associated actions. For instance, each Lambda function is granted only the permissions necessary to perform its designated task. IAM was used in this Guidance to achieve this level of granular access control. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This selection of AWS services was driven by their capability to address the specific requirements of this Guidance, such as error handling, scalability, message delivery, and data storage. For example, the use of Step Functions is attributed to its robust error handling capabilities, enabling it to manage throttling, the AWS Software Development Kit (AWS SDK), service errors, and timeout errors. Lambda functions are also employed due to their scalability and high availability characteristics. In addition, Amazon SNS is used to reliably deliver messages to the Lambda service, thereby invoking the necessary functions. Lastly, Amazon S3 provides high-performance, as well as reliable and durable storage. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services selected allow this Guidance to optimize its performance and operate at scale, using a purely serverless infrastructure. Specifically, the Step Functions distributed map is used to orchestrate the parallel execution of tasks, such as Lambda functions. The AWS SDK running within the Lambda functions enables the processing of multiple parallel API requests, while Athena is utilized to query and process large amounts of data at scale using simple SQL queries. Additionally, Amazon S3 provides high-performance, scalable object storage to access the downloaded S3 Glacier vault inventory. The collective capabilities of these AWS services enable this Guidance to quickly and efficiently fulfill its intended function of emptying an S3 Glacier vault without the need to provision and manage large-scale Amazon Elastic Compute Cloud (Amazon EC2) instances or develop custom, complex scripts. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 provides reliable and cost-effective storage for the S3 Glacier vault inventory, with the ability to enable lifecycle rules to expire unused data. Additionally, Step Functions offers a serverless and cost-effective workflow mechanism to orchestrate tasks, while Lambda provides scalable serverless compute. Athena enables querying and splitting of large data sets without expensive compute resources, and Amazon SNS publishes messages to subscribers in a cost-effective manner. Together, these AWS services deliver a comprehensive, serverless framework for managing the cost-effective storage, workflow orchestration, compute scaling, and data processing required to efficiently empty and delete S3 Glacier vaults. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The combined use of Amazon S3, Lambda, Amazon SNS, and Step Functions allows this Guidance, when configured, to sustainably provide data lifecycle management, serverless orchestration, message delivery, and compute resources to power the workflow. Meaning, Amazon S3 features a lifecycle management capability that automatically expires data deemed no longer necessary. And Lambda, an event-driven compute service that is provisioned and allocated only when required, optimizes energy usage. Lambda and Step Functions collectively provide serverless orchestration and compute resources to execute code on-demand in a sustainable manner. Finally, Amazon SNS delivers a serverless messaging service to facilitate communication between applications and their subscribers. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
