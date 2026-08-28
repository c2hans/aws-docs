---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html
---

# GetShardIterator
<a name="API_GetShardIterator"></a>

Gets an Amazon Kinesis shard iterator. A shard iterator expires 5 minutes after it is returned to the requester.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

A shard iterator specifies the shard position from which to start reading data records sequentially. The position is specified using the sequence number of a data record in a shard. A sequence number is the identifier associated with every record ingested in the stream, and is assigned when a record is put into the stream. Each stream has one or more shards.

You must specify the shard iterator type. For example, you can set the `ShardIteratorType` parameter to read exactly from the position denoted by a specific sequence number by using the `AT_SEQUENCE_NUMBER` shard iterator type. Alternatively, the parameter can read right after the sequence number by using the `AFTER_SEQUENCE_NUMBER` shard iterator type, using sequence numbers returned by earlier calls to [PutRecord](API_PutRecord.md), [PutRecords](API_PutRecords.md), [GetRecords](API_GetRecords.md), or [DescribeStream](API_DescribeStream.md). In the request, you can specify the shard iterator type `AT_TIMESTAMP` to read records from an arbitrary point in time, `TRIM_HORIZON` to cause `ShardIterator` to point to the last untrimmed record in the shard in the system (the oldest data record in the shard), or `LATEST` so that you always read the most recent data in the shard.

When you read repeatedly from a stream, use a [GetShardIterator](#API_GetShardIterator) request to get the first shard iterator for use in your first [GetRecords](API_GetRecords.md) request and for subsequent reads use the shard iterator returned by the [GetRecords](API_GetRecords.md) request in `NextShardIterator`. A new shard iterator is returned by every [GetRecords](API_GetRecords.md) request in `NextShardIterator`, which you use in the `ShardIterator` parameter of the next [GetRecords](API_GetRecords.md) request.

If a [GetShardIterator](#API_GetShardIterator) request is made too often, you receive a `ProvisionedThroughputExceededException`. For more information about throughput limits, see [GetRecords](API_GetRecords.md), and [Streams Limits](https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html) in the *Amazon Kinesis Data Streams Developer Guide*.

If the shard is closed, [GetShardIterator](#API_GetShardIterator) returns a valid iterator for the last sequence number of the shard. A shard can be closed as a result of using [SplitShard](API_SplitShard.md) or [MergeShards](API_MergeShards.md).

 [GetShardIterator](#API_GetShardIterator) has a limit of five transactions per second per account per open shard.

## Request Syntax
<a name="API_GetShardIterator_RequestSyntax"></a>

```
{
   "ShardId": "{{string}}",
   "ShardIteratorType": "{{string}}",
   "StartingSequenceNumber": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}",
   "Timestamp": {{number}}
}
```

## Request Parameters
<a name="API_GetShardIterator_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ShardId](#API_GetShardIterator_RequestSyntax) **   <a name="Streams-GetShardIterator-request-ShardId"></a>
The shard ID of the Kinesis Data Streams shard to get the iterator for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ShardIteratorType](#API_GetShardIterator_RequestSyntax) **   <a name="Streams-GetShardIterator-request-ShardIteratorType"></a>
Determines how the shard iterator is used to start reading data records from the shard.
The following are the valid Amazon Kinesis shard iterator types:
+ AT\_SEQUENCE\_NUMBER - Start reading from the position denoted by a specific sequence number, provided in the value `StartingSequenceNumber`.
+ AFTER\_SEQUENCE\_NUMBER - Start reading right after the position denoted by a specific sequence number, provided in the value `StartingSequenceNumber`.
+ AT\_TIMESTAMP - Start reading from the position denoted by a specific time stamp, provided in the value `Timestamp`.
+ TRIM\_HORIZON - Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard.
+ LATEST - Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard.
Type: String
Valid Values: `AT_SEQUENCE_NUMBER | AFTER_SEQUENCE_NUMBER | TRIM_HORIZON | LATEST | AT_TIMESTAMP`
Required: Yes

 ** [StartingSequenceNumber](#API_GetShardIterator_RequestSyntax) **   <a name="Streams-GetShardIterator-request-StartingSequenceNumber"></a>
The sequence number of the data record in the shard from which to start reading. Used with shard iterator type AT\_SEQUENCE\_NUMBER and AFTER\_SEQUENCE\_NUMBER.
Type: String
Pattern: `0|([1-9]\d{0,128})`
Required: No

 ** [StreamARN](#API_GetShardIterator_RequestSyntax) **   <a name="Streams-GetShardIterator-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_GetShardIterator_RequestSyntax) **   <a name="Streams-GetShardIterator-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_GetShardIterator_RequestSyntax) **   <a name="Streams-GetShardIterator-request-StreamName"></a>
The name of the Amazon Kinesis data stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [Timestamp](#API_GetShardIterator_RequestSyntax) **   <a name="Streams-GetShardIterator-request-Timestamp"></a>
The time stamp of the data record from which to start reading. Used with shard iterator type AT\_TIMESTAMP. A time stamp is the Unix epoch date with precision in milliseconds. For example, `2016-04-04T19:58:46.480-00:00` or `1459799926.480`. If a record with this exact time stamp does not exist, the iterator returned is for the next (later) record. If the time stamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM\_HORIZON).
Type: Timestamp
Required: No

## Response Syntax
<a name="API_GetShardIterator_ResponseSyntax"></a>

```
{
   "ShardIterator": "string"
}
```

## Response Elements
<a name="API_GetShardIterator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ShardIterator](#API_GetShardIterator_ResponseSyntax) **   <a name="Streams-GetShardIterator-response-ShardIterator"></a>
The position in the shard from which to start reading data records sequentially. A shard iterator specifies this position using the sequence number of a data record in a shard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

## Errors
<a name="API_GetShardIterator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** InternalFailureException **
The processing of the request failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The request rate for the stream is too high, or the requested data is too large for the available throughput. Reduce the frequency or size of your requests. For more information, see [Streams Limits](https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html) in the *Amazon Kinesis Data Streams Developer Guide*, and [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) in the * AWS General Reference*.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_GetShardIterator_Examples"></a>

### To get a shard iterator
<a name="API_GetShardIterator_Example_1"></a>

The following JSON example gets the specified shard iterator.

#### Sample Request
<a name="API_GetShardIterator_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.GetShardIterator
{
  "StreamName": "exampleStreamName",
  "ShardId": "shardId-000000000001",
  "ShardIteratorType": "LATEST"
}
```

#### Sample Response
<a name="API_GetShardIterator_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "ShardIterator": "AAAAAAAAAAETYyAYzd665+8e0X7JTsASDM/Hr2rSwc0X2qz93iuA3udrjTH+ikQvpQk/1ZcMMLzRdAesqwBGPnsthzU0/CBlM/U8/8oEqGwX3pKw0XyeDNRAAZyXBo3MqkQtCpXhr942BRTjvWKhFz7OmCb2Ncfr8Tl2cBktooi6kJhr+djN5WYkB38Rr3akRgCl9qaU4dY="
}
```

## See Also
<a name="API_GetShardIterator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/GetShardIterator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/GetShardIterator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/GetShardIterator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/GetShardIterator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/GetShardIterator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/GetShardIterator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/GetShardIterator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/GetShardIterator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/GetShardIterator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/GetShardIterator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
