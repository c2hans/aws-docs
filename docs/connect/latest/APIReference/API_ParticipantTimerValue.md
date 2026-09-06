---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ParticipantTimerValue.html
---

# ParticipantTimerValue
<a name="API_ParticipantTimerValue"></a>

The value of the timer. Either the timer action (`Unset` to delete the timer), or the duration of the timer in minutes. Only one value can be set.

For more information about how chat timeouts work, see [Set up chat timeouts for human participants](https://docs.aws.amazon.com/connect/latest/adminguide/setup-chat-timeouts.html).

## Contents
<a name="API_ParticipantTimerValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ParticipantTimerAction **   <a name="connect-Type-ParticipantTimerValue-ParticipantTimerAction"></a>
The timer action. Currently only one value is allowed: `Unset`. It deletes a timer.
Type: String
Valid Values: `Unset`
Required: No

 ** ParticipantTimerDurationInMinutes **   <a name="connect-Type-ParticipantTimerValue-ParticipantTimerDurationInMinutes"></a>
The duration of a timer, in minutes.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 480.
Required: No

## See Also
<a name="API_ParticipantTimerValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ParticipantTimerValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ParticipantTimerValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ParticipantTimerValue)
