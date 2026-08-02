---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_DataProtection.html
---

# DataProtection
<a name="API_DataProtection"></a>

Specifies the protection behavior for a field type. This is part of the data protection configuration for a web ACL.

## Contents
<a name="API_DataProtection_Contents"></a>

 ** Action **   <a name="WAF-Type-DataProtection-Action"></a>
Specifies how to protect the field. AWS WAF can apply a one-way hash to the field or hard code a string substitution.
+ One-way hash example: `ade099751dEXAMPLEHASH2ea9f3393f80dd5d3bEXAMPLEHASH966ae0d3cd5a1e`
+ Substitution example: `REDACTED`
Type: String
Valid Values: `SUBSTITUTION | HASH`
Required: Yes

 ** Field **   <a name="WAF-Type-DataProtection-Field"></a>
Specifies the field type and optional keys to apply the protection behavior to.
Type: [FieldToProtect](API_FieldToProtect.md) object
Required: Yes

 ** ExcludeRateBasedDetails **   <a name="WAF-Type-DataProtection-ExcludeRateBasedDetails"></a>
Specifies whether to also exclude any rate-based rule details from the data protection you have enabled for a given field. If you specify this exception, RateBasedDetails will show the value of the field. For additional information, see the log field `rateBasedRuleList` at [Log fields for web ACL traffic](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the * AWS WAF Developer Guide*.
Default: `FALSE`
Type: Boolean
Required: No

 ** ExcludeRuleMatchDetails **   <a name="WAF-Type-DataProtection-ExcludeRuleMatchDetails"></a>
Specifies whether to also exclude any rule match details from the data protection you have enabled for a given field. AWS WAF logs these details for non-terminating matching rules and for the terminating matching rule. For additional information, see [Log fields for web ACL traffic](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the * AWS WAF Developer Guide*.
Default: `FALSE`
Type: Boolean
Required: No

## See Also
<a name="API_DataProtection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/DataProtection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/DataProtection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/DataProtection)
