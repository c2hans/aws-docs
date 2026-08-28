---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html
---

# PutRecords
<a name="API_PutRecords"></a>

Writes multiple data records into a Kinesis data stream in a single call (also referred to as a `PutRecords` request). Use this operation to send data into the stream for data ingestion and processing.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

Each `PutRecords` request can support up to 500 records. Each record in the request can be as large as 10 MiB, up to a limit of 10 MiB for the entire request, including partition keys. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second.

You must specify the name of the stream that captures, stores, and transports the data; and an array of request `Records`, with each record in the array requiring a partition key and data blob. The record size limit applies to the total size of the partition key and data blob.

The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on.

The partition key is used by Kinesis Data Streams as input to a hash function that maps the partition key and associated data to a specific shard. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream. For more information, see [Adding Data to a Stream](https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-add-data-to-stream) in the *Amazon Kinesis Data Streams Developer Guide*.

Each record in the `Records` array may include an optional parameter, `ExplicitHashKey`, which overrides the partition key to shard mapping. This parameter allows a data producer to determine explicitly the shard where the record is stored. For more information, see [Adding Multiple Records with PutRecords](https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-putrecords) in the *Amazon Kinesis Data Streams Developer Guide*.

The `PutRecords` response includes an array of response `Records`. Each record in the response array directly correlates with a record in the request array using natural ordering, from the top to the bottom of the request and response. The response `Records` array always includes the same number of records as the request array.

The response `Records` array includes both successfully and unsuccessfully processed records. Kinesis Data Streams attempts to process all records in each `PutRecords` request. A single record failure does not stop the processing of subsequent records. As a result, PutRecords doesn't guarantee the ordering of records. If you need to read records in the same order they are written to the stream, use [PutRecord](API_PutRecord.md) instead of `PutRecords`, and write to the same shard.

A successfully processed record includes `ShardId` and `SequenceNumber` values. The `ShardId` parameter identifies the shard in the stream where the record is stored. The `SequenceNumber` parameter is an identifier assigned to the put record, unique to all records in the stream.

