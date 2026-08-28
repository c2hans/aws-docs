---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafv2RulesActionDetails.html
---

# AwsWafv2RulesActionDetails
<a name="API_AwsWafv2RulesActionDetails"></a>

 The action that AWS WAF should take on a web request when it matches a rule's statement. Settings at the web ACL level can override the rule action setting.

## Contents
<a name="API_AwsWafv2RulesActionDetails_Contents"></a>

 ** Allow **   <a name="securityhub-Type-AwsWafv2RulesActionDetails-Allow"></a>
 Instructs AWS WAF to allow the web request.
Type: [AwsWafv2ActionAllowDetails](API_AwsWafv2ActionAllowDetails.md) object
Required: No

 ** Block **   <a name="securityhub-Type-AwsWafv2RulesActionDetails-Block"></a>
 Instructs AWS WAF to block the web request.
Type: [AwsWafv2ActionBlockDetails](API_AwsWafv2ActionBlockDetails.md) object
Required: No

 ** Captcha **   <a name="securityhub-Type-AwsWafv2RulesActionDetails-Captcha"></a>
 Instructs AWS WAF to run a CAPTCHA check against the web request.
Type: [AwsWafv2RulesActionCaptchaDetails](API_AwsWafv2RulesActionCaptchaDetails.md) object
Required: No

 ** Count **   <a name="securityhub-Type-AwsWafv2RulesActionDetails-Count"></a>
 Instructs AWS WAF to count the web request and then continue evaluating the request using the remaining rules in the web ACL.
Type: [AwsWafv2RulesActionCountDetails](API_AwsWafv2RulesActionCountDetails.md) object
Required: No

## See Also
<a name="API_AwsWafv2RulesActionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafv2RulesActionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafv2RulesActionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafv2RulesActionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
