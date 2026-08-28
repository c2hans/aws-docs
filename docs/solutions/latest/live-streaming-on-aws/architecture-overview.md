---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

Live Streaming on AWS architecture overview

This section provides a reference implementation architecture diagram for the components deployed with this solution.

<a name="architecture-diagram"></a>== Architecture diagram

Deploying this solution with the default parameters deploys the following components in your AWS account.

 **Depicts Live Streaming on AWS solution architecture**

![live streaming on aws architecture](http://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/images/live-streaming-on-aws-architecture.png)

The solution’s AWS CloudFormation template launches the AWS products and services necessary to ingest, transcode, and deliver live streaming video.

1. AWS Elemental MediaLive ingests two input feeds and transcodes your content into two adaptive bitrate (ABR) HTTP Live Streaming (HLS) streams as output.

   Two feeds are ingested for MediaLive redundancy. Each MediaLive transcodes a single ingest feed into ABR outputs.

1. AWS Elemental MediaPackage ingests the MediaLive ABR output and packages the live stream into HTTP Live Streaming (HLS), Dynamic Adaptive Streaming over HTTP (DASH) and Common Media Application Format (CMAF) formats that are delivered to three MediaPackage custom endpoints.

   These three formats were selected because that is what popular streaming devices support. MediaPackage is an origin server that prepares the content for delivery to phones, tablets, smart TVs, and other devices.

1. An Amazon CloudFront distribution is configured to use the MediaPackage custom endpoints as its origin and includes a CDN Identifier custom HTTP header to authenticate requests. MediaPackage only fulfills playback requests that are authorized between MediaPackage and CloudFront using the CDN Identifier. This CDN Identifier is created as part of the CloudFormation deployment and securely stored in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). For details, refer to the [CDN Authorization in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/cdn-auth.html) in the *AWS Elemental MediaPackage User Guide*.

1. The CloudFront distribution delivers your live stream to viewers with low latency and high transfer speeds.

1. A demo HTML preview player is available to help you test the solution. The player is a static website [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket. Amazon CloudFront is used to restrict access to the solution’s website bucket contents.

You can configure this solution to ingest Real-time Transport Protocol (RTP), Real-Time Messaging Protocol (RTMP), HTTP Live Streaming (HLS), or AWS Elemental MediaConnect flows. This solution also includes three encoding profiles.

**Note**
AWS CloudFormation resources are created from [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk) constructs.

<a name="aws-well-architected"></a>== AWS Well-Architected

We designed this solution with best practices from the AWS [Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how we applied the design principles and best practices of the Well-Architected Framework when building this solution.

<a name="operational-excellence"></a>=== Operational excellence

This section describes how the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) were applied when designing this solution.

The Live Streaming on AWS solution tracks all assets via AWS CloudTrail, and logs from AWS Elemental MediaLive, MediaPackage, and Amazon CloudFront provide observability into the infrastructure and the rest of the solution components.

<a name="security-1"></a>=== Security

This section describes how the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) were applied when designing this solution. To help reduce latency and improve security, Live Streaming on AWS includes an Amazon CloudFront distribution with an origin access identity, which is a special CloudFront user that helps restrict access to the solution’s website bucket contents.

AWS Elemental MediaPackage only fulfills playback requests that are authorized between MediaPackage and CloudFront using a CDN identifier. This CDN identifier is created as part of the AWS CloudFormation deployment and securely stored in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). For more details, refer to the [CDN authorization in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/cdn-auth.html) in the *AWS Elemental MediaPackage User Guide*.

<a name="reliability"></a>=== Reliability

This section describes how the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) were applied when designing this solution.

The solution supports primary and secondary live streams throughout AWS Elemental MediaLive and AWS Elemental MediaPackage providing the redundancy that customers require for critical live video events.

<a name="performance-efficiency"></a>=== Performance efficiency

This section describes how the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) were applied when designing this solution.

This solution uses AWS Elemental MediaLive, MediaPackage, and MediaConnect, which are currently available in specific AWS Regions only. If you use MediaConnect as input, you must deploy this solution in the same Region as your MediaConnect flows.

The Live Streaming on AWS solution is automatically tested and reviewed by solution architects and subject matter experts for areas to experiment and improve.

<a name="cost-optimization"></a>=== Cost optimization

This section describes how the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) were applied when designing this solution.

The cost for running this solution varies based on a number of factors, including the encoded profile selected, the bitrate of the live stream and the number of viewers.

Using Application Manager, customers can measure the efficiency of the workloads, and the costs associated with delivery.

<a name="sustainability"></a>=== Sustainability

This section describes how the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) were applied when designing this solution. To minimize the environmental impact of backend services, Live Streaming on AWS uses managed and serverless services. Customers can run this solution only during a live event and delete the stack after the program ends, thereby reducing the carbon footprint as compared to the footprint of continually operating on-premises servers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Live Streaming on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
