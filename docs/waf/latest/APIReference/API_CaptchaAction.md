---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_CaptchaAction.html
---

# CaptchaAction
<a name="API_CaptchaAction"></a>

Specifies that AWS WAF should run a `CAPTCHA` check against the request:
+ If the request includes a valid, unexpired `CAPTCHA` token, AWS WAF applies any custom request handling and labels that you've configured and then allows the web request inspection to proceed to the next rule, similar to a `CountAction`.
+ If the request doesn't include a valid, unexpired token, AWS WAF discontinues the web ACL evaluation of the request and blocks it from going to its intended destination.

   AWS WAF generates a response that it sends back to the client, which includes the following:
  + The header `x-amzn-waf-action` with a value of `captcha`.
  + The HTTP status code `405 Method Not Allowed`.
  + If the request contains an `Accept` header with a value of `text/html`, the response includes a `CAPTCHA` JavaScript page interstitial.

You can configure the expiration time in the `CaptchaConfig` `ImmunityTimeProperty` setting at the rule and web ACL level. The rule setting overrides the web ACL setting.

This action option is available for rules. It isn't available for web ACL default actions.

## Contents
<a name="API_CaptchaAction_Contents"></a>

 ** CustomRequestHandling **   <a name="WAF-Type-CaptchaAction-CustomRequestHandling"></a>
Defines custom handling for the web request, used when the `CAPTCHA` inspection determines that the request's token is valid and unexpired.
For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the * AWS WAF Developer Guide*.
Type: [CustomRequestHandling](API_CustomRequestHandling.md) object
Required: No

## See Also
<a name="API_CaptchaAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/CaptchaAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/CaptchaAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/CaptchaAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
