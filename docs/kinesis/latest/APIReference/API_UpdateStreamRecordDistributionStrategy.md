---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateStreamRecordDistributionStrategy.html
---

# UpdateStreamRecordDistributionStrategy
<a name="API_UpdateStreamRecordDistributionStrategy"></a>

Updates the record distribution strategy for the specified Amazon Kinesis Data Streams on-demand data stream. The record distribution strategy determines how Amazon Kinesis Data Streams distributes records across the shards in a stream.

**Note**
You must specify the stream using the `StreamARN` parameter.

The record distribution strategy is a stream-level setting. You can switch between the following strategies at any time, and the change takes effect immediately without downtime, data loss, or disruption to producer or consumer applications:
+  `AUTO` – Amazon Kinesis Data Streams distributes records evenly across shards using service-managed algorithms, and ignores any partition key and `ExplicitHashKey` that a producer provides. Use this strategy for stateless workloads that do not require partition-key ordering.
+  `USER_PARTITION_KEY` – Producers must provide a partition key, and Amazon Kinesis Data Streams uses the partition key to determine shard placement. Records that share a partition key are sent to the same shard. This is the default strategy.

This operation is only supported for data streams that use the on-demand capacity mode. Provisioned capacity mode streams do not support the record distribution strategy setting. Attempting to set `AUTO` on a provisioned stream results in an `InvalidArgumentException`.

New records that arrive after the change are distributed according to the new strategy. Records already in the stream keep their original shard assignments and are not redistributed.

## Request Syntax
<a name="API_UpdateStreamRecordDistributionStrategy_RequestSyntax"></a>

```
{
   "RecordDistributionStrategy": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateStreamRecordDistributionStrategy_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [RecordDistributionStrategy](#API_UpdateStreamRecordDistributionStrategy_RequestSyntax) **   <a name="Streams-UpdateStreamRecordDistributionStrategy-request-RecordDistributionStrategy"></a>
The record distribution strategy to apply to the stream. Specify one of the following values:
+  `AUTO` – Amazon Kinesis Data Streams distributes records evenly across shards and ignores any partition key and `ExplicitHashKey` that producers supply.
+  `USER_PARTITION_KEY` – Producers must supply a partition key, which Amazon Kinesis Data Streams uses to determine shard placement. This is the default.
Type: String
Valid Values: `AUTO | USER_PARTITION_KEY`
Required: Yes

 ** [StreamARN](#API_UpdateStreamRecordDistributionStrategy_RequestSyntax) **   <a name="Streams-UpdateStreamRecordDistributionStrategy-request-StreamARN"></a>
The Amazon Resource Name (ARN) of the stream to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

 ** [StreamId](#API_UpdateStreamRecordDistributionStrategy_RequestSyntax) **   <a name="Streams-UpdateStreamRecordDistributionStrategy-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

## Response Elements
<a name="API_UpdateStreamRecordDistributionStrategy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateStreamRecordDistributionStrategy_Errors"></a>

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

 ** ValidationException **
Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode.
HTTP Status Code: 400

## Examples
<a name="API_UpdateStreamRecordDistributionStrategy_Examples"></a>

### To set the record distribution strategy to AUTO
<a name="API_UpdateStreamRecordDistributionStrategy_Example_1"></a>

The following example sets the record distribution strategy to `AUTO` for the specified on-demand data stream. After this change, Amazon Kinesis Data Streams distributes new records evenly across shards using service-managed algorithms and ignores any partition key and `ExplicitHashKey` that producers provide.

#### Sample Request
<a name="API_UpdateStreamRecordDistributionStrategy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.UpdateStreamRecordDistributionStrategy
{
    "StreamARN": "arn:aws:kinesis:us-east-1:123456789012:stream/exampleStreamName",
    "RecordDistributionStrategy": "AUTO"
}
```

#### Sample Response
<a name="API_UpdateStreamRecordDistributionStrategy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_UpdateStreamRecordDistributionStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/UpdateStreamRecordDistributionStrategy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/UpdateStreamRecordDistributionStrategy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/UpdateStreamRecordDistributionStrategy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/UpdateStreamRecordDistributionStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/UpdateStreamRecordDistributionStrategy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/UpdateStreamRecordDistributionStrategy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/UpdateStreamRecordDistributionStrategy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/UpdateStreamRecordDistributionStrategy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/UpdateStreamRecordDistributionStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/UpdateStreamRecordDistributionStrategy)
