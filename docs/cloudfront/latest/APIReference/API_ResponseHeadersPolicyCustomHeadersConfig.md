---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyCustomHeadersConfig.html
---

# ResponseHeadersPolicyCustomHeadersConfig
<a name="API_ResponseHeadersPolicyCustomHeadersConfig"></a>

A list of HTTP response header names and their values. CloudFront includes these headers in HTTP responses that it sends for requests that match a cache behavior that's associated with this response headers policy.

## Contents
<a name="API_ResponseHeadersPolicyCustomHeadersConfig_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-ResponseHeadersPolicyCustomHeadersConfig-Quantity"></a>
The number of HTTP response headers in the list.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-ResponseHeadersPolicyCustomHeadersConfig-Items"></a>
The list of HTTP response headers and their values.
Type: Array of [ResponseHeadersPolicyCustomHeader](API_ResponseHeadersPolicyCustomHeader.md) objects
Required: No

## See Also
<a name="API_ResponseHeadersPolicyCustomHeadersConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeadersConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeadersConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeadersConfig)
