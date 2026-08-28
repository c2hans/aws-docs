---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_LineageSyncOutput.html
---

# LineageSyncOutput
<a name="API_LineageSyncOutput"></a>

Contains the current state of lineage sync for a Snowflake connection, including the schedule, timezone, enabled state, and the ID of the associated lineage job.

## Contents
<a name="API_LineageSyncOutput_Contents"></a>

 ** enabled **   <a name="datazone-Type-LineageSyncOutput-enabled"></a>
Specifies whether lineage sync is enabled.
Type: Boolean
Required: No

 ** lineageJobId **   <a name="datazone-Type-LineageSyncOutput-lineageJobId"></a>
The ID of the lineage sync job.
Type: String
Required: No

 ** schedule **   <a name="datazone-Type-LineageSyncOutput-schedule"></a>
The schedule of the lineage sync.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `cron\((\b[0-5]?[0-9]\b) ([*]|\b2[0-3]\b|\b[0-1]?[0-9]\b) ([-?*,/\dLW]){1,83} ([-*,/\d]|[a-zA-Z]{3}){1,23} ([-?#*,/\dL]|[a-zA-Z]{3}){1,13} ([^\)]+)\)`
Required: No

 ** timezone **   <a name="datazone-Type-LineageSyncOutput-timezone"></a>
The timezone of the lineage sync schedule.
Type: String
Valid Values: `UTC | AFRICA_JOHANNESBURG | AMERICA_MONTREAL | AMERICA_SAO_PAULO | ASIA_BAHRAIN | ASIA_BANGKOK | ASIA_CALCUTTA | ASIA_DUBAI | ASIA_HONG_KONG | ASIA_JAKARTA | ASIA_KUALA_LUMPUR | ASIA_SEOUL | ASIA_SHANGHAI | ASIA_SINGAPORE | ASIA_TAIPEI | ASIA_TOKYO | AUSTRALIA_MELBOURNE | AUSTRALIA_SYDNEY | CANADA_CENTRAL | CET | CST6CDT | ETC_GMT | ETC_GMT0 | ETC_GMT_ADD_0 | ETC_GMT_ADD_1 | ETC_GMT_ADD_10 | ETC_GMT_ADD_11 | ETC_GMT_ADD_12 | ETC_GMT_ADD_2 | ETC_GMT_ADD_3 | ETC_GMT_ADD_4 | ETC_GMT_ADD_5 | ETC_GMT_ADD_6 | ETC_GMT_ADD_7 | ETC_GMT_ADD_8 | ETC_GMT_ADD_9 | ETC_GMT_NEG_0 | ETC_GMT_NEG_1 | ETC_GMT_NEG_10 | ETC_GMT_NEG_11 | ETC_GMT_NEG_12 | ETC_GMT_NEG_13 | ETC_GMT_NEG_14 | ETC_GMT_NEG_2 | ETC_GMT_NEG_3 | ETC_GMT_NEG_4 | ETC_GMT_NEG_5 | ETC_GMT_NEG_6 | ETC_GMT_NEG_7 | ETC_GMT_NEG_8 | ETC_GMT_NEG_9 | EUROPE_DUBLIN | EUROPE_LONDON | EUROPE_PARIS | EUROPE_STOCKHOLM | EUROPE_ZURICH | ISRAEL | MEXICO_GENERAL | MST7MDT | PACIFIC_AUCKLAND | US_CENTRAL | US_EASTERN | US_MOUNTAIN | US_PACIFIC`
Required: No

## See Also
<a name="API_LineageSyncOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/LineageSyncOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/LineageSyncOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/LineageSyncOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
