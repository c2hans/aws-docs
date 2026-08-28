---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_Schedule.html
---

# Schedule
<a name="API_connect-outbound-campaigns-v2_Schedule"></a>

Contains the schedule configuration.

## Contents
<a name="API_connect-outbound-campaigns-v2_Schedule_Contents"></a>

 ** endTime **   <a name="connect-Type-connect-outbound-campaigns-v2_Schedule-endTime"></a>
The end time of the schedule in UTC.
Type: Timestamp
Required: Yes

 ** startTime **   <a name="connect-Type-connect-outbound-campaigns-v2_Schedule-startTime"></a>
The start time of the schedule in UTC.
Type: Timestamp
Required: Yes

 ** refreshFrequency **   <a name="connect-Type-connect-outbound-campaigns-v2_Schedule-refreshFrequency"></a>
The refresh frequency of the campaign, specified as an ISO 8601 duration string (for example, `PT1H` for 1 hour or `P1D` for 1 day). The minimum refresh frequency is 1 hour.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `P(?:([-+]?[0-9]+)D)?(T(?:([-+]?[0-9]+)H)?(?:([-+]?[0-9]+)M)?(?:([-+]?[0-9]+)(?:[.,]([0-9]{0,9}))?S)?)?`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_Schedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/Schedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/Schedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/Schedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
