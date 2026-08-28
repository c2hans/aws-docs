---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Replay.html
---

# Replay
<a name="API_Replay"></a>

A `Replay` object that contains details about a replay.

## Contents
<a name="API_Replay_Contents"></a>

 ** EventEndTime **   <a name="eventbridge-Type-Replay-EventEndTime"></a>
A time stamp for the time to start replaying events. Any event with a creation time prior to the `EventEndTime` specified is replayed.
Type: Timestamp
Required: No

 ** EventLastReplayedTime **   <a name="eventbridge-Type-Replay-EventLastReplayedTime"></a>
A time stamp for the time that the last event was replayed.
Type: Timestamp
Required: No

 ** EventSourceArn **   <a name="eventbridge-Type-Replay-EventSourceArn"></a>
The ARN of the archive to replay event from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`
Required: No

 ** EventStartTime **   <a name="eventbridge-Type-Replay-EventStartTime"></a>
A time stamp for the time to start replaying events. This is determined by the time in the event as described in [Time](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEventsRequestEntry.html#eventbridge-Type-PutEventsRequestEntry-Time).
Type: Timestamp
Required: No

 ** ReplayEndTime **   <a name="eventbridge-Type-Replay-ReplayEndTime"></a>
A time stamp for the time that the replay completed.
Type: Timestamp
Required: No

 ** ReplayName **   <a name="eventbridge-Type-Replay-ReplayName"></a>
The name of the replay.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** ReplayStartTime **   <a name="eventbridge-Type-Replay-ReplayStartTime"></a>
A time stamp for the time that the replay started.
Type: Timestamp
Required: No

 ** State **   <a name="eventbridge-Type-Replay-State"></a>
The current state of the replay.
Type: String
Valid Values: `STARTING | RUNNING | CANCELLING | COMPLETED | CANCELLED | FAILED`
Required: No

 ** StateReason **   <a name="eventbridge-Type-Replay-StateReason"></a>
A description of why the replay is in the current state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

## See Also
<a name="API_Replay_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/Replay)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/Replay)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/Replay)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
