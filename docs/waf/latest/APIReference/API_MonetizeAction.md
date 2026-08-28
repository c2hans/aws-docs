---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_MonetizeAction.html
---

# MonetizeAction
<a name="API_MonetizeAction"></a>

Specifies the monetize action settings for a rule. When AWS WAF applies this action, it returns an HTTP 402 Payment Required response containing pricing information that the requesting client uses to complete payment and gain access to the resource. This is a terminating action-if the client does not complete the 402 payment flow, the request is blocked. This action is available only for web ACLs associated with Amazon CloudFront distributions. You must configure a `MonetizationConfig` on the web ACL or rule group before adding rules that use this action. You cannot use the Monetize action for rate-based rules.

## Contents
<a name="API_MonetizeAction_Contents"></a>

 ** PriceMultiplier **   <a name="WAF-Type-MonetizeAction-PriceMultiplier"></a>
An integer multiplier applied to the base price defined in the web ACL's `MonetizationConfig`. The effective price for the request is the base price multiplied by this value. Specify as a string. Valid values: 1 to 100.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3.
Pattern: `^([1-9][0-9]?|100)$`
Required: No

## See Also
<a name="API_MonetizeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/MonetizeAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/MonetizeAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/MonetizeAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
