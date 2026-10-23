---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_NatRule.html
---

# NatRule
<a name="API_NatRule"></a>

Describes a NAT rule of an attachment.

## Contents
<a name="API_NatRule_Contents"></a>

 ** MatchSourceCidr **   <a name="networkmanager-Type-NatRule-MatchSourceCidr"></a>
The source CIDR block that the rule matches for traffic from the attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** NatCidr **   <a name="networkmanager-Type-NatRule-NatCidr"></a>
The CIDR block that matching source addresses are translated to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** RuleNumber **   <a name="networkmanager-Type-NatRule-RuleNumber"></a>
The rule number. Rule numbers identify the rules of an attachment and don't set the order in which rules are evaluated.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 32766.
Required: No

 ** State **   <a name="networkmanager-Type-NatRule-State"></a>
The state of the NAT rule. The possible values are the following:
+  `CREATING`: The rule is being created.
+  `MODIFYING`: The rule is being modified.
+  `DELETING`: The rule is being deleted.
+  `ACTIVATING`: NAT gateway support is being enabled, and the rule is being applied.
+  `ACTIVATED`: NAT gateway support is enabled, and the rule is applied.
+  `DEACTIVATING`: NAT gateway support is being disabled, and the rule is being removed from use.
+  `DEACTIVATED`: NAT gateway support is disabled, and the rule isn't applied.
+  `FAILED`: The attachment failed to be created, and the rule isn't applied.
+  `PENDING_ATTACHMENT_ACCEPTANCE`: The attachment is pending acceptance. The rule is applied after the attachment is accepted.
Type: String
Valid Values: `CREATING | MODIFYING | DELETING | ACTIVATED | ACTIVATING | DEACTIVATED | DEACTIVATING | FAILED | PENDING_ATTACHMENT_ACCEPTANCE`
Required: No

## See Also
<a name="API_NatRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NatRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NatRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NatRule)
