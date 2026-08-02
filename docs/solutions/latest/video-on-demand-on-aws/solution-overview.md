---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/solution-overview.html
---

# Deploy a reference implementation to build a scalable, distributed video-on-demand workflow
<a name="solution-overview"></a>

The Video on Demand on AWS solution automatically provisions the AWS services necessary to build a scalable, distributed workflow to ingest, store, process, and deliver video content on demand. It ingests metadata files and source videos, processes the videos for playback on a wide range of devices, stores the transcoded media files, and delivers the videos to end users through CloudFront.

This solution provides an example architecture to build a global consumer video workflow on AWS. By default, the solution can encode MP4, MPG, M4V, M2TS, and MOV files. You can customize the architecture to encode any media file type supported by AWS Elemental MediaConvert. For more information, refer to [Customization](customization.md).

This implementation guide provides an overview of the Video on Demand on AWS solution, its reference architecture and components, considerations for planning the deployment, configuration steps for deploying the solution to the Amazon Web Services (AWS) Cloud.

The intended audience for discovering and using this solution in their environment includes solution architects, business decision makers, DevOps engineers, data scientists, and cloud professionals.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution.<br />The estimated cost for running this solution in the US East (N. Virginia) Region is **USD $ 4.23 per month** for AWS resources. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security-1.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know which AWS Regions support this solution. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/aws-solutions/video-on-demand-on-aws)  |
