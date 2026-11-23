---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PutAssignmentEntry.html
---

# PutAssignmentEntry

A principal to assign a policy to in a `BatchPutPolicyAssignmentByPolicy` request.

## Contents
<a name="API_PutAssignmentEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PrincipalArn **   <a name="QS-Type-PutAssignmentEntry-PrincipalArn"></a>
The ARN of the user, group, or account to assign the policy to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** ExistingPolicyArn **   <a name="QS-Type-PutAssignmentEntry-ExistingPolicyArn"></a>
The ARN of the policy that you expect the principal to have before this request. If the principal has a different policy of the same type, or no policy of that type, this entry fails with a `ConflictException` error code and makes no change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`
Required: No

 ** Revision **   <a name="QS-Type-PutAssignmentEntry-Revision"></a>
The revision of the assignment from your most recent read. If the assignment has changed since that revision, this entry fails with a `ConflictException` error code.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_PutAssignmentEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PutAssignmentEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PutAssignmentEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PutAssignmentEntry)
