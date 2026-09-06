---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html
---

# GetRecords
<a name="API_GetRecords"></a>

Gets data records from a Kinesis data stream's shard.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

Specify a shard iterator using the `ShardIterator` parameter. The shard iterator specifies the position in the shard from which you want to start reading data records sequentially. If there are no records available in the portion of the shard that the iterator points to, [GetRecords](#API_GetRecords) returns an empty list. It might take multiple calls to get to a portion of the shard that contains records.

You can scale by provisioning multiple shards per stream while considering service limits (for more information, see [Amazon Kinesis Data Streams Limits](https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html) in the *Amazon Kinesis Data Streams Developer Guide*). Your application should have one thread per shard, each reading continuously from its stream. To read from a stream continually, call [GetRecords](#API_GetRecords) in a loop. Use [GetShardIterator](API_GetShardIterator.md) to get the shard iterator to specify in the first [GetRecords](#API_GetRecords) call. [GetRecords](#API_GetRecords) returns a new shard iterator in `NextShardIterator`. Specify the shard iterator returned in `NextShardIterator` in subsequent calls to [GetRecords](#API_GetRecords). If the shard has been closed, the shard iterator can't return more data and [GetRecords](#API_GetRecords) returns `null` in `NextShardIterator`. You can terminate the loop when the shard is closed, or when the shard iterator reaches the record with the sequence number or other attribute that marks it as the last record to process.

Each data record can be up to 1 MiB in size by default. Amazon Kinesis Data Streams supports large records up to 10 MiB in size, but the average throughput for your stream cannot exceed 1 MiB per second. For more information about how large records are handled, see [Large records](https://docs.aws.amazon.com/streams/latest/dev/large-records.html). Each shard can read up to 2 MiB per second. You can ensure that your calls don't exceed the maximum supported size or throughput by using the `Limit` parameter to specify the maximum number of records that [GetRecords](#API_GetRecords) can return. Consider your average record size when determining this limit. The maximum number of records that can be returned per call is 10,000.

The size of the data returned by [GetRecords](#API_GetRecords) varies depending on the utilization of the shard. It is recommended that consumer applications retrieve records via the `GetRecords` command using the 5 TPS limit to remain caught up. Retrieving records less frequently can lead to consumer applications falling behind. The maximum size of data that [GetRecords](#API_GetRecords) can return is 10 MiB. If a call returns this amount of data, subsequent calls made within the next 5 seconds throw `ProvisionedThroughputExceededException`. If there is insufficient provisioned throughput on the stream, subsequent calls made within the next 1 second throw `ProvisionedThroughputExceededException`. [GetRecords](#API_GetRecords) doesn't return any data when it throws an exception. For this reason, we recommend that you wait 1 second between calls to [GetRecords](#API_GetRecords). However, it's possible that the application will get exceptions for longer than 1 second.

To detect whether the application is falling behind in processing, you can use the `MillisBehindLatest` response attribute. You can also monitor the stream using CloudWatch metrics and other mechanisms (see [Monitoring](https://docs.aws.amazon.com/kinesis/latest/dev/monitoring.html) in the *Amazon Kinesis Data Streams Developer Guide*).

Each Amazon Kinesis record includes a value, `ApproximateArrivalTimestamp`, that is set when a stream successfully receives and stores a record. This is commonly referred to as a server-side time stamp, whereas a client-side time stamp is set when a data producer creates or sends the record to a stream (a data producer is any data source putting data records into a stream, for example with [PutRecords](API_PutRecords.md)). The time stamp has millisecond precision. There are no guarantees about the time stamp accuracy, or that the time stamp is always increasing. For example, records in a shard or across a stream might have time stamps that are out of order.

This operation has a limit of five transactions per second per shard.

## Request Syntax
<a name="API_GetRecords_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "Limit": {{number}},
   "ShardIterator": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRecords_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DryRun](#API_GetRecords_RequestSyntax) **   <a name="Streams-GetRecords-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.
Type: Boolean
Required: No

 ** [Limit](#API_GetRecords_RequestSyntax) **   <a name="Streams-GetRecords-request-Limit"></a>
The maximum number of records to return. Specify a value of up to 10,000. If you specify a value that is greater than 10,000, [GetRecords](#API_GetRecords) throws `InvalidArgumentException`. The default value is 10,000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [ShardIterator](#API_GetRecords_RequestSyntax) **   <a name="Streams-GetRecords-request-ShardIterator"></a>
The position in the shard from which you want to start sequentially reading data records. A shard iterator specifies this position using the sequence number of a data record in the shard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** [StreamARN](#API_GetRecords_RequestSyntax) **   <a name="Streams-GetRecords-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_GetRecords_RequestSyntax) **   <a name="Streams-GetRecords-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

## Response Syntax
<a name="API_GetRecords_ResponseSyntax"></a>

```
{
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
   "MillisBehindLatest": number,
   "NextShardIterator": "string",
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
```

## Response Elements
<a name="API_GetRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChildShards](#API_GetRecords_ResponseSyntax) **   <a name="Streams-GetRecords-response-ChildShards"></a>
The list of the current shard's child shards, returned in the `GetRecords` API's response only when the end of the current shard is reached.
Type: Array of [ChildShard](API_ChildShard.md) objects

 ** [MillisBehindLatest](#API_GetRecords_ResponseSyntax) **   <a name="Streams-GetRecords-response-MillisBehindLatest"></a>
The number of milliseconds the [GetRecords](#API_GetRecords) response is from the tip of the stream, indicating how far behind current time the consumer is. A value of zero indicates that record processing is caught up, and there are no new records to process at this moment.
Type: Long
Valid Range: Minimum value of 0.

 ** [NextShardIterator](#API_GetRecords_ResponseSyntax) **   <a name="Streams-GetRecords-response-NextShardIterator"></a>
The next position in the shard from which to start sequentially reading data records. If set to `null`, the shard has been closed and the requested iterator does not return any more data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [Records](#API_GetRecords_ResponseSyntax) **   <a name="Streams-GetRecords-response-Records"></a>
The data records retrieved from the shard.
Type: Array of [Record](API_Record.md) objects

## Errors
<a name="API_GetRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** DryRunOperationException **
The request was rejected because the DryRun parameter was specified.
HTTP Status Code: 400

 ** ExpiredIteratorException **
The provided iterator exceeds the maximum age allowed.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** InternalFailureException **
The processing of the request failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSAccessDeniedException **
The ciphertext references a key that doesn't exist or that you don't have access to.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSDisabledException **
The request was rejected because the specified customer master key (CMK) isn't enabled.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSInvalidStateException **
The request was rejected because the state of the specified resource isn't valid for this request. For more information, see [How Key State Affects Use of a Customer Master Key](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSNotFoundException **
The request was rejected because the specified entity or resource can't be found.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSOptInRequired **
The AWS access key ID needs a subscription for the service.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** KMSThrottlingException **
The request was denied due to request throttling. For more information about throttling, see [Limits](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second) in the * AWS Key Management Service Developer Guide*.
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
<a name="API_GetRecords_Examples"></a>

### To get data from the shards in a stream
<a name="API_GetRecords_Example_1"></a>

The following JSON example gets data from the shards in a stream.

#### Sample Request
<a name="API_GetRecords_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.GetRecords
{
  "ShardIterator": "AAAAAAAAAAETYyAYzd665+8e0X7JTsASDM/Hr2rSwc0X2qz93iuA3udrjTH+ikQvpQk/1ZcMMLzRdAesqwBGPnsthzU0/CBlM/U8/8oEqGwX3pKw0XyeDNRAAZyXBo3MqkQtCpXhr942BRTjvWKhFz7OmCb2Ncfr8Tl2cBktooi6kJhr+djN5WYkB38Rr3akRgCl9qaU4dY=",
  "Limit": 25
}
```

#### Sample Response
<a name="API_GetRecords_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "MillisBehindLatest": 2100,
  "NextShardIterator": "AAAAAAAAAAHsW8zCWf9164uy8Epue6WS3w6wmj4a4USt+CNvMd6uXQ+HL5vAJMznqqC0DLKsIjuoiTi1BpT6nW0LN2M2D56zM5H8anHm30Gbri9ua+qaGgj+3XTyvbhpERfrezgLHbPB/rIcVpykJbaSj5tmcXYRmFnqZBEyHwtZYFmh6hvWVFkIwLuMZLMrpWhG5r5hzkE=",
  "Records": [
    {
      "Data": "XzxkYXRhPl8w",
      "PartitionKey": "partitionKey",
      "ApproximateArrivalTimestamp": 1.441215410867E9,
      "SequenceNumber": "21269319989652663814458848515492872193"
    }
  ]
}
```

## See Also
<a name="API_GetRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/GetRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/GetRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/GetRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/GetRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/GetRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/GetRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/GetRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/GetRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/GetRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/GetRecords)
