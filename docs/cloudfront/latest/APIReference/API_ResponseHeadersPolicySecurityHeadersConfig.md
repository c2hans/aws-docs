---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicySecurityHeadersConfig.html
---

# ResponseHeadersPolicySecurityHeadersConfig
<a name="API_ResponseHeadersPolicySecurityHeadersConfig"></a>

A configuration for a set of security-related HTTP response headers. CloudFront adds these headers to HTTP responses that it sends for requests that match a cache behavior associated with this response headers policy.

## Contents
<a name="API_ResponseHeadersPolicySecurityHeadersConfig_Contents"></a>

 ** ContentSecurityPolicy **   <a name="cloudfront-Type-ResponseHeadersPolicySecurityHeadersConfig-ContentSecurityPolicy"></a>
The policy directives and their values that CloudFront includes as values for the `Content-Security-Policy` HTTP response header.
For more information about the `Content-Security-Policy` HTTP response header, see [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) in the MDN Web Docs.
Type: [ResponseHeadersPolicyContentSecurityPolicy](API_ResponseHeadersPolicyContentSecurityPolicy.md) object
Required: No

 ** ContentTypeOptions **   <a name="cloudfront-Type-ResponseHeadersPolicySecurityHeadersConfig-ContentTypeOptions"></a>
Determines whether CloudFront includes the `X-Content-Type-Options` HTTP response header with its value set to `nosniff`.
For more information about the `X-Content-Type-Options` HTTP response header, see [X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options) in the MDN Web Docs.
Type: [ResponseHeadersPolicyContentTypeOptions](API_ResponseHeadersPolicyContentTypeOptions.md) object
Required: No

 ** FrameOptions **   <a name="cloudfront-Type-ResponseHeadersPolicySecurityHeadersConfig-FrameOptions"></a>
Determines whether CloudFront includes the `X-Frame-Options` HTTP response header and the header's value.
For more information about the `X-Frame-Options` HTTP response header, see [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) in the MDN Web Docs.
Type: [ResponseHeadersPolicyFrameOptions](API_ResponseHeadersPolicyFrameOptions.md) object
Required: No

 ** ReferrerPolicy **   <a name="cloudfront-Type-ResponseHeadersPolicySecurityHeadersConfig-ReferrerPolicy"></a>
Determines whether CloudFront includes the `Referrer-Policy` HTTP response header and the header's value.
For more information about the `Referrer-Policy` HTTP response header, see [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) in the MDN Web Docs.
Type: [ResponseHeadersPolicyReferrerPolicy](API_ResponseHeadersPolicyReferrerPolicy.md) object
Required: No

 ** StrictTransportSecurity **   <a name="cloudfront-Type-ResponseHeadersPolicySecurityHeadersConfig-StrictTransportSecurity"></a>
Determines whether CloudFront includes the `Strict-Transport-Security` HTTP response header and the header's value.
For more information about the `Strict-Transport-Security` HTTP response header, see [Security headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.html#understanding-response-headers-policies-security) in the *Amazon CloudFront Developer Guide* and [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) in the MDN Web Docs.
Type: [ResponseHeadersPolicyStrictTransportSecurity](API_ResponseHeadersPolicyStrictTransportSecurity.md) object
Required: No

 ** XSSProtection **   <a name="cloudfront-Type-ResponseHeadersPolicySecurityHeadersConfig-XSSProtection"></a>
Determines whether CloudFront includes the `X-XSS-Protection` HTTP response header and the header's value.
For more information about the `X-XSS-Protection` HTTP response header, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.
Type: [ResponseHeadersPolicyXSSProtection](API_ResponseHeadersPolicyXSSProtection.md) object
Required: No

## See Also
<a name="API_ResponseHeadersPolicySecurityHeadersConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicySecurityHeadersConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicySecurityHeadersConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicySecurityHeadersConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
