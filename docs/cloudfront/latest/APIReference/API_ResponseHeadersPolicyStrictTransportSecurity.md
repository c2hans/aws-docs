---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyStrictTransportSecurity.html
---

# ResponseHeadersPolicyStrictTransportSecurity
<a name="API_ResponseHeadersPolicyStrictTransportSecurity"></a>

Determines whether CloudFront includes the `Strict-Transport-Security` HTTP response header and the header's value.

For more information about the `Strict-Transport-Security` HTTP response header, see [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) in the MDN Web Docs.

## Contents
<a name="API_ResponseHeadersPolicyStrictTransportSecurity_Contents"></a>

 ** AccessControlMaxAgeSec **   <a name="cloudfront-Type-ResponseHeadersPolicyStrictTransportSecurity-AccessControlMaxAgeSec"></a>
A number that CloudFront uses as the value for the `max-age` directive in the `Strict-Transport-Security` HTTP response header.
Type: Integer
Required: Yes

 ** Override **   <a name="cloudfront-Type-ResponseHeadersPolicyStrictTransportSecurity-Override"></a>
A Boolean that determines whether CloudFront overrides the `Strict-Transport-Security` HTTP response header received from the origin with the one specified in this response headers policy.
Type: Boolean
Required: Yes

 ** IncludeSubdomains **   <a name="cloudfront-Type-ResponseHeadersPolicyStrictTransportSecurity-IncludeSubdomains"></a>
A Boolean that determines whether CloudFront includes the `includeSubDomains` directive in the `Strict-Transport-Security` HTTP response header.
Type: Boolean
Required: No

 ** Preload **   <a name="cloudfront-Type-ResponseHeadersPolicyStrictTransportSecurity-Preload"></a>
A Boolean that determines whether CloudFront includes the `preload` directive in the `Strict-Transport-Security` HTTP response header.
Type: Boolean
Required: No

## See Also
<a name="API_ResponseHeadersPolicyStrictTransportSecurity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyStrictTransportSecurity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyStrictTransportSecurity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyStrictTransportSecurity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
