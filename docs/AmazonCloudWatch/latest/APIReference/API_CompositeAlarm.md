---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CompositeAlarm.html
---

# CompositeAlarm
<a name="API_CompositeAlarm"></a>

The details about a composite alarm.

## Contents
<a name="API_CompositeAlarm_Contents"></a>

 ** ActionsEnabled **   <a name="ACW-Type-CompositeAlarm-ActionsEnabled"></a>
Indicates whether actions should be executed during any changes to the alarm state.
Type: Boolean
Required: No

 ** ActionsSuppressedBy **   <a name="ACW-Type-CompositeAlarm-ActionsSuppressedBy"></a>
 When the value is `ALARM`, it means that the actions are suppressed because the suppressor alarm is in `ALARM` When the value is `WaitPeriod`, it means that the actions are suppressed because the composite alarm is waiting for the suppressor alarm to go into into the `ALARM` state. The maximum waiting time is as specified in `ActionsSuppressorWaitPeriod`. After this time, the composite alarm performs its actions. When the value is `ExtensionPeriod`, it means that the actions are suppressed because the composite alarm is waiting after the suppressor alarm went out of the `ALARM` state. The maximum waiting time is as specified in `ActionsSuppressorExtensionPeriod`. After this time, the composite alarm performs its actions.
Type: String
Valid Values: `WaitPeriod | ExtensionPeriod | Alarm`
Required: No

 ** ActionsSuppressedReason **   <a name="ACW-Type-CompositeAlarm-ActionsSuppressedReason"></a>
 Captures the reason for action suppression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ActionsSuppressor **   <a name="ACW-Type-CompositeAlarm-ActionsSuppressor"></a>
 Actions will be suppressed if the suppressor alarm is in the `ALARM` state. `ActionsSuppressor` can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** ActionsSuppressorExtensionPeriod **   <a name="ACW-Type-CompositeAlarm-ActionsSuppressorExtensionPeriod"></a>
 The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the `ALARM` state. After this time, the composite alarm performs its actions.
 `ExtensionPeriod` is required only when `ActionsSuppressor` is specified.
Type: Integer
Required: No

 ** ActionsSuppressorWaitPeriod **   <a name="ACW-Type-CompositeAlarm-ActionsSuppressorWaitPeriod"></a>
 The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the `ALARM` state. After this time, the composite alarm performs its actions.
 `WaitPeriod` is required only when `ActionsSuppressor` is specified.
Type: Integer
Required: No

 ** AlarmActions **   <a name="ACW-Type-CompositeAlarm-AlarmActions"></a>
The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** AlarmArn **   <a name="ACW-Type-CompositeAlarm-AlarmArn"></a>
The Amazon Resource Name (ARN) of the alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** AlarmConfigurationUpdatedTimestamp **   <a name="ACW-Type-CompositeAlarm-AlarmConfigurationUpdatedTimestamp"></a>
The time stamp of the last update to the alarm configuration.
Type: Timestamp
Required: No

 ** AlarmDescription **   <a name="ACW-Type-CompositeAlarm-AlarmDescription"></a>
The description of the alarm.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** AlarmName **   <a name="ACW-Type-CompositeAlarm-AlarmName"></a>
The name of the alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** AlarmRule **   <a name="ACW-Type-CompositeAlarm-AlarmRule"></a>
The rule that this alarm uses to evaluate its alarm state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Required: No

 ** InsufficientDataActions **   <a name="ACW-Type-CompositeAlarm-InsufficientDataActions"></a>
The actions to execute when this alarm transitions to the INSUFFICIENT\_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** OKActions **   <a name="ACW-Type-CompositeAlarm-OKActions"></a>
The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** StateReason **   <a name="ACW-Type-CompositeAlarm-StateReason"></a>
An explanation for the alarm state, in text format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Required: No

 ** StateReasonData **   <a name="ACW-Type-CompositeAlarm-StateReasonData"></a>
An explanation for the alarm state, in JSON format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4000.
Required: No

 ** StateTransitionedTimestamp **   <a name="ACW-Type-CompositeAlarm-StateTransitionedTimestamp"></a>
 The timestamp of the last change to the alarm's `StateValue`.
Type: Timestamp
Required: No

 ** StateUpdatedTimestamp **   <a name="ACW-Type-CompositeAlarm-StateUpdatedTimestamp"></a>
Tracks the timestamp of any state update, even if `StateValue` doesn't change.
Type: Timestamp
Required: No

 ** StateValue **   <a name="ACW-Type-CompositeAlarm-StateValue"></a>
The state value for the alarm.
Type: String
Valid Values: `OK | ALARM | INSUFFICIENT_DATA`
Required: No

## See Also
<a name="API_CompositeAlarm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/CompositeAlarm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/CompositeAlarm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/CompositeAlarm)
