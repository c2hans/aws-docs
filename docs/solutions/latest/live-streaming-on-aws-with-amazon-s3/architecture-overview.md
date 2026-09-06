---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

 **Live streaming on AWS with MediaStore architecture**

![live streaming on aws with mediastore](http://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/images/live-streaming-on-aws-with-mediastore.png)

The AWS CloudFormation template launches the AWS products and services necessary to ingest, transcode, and deliver live streaming video.

1.  [AWS Elemental MediaLive](https://aws.amazon.com/medialive/) ingests an input feed and transcodes your content into one adaptive bitrate (ABR) HTTP Live Streaming (HLS) stream as output.

1.  [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) provides a scalable highly available storage bucket to host the encoded segments.

1. An [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution is configured to use the Amazon S3 custom endpoints as its origin. The CloudFront distribution delivers your live stream to viewers with low latency and high transfer speeds.

1. An Amazon S3 bucket stores the CloudFront logs.

You can configure this solution to ingest Real-Time Transport Protocol (RTP), Real-Time Messaging Protocol (RTMP), HTTP Live Streaming (HLS) content, or live video from an AWS Elemental Link device. The solution also includes three [encoding profiles](encoding-profiles.md).

**Note**
AWS CloudFormation resources are created from [AWS Cloud Development Kit (AWS CDK) (CDK)](https://aws.amazon.com/cdk) constructs.
