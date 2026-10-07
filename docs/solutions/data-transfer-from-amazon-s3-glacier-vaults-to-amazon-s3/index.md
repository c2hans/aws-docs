---
source_url: https://docs.aws.amazon.com/solutions/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/index.html
---

---
title: 'Guidance for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3'
canonical_url: https://docs.aws.amazon.com/solutions/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3

## Overview

This Guidance demonstrates how to automate data transfers to simplify management and enhance both accessibility and cost-effectiveness of archived data. It shows how to automatically restore, copy, and transfer Amazon Simple Storage Service (Amazon S3) Glacier vault archives to S3 buckets and desired storage classes, including S3 Glacier storage classes. This automation saves time and minimizes the likelihood of human error during data transfer, helping ensure a more reliable and consistent operation for managing archived data.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3.pdf)

![Architecture diagram](/images/solutions/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/images/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3-1.png)

1. **Step 1**: Invoke a transfer workflow using an AWS Systems Manager document.
1. **Step 2**: The Systems Manager document starts an AWS Step Functions Orchestrator execution.
1. **Step 3**: The Step Functions Orchestrator execution initiates a nested Step Functions Get Inventory workflow to retrieve the inventory file.
1. **Step 4**: Upon completion of the inventory retrieval, the Guidance invokes the Initiate Retrieval nested Step Functions workflow.
1. **Step 5**: When a job is ready, Amazon Simple Storage Service (Amazon S3) Glacier sends a notification to an Amazon Simple Notification Service (Amazon SNS) topic, indicating job completion.
1. **Step 6**: The Guidance stores all job completion notifications in the Amazon Simple Queue Service (Amazon SQS) Notifications queue.
1. **Step 7**: When an archive job is ready, the Amazon SQS Notifications queue invokes the AWS Lambda Notifications Processor function. This Lambda function prepares the initial steps for archive retrieval.
1. **Step 8**: The Lambda Notifications Processor function places chunks retrieval messages in Amazon SQS Chunks Retrieval queue for chunk processing.
1. **Step 9**: The Amazon SQS Chunks Retrieval queue invokes the Lambda Chunk Retrieval function to process each chunk.
1. **Step 10**: The Lambda Chunk Retrieval function downloads the chunk from Amazon S3 Glacier.
1. **Step 11**: The Lambda Chunk Retrieval function uploads a multipart upload part to Amazon Simple Storage Service (Amazon S3).
1. **Step 12**: After a new chunk is downloaded, the Guidance stores chunk metadata in Amazon DynamoDB (for example, etag, checksum_sha_256, tree_checksum).
1. **Step 13**: The Lambda Chunk Retrieval function verifies whether all chunks for that archive have been processed. If so, it inserts an event into the Amazon SQS Validation queue to invoke the Lambda Validate function.
1. **Step 14**: The Lambda Validate function performs an integrity check against the tree hash in the inventory, calculates a checksum, and passes it to the into the close multipart upload call. If that hash is wrong, Amazon S3 rejects the request.
1. **Step 15**: DynamoDB Streams invokes the Lambda Metrics Processor function to update the transfer process metrics in DynamoDB.
1. **Step 16**: The Step Functions Orchestrator execution enters an async wait, pausing until the archive retrieval workflow concludes before initiating the Step Functions Cleanup workflow.
1. **Step 17**: The DynamoDB stream invokes the Lambda Async Facilitator function, which unlocks asynchronous waits in Step Functions.
1. **Step 18**: Amazon EventBridge rules periodically initiate Step Functions Extend Download Window and Update Amazon CloudWatch Dashboard workflows.
1. **Step 19**: Monitor the transfer progress using a CloudWatch dashboard.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/overview.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance automates the process of copying archives from Amazon S3 Glacier vaults to S3 buckets, reducing manual effort and the risk of errors to improve operational efficiency. Moving data to different Amazon S3 storage classes enables storage cost optimization based on access patterns and retention requirements. The pre-built CloudWatch dashboard visualizes copy operation progress, providing better visibility into the data transfer process and enabling effective monitoring and troubleshooting. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Lambda is a serverless compute service, which helps reduce the attack surface and responsibilities associated with managing underlying infrastructure. This minimizes user involvement in managing and securing compute resources, improving the overall security posture. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The pre-built CloudWatch dashboard provides visibility into the data transfer process, allowing you to monitor progress and identify potential issues or bottlenecks. This enhanced visibility enables you to quickly detect and address reliability-related problems, helping ensure successful completion of data transfers. By using a serverless compute service that automatically scales and manages the underlying infrastructure, you can reduce the risk of infrastructure-related failures or performance degradation. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda functions are triggered based on events, such as the initiation of the data transfer process. The event-driven nature of Lambda functions optimizes performance by only executing necessary compute resources when required. This helps reduce overall resource utilization and improving efficiency. The automatic scaling and management of underlying infrastructure helps ensure that necessary compute resources are allocated on-demand. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By allowing users to move data to different Amazon S3 storage classes, this Guidance enables storage cost optimization based on access patterns and retention requirements. This helps reduce overall storage costs by placing frequently accessed data in performance-optimized storage classes while moving less frequently accessed data to more cost-effective storage classes. Lambda helps optimize costs by only charging for compute time used, rather than requiring users to manage and pay for underlying infrastructure. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda reduces energy consumption and carbon footprint associated with managing and maintaining underlying infrastructure. Serverless computing leads to more efficient resource utilization and potentially lower energy usage compared to traditional server-based architectures. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
