---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyRemoveHeadersConfig.html
---

# ResponseHeadersPolicyRemoveHeadersConfig
<a name="API_ResponseHeadersPolicyRemoveHeadersConfig"></a>

A list of HTTP header names that CloudFront removes from HTTP responses to requests that match the cache behavior that this response headers policy is attached to.

## Contents
<a name="API_ResponseHeadersPolicyRemoveHeadersConfig_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-ResponseHeadersPolicyRemoveHeadersConfig-Quantity"></a>
The number of HTTP header names in the list.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-ResponseHeadersPolicyRemoveHeadersConfig-Items"></a>
The list of HTTP header names.
Type: Array of [ResponseHeadersPolicyRemoveHeader](API_ResponseHeadersPolicyRemoveHeader.md) objects
Required: No

## See Also
<a name="API_ResponseHeadersPolicyRemoveHeadersConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyRemoveHeadersConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyRemoveHeadersConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyRemoveHeadersConfig)
