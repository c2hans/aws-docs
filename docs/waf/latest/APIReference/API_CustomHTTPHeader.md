---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_CustomHTTPHeader.html
---

# CustomHTTPHeader
<a name="API_CustomHTTPHeader"></a>

A custom header for custom request and response handling. This is used in [CustomResponse](API_CustomResponse.md) and [CustomRequestHandling](API_CustomRequestHandling.md).

## Contents
<a name="API_CustomHTTPHeader_Contents"></a>

 ** Name **   <a name="WAF-Type-CustomHTTPHeader-Name"></a>
The name of the custom header.
For custom request header insertion, when AWS WAF inserts the header into the request, it prefixes this name `x-amzn-waf-`, to avoid confusion with the headers that are already in the request. For example, for the header name `sample`, AWS WAF inserts the header `x-amzn-waf-sample`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._$-]+$`
Required: Yes

 ** Value **   <a name="WAF-Type-CustomHTTPHeader-Value"></a>
The value of the custom header.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_CustomHTTPHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/CustomHTTPHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/CustomHTTPHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/CustomHTTPHeader)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
