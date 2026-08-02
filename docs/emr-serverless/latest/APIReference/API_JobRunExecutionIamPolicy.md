---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobRunExecutionIamPolicy.html
---

# JobRunExecutionIamPolicy
<a name="API_JobRunExecutionIamPolicy"></a>

Optional IAM policy. The resulting job IAM role permissions will be an intersection of the policies passed and the policy associated with your job execution role.

## Contents
<a name="API_JobRunExecutionIamPolicy_Contents"></a>

 ** policy **   <a name="emrserverless-Type-JobRunExecutionIamPolicy-policy"></a>
An IAM inline policy to use as an execution IAM policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([ -ÿ]+)`
Required: No

 ** policyArns **   <a name="emrserverless-Type-JobRunExecutionIamPolicy-policyArns"></a>
A list of Amazon Resource Names (ARNs) to use as an execution IAM policy.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `([ -~… -퟿-�က0-ჿFF]+)`
Required: No

## See Also
<a name="API_JobRunExecutionIamPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/JobRunExecutionIamPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/JobRunExecutionIamPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/JobRunExecutionIamPolicy)
