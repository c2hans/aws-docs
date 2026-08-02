---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_RuleUpdateFailure.html
---

# RuleUpdateFailure
<a name="API_RuleUpdateFailure"></a>

Describes a rule update that failed.

## Contents
<a name="API_RuleUpdateFailure_Contents"></a>

 ** failureCode **   <a name="vpclattice-Type-RuleUpdateFailure-failureCode"></a>
The failure code.
Type: String
Required: No

 ** failureMessage **   <a name="vpclattice-Type-RuleUpdateFailure-failureMessage"></a>
The failure message.
Type: String
Required: No

 ** ruleIdentifier **   <a name="vpclattice-Type-RuleUpdateFailure-ruleIdentifier"></a>
The ID or ARN of the rule.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((rule-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/rule-[0-9a-z]{17}$))`
Required: No

## See Also
<a name="API_RuleUpdateFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/RuleUpdateFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/RuleUpdateFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/RuleUpdateFailure)
