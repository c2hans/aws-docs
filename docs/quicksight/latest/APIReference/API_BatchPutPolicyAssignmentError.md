---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchPutPolicyAssignmentError.html
---

# BatchPutPolicyAssignmentError

A principal that a `BatchPutPolicyAssignmentByPolicy` request couldn't assign the policy to.

## Contents
<a name="API_BatchPutPolicyAssignmentError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorCode **   <a name="QS-Type-BatchPutPolicyAssignmentError-ErrorCode"></a>
The reason the entry failed. Possible values:
+  `ValidationException` – The entry is not valid.
+  `ResourceNotFoundException` – The principal doesn't exist, or the policy was deleted while the request was being processed.
+  `ConflictException` – The principal doesn't have the existing policy that you specified, or the assignment changed since the revision that you specified.
+  `ThrottlingException` – The entry was throttled. You can retry this entry.
+  `InternalFailureException` – An internal error occurred.
Type: String
Required: Yes

 ** ErrorMessage **   <a name="QS-Type-BatchPutPolicyAssignmentError-ErrorMessage"></a>
A description of the error.
Type: String
Required: Yes

 ** PrincipalArn **   <a name="QS-Type-BatchPutPolicyAssignmentError-PrincipalArn"></a>
The ARN of the principal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

## See Also
<a name="API_BatchPutPolicyAssignmentError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BatchPutPolicyAssignmentError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BatchPutPolicyAssignmentError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BatchPutPolicyAssignmentError)
