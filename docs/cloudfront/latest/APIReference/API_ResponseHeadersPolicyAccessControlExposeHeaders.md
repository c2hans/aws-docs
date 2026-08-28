---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyAccessControlExposeHeaders.html
---

# ResponseHeadersPolicyAccessControlExposeHeaders
<a name="API_ResponseHeadersPolicyAccessControlExposeHeaders"></a>

A list of HTTP headers that CloudFront includes as values for the `Access-Control-Expose-Headers` HTTP response header.

For more information about the `Access-Control-Expose-Headers` HTTP response header, see [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers) in the MDN Web Docs.

## Contents
<a name="API_ResponseHeadersPolicyAccessControlExposeHeaders_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-ResponseHeadersPolicyAccessControlExposeHeaders-Quantity"></a>
The number of HTTP headers in the list.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-ResponseHeadersPolicyAccessControlExposeHeaders-Items"></a>
The list of HTTP headers. You can specify `*` to expose all headers.
Type: Array of strings
Required: No

## See Also
<a name="API_ResponseHeadersPolicyAccessControlExposeHeaders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlExposeHeaders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlExposeHeaders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlExposeHeaders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
