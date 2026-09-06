---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_BlockAction.html
---

# BlockAction
<a name="API_BlockAction"></a>

Specifies that AWS WAF should block the request and optionally defines additional custom handling for the response to the web request.

This is used in the context of other settings, for example to specify values for [RuleAction](API_RuleAction.md) and web ACL [DefaultAction](API_DefaultAction.md).

## Contents
<a name="API_BlockAction_Contents"></a>

 ** CustomResponse **   <a name="WAF-Type-BlockAction-CustomResponse"></a>
Defines a custom response for the web request.
For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the * AWS WAF Developer Guide*.
Type: [CustomResponse](API_CustomResponse.md) object
Required: No

## See Also
<a name="API_BlockAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/BlockAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/BlockAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/BlockAction)
