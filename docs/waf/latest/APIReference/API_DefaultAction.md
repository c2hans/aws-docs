---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_DefaultAction.html
---

# DefaultAction
<a name="API_DefaultAction"></a>

In a [WebACL](API_WebACL.md), this is the action that you want AWS WAF to perform when a web request doesn't match any of the rules in the `WebACL`. The default action must be a terminating action.

## Contents
<a name="API_DefaultAction_Contents"></a>

 ** Allow **   <a name="WAF-Type-DefaultAction-Allow"></a>
Specifies that AWS WAF should allow requests by default.
Type: [AllowAction](API_AllowAction.md) object
Required: No

 ** Block **   <a name="WAF-Type-DefaultAction-Block"></a>
Specifies that AWS WAF should block requests by default.
Type: [BlockAction](API_BlockAction.md) object
Required: No

## See Also
<a name="API_DefaultAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/DefaultAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/DefaultAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/DefaultAction)
