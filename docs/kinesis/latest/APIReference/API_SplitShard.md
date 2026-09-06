---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SplitShard.html
---

# SplitShard
<a name="API_SplitShard"></a>

Splits a shard into two new shards in the Kinesis data stream, to increase the stream's capacity to ingest and transport data. `SplitShard` is called when there is a need to increase the overall capacity of a stream because of an expected increase in the volume of data records being ingested. This API is only supported for the data streams with the provisioned capacity mode.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

You can also use `SplitShard` when a shard appears to be approaching its maximum utilization; for example, the producers sending data into the specific shard are suddenly sending more than previously anticipated. You can also call `SplitShard` to increase stream capacity, so that more Kinesis Data Streams applications can simultaneously read data from the stream for real-time processing.

You must specify the shard to be split and the new hash key, which is the position in the shard where the shard gets split in two. In many cases, the new hash key might be the average of the beginning and ending hash key, but it can be any hash key value in the range being mapped into the shard. For more information, see [Split a Shard](https://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-resharding-split.html) in the *Amazon Kinesis Data Streams Developer Guide*.

You can use [DescribeStreamSummary](API_DescribeStreamSummary.md) and the [ListShards](API_ListShards.md) APIs to determine the shard ID and hash key values for the `ShardToSplit` and `NewStartingHashKey` parameters that are specified in the `SplitShard` request.

 `SplitShard` is an asynchronous operation. Upon receiving a `SplitShard` request, Kinesis Data Streams immediately returns a response and sets the stream status to `UPDATING`. After the operation is completed, Kinesis Data Streams sets the stream status to `ACTIVE`. Read and write operations continue to work while the stream is in the `UPDATING` state.

You can use [DescribeStreamSummary](API_DescribeStreamSummary.md) to check the status of the stream, which is returned in `StreamStatus`. If the stream is in the `ACTIVE` state, you can call `SplitShard`.

If the specified stream does not exist, [DescribeStreamSummary](API_DescribeStreamSummary.md) returns a `ResourceNotFoundException`. If you try to create more shards than are authorized for your account, you receive a `LimitExceededException`.

For the default shard limit for an AWS account, see [Kinesis Data Streams Limits](https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html) in the *Amazon Kinesis Data Streams Developer Guide*. To increase this limit, [contact AWS Support](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

If you try to operate on too many streams simultaneously using [CreateStream](API_CreateStream.md), [DeleteStream](API_DeleteStream.md), [MergeShards](API_MergeShards.md), and/or [SplitShard](#API_SplitShard), you receive a `LimitExceededException`.

 `SplitShard` has a limit of five transactions per second per account.

## Request Syntax
<a name="API_SplitShard_RequestSyntax"></a>

```
{
   "NewStartingHashKey": "{{string}}",
   "ShardToSplit": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_SplitShard_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [NewStartingHashKey](#API_SplitShard_RequestSyntax) **   <a name="Streams-SplitShard-request-NewStartingHashKey"></a>
A hash key value for the starting hash key of one of the child shards created by the split. The hash key range for a given shard constitutes a set of ordered contiguous positive integers. The value for `NewStartingHashKey` must be in the range of hash keys being mapped into the shard. The `NewStartingHashKey` hash key value and all higher hash key values in hash key range are distributed to one of the child shards. All the lower hash key values in the range are distributed to the other child shard.
Type: String
Pattern: `^(0|([1-9]\d{0,38}))$`
Required: Yes

 ** [ShardToSplit](#API_SplitShard_RequestSyntax) **   <a name="Streams-SplitShard-request-ShardToSplit"></a>
The shard ID of the shard to split.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [StreamARN](#API_SplitShard_RequestSyntax) **   <a name="Streams-SplitShard-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_SplitShard_RequestSyntax) **   <a name="Streams-SplitShard-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_SplitShard_RequestSyntax) **   <a name="Streams-SplitShard-request-StreamName"></a>
The name of the stream for the shard split.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Elements
<a name="API_SplitShard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SplitShard_Errors"></a>

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
<a name="API_SplitShard_Examples"></a>

### To split a shard
<a name="API_SplitShard_Example_1"></a>

The following JSON example splits the specified shard.

#### Sample Request
<a name="API_SplitShard_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.SplitShard
{
  "StreamName": "exampleStreamName",
  "ShardToSplit": "shardId-000000000000",
  "NewStartingHashKey": "10"
}
```

#### Sample Response
<a name="API_SplitShard_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_SplitShard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/SplitShard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/SplitShard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/SplitShard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/SplitShard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/SplitShard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/SplitShard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/SplitShard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/SplitShard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/SplitShard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/SplitShard)
