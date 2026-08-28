---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/solution-overview.html
---

# Deploy a customizable architecture to build a video-on-demand workflow
<a name="solution-overview"></a>

Publication date: *December 2020 ([last update](revisions.md): November 2024)*

 Video on Demand on AWS Foundation is a reference implementation that automatically provisions the Amazon Web Services (AWS) services necessary to build a scalable, distributed video-on-demand workflow.

 To build highly available, resilient architectures that ingest, store, process, and deliver video content on demand, this solution uses the following AWS services:
+  [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/) to transcode media files from their source format into versions that play back on smartphones, tablets, PCs, and other devices.
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) for global distribution.
+  [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) for object storage.
+  [AWS Lambda](https://aws.amazon.com/lambda/) to run code without provisioning or managing servers.
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) to invoke the Lambda job complete function.
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to log metrics about encoding jobs in MediaConvert.
+  [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) to send notifications for completed jobs.

 We designed this solution to help you begin encoding video files with MediaConvert. Out of the box, this solution provides a sample MediaConvert `job-settings.json` file, which you can use to transcode videos uploaded to an Amazon S3 bucket. By default, the solution can encode MP4, MPG, M4V, M2TS, and MOV files. You can customize the architecture to encode any media file type supported by MediaConvert. For more information, refer to [Customization](customization.md).

 If you want to build out more complex workflows with options around ingest processing and publishing video content, AWS also offers the [Video on Demand on AWS](https://aws.amazon.com/solutions/implementations/video-on-demand-on-aws) solution.

 This implementation guide provides an overview of the Video on Demand on AWS Foundation solution, its reference architecture and components, considerations for planning the deployment, configuration steps for deploying the solution to the AWS Cloud.

 The intended audience for using this solution's features and capabilities in their environment includes IT infrastructure architects, solution architects, administrators, business decision makers, DevOps engineers, data scientists, and cloud professionals.

 Use this navigation table to quickly find answers to these questions:

|  If you want to . . .  |  Read . . .  |
| --- | --- |
|  Know the cost for running this solution. <br /> The estimated cost for running this solution in the US East (N. Virginia) Region is approximately $232.86 per month, per job for AWS resources.  |  [Cost](cost.md)  |
|  Understand the security considerations for this solution.  |  [Security](security-1.md)  |
|  Know how to plan for quotas for this solution.  |  [Quotas](quotas.md)  |
|  Know which AWS Regions support this solution.  |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
|  View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution.  |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. | [GitHub repository](https://github.com/awslabs/video-on-demand-on-aws-foundations) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
