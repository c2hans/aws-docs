---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeReplay.html
---

# DescribeReplay
<a name="API_DescribeReplay"></a>

Retrieves details about a replay. Use `DescribeReplay` to determine the progress of a running replay. A replay processes events to replay based on the time in the event, and replays them using 1 minute intervals. If you use `StartReplay` and specify an `EventStartTime` and an `EventEndTime` that covers a 20 minute time range, the events are replayed from the first minute of that 20 minute range first. Then the events from the second minute are replayed. You can use `DescribeReplay` to determine the progress of a replay. The value returned for `EventLastReplayedTime` indicates the time within the specified time range associated with the last event replayed.

## Request Syntax
<a name="API_DescribeReplay_RequestSyntax"></a>

```
{
   "ReplayName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeReplay_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReplayName](#API_DescribeReplay_RequestSyntax) **   <a name="eventbridge-DescribeReplay-request-ReplayName"></a>
The name of the replay to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DescribeReplay_ResponseSyntax"></a>

```
{
   "Description": "string",
   "Destination": {
      "Arn": "string",
      "FilterArns": [ "string" ]
   },
   "EventEndTime": number,
   "EventLastReplayedTime": number,
   "EventSourceArn": "string",
   "EventStartTime": number,
   "ReplayArn": "string",
   "ReplayEndTime": number,
   "ReplayName": "string",
   "ReplayStartTime": number,
   "State": "string",
   "StateReason": "string"
}
```

## Response Elements
<a name="API_DescribeReplay_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-Description"></a>
The description of the replay.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

 ** [Destination](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-Destination"></a>
A `ReplayDestination` object that contains details about the replay.
Type: [ReplayDestination](API_ReplayDestination.md) object

 ** [EventEndTime](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-EventEndTime"></a>
The time stamp for the last event that was replayed from the archive.
Type: Timestamp

 ** [EventLastReplayedTime](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-EventLastReplayedTime"></a>
The time that the event was last replayed.
Type: Timestamp

 ** [EventSourceArn](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-EventSourceArn"></a>
The ARN of the archive events were replayed from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`

 ** [EventStartTime](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-EventStartTime"></a>
The time stamp of the first event that was last replayed from the archive.
Type: Timestamp

 ** [ReplayArn](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-ReplayArn"></a>
The ARN of the replay.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/[\.\-_A-Za-z0-9]+$`

 ** [ReplayEndTime](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-ReplayEndTime"></a>
A time stamp for the time that the replay stopped.
Type: Timestamp

 ** [ReplayName](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-ReplayName"></a>
The name of the replay.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`

 ** [ReplayStartTime](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-ReplayStartTime"></a>
A time stamp for the time that the replay started.
Type: Timestamp

 ** [State](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-State"></a>
The current state of the replay.
Type: String
Valid Values: `STARTING | RUNNING | CANCELLING | COMPLETED | CANCELLED | FAILED`

 ** [StateReason](#API_DescribeReplay_ResponseSyntax) **   <a name="eventbridge-DescribeReplay-response-StateReason"></a>
The reason that the replay is in the current state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

## Errors
<a name="API_DescribeReplay_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeReplay_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DescribeReplay)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DescribeReplay)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DescribeReplay)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DescribeReplay)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DescribeReplay)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DescribeReplay)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DescribeReplay)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DescribeReplay)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DescribeReplay)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DescribeReplay)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
