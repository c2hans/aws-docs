---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ScheduledTriggerProperties.html
---

# ScheduledTriggerProperties
<a name="API_connect-customer-profiles_ScheduledTriggerProperties"></a>

Specifies the configuration details of a scheduled-trigger flow that you define. Currently, these settings only apply to the scheduled-trigger type.

## Contents
<a name="API_connect-customer-profiles_ScheduledTriggerProperties_Contents"></a>

 ** ScheduleExpression **   <a name="connect-Type-connect-customer-profiles_ScheduledTriggerProperties-ScheduleExpression"></a>
The scheduling expression that determines the rate at which the schedule will run, for example rate (5 minutes).
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** DataPullMode **   <a name="connect-Type-connect-customer-profiles_ScheduledTriggerProperties-DataPullMode"></a>
Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.
Type: String
Valid Values: `Incremental | Complete`
Required: No

 ** FirstExecutionFrom **   <a name="connect-Type-connect-customer-profiles_ScheduledTriggerProperties-FirstExecutionFrom"></a>
Specifies the date range for the records to import from the connector in the first flow run.
Type: Timestamp
Required: No

 ** ScheduleEndTime **   <a name="connect-Type-connect-customer-profiles_ScheduledTriggerProperties-ScheduleEndTime"></a>
Specifies the scheduled end time for a scheduled-trigger flow.
Type: Timestamp
Required: No

 ** ScheduleOffset **   <a name="connect-Type-connect-customer-profiles_ScheduledTriggerProperties-ScheduleOffset"></a>
Specifies the optional offset that is added to the time interval for a schedule-triggered flow.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 36000.
Required: No

 ** ScheduleStartTime **   <a name="connect-Type-connect-customer-profiles_ScheduledTriggerProperties-ScheduleStartTime"></a>
Specifies the scheduled start time for a scheduled-trigger flow.
Type: Timestamp
Required: No

 ** Timezone **   <a name="connect-Type-connect-customer-profiles_ScheduledTriggerProperties-Timezone"></a>
Specifies the time zone used when referring to the date and time of a scheduled-triggered flow, such as America/New\_York.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_connect-customer-profiles_ScheduledTriggerProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ScheduledTriggerProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ScheduledTriggerProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ScheduledTriggerProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
