---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html
---

# PutLogEvents
<a name="API_PutLogEvents"></a>

Uploads a batch of log events to the specified log stream.

**Important**
The sequence token is now ignored in `PutLogEvents` actions. `PutLogEvents` actions are always accepted and never return `InvalidSequenceTokenException` or `DataAlreadyAcceptedException` even if the sequence token is not valid. You can use parallel `PutLogEvents` actions on the same log stream.

The batch of events must satisfy the following constraints:
+ The maximum batch size is 1,048,576 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.
+ Events more than 2 hours in the future are rejected while processing remaining valid events.
+ Events older than 14 days or preceding the log group's retention period are rejected while processing remaining valid events.
+ The log events in the batch must be in chronological order by their timestamp. The timestamp is the time that the event occurred, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`. (In AWS Tools for PowerShell and the AWS SDK for .NET, the timestamp is specified in .NET format: `yyyy-mm-ddThh:mm:ss`. For example, `2017-09-15T13:45:30`.)
+  A batch of log events in a single request must be in a chronological order. Otherwise, the operation fails.
+ Each log event can be no larger than 1 MB.
+ The maximum number of log events in a batch is 10,000.
+ For valid events (within 14 days in the past to 2 hours in future), the time span in a single batch cannot exceed 24 hours. Otherwise, the operation fails.

**Important**
The quota of five requests per second per log stream has been removed. Instead, `PutLogEvents` actions are throttled based on a per-second per-account quota. You can request an increase to the per-second throttling quota by using the Service Quotas service.

If a call to `PutLogEvents` returns "UnrecognizedClientException" the most likely cause is a non-valid AWS access key ID or secret key.

## Request Syntax
<a name="API_PutLogEvents_RequestSyntax"></a>

```
{
   "entity": {
      "attributes": {
         "{{string}}" : "{{string}}"
      },
      "keyAttributes": {
         "{{string}}" : "{{string}}"
      }
   },
   "logEvents": [
      {
         "message": "{{string}}",
         "timestamp": {{number}}
      }
   ],
   "logGroupName": "{{string}}",
   "logStreamName": "{{string}}",
   "sequenceToken": "{{string}}"
}
```

## Request Parameters
<a name="API_PutLogEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [entity](#API_PutLogEvents_RequestSyntax) **   <a name="CWL-PutLogEvents-request-entity"></a>
The entity associated with the log events.
Type: [Entity](API_Entity.md) object
Required: No

 ** [logEvents](#API_PutLogEvents_RequestSyntax) **   <a name="CWL-PutLogEvents-request-logEvents"></a>
The log events.
Type: Array of [InputLogEvent](API_InputLogEvent.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: Yes

 ** [logGroupName](#API_PutLogEvents_RequestSyntax) **   <a name="CWL-PutLogEvents-request-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

 ** [logStreamName](#API_PutLogEvents_RequestSyntax) **   <a name="CWL-PutLogEvents-request-logStreamName"></a>
The name of the log stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: Yes

 ** [sequenceToken](#API_PutLogEvents_RequestSyntax) **   <a name="CWL-PutLogEvents-request-sequenceToken"></a>
The sequence token obtained from the response of the previous `PutLogEvents` call.
The `sequenceToken` parameter is now ignored in `PutLogEvents` actions. `PutLogEvents` actions are now accepted and never return `InvalidSequenceTokenException` or `DataAlreadyAcceptedException` even if the sequence token is not valid.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_PutLogEvents_ResponseSyntax"></a>

```
{
   "nextSequenceToken": "string",
   "rejectedEntityInfo": {
      "errorType": "string"
   },
   "rejectedLogEventsInfo": {
      "expiredLogEventEndIndex": number,
      "tooNewLogEventStartIndex": number,
      "tooOldLogEventEndIndex": number
   }
}
```

## Response Elements
<a name="API_PutLogEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextSequenceToken](#API_PutLogEvents_ResponseSyntax) **   <a name="CWL-PutLogEvents-response-nextSequenceToken"></a>
The next sequence token.
This field has been deprecated.
The sequence token is now ignored in `PutLogEvents` actions. `PutLogEvents` actions are always accepted even if the sequence token is not valid. You can use parallel `PutLogEvents` actions on the same log stream and you do not need to wait for the response of a previous `PutLogEvents` action to obtain the `nextSequenceToken` value.
Type: String
Length Constraints: Minimum length of 1.

 ** [rejectedEntityInfo](#API_PutLogEvents_ResponseSyntax) **   <a name="CWL-PutLogEvents-response-rejectedEntityInfo"></a>
Information about why the entity is rejected when calling `PutLogEvents`. Only returned when the entity is rejected.
When the entity is rejected, the events may still be accepted.
Type: [RejectedEntityInfo](API_RejectedEntityInfo.md) object

 ** [rejectedLogEventsInfo](#API_PutLogEvents_ResponseSyntax) **   <a name="CWL-PutLogEvents-response-rejectedLogEventsInfo"></a>
The rejected events.
Type: [RejectedLogEventsInfo](API_RejectedLogEventsInfo.md) object

## Errors
<a name="API_PutLogEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DataAlreadyAcceptedException **
The event was already logged.
 `PutLogEvents` actions are now always accepted and never return `DataAlreadyAcceptedException` regardless of whether a given batch of log events has already been accepted.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** InvalidSequenceTokenException **
The sequence token is not valid. You can get the correct sequence token in the `expectedSequenceToken` field in the `InvalidSequenceTokenException` message.
 `PutLogEvents` actions are now always accepted and never return `InvalidSequenceTokenException` regardless of receiving an invalid sequence token.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

 ** UnrecognizedClientException **
The most likely cause is an AWS access key ID or secret key that's not valid.
HTTP Status Code: 400

## Examples
<a name="API_PutLogEvents_Examples"></a>

### To upload log events into a log stream
<a name="API_PutLogEvents_Example_1"></a>

The following example uploads the specified log events to the specified log stream.

#### Sample Request
<a name="API_PutLogEvents_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.PutLogEvents
{
  "logGroupName": "my-log-group",
  "logStreamName": "my-log-stream",
  "logEvents": [
    {
      "timestamp": 1396035378988,
      "message": "Example event 1"
    },
    {
      "timestamp": 1396035378988,
      "message": "Example event 2"
    },
    {
      "timestamp": 1396035378989,
      "message": "Example event 3"
    }
  ]
}
```

#### Sample Response
<a name="API_PutLogEvents_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "nextSequenceToken": "49536701251539826331025683274032969384950891766572122113"
}
```

## See Also
<a name="API_PutLogEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutLogEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutLogEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutLogEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutLogEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutLogEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutLogEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutLogEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutLogEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutLogEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutLogEvents)
