---
source_url: https://docs.aws.amazon.com/solutions/data-transfer-hub-on-aws/index.html
---

---
title: 'Guidance for Data Transfer Hub on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/data-transfer-hub-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Data Transfer Hub on AWS

## Overview

This Guidance demonstrates how to securely transfer Amazon Simple Storage Service (Amazon S3) objects and Amazon Elastic Container Registry (Amazon ECR) images across AWS environments. Through an intuitive user interface, you can easily create and manage various types of transfer tasks between AWS partitions (aws, aws-cn, aws-us-gov) and from other cloud providers to AWS. The Guidance provides scalable and trackable data transfers, streamlining the process of moving both Amazon S3 objects and Amazon ECR images between environments. Please note: If you deploy this solution in the AWS (Beijing) Region operated by Beijing Sinnet Technology Co., Ltd. (Sinnet), or the AWS (Ningxia) Region operated by Ningxia Western Cloud Data Technology Co., Ltd., you are required to provide a domain with [ICP Recordal](https://www.amazonaws.cn/en/support/icp) before you can access the web console. The web console is a centralized place to create and manage all data transfer jobs. Each data type (for example, Amazon S3 or Amazon ECR) is a plugin for Data Transfer Hub, and is packaged as an AWS CloudFormation template hosted in an Amazon S3 bucket that AWS owns. When you create a transfer task, an AWS Lambda function initiates the AWS CloudFormation template, and state of each task is stored and displayed in the DynamoDB tables. As of today, the solution supports two data transfer plugins: an Amazon S3 plugin and an Amazon ECR plugin.

## How it works

### Overview

This architecture diagram illustrates how to secure, scale, and track data transfer for Amazon S3 objects and Amazon ECR images.

[Download the architecture diagram PDF](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/images/architecture-diagrams/data-transfer-hub-on-aws-v1.pdf#page=1)Step 1Amazon Simple Storage Service (Amazon S3) stores static web assets (such as the frontend UI), which are made available through Amazon CloudFront.Step 2AWS AppSync GraphQL provides backend APIs.Step 3Users are authenticated by either Amazon Cognito user pools (in AWS Standard Regions) or by an OpenID connect provider (in AWS China Regions) such as Authing or Auth0.Step 4AWS AppSync runs AWS Lambda to call backend APIs.Step 5Lambda starts an AWS Step Functions workflow that uses AWS CloudFormation to start or stop or delete Amazon Elastic Container Registry (Amazon ECR) or the Amazon S3 plugin template.Step 6A centralized S3 bucket, managed by AWS, hosts plugin templates.Step 7The solution also provisions an Amazon Elastic Container Service (Amazon ECS) cluster that runs the container images used by the plugin template, and the container images are hosted in Amazon ECR.Step 8Amazon DynamoDB stores data transfer task information.### S3 transfer option

This architecture diagram illustrates how run the Amazon S3 plugin to transfer objects from their sources into S3 buckets.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/images/architecture-diagrams/data-transfer-hub-on-aws-v1.pdf#page=2)Step 1A time-based EventBridge rule initiates the Lambda function on an hourly basis.Step 2Lambda uses the launch template to launch a data comparison job (JobFinder) in Amazon Elastic Compute Cloud (Amazon EC2).Step 3The job lists all the objects in the source and destination S3 buckets and makes comparisons among objects to determine which objects should be transferred.Step 4Amazon EC2 sends a message for each object that will be transferred to Amazon Simple Queue Service (Amazon SQS). Amazon S3 event messages can also be supported for more real-time data transfer. Whenever an object is uploaded to the source bucket, the event message is sent to the same Amazon SQS queue.Step 5A JobWorker node running in Amazon EC2 consumes the messages in Amazon SQS and transfers the object from the source bucket to the destination bucket. You can use an Auto Scaling group to control the number of EC2 instances to transfer the data based on business needs.Step 6DynamoDB stores a record with transfer status for each object.Step 7The EC2 instance will get (download) the object from the source bucket based on the Amazon SQS message.Step 8The EC2 instance will put (upload) the object to the destination bucket based on the Amazon SQS message.Step 9When the JobWorker node identifies a large file (with a default threshold of 1 GB) for the first time, a multipart upload task running in Amazon EC2 is initiated. The corresponding UploadId is then conveyed to Step Functions, which invokes a scheduled recurring task. Every minute, Step Functions verifies the successful transmission of the distributed shards associated with the UploadId across the entire clusterStep 10If all shards have been transmitted successfully, Amazon EC2 invokes the CompleteMultipartUpload API in Amazon S3 to finalize the consolidation of the shards. Otherwise, any invalid shards are discarded.### ECR transfer option - Pull method

This architecture diagram illustrates how to run the Amazon ECR plugin to transfer container images from other container registries.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/images/architecture-diagrams/data-transfer-hub-on-aws-v1.pdf#page=4)Step 1An Amazon EventBridge rule runs a Step Functions workflow on a regular basis (by default, it runs daily).Step 2Step Functions invokes Lambda to retrieve the list of images from the source.Step 3Lambda will either list all the repository content in the source Amazon ECR or get the stored image list from Parameter Store, a capability of AWS System Manager.Step 4The transfer task will run within AWS Fargate in a maximum concurrency of 10. If a transfer task fails for some reason, it will automatically retry three times.Step 5Each task uses skopeo to copy the images into the target Amazon ECR registry.Step 6After the copy completes, the status (either success or fail) is logged into DynamoDB for tracking purposes.### ECR transfer option - Push method from on-prem

This architecture diagram illustrates how to bulk migrate container images from Local On-Prem repository to Amazon ECR.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/images/architecture-diagrams/data-transfer-hub-on-aws-v1.pdf#page=5)Step 1Guidance code makes an API call to on-prem repository and lists all user repositories.Step 2Guidance code makes an API call to the target Amazon ECR using credentials configured by AWS CLI and checks if the list of on-prem repositories exists in ECR; if not, it creates themStep 3Guidance code returns to on-prem repository and tallies all docker image tags in all repositoriesStep 4Guidance code performs a Checksum verification of image tags in ECR: if a tag exists in ECR and the checksum matches, it is left alone.Step 5Guidance code migrates all Docker container images in bulk to a target Amazon ECR## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](/solutions/latest/data-transfer-hub/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.Use this sample code to deploy the Guidance using the command line interface (CLI)

[Open sample code (console)](https://github.com/aws-solutions-library-samples/data-transfer-hub)
[Open sample code (CLI)](https://github.com/aws-solutions-library-samples/data-transfer-hub-cli)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Step Functions provides a reliable, scalable, and fault-tolerant workflow management system, helping ensure data transfer tasks are executed reliably. Amazon ECS and Amazon ECR simplify the deployment and management of containerized components, improving operational efficiency. These services enable DevOps best practices and promote a culture of continuous improvement and automation while reducing the operational overhead and manual effort required to manage infrastructure and data transfer workflows. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito and OpenID Connect providers help ensure that only authorized users can access and manage data transfer tasks. AWS AppSync provides a secure GraphQL interface to interact with the backend APIs, protecting against unauthorized access. DynamoDB offers secure storage for data transfer task details, with options for encryption at rest. These services provide a comprehensive, end-to-end secure workflow for managing data transfers across AWS partitions and external cloud providers, protecting sensitive data from unauthorized access or tampering. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon ECS and Amazon ECR offer a highly available and scalable way to run and manage container-based components. Amazon Simple Notification Service (Amazon SNS) provides a reliable notification mechanism. These services ensure you can reliably and consistently provision and manage the necessary infrastructure for data transfers, leveraging the scalability and high availability of containerized services like Amazon ECS and Amazon ECR. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda provides a serverless, scalable, and highly performant compute service to run backend components. DynamoDB offers a fast and scalable NoSQL database to store data transfer task information, with low latency access. CloudFront improves performance and responsiveness of the web interface by caching and serving static assets from a global network of edge locations. These services leverage inherent performance and scalability benefits of serverless and managed AWS services, reducing operational overhead while ensuring the Guidance can handle increasing workloads without compromising performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda and the serverless architecture allow for on-demand, pay-as-you-go compute resources, eliminating the need for always-on server infrastructure. DynamoDB provides a pay-per-request NoSQL database service, meaning you only pay for the resources consumed, without incurring costs of provisioning and maintaining a database. Amazon SNS and Amazon SQS provide cost-effective serverless notifications, while Amazon ECS on Fargate enables on-demand infrastructure for containers. This serverless approach helps reduce operational costs and overhead associated with managing and scaling infrastructure. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless design using Lambda, Amazon SQS, and DynamoDB aims at reducing carbon footprint compared to continually operating on-premises servers. Step Functions, Amazon SNS, and Amazon SQS enable serverless notifications, while Amazon ECS on Fargate provides on-demand infrastructure for containers. These serverless and cloud-native services enable you to scale your infrastructure efficiently, reduce required resources and related carbon footprints as compared to on-premises servers, and optimize resource utilization. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
