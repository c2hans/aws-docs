---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListShards.html
---

# ListShards
<a name="API_ListShards"></a>

Lists the shards in a stream and provides information about each shard. This operation has a limit of 1000 transactions per second per data stream.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

This action does not list expired shards. For information about expired shards, see [Data Routing, Data Persistence, and Shard State after a Reshard](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-after-resharding.html#kinesis-using-sdk-java-resharding-data-routing).

**Important**
This API is a new operation that is used by the Amazon Kinesis Client Library (KCL). If you have a fine-grained IAM policy that only allows specific operations, you must update your policy to allow calls to this API. For more information, see [Controlling Access to Amazon Kinesis Data Streams Resources Using IAM](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html).

## Request Syntax
<a name="API_ListShards_RequestSyntax"></a>

```
{
   "ExclusiveStartShardId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ShardFilter": {
      "ShardId": "{{string}}",
      "Timestamp": {{number}},
      "Type": "{{string}}"
   },
   "StreamARN": "{{string}}",
   "StreamCreationTimestamp": {{number}},
   "StreamId": "{{string}}",
   "StreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListShards_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ExclusiveStartShardId](#API_ListShards_RequestSyntax) **   <a name="Streams-ListShards-request-ExclusiveStartShardId"></a>
Specify this parameter to indicate that you want to list the shards starting with the shard whose ID immediately follows `ExclusiveStartShardId`.
If you don't specify this parameter, the default behavior is for `ListShards` to list the shards starting with the first one in the stream.
You cannot specify this parameter if you specify `NextToken`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [MaxResults](#API_ListShards_RequestSyntax) **   <a name="Streams-ListShards-request-MaxResults"></a>
The maximum number of shards to return in a single call to `ListShards`. The maximum number of shards to return in a single call. The default value is 1000. If you specify a value greater than 1000, at most 1000 results are returned.
When the number of shards to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListShards` to list the next set of shards.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [NextToken](#API_ListShards_RequestSyntax) **   <a name="Streams-ListShards-request-NextToken"></a>
When the number of shards in the data stream is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of shards in the data stream, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListShards` to list the next set of shards.
Don't specify `StreamName` or `StreamCreationTimestamp` if you specify `NextToken` because the latter unambiguously identifies the stream.
You can optionally specify a value for the `MaxResults` parameter when you specify `NextToken`. If you specify a `MaxResults` value that is less than the number of shards that the operation returns if you don't specify `MaxResults`, the response will contain a new `NextToken` value. You can use the new `NextToken` value in a subsequent call to the `ListShards` operation.
Tokens expire after 300 seconds. When you obtain a value for `NextToken` in the response to a call to `ListShards`, you have 300 seconds to use that value. If you specify an expired token in a call to `ListShards`, you get `ExpiredNextTokenException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: No

 ** [ShardFilter](#API_ListShards_RequestSyntax) **   <a name="Streams-ListShards-request-ShardFilter"></a>
Enables you to filter out the response of the `ListShards` API. You can only specify one filter at a time.
If you use the `ShardFilter` parameter when invoking the ListShards API, the `Type` is the required property and must be specified. If you specify the `AT_TRIM_HORIZON`, `FROM_TRIM_HORIZON`, or `AT_LATEST` types, you do not need to specify either the `ShardId` or the `Timestamp` optional properties.
If you specify the `AFTER_SHARD_ID` type, you must also provide the value for the optional `ShardId` property. The `ShardId` property is identical in fuctionality to the `ExclusiveStartShardId` parameter of the `ListShards` API. When `ShardId` property is specified, the response includes the shards starting with the shard whose ID immediately follows the `ShardId` that you provided.
If you specify the `AT_TIMESTAMP` or `FROM_TIMESTAMP_ID` type, you must also provide the value for the optional `Timestamp` property. If you specify the AT\_TIMESTAMP type, then all shards that were open at the provided timestamp are returned. If you specify the FROM\_TIMESTAMP type, then all shards starting from the provided timestamp to TIP are returned.
Type: [ShardFilter](API_ShardFilter.md) object
Required: No

 ** [StreamARN](#API_ListShards_RequestSyntax) **   <a name="Streams-ListShards-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamCreationTimestamp](#API_ListShards_RequestSyntax) **   <a name="Streams-ListShards-request-StreamCreationTimestamp"></a>
Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the shards for.
You cannot specify this parameter if you specify the `NextToken` parameter.
Type: Timestamp
Required: No

 ** [StreamId](#API_ListShards_RequestSyntax) **   <a name="Streams-ListShards-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_ListShards_RequestSyntax) **   <a name="Streams-ListShards-request-StreamName"></a>
The name of the data stream whose shards you want to list.
You cannot specify this parameter if you specify the `NextToken` parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_ListShards_ResponseSyntax"></a>

```
{
   "NextToken": "string",
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
   ]
}
```

## Response Elements
<a name="API_ListShards_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListShards_ResponseSyntax) **   <a name="Streams-ListShards-response-NextToken"></a>
When the number of shards in the data stream is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of shards in the data stream, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListShards` to list the next set of shards. For more information about the use of this pagination token when calling the `ListShards` operation, see [ListShards:NextToken](#Streams-ListShards-request-NextToken).
Tokens expire after 300 seconds. When you obtain a value for `NextToken` in the response to a call to `ListShards`, you have 300 seconds to use that value. If you specify an expired token in a call to `ListShards`, you get `ExpiredNextTokenException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.

 ** [Shards](#API_ListShards_ResponseSyntax) **   <a name="Streams-ListShards-response-Shards"></a>
An array of JSON objects. Each object represents one shard and specifies the IDs of the shard, the shard's parent, and the shard that's adjacent to the shard's parent. Each object also contains the starting and ending hash keys and the starting and ending sequence numbers for the shard.
Type: Array of [Shard](API_Shard.md) objects

## Errors
<a name="API_ListShards_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** ExpiredNextTokenException **
The pagination token passed to the operation is expired.
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
<a name="API_ListShards_Examples"></a>

### To list the shards of a stream
<a name="API_ListShards_Example_1"></a>

The following JSON example lists three of the shards of the stream that is specified using `StreamName`. If the stream has more than three shards, the response includes a pagination token named `NextToken`. You can use `NextToken` in your input to a subsequent call to `ListShards` to get a listing of the next set of shards. When there are no more shards to be listed, the response doesn't contain `NextToken`.

#### Sample Request
<a name="API_ListShards_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.ListShards
{
    "StreamName": "exampleStreamName",
    "MaxResults": 3
}
```

#### Sample Response
<a name="API_ListShards_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "NextToken": "AAAAAAAAAAGK9EEG0sJqVhCUS2JsgigQ5dcpB4q9PYswrH2oK44Skbjtm+WR0xA7/hrAFFsohevH1/OyPnbzKBS1byPyCZuVcokYtQe/b1m4c0SCI7jctPT0oUTLRdwSRirKm9dp9YC/EL+kZHOvYAUnztVGsOAPEFC3ECf/bVC927bDZBbRRzy/44OHfWmrCLcbcWqehRh5D14WnL3yLsumhiHDkyuxSlkBepauvMnNLtTOlRtmQ5Q5reoujfq2gzeCSOtLcfXgBMztJqohPdgMzjTQSbwB9Am8rMpHLsDbSdMNXmITvw==",
    "Shards": [
        {
            "ShardId": "shardId-000000000001",
            "HashKeyRange": {
                "EndingHashKey": "68056473384187692692674921486353642280",
                "StartingHashKey": "34028236692093846346337460743176821145"
            },
            "SequenceNumberRange": {
                "StartingSequenceNumber": "49579844037727333356165064238440708846556371693205002258"
            }
        },
        {
            "ShardId": "shardId-000000000002",
            "HashKeyRange": {
                "EndingHashKey": "102084710076281539039012382229530463436",
                "StartingHashKey": "68056473384187692692674921486353642281"
            },
            "SequenceNumberRange": {
                "StartingSequenceNumber": "49579844037749634101363594861582244564829020124710982690"
            }
        },
        {
            "ShardId": "shardId-000000000003",
            "HashKeyRange": {
                "EndingHashKey": "136112946768375385385349842972707284581",
                "StartingHashKey": "102084710076281539039012382229530463437"
            },
            "SequenceNumberRange": {
                "StartingSequenceNumber": "49579844037771934846562125484723780283101668556216963122"
            }
        }
    ]
}
```

## See Also
<a name="API_ListShards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/ListShards)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/ListShards)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ListShards)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/ListShards)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ListShards)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/ListShards)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/ListShards)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/ListShards)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListShards)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ListShards)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
