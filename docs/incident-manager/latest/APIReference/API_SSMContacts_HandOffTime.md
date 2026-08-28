---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_HandOffTime.html
---

# HandOffTime
<a name="API_SSMContacts_HandOffTime"></a>

Details about when an on-call rotation shift begins or ends.

## Contents
<a name="API_SSMContacts_HandOffTime_Contents"></a>

 ** HourOfDay **   <a name="IncidentManager-Type-SSMContacts_HandOffTime-HourOfDay"></a>
The hour when an on-call rotation shift begins or ends.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: Yes

 ** MinuteOfHour **   <a name="IncidentManager-Type-SSMContacts_HandOffTime-MinuteOfHour"></a>
The minute when an on-call rotation shift begins or ends.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 59.
Required: Yes

## See Also
<a name="API_SSMContacts_HandOffTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/HandOffTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/HandOffTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/HandOffTime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
