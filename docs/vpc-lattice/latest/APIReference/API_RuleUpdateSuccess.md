---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_RuleUpdateSuccess.html
---

# RuleUpdateSuccess
<a name="API_RuleUpdateSuccess"></a>

Describes a successful rule update.

## Contents
<a name="API_RuleUpdateSuccess_Contents"></a>

 ** action **   <a name="vpclattice-Type-RuleUpdateSuccess-action"></a>
The action for the rule.
Type: [RuleAction](API_RuleAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** arn **   <a name="vpclattice-Type-RuleUpdateSuccess-arn"></a>
The Amazon Resource Name (ARN) of the listener.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/rule-[0-9a-z]{17}`
Required: No

 ** id **   <a name="vpclattice-Type-RuleUpdateSuccess-id"></a>
The ID of the listener.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 22.
Pattern: `rule-[0-9a-z]{17}`
Required: No

 ** isDefault **   <a name="vpclattice-Type-RuleUpdateSuccess-isDefault"></a>
Indicates whether this is the default rule.
Type: Boolean
Required: No

 ** match **   <a name="vpclattice-Type-RuleUpdateSuccess-match"></a>
The rule match.
Type: [RuleMatch](API_RuleMatch.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** name **   <a name="vpclattice-Type-RuleUpdateSuccess-name"></a>
The name of the listener.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!rule-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** priority **   <a name="vpclattice-Type-RuleUpdateSuccess-priority"></a>
The rule priority.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2000.
Required: No

## See Also
<a name="API_RuleUpdateSuccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/RuleUpdateSuccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/RuleUpdateSuccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/RuleUpdateSuccess)
