---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyXSSProtection.html
---

# ResponseHeadersPolicyXSSProtection
<a name="API_ResponseHeadersPolicyXSSProtection"></a>

Determines whether CloudFront includes the `X-XSS-Protection` HTTP response header and the header's value.

For more information about the `X-XSS-Protection` HTTP response header, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.

## Contents
<a name="API_ResponseHeadersPolicyXSSProtection_Contents"></a>

 ** Override **   <a name="cloudfront-Type-ResponseHeadersPolicyXSSProtection-Override"></a>
A Boolean that determines whether CloudFront overrides the `X-XSS-Protection` HTTP response header received from the origin with the one specified in this response headers policy.
Type: Boolean
Required: Yes

 ** Protection **   <a name="cloudfront-Type-ResponseHeadersPolicyXSSProtection-Protection"></a>
A Boolean that determines the value of the `X-XSS-Protection` HTTP response header. When this setting is `true`, the value of the `X-XSS-Protection` header is `1`. When this setting is `false`, the value of the `X-XSS-Protection` header is `0`.
For more information about these settings, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.
Type: Boolean
Required: Yes

 ** ModeBlock **   <a name="cloudfront-Type-ResponseHeadersPolicyXSSProtection-ModeBlock"></a>
A Boolean that determines whether CloudFront includes the `mode=block` directive in the `X-XSS-Protection` header.
For more information about this directive, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.
Type: Boolean
Required: No

 ** ReportUri **   <a name="cloudfront-Type-ResponseHeadersPolicyXSSProtection-ReportUri"></a>
A reporting URI, which CloudFront uses as the value of the `report` directive in the `X-XSS-Protection` header.
You cannot specify a `ReportUri` when `ModeBlock` is `true`.
For more information about using a reporting URL, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.
Type: String
Required: No

## See Also
<a name="API_ResponseHeadersPolicyXSSProtection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyXSSProtection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyXSSProtection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyXSSProtection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
