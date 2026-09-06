---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

The AWS CloudFormation template deploys a workflow that ingests source videos, or source videos and metadata files. When you upload a source video only, encoding options are defined in the AWS CloudFormation template at launch, and are applied to every video the solution encodes. When you upload a source video and metadata file, encoding parameters for each source video are defined in the metadata file, allowing customers to apply encoding options on a video-by-video basis.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution builds the following environment in the AWS Cloud.

 **Video on Demand on AWS architecture**

![video on demand architecture](http://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/images/video-on-demand-architecture.png)

The high-level process flow for the solution components deployed with the AWS CloudFormation template is as follows:

1. An [Amazon S3](https://aws.amazon.com/s3/) bucket for source media files. Content is eventually stored in [Amazon S3 Glacier](https://aws.amazon.com/s3/glacier/) according to the Amazon S3 lifecycle policy.

1.  [AWS Step Functions](https://aws.amazon.com/step-functions/), which creates ingest, processing, and publishing step functions.

1.  [AWS Lambda](https://aws.amazon.com/lambda/) functions that perform the work of each step, and process error messages. For a description of the 10 Lambda functions, refer to the [README.md](https://github.com/awslabs/video-on-demand-on-aws#nodejs-12) file on the GitHub repository.

1. An [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table to store data captured through the workflow.

1.  [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/) to transcode media files from their source format.

1.  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) for logging and Amazon CloudWatch Events rules for AWS Elemental MediaConvert notifications.

1.  [Amazon SNS](https://aws.amazon.com/sns/) topics to send encoding, publishing, and error notifications.

1.  [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/) (optional) to create video streams formatted to play on several devices from a single video input, and protect content from unauthorized use through content encryption and digital rights management.

1. An Amazon S3 bucket for storing destination media files.

1. An [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution to deliver your video content to end users.

1. An [Amazon SQS](https://aws.amazon.com/sqs/) queue to capture the workflow outputs.
