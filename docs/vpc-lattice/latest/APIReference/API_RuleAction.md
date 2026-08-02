---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_RuleAction.html
---

# RuleAction
<a name="API_RuleAction"></a>

Describes the action for a rule.

## Contents
<a name="API_RuleAction_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fixedResponse **   <a name="vpclattice-Type-RuleAction-fixedResponse"></a>
The fixed response action. The rule returns a custom HTTP response.
Type: [FixedResponseAction](API_FixedResponseAction.md) object
Required: No

 ** forward **   <a name="vpclattice-Type-RuleAction-forward"></a>
The forward action. Traffic that matches the rule is forwarded to the specified target groups.
Type: [ForwardAction](API_ForwardAction.md) object
Required: No

## See Also
<a name="API_RuleAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/RuleAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/RuleAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/RuleAction)
