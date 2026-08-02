---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/aws-services-in-this-solution.html
---

# AWS services in this solution
<a name="aws-services-in-this-solution"></a>

|  AWS service  |  Description  |
| --- | --- |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)  |  Core. Provides the RESTful API endpoint, which is configured to use IAM authentication.  |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  Core. Hosts the web application artifacts such as minimized JavaScript files and graphics stored in the web bucket.  |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  Core. Provides user directory and access management.  |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  Core. Provides the storage for artifacts generated during the ingestion and analysis processes, such as overall status, pointers to where intermediate files are stored, and state machine run tokens.  |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  Core. Supports orchestration of ingestion and analysis workflows.  |
|  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)  |  Core. Stores ingestion attributes and machine learning metadata, and facilitates customers' search and discovery needs.  |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  Core. Provides storage for the uploaded content, file proxies that the solution generates during ingestion, static web application artifacts, and access logs for services used.  |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  |  Core. Provides main state machine which serves as the entry point to the solution's backend ingestion and analysis workflows.  |
|  [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)  |  Supporting. Can be integrated into workflows to transcode input video into mpeg4 format and generate proxies for ingested media.  |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  Supporting. Used by an internal queue management system where the backlog system notifies workflows (state machines) when a queued AI/ML request has been processed.  |
|  [AWS IoT Core](https://aws.amazon.com/iot-core/)  |  Supporting. Allows the ingestion and analysis workflows to communicate with the front-end web application asynchronously through publish/subscribe MQTT messaging.  |
|  [Amazon SNS](https://aws.amazon.com/sns/)  |  Supporting. Allows Amazon Rekognition to publish job status in the video analysis workflow. In addition, Amazon SNS allows Amazon Rekognition to support custom integrations with customers' systems by allowing the solution to publish ingest\_completed and analysis\_completed events.  |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  Supporting. Provides application-level resource monitoring and visualization of resource operations and cost data.  |
|  [Amazon Comprehend](https://aws.amazon.com/comprehend/)  |  Optional. Can be integrated into workflows to find key phrases in text and references to real-world objects, dates, and quantities in text.  |
|  [Amazon Rekognition](https://aws.amazon.com/rekognition/)  |  Optional. Can be integrated into workflows for celebrity recognition, content moderation, face detection, face search, label detection, person tracking, shot, text, and technical cue detection.  |
|  [Amazon Textract](https://aws.amazon.com/textract/)  |  Optional. Can be integrated into workflows to extract tabular metdata from documents using Optical Character Recognition (OCR).  |
|  [Amazon Transcribe](https://aws.amazon.com/transcribe/)  |  Optional. Can be integrated into workflows to create SRT or VTT captions files from video transcripts. It can also convert input audio to text.  |
