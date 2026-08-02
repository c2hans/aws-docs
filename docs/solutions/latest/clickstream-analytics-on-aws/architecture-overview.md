---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

 This section provides a reference implementation architecture diagram for the components deployed with this guidance.

## Architecture diagram
<a name="architecture-diagram"></a>

### Guidance end-to-end architecture
<a name="solution-end-to-end-architecture"></a>

 Deploying this guidance with the default parameters builds the following environment in AWS:

![Clickstream Analytics on AWS architecture](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/clickstream-analytics-on-aws.png)

 This guidance deploys the AWS CloudFormation template in your AWS Cloud account and completes the following settings.

1.  An[Amazon Cognito](https://aws.amazon.com/cognito) user pool or OpenID Connect (OIDC) handles authentication.

1.  [Amazon CloudFront](https://aws.amazon.com/cloudfront) distributes the frontend web UI assets hosted in the [Amazon S3](https://aws.amazon.com/s3/) bucket.

1.  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) manages the backend APIs and routes traffic to [AWS Lambda](https://aws.amazon.com/lambda).

1.   [Amazon DynamoDB](https://aws.amazon.com/dynamodb) stores persistent data from the web UI console.

1.  [AWS Step Functions](https://aws.amazon.com/step-functions), [AWS CloudFormation](https://aws.amazon.com/cloudformation), [AWS Lambda](https://aws.amazon.com/lambda) and [Amazon EventBridge](https://aws.amazon.com/eventbridge) orchestrate the lifecycle management of data pipelines.

1.  The data pipeline, consisting of [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Amazon ECS](https://aws.amazon.com/ecs/), [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/), [Amazon Kinesis](https://aws.amazon.com/kinesis/) Data Streams, Amazon S3, [Amazon EMR](https://aws.amazon.com/emr/) Serverless, [Amazon Redshift](https://aws.amazon.com/redshift/), and [Quick](https://aws.amazon.com/quicksight/) provides scalable clickstream ingestion through load-balanced processing, buffered storage, ETL, and warehouse analytics.

 The key functionality of this guidance is to build a data pipeline to collect, process, and analyze their clickstream data. The data pipeline consists of four modules:
+  Ingestion module
+  Data processing module
+  Data modeling module
+  Reporting module

 The following introduces the architecture diagram for each module.

### Ingestion module
<a name="ingestion-module"></a>

![Ingestion module architecture](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/ingestion-module-arch.png)

 Suppose you create a data pipeline in the guidance. This guidance deploys the Amazon CloudFormation template in your AWS account and completes the following settings.

**Note**
 The ingestion module supports three types of data sinks. You can only have one type of data sink in a data pipeline.

1.  (Optional) The ingestion module creates an AWS global accelerator endpoint to reduce the latency of sending events from your clients (web applications or mobile applications).

1.  [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/) is used for load balancing ingestion web servers.

1.  (Optional) If you enable the authenticating feature, the ALB will communicate with the OIDC provider to authenticate the requests.

1.  ALB forwards all authenticated and valid requests to the ingestion servers.

1.  Amazon ECS cluster is hosting the ingestion fleet servers. Each server consists of a proxy and a worker service. The proxy is a facade of the HTTP protocol, and the worker will send the events to a data sink based on your choice.

1. If Amazon Kinesis Data Streams is used as a buffer, AWS Lambda consumes the clickstream data in Kinesis Data Streams and then sinks them to Amazon S3 in batches.

1. If Amazon MSK is used as a buffer, MSK Connector is provisioned with an S3 connector plugin that sinks the clickstream data to Amazon S3 in batches.

1. If Amazon S3 is selected as data sink, the ingestion server will buffer a batch of events and sink them to Amazon S3.

### Data processing module
<a name="data-processing-module"></a>

![Data processing module architecture](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/data-processing-module-arch.png)

 Suppose you create a data pipeline in the guidance and enable data processing. This guidance deploys the Amazon CloudFormation template in your AWS Cloud account and completes the following settings.

1.  Amazon EventBridge is used to trigger the data processing jobs periodically.

1.  The configurable time-based scheduler invokes an AWS Lambda function.

1.  The Lambda function kicks off an EMR Serverless application based on Spark to process a batch of clickstream events.

1.  The EMR Serverless application uses the configurable transformer and enrichment plug-ins to process the clickstream data from the source S3 bucket.

1.  After processing the clickstream events, the EMR Serverless application sinks the processed clickstream data to the sink S3 bucket.

### Data modeling module
<a name="data-modeling-module"></a>

![Data modeling in Redshift architecture](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/data-modeling-module-arch.png)

 Suppose you create a data pipeline in the guidance and enable data modeling in Amazon Redshift. This guidance deploys the Amazon CloudFormation template in your AWS Cloud account and completes the following settings.

1.  After the processed clickstream data is written in the Amazon S3 bucket, the `Object Created Event` is emitted.

1.  An Amazon EventBridge rule is created for the event emitted in step 1, and an AWS Lambda function is invoked when the event happens.

1.  The Lambda function persists the source event to be loaded in an Amazon DynamoDB table.

1.  When data processing job is done, an event is emitted to Amazon EventBridge.

1.  The pre-defined event rule of Amazon EventBridge processes the EMR job success event.

1.  The rule invokes the AWS Step Functions workflow.

1.  The workflow invokes the `list objects` Lambda function that queries the DynamoDB table to find out the data to be loaded, then creates a manifest file for a batch of event data to optimize the load performance.

1.  After a few seconds, the `check status` Lambda function checks the status of the loading job.

1.  If the load is still in progress, the `check status` Lambda function waits for a few more seconds.

1.  After all objects are loaded, the workflow ends.

![Data modeling in Athena architecture](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/data-modeling-in-athena-arch.png)

 Suppose you create a data pipeline in the guidance and enable data modeling in Amazon Athena. This guidance deploys the Amazon CloudFormation template in your AWS Cloud account and completes the following settings.

1.  Amazon EventBridge invokes the data load into [Amazon Athena](https://aws.amazon.com/athena/) periodically.

1.  The configurable time-based scheduler invokes an AWS Lambda function.

1.  The AWS Lambda function creates the partitions of the [AWS Glue](https://aws.amazon.com/glue/) table for the processed clickstream data.

1.  Amazon Athena is used for interactive querying of clickstream events.

1.  The processed clickstream data is scanned via the Glue table.

### Reporting module
<a name="reporting-module"></a>

![Reporting module architecture](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/reporting-module.png)

 Suppose you create a data pipeline in the guidance, enable data modeling in Amazon Redshift, and enable reporting in Quick. This guidance deploys the Amazon CloudFormation template in your AWS Cloud account and completes the following settings.

1.  VPC connection in Quick is used for securely connecting your Redshift within VPC.

1.  The data source, data sets, template, analysis, and dashboard are created in Quick for out-of-the-box analysis and visualization.

### Analytics Studio
<a name="analytics-studio-2"></a>

Analytics Studio is a unified web interface for business analysts or data analysts to view and create dashboards, query and explore clickstream data, and manage metadata.

![Analytics Studio architecture](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/analytics-studio-arch.png)

1. When analysts access Analytics Studio, requests are sent to [Amazon CloudFront](https://aws.amazon.com/cloudfront/), which distributes the web application.

1. When the analysts log in to Analytics Studio, the requests are redirected to the [Amazon Cognito](https://aws.amazon.com/cognito/) user pool or OpenID Connect (OIDC) for authentication.

1. [Amazon API Gateway](https://aws.amazon.com/api-gateway/) hosts the backend API requests and uses the custom Lambda authorizer to authorize the requests with the public key of OIDC.

1. API Gateway integrates with [AWS Lambda](https://aws.amazon.com/lambda/) to serve the API requests.

1. The AWS Lambda function uses [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) to retrieve and persist the data.

1. When analysts create analyses, the Lambda function requests [Amazon QuickSight](https://aws.amazon.com/quicksight/) to create assets and get the embed URL in the data pipeline Region.

1. The browser of analysts accesses the QuickSight embed URL to view the QuickSight dashboards and visuals.
