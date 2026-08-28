---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafv2RulesActionCaptchaDetails.html
---

# AwsWafv2RulesActionCaptchaDetails
<a name="API_AwsWafv2RulesActionCaptchaDetails"></a>

 Specifies that AWS WAF should run a CAPTCHA check against the request.

## Contents
<a name="API_AwsWafv2RulesActionCaptchaDetails_Contents"></a>

 ** CustomRequestHandling **   <a name="securityhub-Type-AwsWafv2RulesActionCaptchaDetails-CustomRequestHandling"></a>
 Defines custom handling for the web request, used when the CAPTCHA inspection determines that the request's token is valid and unexpired. For more information, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the * AWS WAF Developer Guide.*.
Type: [AwsWafv2CustomRequestHandlingDetails](API_AwsWafv2CustomRequestHandlingDetails.md) object
Required: No

## See Also
<a name="API_AwsWafv2RulesActionCaptchaDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafv2RulesActionCaptchaDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafv2RulesActionCaptchaDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafv2RulesActionCaptchaDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
