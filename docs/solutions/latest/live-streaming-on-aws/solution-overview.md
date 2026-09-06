---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/solution-overview.html
---

# Build highly available live video streaming content using AWS Media Services and Amazon CloudFront
<a name="solution-overview"></a>

Live Streaming on AWS solution overview

Amazon Web Services (AWS) lets broadcasters and content owners to seamlessly scale infrastructure to broadcast live content to a global audience. The Live Streaming on AWS solution helps you build highly available live video streaming content using AWS Media Services and Amazon CloudFront that is highly resilient and secure to deliver real-time viewing experiences to your customers.

This solution provides the following features:
+ Encodes and packages your content for adaptive bitrate streaming across multiple screens via HTTP live streaming (HLS), Dynamic Adaptive Streaming over HTTP (*DASH*), and Common Media Application Format (CMAF) by automatically configuring [AWS Elemental MediaLive](https://aws.amazon.com/medialive/) and [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/).
+ Provides an elastic, highly available, global content delivery network for live video streaming using Amazon CloudFront.

With this solution, you can run it only during a live event and then after the program ends, delete the solution’s stack to ensure you only pay for the infrastructure that you use.

This implementation guide discusses architectural considerations and configuration steps for deploying Live Streaming on AWS in the AWS Cloud. It includes a link to an [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template that launches and configures the AWS services required to deploy this solution using AWS best practices for security and availability.

The guide is intended for IT infrastructure architects, administrators, and DevOps professionals who have practical experience with video streaming and architecting in the AWS Cloud.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution. The estimated cost for running this solution in the US East (N. Virginia) Region is USD $69.74 per month. |  [Cost](plan-your-deployment.md#cost)  |
| Understand the security considerations for this solution. |  [Security](plan-your-deployment.md#security)  |
| Know how to plan for quotas for this solution. |  [Quotas](plan-your-deployment.md#quotas)  |
| Know which AWS Regions are supported for this solution. |  [Supported AWS regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the AWS CloudFormation template included in this solution to Automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation template](deploy-the-solution.md#aws-cloudformation-template)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/awslabs/live-stream-on-aws)  |

<a name="features-and-benefits"></a>== Features and benefits

The Live Streaming on AWS solution provides the following features:

 **Comprehensive output formats**

Using AWS Elemental MediaPackage, this solution supports the standards and formats commonly used to stream video, such as CMAF, HLS, and DASH, for playback support on different media players.

 **Input redundancy**

Using AWS Elemental MediaLive, this solution supports two input feeds and it’s ideal for customers looking to add redundancy to their live feeds.

 **MediaConnect support**

The solution supports AWS Elemental MediaConnect inputs providing a high-quality transport service for live video.

 **Flexible video content protection**

Using this solution, you can apply just-in-time content protection to secure your live streams by integrating with multiple Digital Rights Management (DRM) technologies. Protection capabilities are standards-based, including support for Apple FairPlay, Widevine, and Microsoft PlayReady using AES-128 encryption.

 **Integration with Service Catalog AppRegistry and AWS Systems Manager Application Manager, a capability of AWS Systems Manager**

This solution includes a Service Catalog AppRegistry resource to register the solution’s CloudFormation template and its underlying resources as an application in both [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) and [AWS Systems Manager Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the solution’s resources.

<a name="use-cases"></a>== Use cases

 **Streaming media**

As consumer demand for video streaming increases, media and entertainment companies are looking for secure and reliable web-based video streaming alternatives to traditional television. With Live Streaming on AWS, customers can avoid inefficient trial-and-error approaches and save time and costs for their streaming media projects.

<a name="concepts-and-definitions"></a>== Concepts and definitions

This section describes key concepts and defines terminology specific to this solution:

 **Adaptive Bit Rate (ABR)**

A streaming method that adjusts the video quality based on network conditions to improve video streaming over HTTP networks.

 **HTTP Live Streaming (HLS)**

HTTP-based streaming protocol to deliver media over the internet and developed by Apple Inc.

 **Dynamic Adaptive Streaming over HTTP (DASH)**

HTTP-based streaming protocol (also known as MPEG-DASH) to deliver media over the internet and developed under MPEG (Motion Picture Experts Group).

 **Common Media Application Format (CMAF)**

HTTP-based streaming and packaging standard to improve delivery of media over the internet, compatible with HLS and DASH, and co-developed by Apple and Microsoft.

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).
