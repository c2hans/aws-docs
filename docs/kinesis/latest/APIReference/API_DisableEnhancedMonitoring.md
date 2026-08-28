---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DisableEnhancedMonitoring.html
---

# DisableEnhancedMonitoring
<a name="API_DisableEnhancedMonitoring"></a>

Disables enhanced monitoring.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

## Request Syntax
<a name="API_DisableEnhancedMonitoring_RequestSyntax"></a>

```
{
   "ShardLevelMetrics": [ "{{string}}" ],
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_DisableEnhancedMonitoring_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ShardLevelMetrics](#API_DisableEnhancedMonitoring_RequestSyntax) **   <a name="Streams-DisableEnhancedMonitoring-request-ShardLevelMetrics"></a>
List of shard-level metrics to disable.
The following are the valid shard-level metrics. The value "`ALL`" disables every metric.
+  `IncomingBytes`
+  `IncomingRecords`
+  `OutgoingBytes`
+  `OutgoingRecords`
+  `WriteProvisionedThroughputExceeded`
+  `ReadProvisionedThroughputExceeded`
+  `IteratorAgeMilliseconds`
+  `ALL`
For more information, see [Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch](https://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html) in the *Amazon Kinesis Data Streams Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 7 items.
Valid Values: `IncomingBytes | IncomingRecords | OutgoingBytes | OutgoingRecords | WriteProvisionedThroughputExceeded | ReadProvisionedThroughputExceeded | IteratorAgeMilliseconds | ALL`
Required: Yes

 ** [StreamARN](#API_DisableEnhancedMonitoring_RequestSyntax) **   <a name="Streams-DisableEnhancedMonitoring-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_DisableEnhancedMonitoring_RequestSyntax) **   <a name="Streams-DisableEnhancedMonitoring-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_DisableEnhancedMonitoring_RequestSyntax) **   <a name="Streams-DisableEnhancedMonitoring-request-StreamName"></a>
The name of the Kinesis data stream for which to disable enhanced monitoring.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_DisableEnhancedMonitoring_ResponseSyntax"></a>

```
{
   "CurrentShardLevelMetrics": [ "string" ],
   "DesiredShardLevelMetrics": [ "string" ],
   "StreamARN": "string",
   "StreamName": "string"
}
```

## Response Elements
<a name="API_DisableEnhancedMonitoring_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CurrentShardLevelMetrics](#API_DisableEnhancedMonitoring_ResponseSyntax) **   <a name="Streams-DisableEnhancedMonitoring-response-CurrentShardLevelMetrics"></a>
Represents the current state of the metrics that are in the enhanced state before the operation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 7 items.
Valid Values: `IncomingBytes | IncomingRecords | OutgoingBytes | OutgoingRecords | WriteProvisionedThroughputExceeded | ReadProvisionedThroughputExceeded | IteratorAgeMilliseconds | ALL`

 ** [DesiredShardLevelMetrics](#API_DisableEnhancedMonitoring_ResponseSyntax) **   <a name="Streams-DisableEnhancedMonitoring-response-DesiredShardLevelMetrics"></a>
Represents the list of all the metrics that would be in the enhanced state after the operation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 7 items.
Valid Values: `IncomingBytes | IncomingRecords | OutgoingBytes | OutgoingRecords | WriteProvisionedThroughputExceeded | ReadProvisionedThroughputExceeded | IteratorAgeMilliseconds | ALL`

 ** [StreamARN](#API_DisableEnhancedMonitoring_ResponseSyntax) **   <a name="Streams-DisableEnhancedMonitoring-response-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`

 ** [StreamName](#API_DisableEnhancedMonitoring_ResponseSyntax) **   <a name="Streams-DisableEnhancedMonitoring-response-StreamName"></a>
The name of the Kinesis data stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_DisableEnhancedMonitoring_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** LimitExceededException **
The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is not available for this operation. For successful operation, the resource must be in the `ACTIVE` state.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_DisableEnhancedMonitoring_Examples"></a>

### To disable enhanced monitoring
<a name="API_DisableEnhancedMonitoring_Example_1"></a>

The following JSON example disables enhanced monitoring for `IncomingBytes` and `OutgoingRecords` shard level metrics.

#### Sample Request
<a name="API_DisableEnhancedMonitoring_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.DisableEnhancedMonitoring
{
    "ShardLevelMetrics": [
        "IncomingBytes", "OutgoingRecords"
    ],
    "StreamName": "exampleStreamName"
}
```

#### Sample Response
<a name="API_DisableEnhancedMonitoring_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "StreamName": "exampleStreamName",
    "CurrentShardLevelMetrics": [
        "IncomingBytes",
        "OutgoingRecords"
    ],
    "DesiredShardLevelMetrics": []
}
```

## See Also
<a name="API_DisableEnhancedMonitoring_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/DisableEnhancedMonitoring)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/DisableEnhancedMonitoring)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/DisableEnhancedMonitoring)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/DisableEnhancedMonitoring)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/DisableEnhancedMonitoring)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/DisableEnhancedMonitoring)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/DisableEnhancedMonitoring)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/DisableEnhancedMonitoring)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DisableEnhancedMonitoring)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/DisableEnhancedMonitoring)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
