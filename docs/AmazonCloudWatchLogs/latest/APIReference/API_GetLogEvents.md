---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html
---

# GetLogEvents
<a name="API_GetLogEvents"></a>

Lists log events from the specified log stream. You can list all of the log events or filter using a time range.

 `GetLogEvents` is a paginated operation. Each page returned can contain up to 1 MB of log events or up to 10,000 log events. A returned page might only be partially full, or even empty. For example, if the result of a query would return 15,000 log events, the first page isn't guaranteed to have 10,000 log events even if they all fit into 1 MB.

Partially full or empty pages don't necessarily mean that pagination is finished. As long as the `nextBackwardToken` or `nextForwardToken` returned is NOT equal to the `nextToken` that you passed into the API call, there might be more log events available. The token that you use depends on the direction you want to move in along the log stream. The returned tokens are never null.

**Note**
If you set `startFromHead` to `true` and you don’t include `endTime` in your request, you can end up in a situation where the pagination doesn't terminate. This can happen when the new log events are being added to the target log streams faster than they are being read. This situation is a good use case for the CloudWatch Logs [Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html) feature.

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

You can specify the log group to search by using either `logGroupIdentifier` or `logGroupName`. You must include one of these two parameters, but you can't include both.

**Note**
If you are using [log transformation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html), the `GetLogEvents` operation returns only the original versions of log events, before they were transformed. To view the transformed versions, you must use a [CloudWatch Logs query.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)

## Request Syntax
<a name="API_GetLogEvents_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "limit": {{number}},
   "logGroupIdentifier": "{{string}}",
   "logGroupName": "{{string}}",
   "logStreamName": "{{string}}",
   "nextToken": "{{string}}",
   "startFromHead": {{boolean}},
   "startTime": {{number}},
   "unmask": {{boolean}}
}
```

## Request Parameters
<a name="API_GetLogEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_GetLogEvents_RequestSyntax) **   <a name="CWL-GetLogEvents-request-endTime"></a>
The end of the time range, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`. Events with a timestamp equal to or later than this time are not included.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [limit](#API_GetLogEvents_RequestSyntax) **   <a name="CWL-GetLogEvents-request-limit"></a>
The maximum number of log events returned. If you don't specify a limit, the default is as many log events as can fit in a response size of 1 MB (up to 10,000 log events).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [logGroupIdentifier](#API_GetLogEvents_RequestSyntax) **   <a name="CWL-GetLogEvents-request-logGroupIdentifier"></a>
Specify either the name or ARN of the log group to view events from. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.
 You must include either `logGroupIdentifier` or `logGroupName`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** [logGroupName](#API_GetLogEvents_RequestSyntax) **   <a name="CWL-GetLogEvents-request-logGroupName"></a>
The name of the log group.
 You must include either `logGroupIdentifier` or `logGroupName`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** [logStreamName](#API_GetLogEvents_RequestSyntax) **   <a name="CWL-GetLogEvents-request-logStreamName"></a>
The name of the log stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: Yes

 ** [nextToken](#API_GetLogEvents_RequestSyntax) **   <a name="CWL-GetLogEvents-request-nextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [startFromHead](#API_GetLogEvents_RequestSyntax) **   <a name="CWL-GetLogEvents-request-startFromHead"></a>
If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. The default value is false.
If you are using a previous `nextForwardToken` value as the `nextToken` in this operation, you must specify `true` for `startFromHead`.
Type: Boolean
Required: No

 ** [startTime](#API_GetLogEvents_RequestSyntax) **   <a name="CWL-GetLogEvents-request-startTime"></a>
The start of the time range, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`. Events with a timestamp equal to this time or later than this time are included. Events with a timestamp earlier than this time are not included.
Set `startTime` explicitly to reduce the chances of empty pages in the response.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [unmask](#API_GetLogEvents_RequestSyntax) **   <a name="CWL-GetLogEvents-request-unmask"></a>
Specify `true` to display the log event fields with all sensitive data unmasked and visible. The default is `false`.
To use this operation with this parameter, you must be signed into an account with the `logs:Unmask` permission.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetLogEvents_ResponseSyntax"></a>

```
{
   "events": [
      {
         "ingestionTime": number,
         "message": "string",
         "timestamp": number
      }
   ],
   "nextBackwardToken": "string",
   "nextForwardToken": "string"
}
```

## Response Elements
<a name="API_GetLogEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_GetLogEvents_ResponseSyntax) **   <a name="CWL-GetLogEvents-response-events"></a>
The events.
Type: Array of [OutputLogEvent](API_OutputLogEvent.md) objects

 ** [nextBackwardToken](#API_GetLogEvents_ResponseSyntax) **   <a name="CWL-GetLogEvents-response-nextBackwardToken"></a>
The token for the next set of items in the backward direction. The token expires after 24 hours. This token is not null. If you have reached the end of the stream, it returns the same token you passed in.
Type: String
Length Constraints: Minimum length of 1.

 ** [nextForwardToken](#API_GetLogEvents_ResponseSyntax) **   <a name="CWL-GetLogEvents-response-nextForwardToken"></a>
The token for the next set of items in the forward direction. The token expires after 24 hours. If you have reached the end of the stream, it returns the same token you passed in.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_GetLogEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_GetLogEvents_Examples"></a>

### To list all the events for a log stream
<a name="API_GetLogEvents_Example_1"></a>

The following example lists all events for the specified log stream.

#### Sample Request
<a name="API_GetLogEvents_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.GetLogEvents
{
  "logGroupName": "my-log-group",
  "logStreamName": "my-log-stream"
}
```

#### Sample Response
<a name="API_GetLogEvents_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "events": [
    {
      "ingestionTime": 1396035394997,
      "timestamp": 1396035378988,
      "message": "Example event 1"
    },
    {
      "ingestionTime": 1396035394997,
      "timestamp": 1396035378988,
      "message": "Example event 2"
    },
    {
      "ingestionTime": 1396035394997,
      "timestamp": 1396035378989,
      "message": "Example event 3"
    }
  ],
  "nextBackwardToken": "b/31132629274945519779805322857203735586714454643391594505",
  "nextForwardToken": "f/31132629323784151764587387538205132201699397759403884544"
}
```

### Example
<a name="API_GetLogEvents_Example_2"></a>

The following example lists all events for the specified log stream.

#### Sample Request
<a name="API_GetLogEvents_Example_2_Request"></a>

```
{
  "logGroupIdentifier": "arn:aws:logs:us-east-1:123456789012:log-group:monitoring-logGroup-1234:*",
  "logStreamName": "my-log-stream"
}
```

#### Sample Response
<a name="API_GetLogEvents_Example_2_Response"></a>

```
{
    "events": [
    {
      "ingestionTime": 1396035394997,
      "timestamp": 1396035378988,
      "message": "Example event 1"
    },
    {
      "ingestionTime": 1396035394997,
      "timestamp": 1396035378988,
      "message": "Example event 2"
    },
    {
      "ingestionTime": 1396035394997,
      "timestamp": 1396035378989,
      "message": "Example event 3"
    } ],
    "nextBackwardToken": "b/31132629274945519779805322857203735586714454643391594505",
    "nextForwardToken": "f/31132629323784151764587387538205132201699397759403884544"
}
```

## See Also
<a name="API_GetLogEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetLogEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetLogEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetLogEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetLogEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetLogEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetLogEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetLogEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetLogEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetLogEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetLogEvents)
