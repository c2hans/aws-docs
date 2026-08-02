---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicRefreshSchedule.html
---

# TopicRefreshSchedule
<a name="API_TopicRefreshSchedule"></a>

A structure that represents a topic refresh schedule.

## Contents
<a name="API_TopicRefreshSchedule_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BasedOnSpiceSchedule **   <a name="QS-Type-TopicRefreshSchedule-BasedOnSpiceSchedule"></a>
A Boolean value that controls whether to schedule runs at the same schedule that is specified in SPICE dataset.
Type: Boolean
Required: Yes

 ** IsEnabled **   <a name="QS-Type-TopicRefreshSchedule-IsEnabled"></a>
A Boolean value that controls whether to schedule is enabled.
Type: Boolean
Required: Yes

 ** RepeatAt **   <a name="QS-Type-TopicRefreshSchedule-RepeatAt"></a>
The time of day when the refresh should run, for example, Monday-Sunday.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** StartingAt **   <a name="QS-Type-TopicRefreshSchedule-StartingAt"></a>
The starting date and time for the refresh schedule.
Type: Timestamp
Required: No

 ** Timezone **   <a name="QS-Type-TopicRefreshSchedule-Timezone"></a>
The timezone that you want the refresh schedule to use.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** TopicScheduleType **   <a name="QS-Type-TopicRefreshSchedule-TopicScheduleType"></a>
The type of refresh schedule. Valid values for this structure are `HOURLY`, `DAILY`, `WEEKLY`, and `MONTHLY`.
Type: String
Valid Values: `HOURLY | DAILY | WEEKLY | MONTHLY`
Required: No

## See Also
<a name="API_TopicRefreshSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicRefreshSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicRefreshSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicRefreshSchedule)
