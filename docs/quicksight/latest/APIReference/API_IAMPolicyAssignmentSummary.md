---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_IAMPolicyAssignmentSummary.html
---

# IAMPolicyAssignmentSummary
<a name="API_IAMPolicyAssignmentSummary"></a>

IAM policy assignment summary.

## Contents
<a name="API_IAMPolicyAssignmentSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AssignmentName **   <a name="QS-Type-IAMPolicyAssignmentSummary-AssignmentName"></a>
Assignment name.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `(?=^.{2,256}$)(?!.*\s)[0-9a-zA-Z-_.:=+@]*$`
Required: No

 ** AssignmentStatus **   <a name="QS-Type-IAMPolicyAssignmentSummary-AssignmentStatus"></a>
Assignment status.
Type: String
Valid Values: `ENABLED | DRAFT | DISABLED`
Required: No

## See Also
<a name="API_IAMPolicyAssignmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/IAMPolicyAssignmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/IAMPolicyAssignmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/IAMPolicyAssignmentSummary)
