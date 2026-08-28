---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Core.** Accelerates delivery of your video content to end users. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Core.** Tracks source and destination file metadata and progress through the workflow. |
|  [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)  |  **Core.** Transcodes media files from their source format into versions that play back smartphones, tablets, PCs and other devices. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core.** Runs code without provisioning or managing servers. |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Core.** Provides buckets for object storage. |
|  [Amazon SNS](https://aws.amazon.com/sns/)  |  **Core.** Sends publishing, encoding, and error notifications. |
|  [Amazon SQS](https://aws.amazon.com/sqs/)  |  **Core.** Captures the workflow output. |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  |  **Core.** Builds applications from individual components that each perform a discrete function. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch)  |  **Supporting.** Tracks encoding jobs. |
|  [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)  |  **Supporting.** Assigns granular access policies and permissions to services and users. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting.** Provides application-level resource monitoring and visualization of resource operations and cost data. |
|  [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)  |  **Optional.** Creates video streams formatted to play on several devices from a single video input, and protects content from unauthorized use through content encryption and digital rights management. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
