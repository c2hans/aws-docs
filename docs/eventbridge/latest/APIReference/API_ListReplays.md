---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListReplays.html
---

# ListReplays
<a name="API_ListReplays"></a>

Lists your replays. You can either list all the replays or you can provide a prefix to match to the replay names. Filter parameters are exclusive.

## Request Syntax
<a name="API_ListReplays_RequestSyntax"></a>

```
{
   "EventSourceArn": "{{string}}",
   "Limit": {{number}},
   "NamePrefix": "{{string}}",
   "NextToken": "{{string}}",
   "State": "{{string}}"
}
```

## Request Parameters
<a name="API_ListReplays_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventSourceArn](#API_ListReplays_RequestSyntax) **   <a name="eventbridge-ListReplays-request-EventSourceArn"></a>
The ARN of the archive from which the events are replayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`
Required: No

 ** [Limit](#API_ListReplays_RequestSyntax) **   <a name="eventbridge-ListReplays-request-Limit"></a>
The maximum number of replays to retrieve.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NamePrefix](#API_ListReplays_RequestSyntax) **   <a name="eventbridge-ListReplays-request-NamePrefix"></a>
A name prefix to filter the replays returned. Only replays with name that match the prefix are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [NextToken](#API_ListReplays_RequestSyntax) **   <a name="eventbridge-ListReplays-request-NextToken"></a>
The token returned by a previous call, which you can use to retrieve the next set of results.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [State](#API_ListReplays_RequestSyntax) **   <a name="eventbridge-ListReplays-request-State"></a>
The state of the replay.
Type: String
Valid Values: `STARTING | RUNNING | CANCELLING | COMPLETED | CANCELLED | FAILED`
Required: No

## Response Syntax
<a name="API_ListReplays_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Replays": [
      {
         "EventEndTime": number,
         "EventLastReplayedTime": number,
         "EventSourceArn": "string",
         "EventStartTime": number,
         "ReplayEndTime": number,
         "ReplayName": "string",
         "ReplayStartTime": number,
         "State": "string",
         "StateReason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListReplays_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListReplays_ResponseSyntax) **   <a name="eventbridge-ListReplays-response-NextToken"></a>
A token indicating there are more results available. If there are no more results, no token is included in the response.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Replays](#API_ListReplays_ResponseSyntax) **   <a name="eventbridge-ListReplays-response-Replays"></a>
An array of `Replay` objects that contain information about the replay.
Type: Array of [Replay](API_Replay.md) objects

## Errors
<a name="API_ListReplays_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

## See Also
<a name="API_ListReplays_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/ListReplays)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/ListReplays)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ListReplays)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/ListReplays)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ListReplays)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/ListReplays)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/ListReplays)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/ListReplays)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/ListReplays)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ListReplays)
