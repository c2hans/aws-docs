---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KnowledgeBaseScheduleRefreshOnEntity.html
---

# KnowledgeBaseScheduleRefreshOnEntity

The day on which the refresh runs. Specify one of the following:
+  `DayOfWeek` – For a weekly schedule.
+  `DayOfMonth` – For a monthly schedule.

## Contents
<a name="API_KnowledgeBaseScheduleRefreshOnEntity_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DayOfMonth **   <a name="QS-Type-KnowledgeBaseScheduleRefreshOnEntity-DayOfMonth"></a>
The day of the month on which a monthly refresh runs. Valid values include:
+  `1` through `28` – The refresh runs on that day of each month.
+  `LAST_DAY_OF_MONTH` – The refresh runs on the last day of each month.
Type: String
Pattern: `(?:LAST_DAY_OF_MONTH|1[0-9]|2[0-8]|[12]|[3-9])`
Required: No

 ** DayOfWeek **   <a name="QS-Type-KnowledgeBaseScheduleRefreshOnEntity-DayOfWeek"></a>
The day of the week on which a weekly refresh runs.
Type: String
Valid Values: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
Required: No

## See Also
<a name="API_KnowledgeBaseScheduleRefreshOnEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/KnowledgeBaseScheduleRefreshOnEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/KnowledgeBaseScheduleRefreshOnEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/KnowledgeBaseScheduleRefreshOnEntity)
