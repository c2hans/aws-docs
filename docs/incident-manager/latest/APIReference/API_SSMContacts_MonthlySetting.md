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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
