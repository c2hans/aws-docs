---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShard.html
---

# SubscribeToShard
<a name="API_SubscribeToShard"></a>

This operation establishes an HTTP/2 connection between the consumer you specify in the `ConsumerARN` parameter and the shard you specify in the `ShardId` parameter. After the connection is successfully established, Kinesis Data Streams pushes records from the shard to the consumer over this connection. Before you call this operation, call [RegisterStreamConsumer](API_RegisterStreamConsumer.md) to register the consumer with Kinesis Data Streams.

When the `SubscribeToShard` call succeeds, your consumer starts receiving events of type [SubscribeToShardEvent](API_SubscribeToShardEvent.md) over the HTTP/2 connection for up to 5 minutes, after which time you need to call `SubscribeToShard` again to renew the subscription if you want to continue to receive records.

You can make one call to `SubscribeToShard` per second per registered consumer per shard. For example, if you have a 4000 shard stream and two registered stream consumers, you can make one `SubscribeToShard` request per second for each combination of shard and registered consumer, allowing you to subscribe both consumers to all 4000 shards in one second.

If you call `SubscribeToShard` again with the same `ConsumerARN` and `ShardId` within 5 seconds of a successful call, you'll get a `ResourceInUseException`. If you call `SubscribeToShard` 5 seconds or more after a successful call, the second call takes over the subscription and the previous connection expires or fails with a `ResourceInUseException`.

For an example of how to use this operation, see [Enhanced Fan-Out Using the Kinesis Data Streams API](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-api.html).

## Request Syntax
<a name="API_SubscribeToShard_RequestSyntax"></a>

```
{
   "ConsumerARN": "{{string}}",
   "ShardId": "{{string}}",
   "StartingPosition": {
      "SequenceNumber": "{{string}}",
      "Timestamp": {{number}},
      "Type": "{{string}}"
   },
   "StreamId": "{{string}}"
}
```

## Request Parameters
<a name="API_SubscribeToShard_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ConsumerARN](#API_SubscribeToShard_RequestSyntax) **   <a name="Streams-SubscribeToShard-request-ConsumerARN"></a>
For this parameter, use the value you obtained when you called [RegisterStreamConsumer](API_RegisterStreamConsumer.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(arn):aws.*:kinesis:.*:\d{12}:.*stream\/[a-zA-Z0-9_.-]+\/consumer\/[a-zA-Z0-9_.-]+:[0-9]+`
Required: Yes

 ** [ShardId](#API_SubscribeToShard_RequestSyntax) **   <a name="Streams-SubscribeToShard-request-ShardId"></a>
The ID of the shard you want to subscribe to. To see a list of all the shards for a given stream, use [ListShards](API_ListShards.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [StartingPosition](#API_SubscribeToShard_RequestSyntax) **   <a name="Streams-SubscribeToShard-request-StartingPosition"></a>
The starting position in the data stream from which to start streaming.
Type: [StartingPosition](API_StartingPosition.md) object
Required: Yes

 ** [StreamId](#API_SubscribeToShard_RequestSyntax) **   <a name="Streams-SubscribeToShard-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

## Response Syntax
<a name="API_SubscribeToShard_ResponseSyntax"></a>

```
{
   "EventStream": {
      "InternalFailureException": {
      },
      "KMSAccessDeniedException": {
      },
      "KMSDisabledException": {
      },
      "KMSInvalidStateException": {
      },
      "KMSNotFoundException": {
      },
      "KMSOptInRequired": {
      },
      "KMSThrottlingException": {
      },
      "ResourceInUseException": {
      },
      "ResourceNotFoundException": {
      },
      "SubscribeToShardEvent": {
         "ChildShards": [
            {
               "HashKeyRange": {
                  "EndingHashKey": "string",
                  "StartingHashKey": "string"
               },
               "ParentShards": [ "string" ],
               "ShardId": "string"
            }
         ],
         "ContinuationSequenceNumber": "string",
         "MillisBehindLatest": number,
         "Records": [
            {
               "ApproximateArrivalTimestamp": number,
               "Data": blob,
               "EncryptionType": "string",
               "PartitionKey": "string",
               "SequenceNumber": "string"
            }
         ]
      }
   }
}
```

## Response Elements
<a name="API_SubscribeToShard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventStream](#API_SubscribeToShard_ResponseSyntax) **   <a name="Streams-SubscribeToShard-response-EventStream"></a>
The event stream that your consumer can use to read records from the shard.
Type: [SubscribeToShardEventStream](API_SubscribeToShardEventStream.md) object

## Errors
<a name="API_SubscribeToShard_Errors"></a>

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

## See Also
<a name="API_SubscribeToShard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/SubscribeToShard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/SubscribeToShard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/SubscribeToShard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/SubscribeToShard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/SubscribeToShard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/SubscribeToShard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/SubscribeToShard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/SubscribeToShard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/SubscribeToShard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/SubscribeToShard)
