---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchPutPolicyAssignmentSuccess.html
---

# BatchPutPolicyAssignmentSuccess

A principal that a `BatchPutPolicyAssignmentByPolicy` request assigned the policy to.

## Contents
<a name="API_BatchPutPolicyAssignmentSuccess_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PrincipalArn **   <a name="QS-Type-BatchPutPolicyAssignmentSuccess-PrincipalArn"></a>
The ARN of the principal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** Revision **   <a name="QS-Type-BatchPutPolicyAssignmentSuccess-Revision"></a>
The revision of the assignment after this request.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** ReplacedPolicyArn **   <a name="QS-Type-BatchPutPolicyAssignmentSuccess-ReplacedPolicyArn"></a>
The ARN of the policy that this assignment replaced. This value is absent if the principal had no policy of this type before the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]+:[\x21-\x39\x3b-\x7e]*:[0-9]{12}:[\x21-\x7e]+`
Required: No

## See Also
<a name="API_BatchPutPolicyAssignmentSuccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BatchPutPolicyAssignmentSuccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BatchPutPolicyAssignmentSuccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BatchPutPolicyAssignmentSuccess)
