---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_CustomRequestHandling.html
---

# CustomRequestHandling
<a name="API_CustomRequestHandling"></a>

Custom request handling behavior that inserts custom headers into a web request. You can add custom request handling for AWS WAF to use when the rule action doesn't block the request. For example, `CaptchaAction` for requests with valid t okens, and `AllowAction`.

For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_CustomRequestHandling_Contents"></a>

 ** InsertHeaders **   <a name="WAF-Type-CustomRequestHandling-InsertHeaders"></a>
The HTTP headers to insert into the request. Duplicate header names are not allowed.
For information about the limits on count and size for custom request and response settings, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the * AWS WAF Developer Guide*.
Type: Array of [CustomHTTPHeader](API_CustomHTTPHeader.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## See Also
<a name="API_CustomRequestHandling_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/CustomRequestHandling)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/CustomRequestHandling)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/CustomRequestHandling)
