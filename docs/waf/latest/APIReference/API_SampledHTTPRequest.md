---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_SampledHTTPRequest.html
---

# SampledHTTPRequest
<a name="API_SampledHTTPRequest"></a>

Represents a single sampled web request. The response from [GetSampledRequests](API_GetSampledRequests.md) includes a `SampledHTTPRequests` complex type that appears as `SampledRequests` in the response syntax. `SampledHTTPRequests` contains an array of `SampledHTTPRequest` objects.

## Contents
<a name="API_SampledHTTPRequest_Contents"></a>

 ** Request **   <a name="WAF-Type-SampledHTTPRequest-Request"></a>
A complex type that contains detailed information about the request.
Type: [HTTPRequest](API_HTTPRequest.md) object
Required: Yes

 ** Weight **   <a name="WAF-Type-SampledHTTPRequest-Weight"></a>
A value that indicates how one result in the response relates proportionally to other results in the response. For example, a result that has a weight of `2` represents roughly twice as many web requests as a result that has a weight of `1`.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** Action **   <a name="WAF-Type-SampledHTTPRequest-Action"></a>
The action that AWS WAF applied to the request.
Type: String
Required: No

 ** CaptchaResponse **   <a name="WAF-Type-SampledHTTPRequest-CaptchaResponse"></a>
The `CAPTCHA` response for the request.
Type: [CaptchaResponse](API_CaptchaResponse.md) object
Required: No

 ** ChallengeResponse **   <a name="WAF-Type-SampledHTTPRequest-ChallengeResponse"></a>
The `Challenge` response for the request.
Type: [ChallengeResponse](API_ChallengeResponse.md) object
Required: No

 ** Labels **   <a name="WAF-Type-SampledHTTPRequest-Labels"></a>
Labels applied to the web request by matching rules. AWS WAF applies fully qualified labels to matching web requests. A fully qualified label is the concatenation of a label namespace and a rule label. The rule's rule group or web ACL defines the label namespace.
For example, `awswaf:111122223333:myRuleGroup:testRules:testNS1:testNS2:labelNameA` or `awswaf:managed:aws:managed-rule-set:header:encoding:utf8`.
Type: Array of [Label](API_Label.md) objects
Required: No

 ** OverriddenAction **   <a name="WAF-Type-SampledHTTPRequest-OverriddenAction"></a>
Used only for rule group rules that have a rule action override in place in the web ACL. This is the action that the rule group rule is configured for, and not the action that was applied to the request. The action that AWS WAF applied is the `Action` value.
Type: String
Required: No

 ** RequestHeadersInserted **   <a name="WAF-Type-SampledHTTPRequest-RequestHeadersInserted"></a>
Custom request headers inserted by AWS WAF into the request, according to the custom request configuration for the matching rule action.
Type: Array of [HTTPHeader](API_HTTPHeader.md) objects
Required: No

 ** ResponseCodeSent **   <a name="WAF-Type-SampledHTTPRequest-ResponseCodeSent"></a>
The response code that was sent for the request.
Type: Integer
Valid Range: Minimum value of 200. Maximum value of 599.
Required: No

 ** RuleNameWithinRuleGroup **   <a name="WAF-Type-SampledHTTPRequest-RuleNameWithinRuleGroup"></a>
The name of the `Rule` that the request matched. For managed rule groups, the format for this name is `<vendor name>#<managed rule group name>#<rule name>`. For your own rule groups, the format for this name is `<rule group name>#<rule name>`. If the rule is not in a rule group, this field is absent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: No

 ** Timestamp **   <a name="WAF-Type-SampledHTTPRequest-Timestamp"></a>
The time at which AWS WAF received the request from your AWS resource, in Unix time format (in seconds).
Type: Timestamp
Required: No

## See Also
<a name="API_SampledHTTPRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/SampledHTTPRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/SampledHTTPRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/SampledHTTPRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
