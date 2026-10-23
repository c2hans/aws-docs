---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_FindingPosture.html
---

# FindingPosture
<a name="API_FindingPosture"></a>

The compliance posture a finding reports, for the Application Security Posture Finding class. Absent for a vulnerability finding.

## Contents
<a name="API_FindingPosture_Contents"></a>

 ** application **   <a name="continuum-Type-FindingPosture-application"></a>
The application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** applicationUid **   <a name="continuum-Type-FindingPosture-applicationUid"></a>
The identifier of the application Uid.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** applicationVersion **   <a name="continuum-Type-FindingPosture-applicationVersion"></a>
The application Version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** checks **   <a name="continuum-Type-FindingPosture-checks"></a>
The checks.
Type: Array of [FindingComplianceCheck](API_FindingComplianceCheck.md) objects
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Required: No

 ** control **   <a name="continuum-Type-FindingPosture-control"></a>
The control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** description **   <a name="continuum-Type-FindingPosture-description"></a>
The description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: No

 ** remediation **   <a name="continuum-Type-FindingPosture-remediation"></a>
The remediation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: No

 ** remediationReferences **   <a name="continuum-Type-FindingPosture-remediationReferences"></a>
The remediation References.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** requirements **   <a name="continuum-Type-FindingPosture-requirements"></a>
The requirements.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** standards **   <a name="continuum-Type-FindingPosture-standards"></a>
The standards.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** status **   <a name="continuum-Type-FindingPosture-status"></a>
The current status of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** statusId **   <a name="continuum-Type-FindingPosture-statusId"></a>
The identifier of the status.
Type: Integer
Required: No

## See Also
<a name="API_FindingPosture_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/FindingPosture)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/FindingPosture)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/FindingPosture)
