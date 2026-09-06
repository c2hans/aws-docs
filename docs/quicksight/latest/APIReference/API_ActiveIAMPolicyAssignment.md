---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ActiveIAMPolicyAssignment.html
---

# ActiveIAMPolicyAssignment
<a name="API_ActiveIAMPolicyAssignment"></a>

The active AWS Identity and Access Management (IAM) policy assignment.

## Contents
<a name="API_ActiveIAMPolicyAssignment_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AssignmentName **   <a name="QS-Type-ActiveIAMPolicyAssignment-AssignmentName"></a>
A name for the IAM policy assignment.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$`
Required: No

 ** PolicyArn **   <a name="QS-Type-ActiveIAMPolicyAssignment-PolicyArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

## See Also
<a name="API_ActiveIAMPolicyAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ActiveIAMPolicyAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ActiveIAMPolicyAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ActiveIAMPolicyAssignment)
