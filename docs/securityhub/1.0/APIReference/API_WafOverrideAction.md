---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_WafOverrideAction.html
---

# WafOverrideAction
<a name="API_WafOverrideAction"></a>

Details about an override action for a rule.

## Contents
<a name="API_WafOverrideAction_Contents"></a>

 ** Type **   <a name="securityhub-Type-WafOverrideAction-Type"></a>
 `COUNT` overrides the action specified by the individual rule within a `RuleGroup` .
If set to `NONE`, the rule's action takes place.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_WafOverrideAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/WafOverrideAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/WafOverrideAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/WafOverrideAction)
