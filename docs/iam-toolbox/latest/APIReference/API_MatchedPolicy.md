---
source_url: https://docs.aws.amazon.com/iam-toolbox/latest/APIReference/API_MatchedPolicy.html
---

# MatchedPolicy
<a name="API_MatchedPolicy"></a>

A policy that matched during evaluation, referenced by URI. The URI corresponds to a policy in the top-level policies list.

## Contents
<a name="API_MatchedPolicy_Contents"></a>

 ** uri **   <a name="iamtoolbox-Type-MatchedPolicy-uri"></a>
The URI of the policy. This cross-references an entry in the top-level policies list. The value depends on the policy type:
+ For managed policies, this is the policy ARN.
+ For inline policies, this is an opaque identifier.
Type: String
Required: Yes

 ** matchedStatements **   <a name="iamtoolbox-Type-MatchedPolicy-matchedStatements"></a>
The statements within the policy that matched during the evaluation.
Type: Array of [MatchedStatement](API_MatchedStatement.md) objects
Required: No

## See Also
<a name="API_MatchedPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-toolbox-2018-05-10/MatchedPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-toolbox-2018-05-10/MatchedPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-toolbox-2018-05-10/MatchedPolicy)
