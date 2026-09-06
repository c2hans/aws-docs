---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/solution-overview.html
---

# Deliver resilient and secure real-time viewing experiences using AWS Elemental MediaLive and Amazon S3 services
<a name="solution-overview"></a>

Amazon Web Services (AWS) helps broadcasters and content owners to automate media supply chains, streamline content distribution, and cost-effectively broadcast live content to a global audience. With AWS, you can seamlessly scale your infrastructure to meet demand, and pay only for what you use, helping you build highly available and cost-effective solutions for live video streaming.

The Live Streaming on AWS with Amazon S3 solution helps you build highly available live video streaming content using [AWS Elemental MediaLive](https://aws.amazon.com/medialive/) and [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) services to deliver resilient and secure real-time viewing experiences to your customers.

This solution is used only during the live event. When you finish streaming, you can delete the solution’s stack to help ensure that you only pay for the infrastructure you use.

This solution provides the following features:
+ Automatically configures MediaLive and Amazon S3 to encode and originate your content for adaptive bitrate streaming across multiple screens via HTTP Live Streaming (HLS).
+ Provides an elastic, highly available, global content delivery network for live video streaming using [Amazon CloudFront](https://aws.amazon.com/cloudfront/).
+ Supports four input types ([RTP\_PUSH](rtmp-push-and-rtp-push-input-configuration.md), [RTMP\_PUSH](rtmp-push-and-rtp-push-input-configuration.md), [URL\_PULL](url-pull-hls-input-configuration.md), and [INPUT\_DEVICE](aws-elemental-link-input-configuration.md)) as the source for your video stream, including a device input so you can use an [AWS Elemental Link](https://aws.amazon.com/medialive/features/link/) as the source for the input for your live channel.

This implementation guide provides an overview of the Live Streaming on AWS with Amazon S3 solution, its reference architecture and components, considerations for planning the deployment, configuration steps for deploying the solution to the AWS Cloud.

The intended audience for using this solution’s features and capabilities in their environment includes solution architects, business decision makers, DevOps engineers, data scientists, and cloud professionals who have practical experience with video streaming and architecting in the AWS Cloud.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know which AWS Regions support this solution. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/aws-solutions/live-streaming-on-aws-with-amazon-s3/)  |
