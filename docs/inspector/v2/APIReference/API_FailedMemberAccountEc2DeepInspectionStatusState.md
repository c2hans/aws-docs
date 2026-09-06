---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FailedMemberAccountEc2DeepInspectionStatusState.html
---

# FailedMemberAccountEc2DeepInspectionStatusState
<a name="API_FailedMemberAccountEc2DeepInspectionStatusState"></a>

An object that contains details about a member account in your organization that failed to activate Amazon Inspector deep inspection.

## Contents
<a name="API_FailedMemberAccountEc2DeepInspectionStatusState_Contents"></a>

 ** accountId **   <a name="inspector2-Type-FailedMemberAccountEc2DeepInspectionStatusState-accountId"></a>
The unique identifier for the AWS account of the organization member that failed to activate Amazon Inspector deep inspection.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** ec2ScanStatus **   <a name="inspector2-Type-FailedMemberAccountEc2DeepInspectionStatusState-ec2ScanStatus"></a>
The status of EC2 scanning in the account that failed to activate Amazon Inspector deep inspection.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | SUSPENDING | SUSPENDED`
Required: No

 ** errorMessage **   <a name="inspector2-Type-FailedMemberAccountEc2DeepInspectionStatusState-errorMessage"></a>
The error message explaining why the account failed to activate Amazon Inspector deep inspection.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_FailedMemberAccountEc2DeepInspectionStatusState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FailedMemberAccountEc2DeepInspectionStatusState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FailedMemberAccountEc2DeepInspectionStatusState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FailedMemberAccountEc2DeepInspectionStatusState)
