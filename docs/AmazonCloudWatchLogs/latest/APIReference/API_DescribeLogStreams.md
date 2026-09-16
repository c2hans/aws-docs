---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogStreams.html
---

# DescribeLogStreams
<a name="API_DescribeLogStreams"></a>

Lists the log streams for the specified log group. You can list all the log streams or filter the results by prefix. You can also control how the results are ordered.

You can specify the log group to search by using either `logGroupIdentifier` or `logGroupName`. You must include one of these two parameters, but you can't include both.

This operation has a limit of 25 transactions per second, after which transactions are throttled.

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

## Request Syntax
<a name="API_DescribeLogStreams_RequestSyntax"></a>

```
{
   "descending": {{boolean}},
   "limit": {{number}},
   "logGroupIdentifier": "{{string}}",
   "logGroupName": "{{string}}",
   "logStreamNamePrefix": "{{string}}",
   "nextToken": "{{string}}",
   "orderBy": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLogStreams_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [descending](#API_DescribeLogStreams_RequestSyntax) **   <a name="CWL-DescribeLogStreams-request-descending"></a>
If the value is true, results are returned in descending order. If the value is to false, results are returned in ascending order. The default value is false.
Type: Boolean
Required: No

 ** [limit](#API_DescribeLogStreams_RequestSyntax) **   <a name="CWL-DescribeLogStreams-request-limit"></a>
The maximum number of items returned. If you don't specify a value, the default is up to 50 items.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [logGroupIdentifier](#API_DescribeLogStreams_RequestSyntax) **   <a name="CWL-DescribeLogStreams-request-logGroupIdentifier"></a>
Specify either the name or ARN of the log group to view. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.
 You must include either `logGroupIdentifier` or `logGroupName`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** [logGroupName](#API_DescribeLogStreams_RequestSyntax) **   <a name="CWL-DescribeLogStreams-request-logGroupName"></a>
The name of the log group.
 You must include either `logGroupIdentifier` or `logGroupName`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** [logStreamNamePrefix](#API_DescribeLogStreams_RequestSyntax) **   <a name="CWL-DescribeLogStreams-request-logStreamNamePrefix"></a>
The prefix to match.
If `orderBy` is `LastEventTime`, you cannot specify this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** [nextToken](#API_DescribeLogStreams_RequestSyntax) **   <a name="CWL-DescribeLogStreams-request-nextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [orderBy](#API_DescribeLogStreams_RequestSyntax) **   <a name="CWL-DescribeLogStreams-request-orderBy"></a>
If the value is `LogStreamName`, the results are ordered by log stream name. If the value is `LastEventTime`, the results are ordered by the event time. The default value is `LogStreamName`.
If you order the results by event time, you cannot specify the `logStreamNamePrefix` parameter.
 `lastEventTimestamp` represents the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`. `lastEventTimestamp` updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but in rare situations might take longer.
Type: String
Valid Values: `LogStreamName | LastEventTime`
Required: No

## Response Syntax
<a name="API_DescribeLogStreams_ResponseSyntax"></a>

```
{
   "logStreams": [
      {
         "arn": "string",
         "creationTime": number,
         "firstEventTimestamp": number,
         "lastEventTimestamp": number,
         "lastIngestionTime": number,
         "logStreamName": "string",
         "storedBytes": number,
         "uploadSequenceToken": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeLogStreams_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [logStreams](#API_DescribeLogStreams_ResponseSyntax) **   <a name="CWL-DescribeLogStreams-response-logStreams"></a>
The log streams.
Type: Array of [LogStream](API_LogStream.md) objects

 ** [nextToken](#API_DescribeLogStreams_ResponseSyntax) **   <a name="CWL-DescribeLogStreams-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeLogStreams_Errors"></a>

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
<a name="API_DescribeLogStreams_Examples"></a>

### To list the log streams for a log group
<a name="API_DescribeLogStreams_Example_1"></a>

The following example lists the log streams associated with the specified log group.

#### Sample Request
<a name="API_DescribeLogStreams_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.DescribeLogStreams
{
  "logGroupName": "my-log-group"
}
```

#### Sample Response
<a name="API_DescribeLogStreams_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "logStreams": [
    {
      "storedBytes": 0,
      "arn": "arn:aws:logs:us-east-1:123456789012:log-group:my-log-group-1:log-stream:my-log-stream-1",
      "creationTime": 1393545600000,
      "firstEventTimestamp": 1393545600000,
      "lastEventTimestamp": 1393567800000,
      "lastIngestionTime": 1393589200000,
      "logStreamName": "my-log-stream-1"
    },
    {
      "storedBytes": 0,
      "arn": "arn:aws:logs:us-east-1:123456789012:log-group:my-log-group-2:log-stream:my-log-stream-2",
      "creationTime": 1396224000000,
      "firstEventTimestamp": 1396224000000,
      "lastEventTimestamp": 1396235500000,
      "lastIngestionTime": 1396225560000,
      "logStreamName": "my-log-stream-2"
    }
  ]
}
```

### Example
<a name="API_DescribeLogStreams_Example_2"></a>

The following example lists the log streams associated with the specified log group.

#### Sample Request
<a name="API_DescribeLogStreams_Example_2_Request"></a>

```
{
  "logGroupIdentifier": "arn:aws:logs:us-east-1:123456789012:log-group:my-log-group-1:dli"
}
```

#### Sample Response
<a name="API_DescribeLogStreams_Example_2_Response"></a>

```
{
  "logStreams": [
    {
      "storedBytes": 0,
      "arn": "arn:aws:logs:us-east-1:123456789012:log-group:my-log-group-1:log-stream:my-
log-stream-1",
      "creationTime": 1393545600000,
      "firstEventTimestamp": 1393545600000,
      "lastEventTimestamp": 1393567800000,
      "lastIngestionTime": 1393589200000,
      "logStreamName": "my-log-stream-1"
      },
      {
      "storedBytes": 0,
      "arn": "arn:aws:logs:us-east-1:123456789012:log-group:my-log-group-2:log-stream:my-
log-stream-2",
      "creationTime": 1396224000000,
      "firstEventTimestamp": 1396224000000,
      "lastEventTimestamp": 1396235500000,
      "lastIngestionTime": 1396225560000,
      "logStreamName": "my-log-stream-2"
      } ]
}
```

## See Also
<a name="API_DescribeLogStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeLogStreams)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeLogStreams)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeLogStreams)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeLogStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeLogStreams)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeLogStreams)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeLogStreams)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeLogStreams)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeLogStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeLogStreams)
