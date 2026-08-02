---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_RuleUpdate.html
---

# RuleUpdate
<a name="API_RuleUpdate"></a>

Describes a rule update.

## Contents
<a name="API_RuleUpdate_Contents"></a>

 ** ruleIdentifier **   <a name="vpclattice-Type-RuleUpdate-ruleIdentifier"></a>
The ID or ARN of the rule.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rule-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/rule-[0-9a-z]{17}$))`
Required: Yes

 ** action **   <a name="vpclattice-Type-RuleUpdate-action"></a>
The rule action.
Type: [RuleAction](API_RuleAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** match **   <a name="vpclattice-Type-RuleUpdate-match"></a>
The rule match.
Type: [RuleMatch](API_RuleMatch.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** priority **   <a name="vpclattice-Type-RuleUpdate-priority"></a>
The rule priority. A listener can't have multiple rules with the same priority.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2000.
Required: No

## See Also
<a name="API_RuleUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/RuleUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/RuleUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/RuleUpdate)
