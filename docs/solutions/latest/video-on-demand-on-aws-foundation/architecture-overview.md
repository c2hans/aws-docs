---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

 This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

 Deploying this solution with the default parameters deploys the following components in your AWS account.

![Architecture diagram depicting the following steps.](http://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/images/vod-on-aws-foundation-architecture-diagram.png)

 The AWS CloudFormation template deploys the following infrastructure:

1.  An [Amazon S3](https://aws.amazon.com/s3/) bucket stores source video files. The solution uploads a sample job settings file to the source S3 bucket. This file defines the encoding settings for [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/).

1.  An [AWS Lambda](https://aws.amazon.com/lambda/) job submit function creates the encoding jobs in MediaConvert.

1.  MediaConvert transcodes the video into HLS adaptive bitrate (ABR) files.

1.  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) logs metrics about encoding jobs in MediaConvert.

1.  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) invokes the Lambda job complete function.

1.  A Lambda job complete function processes the outputs.

1.  An [Amazon SNS](https://aws.amazon.com/sns/) topic sends notifications of completed jobs.

1.  A destination S3 bucket stores the MediaConvert outputs.

1.  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) is configured with the destination S3 bucket as the origin for global distribution of the transcoded video content.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
