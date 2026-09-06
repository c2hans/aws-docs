---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_IAMPolicyAssignment.html
---

# IAMPolicyAssignment
<a name="API_IAMPolicyAssignment"></a>

An AWS Identity and Access Management (IAM) policy assignment.

## Contents
<a name="API_IAMPolicyAssignment_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AssignmentId **   <a name="QS-Type-IAMPolicyAssignment-AssignmentId"></a>
Assignment ID.
Type: String
Required: No

 ** AssignmentName **   <a name="QS-Type-IAMPolicyAssignment-AssignmentName"></a>
Assignment name.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$`
Required: No

 ** AssignmentStatus **   <a name="QS-Type-IAMPolicyAssignment-AssignmentStatus"></a>
Assignment status.
Type: String
Valid Values: `ENABLED | DRAFT | DISABLED`
Required: No

 ** AwsAccountId **   <a name="QS-Type-IAMPolicyAssignment-AwsAccountId"></a>
The AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

 ** Identities **   <a name="QS-Type-IAMPolicyAssignment-Identities"></a>
Identities.
Type: String to array of strings map
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** PolicyArn **   <a name="QS-Type-IAMPolicyAssignment-PolicyArn"></a>
The Amazon Resource Name (ARN) for the IAM policy.
Type: String
Required: No

## See Also
<a name="API_IAMPolicyAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/IAMPolicyAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/IAMPolicyAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/IAMPolicyAssignment)
