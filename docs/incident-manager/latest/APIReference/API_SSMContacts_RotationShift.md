---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_RotationShift.html
---

# RotationShift
<a name="API_SSMContacts_RotationShift"></a>

Information about a shift that belongs to an on-call rotation.

## Contents
<a name="API_SSMContacts_RotationShift_Contents"></a>

 ** EndTime **   <a name="IncidentManager-Type-SSMContacts_RotationShift-EndTime"></a>
The time a shift rotation ends.
Type: Timestamp
Required: Yes

 ** StartTime **   <a name="IncidentManager-Type-SSMContacts_RotationShift-StartTime"></a>
The time a shift rotation begins.
Type: Timestamp
Required: Yes

 ** ContactIds **   <a name="IncidentManager-Type-SSMContacts_RotationShift-ContactIds"></a>
The Amazon Resource Names (ARNs) of the contacts who are part of the shift rotation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: No

 ** ShiftDetails **   <a name="IncidentManager-Type-SSMContacts_RotationShift-ShiftDetails"></a>
Additional information about an on-call rotation shift.
Type: [ShiftDetails](API_SSMContacts_ShiftDetails.md) object
Required: No

 ** Type **   <a name="IncidentManager-Type-SSMContacts_RotationShift-Type"></a>
The type of shift rotation.
Type: String
Valid Values: `REGULAR | OVERRIDDEN`
Required: No

## See Also
<a name="API_SSMContacts_RotationShift_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/RotationShift)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/RotationShift)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/RotationShift)
