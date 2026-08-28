---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_CountAction.html
---

# CountAction
<a name="API_CountAction"></a>

Specifies that AWS WAF should count the request. Optionally defines additional custom handling for the request.

This is used in the context of other settings, for example to specify values for [RuleAction](API_RuleAction.md) and web ACL [DefaultAction](API_DefaultAction.md).

## Contents
<a name="API_CountAction_Contents"></a>

 ** CustomRequestHandling **   <a name="WAF-Type-CountAction-CustomRequestHandling"></a>
Defines custom handling for the web request.
For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the * AWS WAF Developer Guide*.
Type: [CustomRequestHandling](API_CustomRequestHandling.md) object
Required: No

## See Also
<a name="API_CountAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/CountAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/CountAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/CountAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
