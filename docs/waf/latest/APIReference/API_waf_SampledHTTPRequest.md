---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SampledHTTPRequest.html
---

# SampledHTTPRequest
<a name="API_waf_SampledHTTPRequest"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The response from a [GetSampledRequests](API_waf_GetSampledRequests.md) request includes a `SampledHTTPRequests` complex type that appears as `SampledRequests` in the response syntax. `SampledHTTPRequests` contains one `SampledHTTPRequest` object for each web request that is returned by `GetSampledRequests`.

## Contents
<a name="API_waf_SampledHTTPRequest_Contents"></a>

 ** Request **   <a name="WAF-Type-waf_SampledHTTPRequest-Request"></a>
A complex type that contains detailed information about the request.
Type: [HTTPRequest](API_waf_HTTPRequest.md) object
Required: Yes

 ** Weight **   <a name="WAF-Type-waf_SampledHTTPRequest-Weight"></a>
A value that indicates how one result in the response relates proportionally to other results in the response. A result that has a weight of `2` represents roughly twice as many Amazon CloudFront web requests as a result that has a weight of `1`.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** Action **   <a name="WAF-Type-waf_SampledHTTPRequest-Action"></a>
The action for the `Rule` that the request matched: `ALLOW`, `BLOCK`, or `COUNT`.
Type: String
Required: No

 ** RuleWithinRuleGroup **   <a name="WAF-Type-waf_SampledHTTPRequest-RuleWithinRuleGroup"></a>
This value is returned if the `GetSampledRequests` request specifies the ID of a `RuleGroup` rather than the ID of an individual rule. `RuleWithinRuleGroup` is the rule within the specified `RuleGroup` that matched the request listed in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** Timestamp **   <a name="WAF-Type-waf_SampledHTTPRequest-Timestamp"></a>
The time at which AWS WAF received the request from your AWS resource, in Unix time format (in seconds).
Type: Timestamp
Required: No

## See Also
<a name="API_waf_SampledHTTPRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/SampledHTTPRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/SampledHTTPRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/SampledHTTPRequest)
