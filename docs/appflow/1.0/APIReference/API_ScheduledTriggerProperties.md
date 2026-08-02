---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ScheduledTriggerProperties.html
---

# ScheduledTriggerProperties
<a name="API_ScheduledTriggerProperties"></a>

 Specifies the configuration details of a schedule-triggered flow as defined by the user. Currently, these settings only apply to the `Scheduled` trigger type.

## Contents
<a name="API_ScheduledTriggerProperties_Contents"></a>

 ** scheduleExpression **   <a name="appflow-Type-ScheduledTriggerProperties-scheduleExpression"></a>
 The scheduling expression that determines the rate at which the schedule will run, for example `rate(5minutes)`.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** dataPullMode **   <a name="appflow-Type-ScheduledTriggerProperties-dataPullMode"></a>
 Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.
Type: String
Valid Values: `Incremental | Complete`
Required: No

 ** firstExecutionFrom **   <a name="appflow-Type-ScheduledTriggerProperties-firstExecutionFrom"></a>
 Specifies the date range for the records to import from the connector in the first flow run.
Type: Timestamp
Required: No

 ** flowErrorDeactivationThreshold **   <a name="appflow-Type-ScheduledTriggerProperties-flowErrorDeactivationThreshold"></a>
Defines how many times a scheduled flow fails consecutively before Amazon AppFlow deactivates it.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** scheduleEndTime **   <a name="appflow-Type-ScheduledTriggerProperties-scheduleEndTime"></a>
The time at which the scheduled flow ends. The time is formatted as a timestamp that follows the ISO 8601 standard, such as `2022-04-27T13:00:00-07:00`.
Type: Timestamp
Required: No

 ** scheduleOffset **   <a name="appflow-Type-ScheduledTriggerProperties-scheduleOffset"></a>
 Specifies the optional offset that is added to the time interval for a schedule-triggered flow.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 36000.
Required: No

 ** scheduleStartTime **   <a name="appflow-Type-ScheduledTriggerProperties-scheduleStartTime"></a>
The time at which the scheduled flow starts. The time is formatted as a timestamp that follows the ISO 8601 standard, such as `2022-04-26T13:00:00-07:00`.
Type: Timestamp
Required: No

 ** timezone **   <a name="appflow-Type-ScheduledTriggerProperties-timezone"></a>
Specifies the time zone used when referring to the dates and times of a scheduled flow, such as `America/New_York`. This time zone is only a descriptive label. It doesn't affect how Amazon AppFlow interprets the timestamps that you specify to schedule the flow.
If you want to schedule a flow by using times in a particular time zone, indicate the time zone as a UTC offset in your timestamps. For example, the UTC offsets for the `America/New_York` timezone are `-04:00` EDT and `-05:00 EST`.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_ScheduledTriggerProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ScheduledTriggerProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ScheduledTriggerProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ScheduledTriggerProperties)
