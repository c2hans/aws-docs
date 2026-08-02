---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_HTTPRequest.html
---

# HTTPRequest
<a name="API_HTTPRequest"></a>

Part of the response from [GetSampledRequests](API_GetSampledRequests.md). This is a complex type that appears as `Request` in the response syntax. `HTTPRequest` contains information about one of the web requests.

## Contents
<a name="API_HTTPRequest_Contents"></a>

 ** ClientIP **   <a name="WAF-Type-HTTPRequest-ClientIP"></a>
The IP address that the request originated from. If the web ACL is associated with a CloudFront distribution, this is the value of one of the following fields in CloudFront access logs:
+  `c-ip`, if the viewer did not use an HTTP proxy or a load balancer to send the request
+  `x-forwarded-for`, if the viewer did use an HTTP proxy or a load balancer to send the request
Type: String
Required: No

 ** Country **   <a name="WAF-Type-HTTPRequest-Country"></a>
The two-letter country code for the country that the request originated from. For a current list of country codes, see the Wikipedia entry [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
Type: String
Required: No

 ** Headers **   <a name="WAF-Type-HTTPRequest-Headers"></a>
A complex type that contains the name and value for each header in the sampled web request.
Type: Array of [HTTPHeader](API_HTTPHeader.md) objects
Required: No

 ** HTTPVersion **   <a name="WAF-Type-HTTPRequest-HTTPVersion"></a>
The HTTP version specified in the sampled web request, for example, `HTTP/1.1`.
Type: String
Required: No

 ** Method **   <a name="WAF-Type-HTTPRequest-Method"></a>
The HTTP method specified in the sampled web request.
Type: String
Required: No

 ** URI **   <a name="WAF-Type-HTTPRequest-URI"></a>
The URI path of the request, which identifies the resource, for example, `/images/daily-ad.jpg`.
Type: String
Required: No

## See Also
<a name="API_HTTPRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/HTTPRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/HTTPRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/HTTPRequest)
