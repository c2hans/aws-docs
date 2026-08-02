---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RefreshFrequency.html
---

# RefreshFrequency
<a name="API_RefreshFrequency"></a>

Specifies the interval between each scheduled refresh of a dataset.

## Contents
<a name="API_RefreshFrequency_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Interval **   <a name="QS-Type-RefreshFrequency-Interval"></a>
The interval between scheduled refreshes. Valid values are as follows:
+  `MINUTE15`: The dataset refreshes every 15 minutes. This value is only supported for incremental refreshes. This interval can only be used for one schedule per dataset.
+  `MINUTE30`:The dataset refreshes every 30 minutes. This value is only supported for incremental refreshes. This interval can only be used for one schedule per dataset.
+  `HOURLY`: The dataset refreshes every hour. This interval can only be used for one schedule per dataset.
+  `DAILY`: The dataset refreshes every day.
+  `WEEKLY`: The dataset refreshes every week.
+  `MONTHLY`: The dataset refreshes every month.
Type: String
Valid Values: `MINUTE15 | MINUTE30 | HOURLY | DAILY | WEEKLY | MONTHLY`
Required: Yes

 ** RefreshOnDay **   <a name="QS-Type-RefreshFrequency-RefreshOnDay"></a>
The day of the week that you want to schedule the refresh on. This value is required for weekly and monthly refresh intervals.
Type: [ScheduleRefreshOnEntity](API_ScheduleRefreshOnEntity.md) object
Required: No

 ** TimeOfTheDay **   <a name="QS-Type-RefreshFrequency-TimeOfTheDay"></a>
The time of day that you want the datset to refresh. This value is expressed in HH:MM format. This field is not required for schedules that refresh hourly.
Type: String
Required: No

 ** Timezone **   <a name="QS-Type-RefreshFrequency-Timezone"></a>
The timezone that you want the refresh schedule to use. The timezone ID must match a corresponding ID found on `java.util.time.getAvailableIDs()`.
Type: String
Required: No

## See Also
<a name="API_RefreshFrequency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RefreshFrequency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RefreshFrequency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RefreshFrequency)
