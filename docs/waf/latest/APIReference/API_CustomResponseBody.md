---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_CustomResponseBody.html
---

# CustomResponseBody
<a name="API_CustomResponseBody"></a>

The response body to use in a custom response to a web request. This is referenced by key from [CustomResponse](API_CustomResponse.md) `CustomResponseBodyKey`.

## Contents
<a name="API_CustomResponseBody_Contents"></a>

 ** Content **   <a name="WAF-Type-CustomResponseBody-Content"></a>
The payload of the custom response.
You can use JSON escape strings in JSON content. To do this, you must specify JSON content in the `ContentType` setting.
For information about the limits on count and size for custom request and response settings, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the * AWS WAF Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `[\s\S]*`
Required: Yes

 ** ContentType **   <a name="WAF-Type-CustomResponseBody-ContentType"></a>
The type of content in the payload that you are defining in the `Content` string.
Type: String
Valid Values: `TEXT_PLAIN | TEXT_HTML | APPLICATION_JSON`
Required: Yes

## See Also
<a name="API_CustomResponseBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/CustomResponseBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/CustomResponseBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/CustomResponseBody)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
