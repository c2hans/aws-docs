---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_FailureDetails.html
---

# FailureDetails
<a name="API_FailureDetails"></a>

Information about an Automation failure.

## Contents
<a name="API_FailureDetails_Contents"></a>

 ** Details **   <a name="systemsmanager-Type-FailureDetails-Details"></a>
Detailed information about the Automation step failure.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** FailureStage **   <a name="systemsmanager-Type-FailureDetails-FailureStage"></a>
The stage of the Automation execution when the failure occurred. The stages include the following: InputValidation, PreVerification, Invocation, PostVerification.
Type: String
Required: No

 ** FailureType **   <a name="systemsmanager-Type-FailureDetails-FailureType"></a>
The type of Automation failure. Failure types include the following: Action, Permission, Throttling, Verification, Internal.
Type: String
Required: No

## See Also
<a name="API_FailureDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/FailureDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/FailureDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/FailureDetails)
