---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_Statement.html
---

# Statement
<a name="API_Statement"></a>

Contains a reference to a `Statement` element in a policy document that determines the result of the simulation.

This data type is used by the `MatchedStatements` member of the ` [EvaluationResult](https://docs.aws.amazon.com/IAM/latest/APIReference/API_EvaluationResult.html) ` type.

## Contents
<a name="API_Statement_Contents"></a>

 ** EndPosition **
The row and column of the end of a `Statement` in an IAM policy.
Type: [Position](API_Position.md) object
Required: No

 ** SourcePolicyId **
The identifier of the policy that was provided as an input.
Type: String
Required: No

 ** SourcePolicyType **
The type of the policy.
Type: String
Valid Values: `user | group | role | aws-managed | user-managed | resource | none`
Required: No

 ** StartPosition **
The row and column of the beginning of the `Statement` in an IAM policy.
Type: [Position](API_Position.md) object
Required: No

## See Also
<a name="API_Statement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/Statement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/Statement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/Statement)
