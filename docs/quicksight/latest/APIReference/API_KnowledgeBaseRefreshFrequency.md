---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KnowledgeBaseRefreshFrequency.html
---

# KnowledgeBaseRefreshFrequency

Specifies how often a knowledge base refresh schedule runs and, for weekly or monthly schedules, which day the refresh runs.

## Contents
<a name="API_KnowledgeBaseRefreshFrequency_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Interval **   <a name="QS-Type-KnowledgeBaseRefreshFrequency-Interval"></a>
The interval at which the schedule refreshes the knowledge base. Valid values include:
+  `DAILY` – The schedule refreshes the knowledge base once each day.
+  `WEEKLY` – The schedule refreshes the knowledge base once each week, on the day that you specify in `RefreshOnDay.DayOfWeek`.
+  `MONTHLY` – The schedule refreshes the knowledge base once each month, on the day that you specify in `RefreshOnDay.DayOfMonth`.
+  `HOURLY` – The schedule refreshes the knowledge base once each hour. Available only if your account is enabled for hourly refresh. Otherwise, the request fails with an `InvalidParameterValueException`.
For `DAILY`, `WEEKLY`, and `MONTHLY` intervals, the service chooses the time of day at which the refresh runs. You can't specify the time of day.
Type: String
Valid Values: `DAILY | WEEKLY | MONTHLY | HOURLY`
Required: Yes

 ** RefreshOnDay **   <a name="QS-Type-KnowledgeBaseRefreshFrequency-RefreshOnDay"></a>
The day on which the refresh runs. This parameter is required for a `WEEKLY` or `MONTHLY` interval: specify the day of the week for `WEEKLY` or the day of the month for `MONTHLY`. If you don't specify it for one of these intervals, the request fails. This parameter isn't used for a `DAILY` or `HOURLY` interval.
Type: [KnowledgeBaseScheduleRefreshOnEntity](API_KnowledgeBaseScheduleRefreshOnEntity.md) object
Required: No

## See Also
<a name="API_KnowledgeBaseRefreshFrequency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/KnowledgeBaseRefreshFrequency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/KnowledgeBaseRefreshFrequency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/KnowledgeBaseRefreshFrequency)
