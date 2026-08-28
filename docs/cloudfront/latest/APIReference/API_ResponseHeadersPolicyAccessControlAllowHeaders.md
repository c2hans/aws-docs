---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyAccessControlAllowHeaders.html
---

# ResponseHeadersPolicyAccessControlAllowHeaders
<a name="API_ResponseHeadersPolicyAccessControlAllowHeaders"></a>

A list of HTTP header names that CloudFront includes as values for the `Access-Control-Allow-Headers` HTTP response header.

For more information about the `Access-Control-Allow-Headers` HTTP response header, see [Access-Control-Allow-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers) in the MDN Web Docs.

## Contents
<a name="API_ResponseHeadersPolicyAccessControlAllowHeaders_Contents"></a>

 ** Items **   <a name="cloudfront-Type-ResponseHeadersPolicyAccessControlAllowHeaders-Items"></a>
The list of HTTP header names. You can specify `*` to allow all headers.
Type: Array of strings
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-ResponseHeadersPolicyAccessControlAllowHeaders-Quantity"></a>
The number of HTTP header names in the list.
Type: Integer
Required: Yes

## See Also
<a name="API_ResponseHeadersPolicyAccessControlAllowHeaders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlAllowHeaders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlAllowHeaders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlAllowHeaders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
