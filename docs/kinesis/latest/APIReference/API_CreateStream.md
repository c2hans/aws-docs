---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html
---

# CreateStream
<a name="API_CreateStream"></a>

Creates a Kinesis data stream. A stream captures and transports data records that are continuously emitted from different data sources or *producers*. Scale-out within a stream is explicitly supported by means of shards, which are uniquely identified groups of data records in a stream.

You can create your data stream using either on-demand or provisioned capacity mode. Data streams with an on-demand mode require no capacity planning and automatically scale to handle gigabytes of write and read throughput per minute. With the on-demand mode, Kinesis Data Streams automatically manages the shards in order to provide the necessary throughput.

If you'd still like to proactively scale your on-demand data stream’s capacity, you can unlock the warm throughput feature for on-demand data streams by enabling `MinimumThroughputBillingCommitment` for your account. Once your account has `MinimumThroughputBillingCommitment` enabled, you can specify the warm throughput in MiB per second that your stream can support in writes.

For the data streams with a provisioned mode, you must specify the number of shards for the data stream. Each shard can support reads up to five transactions per second, up to a maximum data read total of 2 MiB per second. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MiB per second. If the amount of data input increases or decreases, you can add or remove shards.

The stream name identifies the stream. The name is scoped to the AWS account used by the application. It is also scoped by AWS Region. That is, two streams in two different accounts can have the same name, and two streams in the same account, but in two different Regions, can have the same name.

 `CreateStream` is an asynchronous operation. Upon receiving a `CreateStream` request, Kinesis Data Streams immediately returns and sets the stream status to `CREATING`. After the stream is created, Kinesis Data Streams sets the stream status to `ACTIVE`. You should perform read and write operations only on an `ACTIVE` stream.

You receive a `LimitExceededException` when making a `CreateStream` request when you try to do one of the following:
+ Have more than five streams in the `CREATING` state at any point in time.
+ Create more shards than are authorized for your account.

For the default shard or on-demand throughput limits for an AWS account, see [Amazon Kinesis Data Streams Limits](https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html) in the *Amazon Kinesis Data Streams Developer Guide*. To increase this limit, [contact AWS Support](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

You can use [DescribeStreamSummary](API_DescribeStreamSummary.md) to check the stream status, which is returned in `StreamStatus`.

 [CreateStream](#API_CreateStream) has a limit of five transactions per second per account.

You can add tags to the stream when making a `CreateStream` request by setting the `Tags` parameter. If you pass the `Tags` parameter, in addition to having the `kinesis:CreateStream` permission, you must also have the `kinesis:AddTagsToStream` permission for the stream that will be created. The `kinesis:TagResource` permission won’t work to tag streams on creation. Tags will take effect from the `CREATING` status of the stream, but you can't make any updates to the tags until the stream is in `ACTIVE` state.

## Request Syntax
<a name="API_CreateStream_RequestSyntax"></a>

```
{
   "MaxRecordSizeInKiB": {{number}},
   "ShardCount": {{number}},
   "StreamModeDetails": {
      "StreamMode": "{{string}}"
   },
   "StreamName": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "WarmThroughputMiBps": {{number}}
}
```

## Request Parameters
<a name="API_CreateStream_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [MaxRecordSizeInKiB](#API_CreateStream_RequestSyntax) **   <a name="Streams-CreateStream-request-MaxRecordSizeInKiB"></a>
The maximum record size of a single record in kibibyte (KiB) that you can write to, and read from a stream.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 10240.
Required: No

 ** [ShardCount](#API_CreateStream_RequestSyntax) **   <a name="Streams-CreateStream-request-ShardCount"></a>
The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [StreamModeDetails](#API_CreateStream_RequestSyntax) **   <a name="Streams-CreateStream-request-StreamModeDetails"></a>
 Indicates the capacity mode of the data stream. Currently, in Kinesis Data Streams, you can choose between an **on-demand** capacity mode and a **provisioned** capacity mode for your data streams.
Type: [StreamModeDetails](API_StreamModeDetails.md) object
Required: No

 ** [StreamName](#API_CreateStream_RequestSyntax) **   <a name="Streams-CreateStream-request-StreamName"></a>
A name to identify the stream. The stream name is scoped to the AWS account used by the application that creates the stream. It is also scoped by AWS Region. That is, two streams in two different AWS accounts can have the same name. Two streams in the same AWS account but in two different Regions can also have the same name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Tags](#API_CreateStream_RequestSyntax) **   <a name="Streams-CreateStream-request-Tags"></a>
A set of up to 50 key-value pairs to use to create the tags. A tag consists of a required key and an optional value.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [WarmThroughputMiBps](#API_CreateStream_RequestSyntax) **   <a name="Streams-CreateStream-request-WarmThroughputMiBps"></a>
The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Elements
<a name="API_CreateStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ValidationException **
Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode.
HTTP Status Code: 400

## Examples
<a name="API_CreateStream_Examples"></a>

### To create a stream
<a name="API_CreateStream_Example_1"></a>

The following JSON example creates a stream with three shards.

#### Sample Request
<a name="API_CreateStream_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.CreateStream
{
    "StreamName": "exampleStreamName",
}
```

#### Sample Response
<a name="API_CreateStream_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_CreateStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/CreateStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/CreateStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/CreateStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/CreateStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/CreateStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/CreateStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/CreateStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/CreateStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/CreateStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/CreateStream)
