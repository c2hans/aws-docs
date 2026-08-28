---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_StartReplay.html
---

# StartReplay
<a name="API_StartReplay"></a>

Starts the specified replay. Events are not necessarily replayed in the exact same order that they were added to the archive. A replay processes events to replay based on the time in the event, and replays them using 1 minute intervals. If you specify an `EventStartTime` and an `EventEndTime` that covers a 20 minute time range, the events are replayed from the first minute of that 20 minute range first. Then the events from the second minute are replayed. You can use `DescribeReplay` to determine the progress of a replay. The value returned for `EventLastReplayedTime` indicates the time within the specified time range associated with the last event replayed.

## Request Syntax
<a name="API_StartReplay_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Destination": {
      "Arn": "{{string}}",
      "FilterArns": [ "{{string}}" ]
   },
   "EventEndTime": {{number}},
   "EventSourceArn": "{{string}}",
   "EventStartTime": {{number}},
   "ReplayName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartReplay_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_StartReplay_RequestSyntax) **   <a name="eventbridge-StartReplay-request-Description"></a>
A description for the replay to start.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** [Destination](#API_StartReplay_RequestSyntax) **   <a name="eventbridge-StartReplay-request-Destination"></a>
A `ReplayDestination` object that includes details about the destination for the replay.
Type: [ReplayDestination](API_ReplayDestination.md) object
Required: Yes

 ** [EventEndTime](#API_StartReplay_RequestSyntax) **   <a name="eventbridge-StartReplay-request-EventEndTime"></a>
A time stamp for the time to stop replaying events. Only events that occurred between the `EventStartTime` and `EventEndTime` are replayed.
Type: Timestamp
Required: Yes

 ** [EventSourceArn](#API_StartReplay_RequestSyntax) **   <a name="eventbridge-StartReplay-request-EventSourceArn"></a>
The ARN of the archive to replay events from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`
Required: Yes

 ** [EventStartTime](#API_StartReplay_RequestSyntax) **   <a name="eventbridge-StartReplay-request-EventStartTime"></a>
A time stamp for the time to start replaying events. Only events that occurred between the `EventStartTime` and `EventEndTime` are replayed.
Type: Timestamp
Required: Yes

 ** [ReplayName](#API_StartReplay_RequestSyntax) **   <a name="eventbridge-StartReplay-request-ReplayName"></a>
The name of the replay to start.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_StartReplay_ResponseSyntax"></a>

```
{
   "ReplayArn": "string",
   "ReplayStartTime": number,
   "State": "string",
   "StateReason": "string"
}
```

## Response Elements
<a name="API_StartReplay_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplayArn](#API_StartReplay_ResponseSyntax) **   <a name="eventbridge-StartReplay-response-ReplayArn"></a>
The ARN of the replay.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/[\.\-_A-Za-z0-9]+$`

 ** [ReplayStartTime](#API_StartReplay_ResponseSyntax) **   <a name="eventbridge-StartReplay-response-ReplayStartTime"></a>
The time at which the replay started.
Type: Timestamp

 ** [State](#API_StartReplay_ResponseSyntax) **   <a name="eventbridge-StartReplay-response-State"></a>
The state of the replay.
Type: String
Valid Values: `STARTING | RUNNING | CANCELLING | COMPLETED | CANCELLED | FAILED`

 ** [StateReason](#API_StartReplay_ResponseSyntax) **   <a name="eventbridge-StartReplay-response-StateReason"></a>
The reason that the replay is in the state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

## Errors
<a name="API_StartReplay_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** InvalidEventPatternException **
The event pattern is not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The request failed because it attempted to create resource beyond the allowed service quota.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The resource you are trying to create already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_StartReplay_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/StartReplay)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/StartReplay)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/StartReplay)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/StartReplay)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/StartReplay)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/StartReplay)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/StartReplay)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/StartReplay)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/StartReplay)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/StartReplay)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
