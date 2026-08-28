---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicy.html
---

# ResponseHeadersPolicy
<a name="API_ResponseHeadersPolicy"></a>

A response headers policy.

A response headers policy contains information about a set of HTTP response headers.

After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it's attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.

For more information, see [Adding or removing HTTP headers in CloudFront responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html) in the *Amazon CloudFront Developer Guide*.

## Contents
<a name="API_ResponseHeadersPolicy_Contents"></a>

 ** Id **   <a name="cloudfront-Type-ResponseHeadersPolicy-Id"></a>
The identifier for the response headers policy.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-ResponseHeadersPolicy-LastModifiedTime"></a>
The date and time when the response headers policy was last modified.
Type: Timestamp
Required: Yes

 ** ResponseHeadersPolicyConfig **   <a name="cloudfront-Type-ResponseHeadersPolicy-ResponseHeadersPolicyConfig"></a>
A response headers policy configuration.
Type: [ResponseHeadersPolicyConfig](API_ResponseHeadersPolicyConfig.md) object
Required: Yes

## See Also
<a name="API_ResponseHeadersPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
