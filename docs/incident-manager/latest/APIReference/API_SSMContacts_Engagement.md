---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_Engagement.html
---

# Engagement
<a name="API_SSMContacts_Engagement"></a>

Incident Manager reaching out to a contact or escalation plan to engage contact during an incident.

## Contents
<a name="API_SSMContacts_Engagement_Contents"></a>

 ** ContactArn **   <a name="IncidentManager-Type-SSMContacts_Engagement-ContactArn"></a>
The ARN of the escalation plan or contact that Incident Manager is engaging.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** EngagementArn **   <a name="IncidentManager-Type-SSMContacts_Engagement-EngagementArn"></a>
The Amazon Resource Name (ARN) of the engagement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** Sender **   <a name="IncidentManager-Type-SSMContacts_Engagement-Sender"></a>
The user that started the engagement.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`
Required: Yes

 ** IncidentId **   <a name="IncidentManager-Type-SSMContacts_Engagement-IncidentId"></a>
The ARN of the incident that's engaging the contact.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`
Required: No

 ** StartTime **   <a name="IncidentManager-Type-SSMContacts_Engagement-StartTime"></a>
The time that the engagement began.
Type: Timestamp
Required: No

 ** StopTime **   <a name="IncidentManager-Type-SSMContacts_Engagement-StopTime"></a>
The time that the engagement ended.
Type: Timestamp
Required: No

## See Also
<a name="API_SSMContacts_Engagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/Engagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/Engagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/Engagement)
