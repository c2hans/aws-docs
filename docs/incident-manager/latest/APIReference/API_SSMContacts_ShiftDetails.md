---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ShiftDetails.html
---

# ShiftDetails
<a name="API_SSMContacts_ShiftDetails"></a>

Information about overrides to an on-call rotation shift.

## Contents
<a name="API_SSMContacts_ShiftDetails_Contents"></a>

 ** OverriddenContactIds **   <a name="IncidentManager-Type-SSMContacts_ShiftDetails-OverriddenContactIds"></a>
The Amazon Resources Names (ARNs) of the contacts who were replaced in a shift when an override was created. If the override is deleted, these contacts are restored to the shift.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

## See Also
<a name="API_SSMContacts_ShiftDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ShiftDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ShiftDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ShiftDetails)
