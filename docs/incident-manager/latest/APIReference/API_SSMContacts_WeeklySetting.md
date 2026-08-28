---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_WeeklySetting.html
---

# WeeklySetting
<a name="API_SSMContacts_WeeklySetting"></a>

Information about rotations that recur weekly.

## Contents
<a name="API_SSMContacts_WeeklySetting_Contents"></a>

 ** DayOfWeek **   <a name="IncidentManager-Type-SSMContacts_WeeklySetting-DayOfWeek"></a>
The day of the week when weekly recurring on-call shift rotations begins.
Type: String
Valid Values: `MON | TUE | WED | THU | FRI | SAT | SUN`
Required: Yes

 ** HandOffTime **   <a name="IncidentManager-Type-SSMContacts_WeeklySetting-HandOffTime"></a>
The time of day when a weekly recurring on-call shift rotation begins.
Type: [HandOffTime](API_SSMContacts_HandOffTime.md) object
Required: Yes

## See Also
<a name="API_SSMContacts_WeeklySetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/WeeklySetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/WeeklySetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/WeeklySetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
