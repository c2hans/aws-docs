---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ScheduleRefreshOnEntity.html
---

# ScheduleRefreshOnEntity
<a name="API_ScheduleRefreshOnEntity"></a>

The refresh on entity for weekly or monthly schedules.

## Contents
<a name="API_ScheduleRefreshOnEntity_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DayOfMonth **   <a name="QS-Type-ScheduleRefreshOnEntity-DayOfMonth"></a>
The day of the month that you want to schedule refresh on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 17.
Pattern: `^(?:LAST_DAY_OF_MONTH|1[0-9]|2[0-8]|[12]|[3-9])$`
Required: No

 ** DayOfWeek **   <a name="QS-Type-ScheduleRefreshOnEntity-DayOfWeek"></a>
The day of the week that you want to schedule a refresh on.
Type: String
Valid Values: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
Required: No

## See Also
<a name="API_ScheduleRefreshOnEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ScheduleRefreshOnEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ScheduleRefreshOnEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ScheduleRefreshOnEntity)
