---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_OpenHours.html
---

# OpenHours
<a name="API_connect-outbound-campaigns-v2_OpenHours"></a>

Contains information about open hours.

## Contents
<a name="API_connect-outbound-campaigns-v2_OpenHours_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dailyHours **   <a name="connect-Type-connect-outbound-campaigns-v2_OpenHours-dailyHours"></a>
The daily hours configuration.
Type: String to array of [TimeRange](API_connect-outbound-campaigns-v2_TimeRange.md) objects map
Valid Keys: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_OpenHours_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/OpenHours)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/OpenHours)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/OpenHours)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
