---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyAccessControlAllowOrigins.html
---

# ResponseHeadersPolicyAccessControlAllowOrigins
<a name="API_ResponseHeadersPolicyAccessControlAllowOrigins"></a>

A list of origins (domain names) that CloudFront can use as the value for the `Access-Control-Allow-Origin` HTTP response header.

For more information about the `Access-Control-Allow-Origin` HTTP response header, see [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) in the MDN Web Docs.

## Contents
<a name="API_ResponseHeadersPolicyAccessControlAllowOrigins_Contents"></a>

 ** Items **   <a name="cloudfront-Type-ResponseHeadersPolicyAccessControlAllowOrigins-Items"></a>
The list of origins (domain names). You can specify `*` to allow all origins.
Type: Array of strings
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-ResponseHeadersPolicyAccessControlAllowOrigins-Quantity"></a>
The number of origins in the list.
Type: Integer
Required: Yes

## See Also
<a name="API_ResponseHeadersPolicyAccessControlAllowOrigins_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlAllowOrigins)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlAllowOrigins)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlAllowOrigins)
