---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The solution provides the following features:

 **Input format support**

Supports four input types ([RTP\_PUSH](https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/rtmp-rtp-push.html), [RTMP\_PUSH](https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/rtmp-rtp-push.html), [URL\_PULL](https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/url-pull-input.html), and [INPUT\_DEVICE](https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/link-input-config.html)) as the source for your video stream, including a device input so you can use an [AWS Elemental Link](https://aws.amazon.com/medialive/features/link/) as the source for the input for your live channel.

 **Simple configuration**

Automatically configures MediaLive and Amazon S3 to encode and originate your content for adaptive bitrate streaming across multiple screens via HTTP Live Streaming (HLS).

 **Integration with Service Catalog AppRegistry and Application Manager, a capability of AWS Systems Manager**

This solution includes a [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) resource to register the solution’s CloudFormation template and its underlying resources as an application in both Service Catalog AppRegistry and [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the solution’s resources and enable application search, reporting, and management actions.
