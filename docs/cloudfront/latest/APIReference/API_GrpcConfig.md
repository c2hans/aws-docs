---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GrpcConfig.html
---

# GrpcConfig
<a name="API_GrpcConfig"></a>

Amazon CloudFront supports gRPC, an open-source remote procedure call (RPC) framework built on HTTP/2. gRPC offers bi-directional streaming and binary protocol that buffers payloads, making it suitable for applications that require low latency communications.

To enable your distribution to handle gRPC requests, you must include HTTP/2 as one of the supported `HTTP` versions and allow `HTTP` methods, including `POST`.

For more information, see [Using gRPC with CloudFront distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-using-grpc.html) in the *Amazon CloudFront Developer Guide*.

## Contents
<a name="API_GrpcConfig_Contents"></a>

 ** Enabled **   <a name="cloudfront-Type-GrpcConfig-Enabled"></a>
Enables your CloudFront distribution to receive gRPC requests and to proxy them directly to your origins.
Type: Boolean
Required: Yes

## See Also
<a name="API_GrpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GrpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GrpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GrpcConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
