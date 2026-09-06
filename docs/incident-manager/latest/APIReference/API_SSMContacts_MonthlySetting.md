---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_MonthlySetting.html
---

# MonthlySetting
<a name="API_SSMContacts_MonthlySetting"></a>

Information about on-call rotations that recur monthly.

## Contents
<a name="API_SSMContacts_MonthlySetting_Contents"></a>

 ** DayOfMonth **   <a name="IncidentManager-Type-SSMContacts_MonthlySetting-DayOfMonth"></a>
The day of the month when monthly recurring on-call rotations begin.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 31.
Required: Yes

 ** HandOffTime **   <a name="IncidentManager-Type-SSMContacts_MonthlySetting-HandOffTime"></a>
The time of day when a monthly recurring on-call shift rotation begins.
Type: [HandOffTime](API_SSMContacts_HandOffTime.md) object
Required: Yes

## See Also
<a name="API_SSMContacts_MonthlySetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/MonthlySetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/MonthlySetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/MonthlySetting)
