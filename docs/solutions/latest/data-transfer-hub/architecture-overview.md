---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

 This section provides reference implementation architecture diagrams for the components deployed with this Guidance.

## Architecture diagram
<a name="architecture-diagram"></a>

 Deploying the Data Transfer Hub Guidance with the default parameters builds the following environment in the AWS Cloud.

![Data Transfer Hub architecture on AWS](https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/guidance-arch.png)

 The Guidance automatically deploys and configures a serverless architecture with the following services:

1.  [Amazon Simple Storage Service](https://aws.amazon.com/s3/) stores static web assets (such as the frontend UI), which are made available through [Amazon CloudFront](https://aws.amazon.com/cloudfront/).

1.  [AWS AppSync](https://aws.amazon.com/appsync/) GraphQL provides backend APIs.

1.  Users are authenticated by either [Amazon Cognito](https://aws.amazon.com/cognito/) user pools (in AWS Standard Regions) or by an OpenID connect provider (in AWS China Regions) such as [Authing](https://www.authing.cn/), [Auth0](https://auth0.com/).

1.  AWS AppSync runs [AWS Lambda](https://aws.amazon.com/lambda/) to call backend APIs.

1.  Lambda starts an [AWS Step Functions](https://aws.amazon.com/step-functions/) workflow that uses [AWS CloudFormation](https://aws.amazon.com/cloudformation/) to start or stop/delete the Amazon ECR or Amazon S3 plugin template.

1.  A centralized S3 bucket hosts plugin templates.

1.  The Guidance also provisions an [Amazon ECS](https://docs.aws.amazon.com/ecs/) cluster that runs the container images used by the plugin template, and the container images are hosted in [Amazon ECR](https://aws.amazon.com/ecr/).

1.  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) stores data transfer task information.

 After deploying the Guidance, you can use [AWS WAF](https://aws.amazon.com/waf/) to protect CloudFront or AppSync.

**Important**
If you deploy this Guidance in AWS (Beijing) Region operated by Beijing Sinnet Technology Co., Ltd. (Sinnet), or the AWS (Ningxia) Region operated by Ningxia Western Cloud Data Technology Co., Ltd., you are required to provide a domain with [ICP Recordal](https://www.amazonaws.cn/en/support/icp/) before you can access the web console.

 The web console is a centralized place to create and manage all data transfer jobs. Each data type (for example, Amazon S3 or Amazon ECR) is a plugin for Data Transfer Hub, and is packaged as an AWS CloudFormation template hosted in an S3 bucket that AWS owns. When the you create a transfer task, an AWS Lambda function initiates the Amazon CloudFormation template, and state of each task is stored and displayed in the DynamoDB tables.

 As of this revision, the Guidance supports two data transfer plugins: an Amazon S3 plugin and an Amazon ECR plugin.

**Amazon S3 plugin**

![Data Transfer Hub Amazon S3 plugin architecture](https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/guidance-s3-plugin.png)

 The Amazon S3 plugin runs the following workflows:

1.  A time-based EventBridge rule initiates the AWS Lambda function on an hourly basis.

1.  AWS Lambda uses the launch template to launch a data comparison job (JobFinder) in an [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/).

1.  The job lists all the objects in the source and destination Amazon S3 buckets and makes comparisons among objects to determine which objects should be transferred.

1.  Amazon EC2 sends a message for each object that will be transferred to [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/). Amazon S3 event messages can also be supported for more real-time data transfer. Whenever there is object uploaded to source bucket, the event message is sent to the same Amazon SQS queue.

1.  A JobWorker node running in Amazon EC2 consumes the messages in Amazon SQS and transfers the object from the source bucket to the destination bucket. You can use an Auto Scaling group to control the number of Amazon EC2 instances to transfer the data based on business needs.

1.  DynamoDB stores a record with transfer status for each object.

1.  The Amazon EC2 instance will get (download) the object from the source bucket based on the Amazon SQS message.

1.  The Amazon EC2 instance will put (upload) the object to the destination bucket based on the Amazon SQS message.

1. When the JobWorker node identifies a large file (with a default threshold of 1 GB) for the first time, a Multipart Upload task running in Amazon EC2 is initiated. The corresponding UploadId is then conveyed to the AWS Step Functions, which invokes a scheduled recurring task. Every minute, AWS Step Functions verifies the successful transmission of the distributed shards associated with the UploadId across the entire cluster.

1. If all shards have been transmitted successfully, Amazon EC2 invokes the CompleteMultipartUpload API in Amazon S3 to finalize the consolidation of the shards. Otherwise, any invalid shards are discarded.

**Note**
If an object (or part of an object) transfer failed, the JobWorker releases the message in the queue, and the object is transferred again after the message is visible in the queue (default visibility timeout is set to 15 minutes). If the transfer failed five times, the message is sent to the dead letter queue and a notification alarm is initiated.

 **Amazon ECR plugin**

![Data Transfer Hub Amazon ECR plugin architecture](https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/guidance-ecr-plugin.png)

 The Amazon ECR plugin runs the following workflows:

1.  An Amazon EventBridge rule runs an AWS Step Functions workflow on a regular basis (by default, it runs daily).

1.  Step Functions invokes AWS Lambda to retrieve the list of images from the source.

1.  Lambda will either list all the repository content in the source Amazon ECR, or get the stored image list from Parameter Store, a capability of AWS System Manager.

1.  The transfer task will run within AWS FARGATE; in a maximum concurrency of 10. If a transfer task failed for some reason, it will automatically retry three times.

1.  Each task uses [skopeo](https://github.com/containers/skopeo) to copy the images into the target Amazon ECR registry.

1.  After the copy completes, the status (either success or fail) is logged into DynamoDB for tracking purposes.
