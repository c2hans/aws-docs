---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

 Deploying the Media2Cloud on AWS solution builds the following environment in the AWS Cloud.

![Media2Cloud on AWS architecture on AWS](https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-architecture-diagram.png)

 The AWS CloudFormation template deploys the following infrastructure:

1.  An [Amazon Cognito](https://aws.amazon.com/cognito/) user pool to provide a user directory.

1.  An [Amazon API Gateway](https://aws.amazon.com/api-gateway/) RESTful API endpoint, which is configured to use AWS IAM authentication.

1.  An [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution that hosts the web application artifacts such as minimized JavaScript files and graphics stored in the web bucket.

1.  An [AWS Step Functions](https://aws.amazon.com/step-functions/) main state machine which serves as the entry point to the solution’s backend ingestion and analysis workflows.

1.  An AWS Step Functions ingestion sub-state machine that orchestrates the ingestion process by media file type and generates proxies for ingested media. It uses [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/) for video and audio files and open-source tools for image files and documents.

1.  A Step Functions analysis sub-state machine that is responsible for the analysis process. It consists of AWS Step Functions that run analysis jobs with [Amazon Rekognition](https://aws.amazon.com/rekognition/), [Amazon Transcribe](https://aws.amazon.com/transcribe/), [Amazon Comprehend](https://aws.amazon.com/comprehend/), and [Amazon Textract](https://aws.amazon.com/textract/).

1.  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) tables to store artifacts generated during the ingestion and analysis processes, such as overall status, pointers to where intermediate files are stored, and state machine run tokens.

1.  An [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) cluster, which stores ingestion attributes and machine learning metadata, and facilitates customers’ search and discovery needs.

1.  Four [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) buckets to store uploaded content, file proxies that the solution generates during ingestion, static web application artifacts, and access logs for services used.

1.  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) event rules that are logged when specific tasks undergo state changes.

1.  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) used by an internal queue management system where the backlog system notifies workflows (state machines) when a queued AI/ML request has been processed.

1.  An [AWS IoT Core](https://aws.amazon.com/iot-core/) topic that allows the ingestion and analysis workflows to communicate with the front-end web application asynchronously through publish/subscribe MQTT messaging.

1.  [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) topics to allow Amazon Rekognition to publish job status in the video analysis workflow, and to support custom integration with customers’ system, by allowing the solution to publish `ingest_completed` and `analysis_completed` events.
