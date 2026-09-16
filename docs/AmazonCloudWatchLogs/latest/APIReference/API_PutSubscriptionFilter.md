---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.html
---

# PutSubscriptionFilter
<a name="API_PutSubscriptionFilter"></a>

Creates or updates a subscription filter and associates it with the specified log group. With subscription filters, you can subscribe to a real-time stream of log events ingested through [PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html) and have them delivered to a specific destination. When log events are sent to the receiving service, they are Base64 encoded and compressed with the GZIP format.

The following destinations are supported for subscription filters:
+ An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.
+ A logical destination created with [PutDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html) that belongs to a different account, for cross-account delivery. We currently support Kinesis Data Streams and Firehose as logical destinations.
+ An Amazon Kinesis Data Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.
+ An AWS Lambda function that belongs to the same account as the subscription filter, for same-account delivery.

Each log group can have up to two subscription filters associated with it. If you are updating an existing filter, you must specify the correct name in `filterName`.

Using regular expressions in filter patterns is supported. For these filters, there is a quotas of quota of two regular expression patterns within a single filter pattern. There is also a quota of five regular expression patterns per log group. For more information about using regular expressions in filter patterns, see [ Filter pattern syntax for metric filters, subscription filters, filter log events, and Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

To perform a `PutSubscriptionFilter` operation for any destination except a Lambda function, you must also have the `iam:PassRole` permission.

## Request Syntax
<a name="API_PutSubscriptionFilter_RequestSyntax"></a>

```
{
   "applyOnTransformedLogs": {{boolean}},
   "destinationArn": "{{string}}",
   "distribution": "{{string}}",
   "emitSystemFields": [ "{{string}}" ],
   "fieldSelectionCriteria": "{{string}}",
   "filterName": "{{string}}",
   "filterPattern": "{{string}}",
   "logGroupName": "{{string}}",
   "roleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_PutSubscriptionFilter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applyOnTransformedLogs](#API_PutSubscriptionFilter_RequestSyntax) **   <a name="CWL-PutSubscriptionFilter-request-applyOnTransformedLogs"></a>
This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see [PutTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html).
If the log group uses either a log-group level or account-level transformer, and you specify `true`, the subscription filter will be applied on the transformed version of the log events instead of the original ingested log events.
Type: Boolean
Required: No

 ** [destinationArn](#API_PutSubscriptionFilter_RequestSyntax) **   <a name="CWL-PutSubscriptionFilter-request-destinationArn"></a>
The ARN of the destination to deliver matching log events to. Currently, the supported destinations are:
+ An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.
+ A logical destination (specified using an ARN) belonging to a different account, for cross-account delivery.

  If you're setting up a cross-account subscription, the destination must have an IAM policy associated with it. The IAM policy must allow the sender to send logs to the destination. For more information, see [PutDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.html).
+ A Kinesis Data Firehose delivery stream belonging to the same account as the subscription filter, for same-account delivery.
+ A Lambda function belonging to the same account as the subscription filter, for same-account delivery.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [distribution](#API_PutSubscriptionFilter_RequestSyntax) **   <a name="CWL-PutSubscriptionFilter-request-distribution"></a>
The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis data stream.
Type: String
Valid Values: `Random | ByLogStream`
Required: No

 ** [emitSystemFields](#API_PutSubscriptionFilter_RequestSyntax) **   <a name="CWL-PutSubscriptionFilter-request-emitSystemFields"></a>
A list of system fields to include in the log events sent to the subscription destination. Valid values are `@aws.account`, `@aws.region`, and `@source.log`. These fields provide source information for centralized log data in the forwarded payload.
Type: Array of strings
Required: No

 ** [fieldSelectionCriteria](#API_PutSubscriptionFilter_RequestSyntax) **   <a name="CWL-PutSubscriptionFilter-request-fieldSelectionCriteria"></a>
A filter expression that specifies which log events should be processed by this subscription filter based on system fields such as source account and source region. Uses selection criteria syntax with operators like `=`, `!=`, `AND`, `OR`, `IN`, `NOT IN`. Example: `@aws.region NOT IN ["cn-north-1"]` or `@aws.account = "123456789012" AND @aws.region = "us-east-1"`. Maximum length: 2000 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [filterName](#API_PutSubscriptionFilter_RequestSyntax) **   <a name="CWL-PutSubscriptionFilter-request-filterName"></a>
A name for the subscription filter. If you are updating an existing filter, you must specify the correct name in `filterName`. To find the name of the filter currently associated with a log group, use [DescribeSubscriptionFilters](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeSubscriptionFilters.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: Yes

 ** [filterPattern](#API_PutSubscriptionFilter_RequestSyntax) **   <a name="CWL-PutSubscriptionFilter-request-filterPattern"></a>
A filter pattern for subscribing to a filtered stream of log events.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** [logGroupName](#API_PutSubscriptionFilter_RequestSyntax) **   <a name="CWL-PutSubscriptionFilter-request-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

 ** [roleArn](#API_PutSubscriptionFilter_RequestSyntax) **   <a name="CWL-PutSubscriptionFilter-request-roleArn"></a>
The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Elements
<a name="API_PutSubscriptionFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutSubscriptionFilter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidOperationException **
The operation is not valid on the specified resource.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_PutSubscriptionFilter_Examples"></a>

### To create or update a subscription filter
<a name="API_PutSubscriptionFilter_Example_1"></a>

The following example creates a subscription filter.

#### Sample Request
<a name="API_PutSubscriptionFilter_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.PutSubscriptionFilter
{
  "logGroupName": "my-log-group",
  "filterName": "my-subscription-filter",
  "filterPattern": "[ip, identity, user_id, timestamp, request, status_code = 500, size]",
  "destinationArn": "arn:aws:kinesis:us-east-1:123456789012:stream/my-kinesis-stream",
  "roleArn": "arn:aws:iam::123456789012:role/my-subscription-role",
  "applyOnTransformedLogs" : true
}
```

#### Sample Response
<a name="API_PutSubscriptionFilter_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_PutSubscriptionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutSubscriptionFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutSubscriptionFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutSubscriptionFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutSubscriptionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutSubscriptionFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutSubscriptionFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutSubscriptionFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutSubscriptionFilter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutSubscriptionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutSubscriptionFilter)
