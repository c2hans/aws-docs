---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/services-in-this-solution.html
---

# AWS services in this guidance
<a name="services-in-this-solution"></a>

The following AWS services are included in this guidance:

|  **AWS service**  |  **Description**  |
| --- | --- |
|  [Amazon Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)  |  Core. To distribute network traffic to ingestion fleet.  |
|  [Amazon ECS](https://aws.amazon.com/ecs/)  |  Core. To run the ingestion module fleet.  |
|  [Amazon EC2](https://aws.amazon.com/ec2/)  |  Core. To provide the underlying computing resources for ingestion fleet.  |
|  [Amazon ECR](https://aws.amazon.com/ecr/)  |  Core. To host the container images used by ingestion fleet.  |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  Core. To store the ingested and processed Clickstream data. And it also stores the service logs and static web assets (frontend user interface).  |
|  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/)  |  Supporting. To improve the availability, performance, and security of the ingestion service in AWS Regions.  |
|  [AWS CloudWatch](https://aws.amazon.com/cloudwatch/)  |  Supporting. To monitor the metrics, logs and trace of data pipeline.  |
|  [Amazon SNS](https://aws.amazon.com/sns/)  |  Supporting. To provide topic and email subscription notifications for the alarms of data pipeline.  |
|  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)  |  Supporting. To provide the ingestion buffer.  |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  Supporting. To integrate with kinds of AWS services. For example, sink ingestion data to S3, manage the lifecycle of AWS resources.  |
|  [Amazon Managed Streaming for Apache Kafka (MSK)](https://aws.amazon.com/msk/)  |  Supporting. To provide the ingestion buffer with Apache Kafka.  |
|  [Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/)  |  Supporting. To process the ingested data.  |
|  [Amazon Glue](https://aws.amazon.com/glue/)  |  Supporting. To manage the data catalog of ingested data.  |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  Supporting. To integrate with AWS services with events or schedule.  |
|  [Amazon Redshift](https://aws.amazon.com/redshift/)  |  Supporting. To analyze your Clickstream data in data warehouse.  |
|  [Amazon Athena](https://aws.amazon.com/athena/)  |  Supporting. To analyze your Clickstream data in data lake.  |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  |  Supporting. To orchestrate the lifecycle management of project's pipeline. Also it manages the workflow to load data into data warehouse.  |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)  |  Supporting. To store the credential for OIDC credentials and BI user in Redshift.  |
|  [Quick](https://aws.amazon.com/quicksight/)  |  Supporting. Visual your analysis reporting of your Clickstream data.  |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  Supporting. To made available the static web assets (frontend user interface) and proxy the backend in the same origin.  |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  Supporting. To authenticate users (in AWS Regions).  |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)  |  Supporting. To provide the backend APIs.  |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  Supporting. To store projects data.  |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  Supporting. To provision the AWS resources for the modules of data pipeline.  |
