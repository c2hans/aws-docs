---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_CustomResponse.html
---

# CustomResponse
<a name="API_CustomResponse"></a>

A custom response to send to the client. You can define a custom response for rule actions and default web ACL actions that are set to [BlockAction](API_BlockAction.md).

For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_CustomResponse_Contents"></a>

 ** ResponseCode **   <a name="WAF-Type-CustomResponse-ResponseCode"></a>
The HTTP status code to return to the client.
For a list of status codes that you can use in your custom responses, see [Supported status codes for custom response](https://docs.aws.amazon.com/waf/latest/developerguide/customizing-the-response-status-codes.html) in the * AWS WAF Developer Guide*.
Type: Integer
Valid Range: Minimum value of 200. Maximum value of 599.
Required: Yes

 ** CustomResponseBodyKey **   <a name="WAF-Type-CustomResponse-CustomResponseBodyKey"></a>
References the response body that you want AWS WAF to return to the web request client. You can define a custom response for a rule action or a default web ACL action that is set to block. To do this, you first define the response body key and value in the `CustomResponseBodies` setting for the [WebACL](API_WebACL.md) or [RuleGroup](API_RuleGroup.md) where you want to use it. Then, in the rule action or web ACL default action `BlockAction` setting, you reference the response body using this key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: No

 ** ResponseHeaders **   <a name="WAF-Type-CustomResponse-ResponseHeaders"></a>
The HTTP headers to use in the response. You can specify any header name except for `content-type`. Duplicate header names are not allowed.
For information about the limits on count and size for custom request and response settings, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the * AWS WAF Developer Guide*.
Type: Array of [CustomHTTPHeader](API_CustomHTTPHeader.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_CustomResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/CustomResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/CustomResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/CustomResponse)
