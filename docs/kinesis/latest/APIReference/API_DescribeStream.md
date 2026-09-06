---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStream.html
---

# DescribeStream
<a name="API_DescribeStream"></a>

Describes the specified Kinesis data stream.

**Note**
This API has been revised. It's highly recommended that you use the [DescribeStreamSummary](API_DescribeStreamSummary.md) API to get a summarized description of the specified Kinesis data stream and the [ListShards](API_ListShards.md) API to list the shards in a specified data stream and obtain information about each shard.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

The information returned includes the stream name, Amazon Resource Name (ARN), creation time, enhanced metric configuration, and shard map. The shard map is an array of shard objects. For each shard object, there is the hash key and sequence number ranges that the shard spans, and the IDs of any earlier shards that played in a role in creating the shard. Every record ingested in the stream is identified by a sequence number, which is assigned when the record is put into the stream.

You can limit the number of shards returned by each call. For more information, see [Retrieving Shards from a Stream](https://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-retrieve-shards.html) in the *Amazon Kinesis Data Streams Developer Guide*.

There are no guarantees about the chronological order shards returned. To process shards in chronological order, use the ID of the parent shard to track the lineage to the oldest shard.

This operation has a limit of 10 transactions per second per account.

## Request Syntax
<a name="API_DescribeStream_RequestSyntax"></a>

```
{
   "ExclusiveStartShardId": "{{string}}",
   "Limit": {{number}},
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeStream_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ExclusiveStartShardId](#API_DescribeStream_RequestSyntax) **   <a name="Streams-DescribeStream-request-ExclusiveStartShardId"></a>
The shard ID of the shard to start with.
Specify this parameter to indicate that you want to describe the stream starting with the shard whose ID immediately follows `ExclusiveStartShardId`.
If you don't specify this parameter, the default behavior for `DescribeStream` is to describe the stream starting with the first shard in the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [Limit](#API_DescribeStream_RequestSyntax) **   <a name="Streams-DescribeStream-request-Limit"></a>
The maximum number of shards to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [StreamARN](#API_DescribeStream_RequestSyntax) **   <a name="Streams-DescribeStream-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_DescribeStream_RequestSyntax) **   <a name="Streams-DescribeStream-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_DescribeStream_RequestSyntax) **   <a name="Streams-DescribeStream-request-StreamName"></a>
The name of the stream to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_DescribeStream_ResponseSyntax"></a>

```
{
   "StreamDescription": {
      "EncryptionType": "string",
      "EnhancedMonitoring": [
         {
            "ShardLevelMetrics": [ "string" ]
         }
      ],
      "HasMoreShards": boolean,
      "KeyId": "string",
      "RetentionPeriodHours": number,
      "Shards": [
         {
            "AdjacentParentShardId": "string",
            "HashKeyRange": {
               "EndingHashKey": "string",
               "StartingHashKey": "string"
            },
            "ParentShardId": "string",
            "SequenceNumberRange": {
               "EndingSequenceNumber": "string",
               "StartingSequenceNumber": "string"
            },
            "ShardId": "string"
         }
      ],
      "StreamARN": "string",
      "StreamCreationTimestamp": number,
      "StreamModeDetails": {
         "StreamMode": "string"
      },
      "StreamName": "string",
      "StreamStatus": "string"
   }
}
```

## Response Elements
<a name="API_DescribeStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StreamDescription](#API_DescribeStream_ResponseSyntax) **   <a name="Streams-DescribeStream-response-StreamDescription"></a>
The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard objects that comprise the stream, and whether there are more shards available.
Type: [StreamDescription](API_StreamDescription.md) object

## Errors
<a name="API_DescribeStream_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_DescribeStream_Examples"></a>

### To get information about a stream
<a name="API_DescribeStream_Example_1"></a>

The following JSON example describes the specified stream.

#### Sample Request
<a name="API_DescribeStream_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.DescribeStream
{
    "StreamName":"exampleStreamName"
}
```

#### Sample Response
<a name="API_DescribeStream_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "StreamDescription": {
    "EnhancedMonitoring":[
       {
          "ShardLevelMetrics":[
             "IncomingBytes",
             "OutgoingRecords"
          ]
       }
    ],
    "HasMoreShards": false,
    "RetentionPeriodHours": 24,
    "StreamCreationTimestamp": 1.468346745E9,
    "Shards": [
      {
        "HashKeyRange": {
          "EndingHashKey": "113427455640312821154458202477256070484",
          "StartingHashKey": "0"
        },
        "SequenceNumberRange": {
          "EndingSequenceNumber": "21269319989741826081360214168359141376",
          "StartingSequenceNumber": "21267647932558653966460912964485513216"
        },
        "ShardId": "shardId-000000000000"
      },
      {
        "HashKeyRange": {
          "EndingHashKey": "226854911280625642308916404954512140969",
          "StartingHashKey": "113427455640312821154458202477256070485"
        },
        "SequenceNumberRange": {
          "StartingSequenceNumber": "21267647932558653966460912964485513217"
        },
        "ShardId": "shardId-000000000001"
      },
      {
        "HashKeyRange": {
          "EndingHashKey": "340282366920938463463374607431768211455",
          "StartingHashKey": "226854911280625642308916404954512140970"
        },
        "SequenceNumberRange": {
          "StartingSequenceNumber": "21267647932558653966460912964485513218"
        },
        "ShardId": "shardId-000000000002"
      }
    ],
    "StreamARN": "arn:aws:kinesis:us-east-1:111122223333:exampleStreamName",
    "StreamName": "exampleStreamName",
    "StreamStatus": "ACTIVE"
  }
}
```

## See Also
<a name="API_DescribeStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/DescribeStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/DescribeStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/DescribeStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/DescribeStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/DescribeStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/DescribeStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/DescribeStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/DescribeStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/DescribeStream)
