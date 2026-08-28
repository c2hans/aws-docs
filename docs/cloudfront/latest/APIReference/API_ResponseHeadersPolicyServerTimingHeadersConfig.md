---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyServerTimingHeadersConfig.html
---

# ResponseHeadersPolicyServerTimingHeadersConfig
<a name="API_ResponseHeadersPolicyServerTimingHeadersConfig"></a>

A configuration for enabling the `Server-Timing` header in HTTP responses sent from CloudFront. CloudFront adds this header to HTTP responses that it sends in response to requests that match a cache behavior that's associated with this response headers policy.

You can use the `Server-Timing` header to view metrics that can help you gain insights about the behavior and performance of CloudFront. For example, you can see which cache layer served a cache hit, or the first byte latency from the origin when there was a cache miss. You can use the metrics in the `Server-Timing` header to troubleshoot issues or test the efficiency of your CloudFront configuration. For more information, see [Server-Timing header](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.html#server-timing-header) in the *Amazon CloudFront Developer Guide*.

## Contents
<a name="API_ResponseHeadersPolicyServerTimingHeadersConfig_Contents"></a>

 ** Enabled **   <a name="cloudfront-Type-ResponseHeadersPolicyServerTimingHeadersConfig-Enabled"></a>
A Boolean that determines whether CloudFront adds the `Server-Timing` header to HTTP responses that it sends in response to requests that match a cache behavior that's associated with this response headers policy.
Type: Boolean
Required: Yes

 ** SamplingRate **   <a name="cloudfront-Type-ResponseHeadersPolicyServerTimingHeadersConfig-SamplingRate"></a>
A number 0–100 (inclusive) that specifies the percentage of responses that you want CloudFront to add the `Server-Timing` header to. When you set the sampling rate to 100, CloudFront adds the `Server-Timing` header to the HTTP response for every request that matches the cache behavior that this response headers policy is attached to. When you set it to 50, CloudFront adds the header to 50% of the responses for requests that match the cache behavior. You can set the sampling rate to any number 0–100 with up to four decimal places.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 100.0.
Required: No

## See Also
<a name="API_ResponseHeadersPolicyServerTimingHeadersConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyServerTimingHeadersConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyServerTimingHeadersConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyServerTimingHeadersConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
