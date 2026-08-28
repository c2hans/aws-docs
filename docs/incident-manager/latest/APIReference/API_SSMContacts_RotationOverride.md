---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_RotationOverride.html
---

# RotationOverride
<a name="API_SSMContacts_RotationOverride"></a>

Information about an override specified for an on-call rotation.

## Contents
<a name="API_SSMContacts_RotationOverride_Contents"></a>

 ** CreateTime **   <a name="IncidentManager-Type-SSMContacts_RotationOverride-CreateTime"></a>
The time a rotation override was created.
Type: Timestamp
Required: Yes

 ** EndTime **   <a name="IncidentManager-Type-SSMContacts_RotationOverride-EndTime"></a>
The time a rotation override ends.
Type: Timestamp
Required: Yes

 ** NewContactIds **   <a name="IncidentManager-Type-SSMContacts_RotationOverride-NewContactIds"></a>
The Amazon Resource Names (ARNs) of the contacts assigned to the override of the on-call rotation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** RotationOverrideId **   <a name="IncidentManager-Type-SSMContacts_RotationOverride-RotationOverrideId"></a>
The Amazon Resource Name (ARN) of the override to an on-call rotation.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 39.
Pattern: `([a-fA-Z0-9]{8,11}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}){1}`
Required: Yes

 ** StartTime **   <a name="IncidentManager-Type-SSMContacts_RotationOverride-StartTime"></a>
The time a rotation override begins.
Type: Timestamp
Required: Yes

## See Also
<a name="API_SSMContacts_RotationOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/RotationOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/RotationOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/RotationOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
