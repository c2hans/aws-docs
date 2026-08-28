---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ResolutionContact.html
---

# ResolutionContact
<a name="API_SSMContacts_ResolutionContact"></a>

Information about the engagement resolution steps. The resolution starts from the first contact, which can be an escalation plan, then resolves to an on-call rotation, and finally to a personal contact.

The `ResolutionContact` structure describes the information for each node or step in that process. It contains information about different contact types, such as the escalation, rotation, and personal contacts.

## Contents
<a name="API_SSMContacts_ResolutionContact_Contents"></a>

 ** ContactArn **   <a name="IncidentManager-Type-SSMContacts_ResolutionContact-ContactArn"></a>
The Amazon Resource Name (ARN) of a contact in the engagement resolution process.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** Type **   <a name="IncidentManager-Type-SSMContacts_ResolutionContact-Type"></a>
The type of contact for a resolution step.
Type: String
Valid Values: `PERSONAL | ESCALATION | ONCALL_SCHEDULE`
Required: Yes

 ** StageIndex **   <a name="IncidentManager-Type-SSMContacts_ResolutionContact-StageIndex"></a>
The stage in the escalation plan that resolves to this contact.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_SSMContacts_ResolutionContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ResolutionContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ResolutionContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ResolutionContact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