An unsuccessfully processed record includes `ErrorCode` and `ErrorMessage` values. `ErrorCode` reflects the type of error and can be one of the following values: `ProvisionedThroughputExceededException` or `InternalFailure`. `ErrorMessage` provides more detailed information about the `ProvisionedThroughputExceededException` exception including the account ID, stream name, and shard ID of the record that was throttled. For more information about partially successful responses, see [Adding Multiple Records with PutRecords](https://docs.aws.amazon.com/kinesis/latest/dev/kinesis-using-sdk-java-add-data-to-stream.html#kinesis-using-sdk-java-putrecords) in the *Amazon Kinesis Data Streams Developer Guide*.

**Important**
After you write a record to a stream, you cannot modify that record or its order within the stream.

By default, data records are accessible for 24 hours from the time that they are added to a stream. You can use [IncreaseStreamRetentionPeriod](API_IncreaseStreamRetentionPeriod.md) or [DecreaseStreamRetentionPeriod](API_DecreaseStreamRetentionPeriod.md) to modify this retention period.

## Request Syntax
<a name="API_PutRecords_RequestSyntax"></a>

```
{
   "Records": [
      {
         "Data": {{blob}},
         "ExplicitHashKey": "{{string}}",
         "PartitionKey": "{{string}}"
      }
   ],
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutRecords_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Records](#API_PutRecords_RequestSyntax) **   <a name="Streams-PutRecords-request-Records"></a>
The records associated with the request.
Type: Array of [PutRecordsRequestEntry](API_PutRecordsRequestEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: Yes

 ** [StreamARN](#API_PutRecords_RequestSyntax) **   <a name="Streams-PutRecords-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_PutRecords_RequestSyntax) **   <a name="Streams-PutRecords-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_PutRecords_RequestSyntax) **   <a name="Streams-PutRecords-request-StreamName"></a>
The stream name associated with the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_PutRecords_ResponseSyntax"></a>

```
{
   "EncryptionType": "string",
   "FailedRecordCount": number,
   "Records": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "SequenceNumber": "string",
         "ShardId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_PutRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EncryptionType](#API_PutRecords_ResponseSyntax) **   <a name="Streams-PutRecords-response-EncryptionType"></a>
The encryption type used on the records. This parameter can be one of the following values:
+  `NONE`: Do not encrypt the records.
+  `KMS`: Use server-side encryption on the records using a customer-managed AWS KMS key.
Type: String
Valid Values: `NONE | KMS`

 ** [FailedRecordCount](#API_PutRecords_ResponseSyntax) **   <a name="Streams-PutRecords-response-FailedRecordCount"></a>
The number of unsuccessfully processed records in a `PutRecords` request.
Type: Integer
Valid Range: Minimum value of 1.

 ** [Records](#API_PutRecords_ResponseSyntax) **   <a name="Streams-PutRecords-response-Records"></a>
An array of successfully and unsuccessfully processed record results. A record that is successfully added to a stream includes `SequenceNumber` and `ShardId` in the result. A record that fails to be added to a stream includes `ErrorCode` and `ErrorMessage` in the result.
Type: Array of [PutRecordsResultEntry](API_PutRecordsResultEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.

## Errors
<a name="API_PutRecords_Errors"></a>

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
<a name="API_PutRecords_Examples"></a>

### To add data to a stream, with complete success
<a name="API_PutRecords_Example_1"></a>

The following JSON example adds data to the specified stream with a successful response.

#### Sample Request
<a name="API_PutRecords_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.PutRecords
{
    "Records": [
        {
            "Data": "XzxkYXRhPl8x",
            "PartitionKey": "partitionKey1"
        },
        {
            "Data": "f1PxFQo92Afh",
            "PartitionKey": "partitionKey2"
        },
        {
            "Data": "Gi4sEdd08HypA",
            "PartitionKey": "partitionKey3"
        }
    ],
    "StreamName": "exampleStreamName"
}
```

#### Sample Response
<a name="API_PutRecords_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "FailedRecordCount": 0,
    "Records": [
        {
            "SequenceNumber": "49543463076548007577105092703039560359975228518395019266",
            "ShardId": "shardId-000000000000"
        },
        {
            "SequenceNumber": "49543463076570308322303623326179887152428262250726293522",
            "ShardId": "shardId-000000000001"
        },
        {
            "SequenceNumber": "49543463076570308322303623326179887152428262250726293588",
            "ShardId": "shardId-000000000003"
        }
    ]
}
```

### To add data to a stream, with a partially successful response
<a name="API_PutRecords_Example_2"></a>

The following JSON example adds data to the specified stream with a partially successful response and contains failed records.

#### Sample Request
<a name="API_PutRecords_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: kinesis.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Kinesis_20131202.PutRecords
{
    "Records": [
        {
            "Data": "XzxkYXRhPl8x",
            "PartitionKey": "partitionKey1"
        },
        {
            "Data": "f1PxFQo92Afh",
            "PartitionKey": "partitionKey2"
        },
        {
            "Data": "Gi4sEdd08HypA",
            "PartitionKey": "partitionKey3"
        }
    ],
    "StreamName": "exampleStreamName"
}
```

#### Sample Response
<a name="API_PutRecords_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "FailedRecordCount": 2,
    "Records": [
        {
            "SequenceNumber": "49543463076548007577105092703039560359975228518395012686",
            "ShardId": "shardId-000000000000"
        },
        {
            "ErrorCode": "ProvisionedThroughputExceededException",
            "ErrorMessage": "Rate exceeded for shard shardId-000000000001 in stream exampleStreamName under account 111111111111."
        },
        {
            "ErrorCode": "InternalFailure",
            "ErrorMessage": "Internal service failure."
        }
    ]
}
```

## See Also
<a name="API_PutRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/PutRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/PutRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/PutRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/PutRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/PutRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/PutRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/PutRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/PutRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/PutRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/PutRecords)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
