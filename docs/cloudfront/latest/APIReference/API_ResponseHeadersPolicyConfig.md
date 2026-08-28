---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyConfig.html
---

# ResponseHeadersPolicyConfig
<a name="API_ResponseHeadersPolicyConfig"></a>

A response headers policy configuration.

A response headers policy configuration contains metadata about the response headers policy, and configurations for sets of HTTP response headers.

## Contents
<a name="API_ResponseHeadersPolicyConfig_Contents"></a>

 ** Name **   <a name="cloudfront-Type-ResponseHeadersPolicyConfig-Name"></a>
A name to identify the response headers policy.
The name must be unique for response headers policies in this AWS account.
Type: String
Required: Yes

 ** Comment **   <a name="cloudfront-Type-ResponseHeadersPolicyConfig-Comment"></a>
A comment to describe the response headers policy.
The comment cannot be longer than 128 characters.
Type: String
Required: No

 ** CorsConfig **   <a name="cloudfront-Type-ResponseHeadersPolicyConfig-CorsConfig"></a>
A configuration for a set of HTTP response headers that are used for cross-origin resource sharing (CORS).
Type: [ResponseHeadersPolicyCorsConfig](API_ResponseHeadersPolicyCorsConfig.md) object
Required: No

 ** CustomHeadersConfig **   <a name="cloudfront-Type-ResponseHeadersPolicyConfig-CustomHeadersConfig"></a>
A configuration for a set of custom HTTP response headers.
Type: [ResponseHeadersPolicyCustomHeadersConfig](API_ResponseHeadersPolicyCustomHeadersConfig.md) object
Required: No

 ** RemoveHeadersConfig **   <a name="cloudfront-Type-ResponseHeadersPolicyConfig-RemoveHeadersConfig"></a>
A configuration for a set of HTTP headers to remove from the HTTP response.
Type: [ResponseHeadersPolicyRemoveHeadersConfig](API_ResponseHeadersPolicyRemoveHeadersConfig.md) object
Required: No

 ** SecurityHeadersConfig **   <a name="cloudfront-Type-ResponseHeadersPolicyConfig-SecurityHeadersConfig"></a>
A configuration for a set of security-related HTTP response headers.
Type: [ResponseHeadersPolicySecurityHeadersConfig](API_ResponseHeadersPolicySecurityHeadersConfig.md) object
Required: No

 ** ServerTimingHeadersConfig **   <a name="cloudfront-Type-ResponseHeadersPolicyConfig-ServerTimingHeadersConfig"></a>
A configuration for enabling the `Server-Timing` header in HTTP responses sent from CloudFront.
Type: [ResponseHeadersPolicyServerTimingHeadersConfig](API_ResponseHeadersPolicyServerTimingHeadersConfig.md) object
Required: No

## See Also
<a name="API_ResponseHeadersPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
