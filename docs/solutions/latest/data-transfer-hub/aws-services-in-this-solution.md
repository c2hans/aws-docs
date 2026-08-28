---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/aws-services-in-this-solution.html
---

# AWS services in this Guidance
<a name="aws-services-in-this-solution"></a>

 The following AWS services are included in this Guidance:

|  **AWS service**  |  **Description**  |
| --- | --- |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  Core. To made available the static web assets (frontend user interface).  |
|  [AWS AppSync](https://aws.amazon.com/appsync/)   |  Core. To provide the backend APIs.  |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  Core. To call backend APIs.  |
|  [Amazon ECS](https://aws.amazon.com/ecs/)  |  Core. To run the container images used by the plugin template.  |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  Core. To store a record with transfer status for each object.  |
|  [Amazon EC2](https://aws.amazon.com/ec2/)  |  Core. To consume the messages in Amazon SQS and transfer the object from the source bucket to the destination bucket.  |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)  |  Core. Stores the credential for data transfer.  |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  |  Supporting. To start or stop/delete the ECR or S3 plugin template.  |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  Supporting. To authenticate users (in AWS Regions).  |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  Supporting. To store the static web assets (frontend user interface).  |
|  [Amazon ECR](https://aws.amazon.com/ecr/)  |  Supporting. To host the container images.  |
|  [Amazon SQS](https://aws.amazon.com/sqs/)  |  Supporting. To store the transfer tasks temporarily as a buffer.  |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  Supporting. To invoke the transfer tasks regularly.  |
|  [Amazon SNS](https://aws.amazon.com/sns/)  |  Supporting. Provides topic and email subscription notifications for data transfer results.  |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  Supporting. To monitor the data transfer progress.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
