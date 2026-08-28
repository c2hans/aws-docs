---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_PreviewOverride.html
---

# PreviewOverride
<a name="API_SSMContacts_PreviewOverride"></a>

Information about contacts and times that an on-call override replaces.

## Contents
<a name="API_SSMContacts_PreviewOverride_Contents"></a>

 ** EndTime **   <a name="IncidentManager-Type-SSMContacts_PreviewOverride-EndTime"></a>
Information about the time a rotation override would end.
Type: Timestamp
Required: No

 ** NewMembers **   <a name="IncidentManager-Type-SSMContacts_PreviewOverride-NewMembers"></a>
Information about contacts to add to an on-call rotation override.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*\S.*`
Required: No

 ** StartTime **   <a name="IncidentManager-Type-SSMContacts_PreviewOverride-StartTime"></a>
Information about the time a rotation override would begin.
Type: Timestamp
Required: No

## See Also
<a name="API_SSMContacts_PreviewOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/PreviewOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/PreviewOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/PreviewOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
