---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/ingestion-pipeline.html
---

# Building the data ingestion pipeline for your Amazon selling partner data
<a name="ingestion-pipeline"></a>

This section provides a strategy to ingests Amazon vendor and seller data from the Amazon Selling Partner API (SP-API) to a data lake in your AWS account. This data pipeline architecture is designed for agility. After the data is available in your account, you can implement analytics and generative AI capabilities to obtain advanced business insights from this data. This data helps you understand your business, inventory details, and analytics at scale across all marketplaces.

The following architecture diagram shows how you use [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions in an [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) workflow in order to ingest data from the SP-API into a data lake in your AWS account. The data is stored in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) and in [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), which is a capability of AWS Systems Manager.

![Serverless architecture that ingests data from the SP-API and stores it in a data lake.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/images/guide-img/fd951ab0-b7f5-4ded-9451-ea838cf4c59a/images/f91d3c2a-ca5c-4272-bd9e-2c9893c765a4.png)

The architecture diagram includes the following components:

1. Step Functions is used as a serverless orchestration service to centrally manage the workflow for integrating with the SP-API.

1. The [Selling Partner API for Reports](https://developer-docs.amazon.com/sp-api/docs/reports-api-v2021-06-30-use-case-guide) (Reports API) supports notifications to automate the report workflows. For this, you use an **SP-API notification** Lambda function to subscribe the application to the `REPORT_PROCESSING_FINISHED` notification type.

1. In order to make calls to the SP-API, you use an **Authentication** Lambda function to obtain a Login with Amazon (LWA) access token.

1. The LWA access token from the authentication function is passed to a **Report creator** Lambda function. This function makes a `createReport` call to the SP-API by using the LWA access token and the regional endpoints, marketplace IDs, and report configurations data that is stored in Parameter Store.

1. The SP-API generates the report. Upon completion, a `REPORT_PROCESSING_FINISHED` notification event is sent to an [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) queue, which provides information when report processing is `CANCELLED`, `DONE`, or `FATAL`. This triggers a **Notification processing** Lambda function to process the event. If the notification event has a status of `DONE`, a `reportDocumentId` is included.

1. The notification event is passed to a **Data processing** Lambda function in the Step Functions workflow. This function uses the `reportDocumentId` to make a `getReportDocument` call to the SP-API. The SP-API returns a pre-signed URL for the location of the report document and the compression algorithm used, if the report document contents have been compressed.

1. This response is passed to a **Storage** Lambda function, which downloads the report document, decompresses it (if applicable), and stores the report document in Amazon S3.

1. [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) is used to centrally manage encryption keys, which can be used to encrypt the secrets in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). Data is stored in Amazon S3 and Parameter Store.

1. SP-API requests are limited by using the token bucket algorithm. Therefore, an API client is recommended for rate limiting.

1. [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) are used for monitoring and logging across the AWS services. These logs provide traceability.
