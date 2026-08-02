---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CustomOriginConfig.html
---

# CustomOriginConfig
<a name="API_CustomOriginConfig"></a>

A custom origin. A custom origin is any origin that is *not* an Amazon S3 bucket, with one exception. An Amazon S3 bucket that is [configured with static website hosting](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) *is* a custom origin.

## Contents
<a name="API_CustomOriginConfig_Contents"></a>

 ** HTTPPort **   <a name="cloudfront-Type-CustomOriginConfig-HTTPPort"></a>
The HTTP port that CloudFront uses to connect to the origin. Specify the HTTP port that the origin listens on.
Type: Integer
Required: Yes

 ** HTTPSPort **   <a name="cloudfront-Type-CustomOriginConfig-HTTPSPort"></a>
The HTTPS port that CloudFront uses to connect to the origin. Specify the HTTPS port that the origin listens on.
Type: Integer
Required: Yes

 ** OriginProtocolPolicy **   <a name="cloudfront-Type-CustomOriginConfig-OriginProtocolPolicy"></a>
Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Valid values are:
+  `http-only` – CloudFront always uses HTTP to connect to the origin.
+  `match-viewer` – CloudFront connects to the origin using the same protocol that the viewer used to connect to CloudFront.
+  `https-only` – CloudFront always uses HTTPS to connect to the origin.
Type: String
Valid Values: `http-only | match-viewer | https-only`
Required: Yes

 ** IpAddressType **   <a name="cloudfront-Type-CustomOriginConfig-IpAddressType"></a>
Specifies which IP protocol CloudFront uses when connecting to your origin. If your origin uses both IPv4 and IPv6 protocols, you can choose `dualstack` to help optimize reliability.
Type: String
Valid Values: `ipv4 | ipv6 | dualstack`
Required: No

 ** OriginKeepaliveTimeout **   <a name="cloudfront-Type-CustomOriginConfig-OriginKeepaliveTimeout"></a>
Specifies how long, in seconds, CloudFront persists its connection to the origin. The minimum timeout is 1 second, the maximum is 300 seconds, and the default (if you don't specify otherwise) is 5 seconds.
For more information, see [Keep-alive timeout (custom origins only)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginKeepaliveTimeout) in the *Amazon CloudFront Developer Guide*.
Type: Integer
Required: No

 ** OriginMtlsConfig **   <a name="cloudfront-Type-CustomOriginConfig-OriginMtlsConfig"></a>
Configures mutual TLS authentication between CloudFront and your origin server.
Type: [OriginMtlsConfig](API_OriginMtlsConfig.md) object
Required: No

 ** OriginReadTimeout **   <a name="cloudfront-Type-CustomOriginConfig-OriginReadTimeout"></a>
Specifies how long, in seconds, CloudFront waits for a response from the origin. This is also known as the *origin response timeout*. The minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is 30 seconds.
For more information, see [Response timeout](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginResponseTimeout) in the *Amazon CloudFront Developer Guide*.
Type: Integer
Required: No

 ** OriginSslProtocols **   <a name="cloudfront-Type-CustomOriginConfig-OriginSslProtocols"></a>
Specifies the minimum SSL/TLS protocol that CloudFront uses when connecting to your origin over HTTPS. Valid values include `SSLv3`, `TLSv1`, `TLSv1.1`, and `TLSv1.2`.
For more information, see [Minimum Origin SSL Protocol](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginSSLProtocols) in the *Amazon CloudFront Developer Guide*.
Type: [OriginSslProtocols](API_OriginSslProtocols.md) object
Required: No

## See Also
<a name="API_CustomOriginConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CustomOriginConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CustomOriginConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CustomOriginConfig)
