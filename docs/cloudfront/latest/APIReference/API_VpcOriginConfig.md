---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_VpcOriginConfig.html
---

# VpcOriginConfig
<a name="API_VpcOriginConfig"></a>

An Amazon CloudFront VPC origin configuration.

## Contents
<a name="API_VpcOriginConfig_Contents"></a>

 ** VpcOriginId **   <a name="cloudfront-Type-VpcOriginConfig-VpcOriginId"></a>
The VPC origin ID.
Type: String
Required: Yes

 ** OriginKeepaliveTimeout **   <a name="cloudfront-Type-VpcOriginConfig-OriginKeepaliveTimeout"></a>
Specifies how long, in seconds, CloudFront persists its connection to the origin. The minimum timeout is 1 second, the maximum is 300 seconds, and the default (if you don't specify otherwise) is 5 seconds.
For more information, see [Keep-alive timeout (custom origins only)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginKeepaliveTimeout) in the *Amazon CloudFront Developer Guide*.
Type: Integer
Required: No

 ** OriginReadTimeout **   <a name="cloudfront-Type-VpcOriginConfig-OriginReadTimeout"></a>
Specifies how long, in seconds, CloudFront waits for a response from the origin. This is also known as the *origin response timeout*. The minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is 30 seconds.
For more information, see [Response timeout](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginResponseTimeout) in the *Amazon CloudFront Developer Guide*.
Type: Integer
Required: No

## See Also
<a name="API_VpcOriginConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/VpcOriginConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/VpcOriginConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/VpcOriginConfig)
