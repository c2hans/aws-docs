---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/workflow-configuration.html
---

# Workflow configuration
<a name="workflow-configuration"></a>

The `Input Validate` AWS Lambda function contains the following environment variables that define the workflow configuration.

| Environment Variable | Description |
| --- | --- |
|  **Archive Source**  | Choose whether to archive source videos in Amazon Glacier or Glacier Deep Archive. |
|  **CloudFront**  | The CloudFront domain name. This is used to generate the playback URLs for the MediaConvert outputs. |
|  **Destination**  | The name of the destination Amazon S3 bucket for all MediaConvert outputs. |
|  **FrameCapture**  | Choose whether to create thumbnails for each MediaConvert output. |
|  **MediaConvert\_Template\_2160p**  | The name of the UHD template for MediaConvert. |
|  **MediaConvert\_Template\_1080p**  | The name of the HD template for MediaConvert. |
|  **MediaConvert\_Template\_720p**  | The name of the SD template for MediaConvert. |
|  **Source**  | The name of the source Amazon S3 bucket. |
|  **WorkflowName**  | Used to tag MediaConvert encoding jobs. This is defined by the AWS CloudFormation stack name. |
|  **InputRotate**  | Specify how MediaConvert should rotate the source video. |
|  **AcceleratedTranscoding**  | The option to activate Accelerated Transcoding in MediaConvert. |
|  **EnableSQS**  | The option to activate SQS. |
|  **EnableSNS**  | The option to activate SNS. |

These variables are set when you deploy the AWS CloudFormation template and apply to all source videos uploaded to the solution’s Amazon S3 bucket.

If you set the solution to ingest source videos and metadata files, you can overwrite these files using a metadata file. For more information, refer to [MediaConvert templates](mediaconvert-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
