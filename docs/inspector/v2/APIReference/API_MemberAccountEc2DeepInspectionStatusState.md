---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_MemberAccountEc2DeepInspectionStatusState.html
---

# MemberAccountEc2DeepInspectionStatusState
<a name="API_MemberAccountEc2DeepInspectionStatusState"></a>

An object that contains details about the state of Amazon Inspector deep inspection for a member account.

## Contents
<a name="API_MemberAccountEc2DeepInspectionStatusState_Contents"></a>

 ** accountId **   <a name="inspector2-Type-MemberAccountEc2DeepInspectionStatusState-accountId"></a>
The unique identifier for the AWS account of the organization member
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** errorMessage **   <a name="inspector2-Type-MemberAccountEc2DeepInspectionStatusState-errorMessage"></a>
The error message explaining why the account failed to activate Amazon Inspector deep inspection.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** status **   <a name="inspector2-Type-MemberAccountEc2DeepInspectionStatusState-status"></a>
The state of Amazon Inspector deep inspection in the member account.
Type: String
Valid Values: `ACTIVATED | DEACTIVATED | PENDING | FAILED`
Required: No

## See Also
<a name="API_MemberAccountEc2DeepInspectionStatusState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/MemberAccountEc2DeepInspectionStatusState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/MemberAccountEc2DeepInspectionStatusState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/MemberAccountEc2DeepInspectionStatusState)
