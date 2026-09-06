---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_Contact.html
---

# Contact
<a name="API_SSMContacts_Contact"></a>

A personal contact or escalation plan that Incident Manager engages during an incident.

## Contents
<a name="API_SSMContacts_Contact_Contents"></a>

 ** Alias **   <a name="IncidentManager-Type-SSMContacts_Contact-Alias"></a>
The unique and identifiable alias of the contact or escalation plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-z0-9_\-]*$`
Required: Yes

 ** ContactArn **   <a name="IncidentManager-Type-SSMContacts_Contact-ContactArn"></a>
The Amazon Resource Name (ARN) of the contact or escalation plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** Type **   <a name="IncidentManager-Type-SSMContacts_Contact-Type"></a>
The type of contact.
+  `PERSONAL`: A single, individual contact.
+  `ESCALATION`: An escalation plan.
+  `ONCALL_SCHEDULE`: An on-call schedule.
Type: String
Valid Values: `PERSONAL | ESCALATION | ONCALL_SCHEDULE`
Required: Yes

 ** DisplayName **   <a name="IncidentManager-Type-SSMContacts_Contact-DisplayName"></a>
The full name of the contact or escalation plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^[\p{L}\p{Z}\p{N}_.\-]*$`
Required: No

## See Also
<a name="API_SSMContacts_Contact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/Contact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/Contact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/Contact)
