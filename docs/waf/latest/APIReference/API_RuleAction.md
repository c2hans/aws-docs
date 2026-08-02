---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleAction.html
---

# RuleAction
<a name="API_RuleAction"></a>

The action that AWS WAF should take on a web request when it matches a rule's statement. Settings at the web ACL level can override the rule action setting.

## Contents
<a name="API_RuleAction_Contents"></a>

 ** Allow **   <a name="WAF-Type-RuleAction-Allow"></a>
Instructs AWS WAF to allow the web request.
Type: [AllowAction](API_AllowAction.md) object
Required: No

 ** Block **   <a name="WAF-Type-RuleAction-Block"></a>
Instructs AWS WAF to block the web request.
Type: [BlockAction](API_BlockAction.md) object
Required: No

 ** Captcha **   <a name="WAF-Type-RuleAction-Captcha"></a>
Instructs AWS WAF to run a `CAPTCHA` check against the web request.
Type: [CaptchaAction](API_CaptchaAction.md) object
Required: No

 ** Challenge **   <a name="WAF-Type-RuleAction-Challenge"></a>
Instructs AWS WAF to run a `Challenge` check against the web request.
Type: [ChallengeAction](API_ChallengeAction.md) object
Required: No

 ** Count **   <a name="WAF-Type-RuleAction-Count"></a>
Instructs AWS WAF to count the web request and then continue evaluating the request using the remaining rules in the web ACL.
Type: [CountAction](API_CountAction.md) object
Required: No

 ** Monetize **   <a name="WAF-Type-RuleAction-Monetize"></a>
Instructs AWS WAF to return an HTTP 402 Payment Required response with a price manifest. The requesting client can complete payment and resubmit the request to gain access. This is a terminating action-requests that do not complete payment are blocked. This action is available only for web ACLs associated with Amazon CloudFront distributions and requires a `MonetizationConfig` on the web ACL.
Type: [MonetizeAction](API_MonetizeAction.md) object
Required: No

## See Also
<a name="API_RuleAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RuleAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RuleAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RuleAction)
