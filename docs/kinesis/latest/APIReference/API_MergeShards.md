---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_MergeShards.html
---

# MergeShards
<a name="API_MergeShards"></a>

Merges two adjacent shards in a Kinesis data stream and combines them into a single shard to reduce the stream's capacity to ingest and transport data. This API is only supported for the data streams with the provisioned capacity mode. Two shards are considered adjacent if the union of the hash key ranges for the two shards form a contiguous set with no gaps. For example, if you have two shards, one with a hash key range of 276...381 and the other with a hash key range of 382...454, then you could merge these two shards into a single shard that would have a hash key range of 276...454. After the merge, the single child shard receives data for all hash key values covered by the two parent shards.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

 `MergeShards` is called when there is a need to reduce the overall capacity of a stream because of excess capacity that is not being used. You must specify the shard to be merged and the adjacent shard for a stream. For more information about merging shards, see [Merge Two Shards](https://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-resharding-merge.html) in the *Amazon Kinesis Data Streams Developer Guide*.

If the stream is in the `ACTIVE` state, you can call `MergeShards`. If a stream is in the `CREATING`, `UPDATING`, or `DELETING` state, `MergeShards` returns a `ResourceInUseException`. If the specified stream does not exist, `MergeShards` returns a `ResourceNotFoundException`.

You can use [DescribeStreamSummary](API_DescribeStreamSummary.md) to check the state of the stream, which is returned in `StreamStatus`.

 `MergeShards` is an asynchronous operation. Upon receiving a `MergeShards` request, Amazon Kinesis Data Streams immediately returns a response and sets the `StreamStatus` to `UPDATING`. After the operation is completed, Kinesis Data Streams sets the `StreamStatus` to `ACTIVE`. Read and write operations continue to work while the stream is in the `UPDATING` state.

You use [DescribeStreamSummary](API_DescribeStreamSummary.md) and the [ListShards](API_ListShards.md) APIs to determine the shard IDs that are specified in the `MergeShards` request.

If you try to operate on too many streams in parallel using [CreateStream](API_CreateStream.md), [DeleteStream](API_DeleteStream.md), `MergeShards`, or [SplitShard](API_SplitShard.md), you receive a `LimitExceededException`.

 `MergeShards` has a limit of five transactions per second per account.

## Request Syntax
<a name="API_MergeShards_RequestSyntax"></a>

```
{
   "AdjacentShardToMerge": "{{string}}",
   "ShardToMerge": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_MergeShards_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AdjacentShardToMerge](#API_MergeShards_RequestSyntax) **   <a name="Streams-MergeShards-request-AdjacentShardToMerge"></a>
The shard ID of the adjacent shard for the merge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ShardToMerge](#API_MergeShards_RequestSyntax) **   <a name="Streams-MergeShards-request-ShardToMerge"></a>
The shard ID of the shard to combine with the adjacent shard for the merge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [StreamARN](#API_MergeShards_RequestSyntax) **   <a name="Streams-MergeShards-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_MergeShards_RequestSyntax) **   <a name="Streams-MergeShards-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_MergeShards_RequestSyntax) **   <a name="Streams-MergeShards-request-StreamName"></a>
The name of the stream for the merge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Elements
<a name="API_MergeShards_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_MergeShards_Errors"></a>

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
<a name="API_MergeShards_Examples"></a>

### To merge two adjacent shards
<a name="API_MergeShards_Example_1"></a>

The following JSON example merges two adjacent shards.

#### Sample Request
<a name="API_MergeShards_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.MergeShards
{
  "StreamName": "exampleStreamName",
  "ShardToMerge": "shardId-000000000000",
  "AdjacentShardToMerge": "shardId-000000000001"
}
```

#### Sample Response
<a name="API_MergeShards_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_MergeShards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/MergeShards)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/MergeShards)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/MergeShards)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/MergeShards)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/MergeShards)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/MergeShards)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/MergeShards)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/MergeShards)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/MergeShards)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/MergeShards)
