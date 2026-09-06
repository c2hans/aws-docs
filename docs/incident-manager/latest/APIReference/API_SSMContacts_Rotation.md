---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_Rotation.html
---

# Rotation
<a name="API_SSMContacts_Rotation"></a>

Information about a rotation in an on-call schedule.

## Contents
<a name="API_SSMContacts_Rotation_Contents"></a>

 ** Name **   <a name="IncidentManager-Type-SSMContacts_Rotation-Name"></a>
The name of the rotation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-\s\.]*$`
Required: Yes

 ** RotationArn **   <a name="IncidentManager-Type-SSMContacts_Rotation-RotationArn"></a>
The Amazon Resource Name (ARN) of the rotation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** ContactIds **   <a name="IncidentManager-Type-SSMContacts_Rotation-ContactIds"></a>
The Amazon Resource Names (ARNs) of the contacts assigned to the rotation team.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: No

 ** Recurrence **   <a name="IncidentManager-Type-SSMContacts_Rotation-Recurrence"></a>
Information about when an on-call rotation is in effect and how long the rotation period lasts.
Type: [RecurrenceSettings](API_SSMContacts_RecurrenceSettings.md) object
Required: No

 ** StartTime **   <a name="IncidentManager-Type-SSMContacts_Rotation-StartTime"></a>
The date and time the rotation becomes active.
Type: Timestamp
Required: No

 ** TimeZoneId **   <a name="IncidentManager-Type-SSMContacts_Rotation-TimeZoneId"></a>
The time zone the rotation’s activity is based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los\_Angeles", "UTC", or "Asia/Seoul".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[:a-zA-Z0-9_\-\s\.\\/]*$`
Required: No

## See Also
<a name="API_SSMContacts_Rotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/Rotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/Rotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/Rotation)
