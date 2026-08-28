---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_Page.html
---

# Page
<a name="API_SSMContacts_Page"></a>

Incident Manager engaging a contact's contact channel.

## Contents
<a name="API_SSMContacts_Page_Contents"></a>

 ** ContactArn **   <a name="IncidentManager-Type-SSMContacts_Page-ContactArn"></a>
The ARN of the contact that Incident Manager is engaging.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** EngagementArn **   <a name="IncidentManager-Type-SSMContacts_Page-EngagementArn"></a>
The ARN of the engagement that this page is part of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** PageArn **   <a name="IncidentManager-Type-SSMContacts_Page-PageArn"></a>
The Amazon Resource Name (ARN) of the page to the contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** Sender **   <a name="IncidentManager-Type-SSMContacts_Page-Sender"></a>
The user that started the engagement.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`
Required: Yes

 ** DeliveryTime **   <a name="IncidentManager-Type-SSMContacts_Page-DeliveryTime"></a>
The time the message was delivered to the contact channel.
Type: Timestamp
Required: No

 ** IncidentId **   <a name="IncidentManager-Type-SSMContacts_Page-IncidentId"></a>
The ARN of the incident that's engaging the contact channel.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`
Required: No

 ** ReadTime **   <a name="IncidentManager-Type-SSMContacts_Page-ReadTime"></a>
The time that the contact channel acknowledged engagement.
Type: Timestamp
Required: No

 ** SentTime **   <a name="IncidentManager-Type-SSMContacts_Page-SentTime"></a>
The time that Incident Manager engaged the contact channel.
Type: Timestamp
Required: No

## See Also
<a name="API_SSMContacts_Page_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/Page)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/Page)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/Page)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
