---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html
---

# PutRecordBatch
<a name="API_PutRecordBatch"></a>

Writes multiple data records into a Firehose stream in a single call, which can achieve higher throughput per producer than when writing single records. To write single data records into a Firehose stream, use [PutRecord](API_PutRecord.md). Applications using these operations are referred to as producers.

Firehose accumulates and publishes a particular metric for a customer account in one minute intervals. It is possible that the bursts of incoming bytes/records ingested to a Firehose stream last only for a few seconds. Due to this, the actual spikes in the traffic might not be fully visible in the customer's 1 minute CloudWatch metrics.

For information about service quota, see [Amazon Firehose Quota](https://docs.aws.amazon.com/firehose/latest/dev/limits.html).

Each [PutRecordBatch](#API_PutRecordBatch) request supports up to 500 records. Each record in the request can be as large as 1,000 KB (before base64 encoding), up to a limit of 4 MB for the entire request. These limits cannot be changed.

You must specify the name of the Firehose stream and the data record when using [PutRecord](API_PutRecord.md). The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data. For example, it could be a segment from a log file, geographic location data, website clickstream data, and so on.

For multi record de-aggregation, you can not put more than 500 records even if the data blob length is less than 1000 KiB. If you include more than 500 records, the request succeeds but the record de-aggregation doesn't work as expected and transformation lambda is invoked with the complete base64 encoded data blob instead of de-aggregated base64 decoded records.

Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (`\n`) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination.

The [PutRecordBatch](#API_PutRecordBatch) response includes a count of failed records, `FailedPutCount`, and an array of responses, `RequestResponses`. Even if the [PutRecordBatch](#API_PutRecordBatch) call succeeds, the value of `FailedPutCount` may be greater than 0, indicating that there are records for which the operation didn't succeed. Each entry in the `RequestResponses` array provides additional information about the processed record. It directly correlates with a record in the request array using the same ordering, from the top to the bottom. The response array always includes the same number of records as the request array. `RequestResponses` includes both successfully and unsuccessfully processed records. Firehose tries to process all records in each [PutRecordBatch](#API_PutRecordBatch) request. A single record failure does not stop the processing of subsequent records.

A successfully processed record includes a `RecordId` value, which is unique for the record. An unsuccessfully processed record includes `ErrorCode` and `ErrorMessage` values. `ErrorCode` reflects the type of error, and is one of the following values: `ServiceUnavailableException` or `InternalFailure`. `ErrorMessage` provides more detailed information about the error.

If there is an internal server error or a timeout, the write might have completed or it might have failed. If `FailedPutCount` is greater than 0, retry the request, resending only those records that might have failed processing. This minimizes the possible duplicate records and also reduces the total bytes sent (and corresponding charges). We recommend that you handle any duplicates at the destination.

If [PutRecordBatch](#API_PutRecordBatch) throws `ServiceUnavailableException`, the API is automatically reinvoked (retried) 3 times. If the exception persists, it is possible that the throughput limits have been exceeded for the Firehose stream.

Re-invoking the Put API operations (for example, PutRecord and PutRecordBatch) can result in data duplicates. For larger data assets, allow for a longer time out before retrying Put API operations.

Data records sent to Firehose are stored for 24 hours from the time they are added to a Firehose stream as it attempts to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.

**Important**
Don't concatenate two or more base64 strings to form the data fields of your records. Instead, concatenate the raw data, then perform base64 encoding.

## Request Syntax
<a name="API_PutRecordBatch_RequestSyntax"></a>

```
{
   "DeliveryStreamName": "{{string}}",
   "Records": [
      {
         "Data": {{blob}}
      }
   ]
}
```

## Request Parameters
<a name="API_PutRecordBatch_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeliveryStreamName](#API_PutRecordBatch_RequestSyntax) **   <a name="Firehose-PutRecordBatch-request-DeliveryStreamName"></a>
The name of the Firehose stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Records](#API_PutRecordBatch_RequestSyntax) **   <a name="Firehose-PutRecordBatch-request-Records"></a>
One or more records.
Type: Array of [Record](API_Record.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: Yes

## Response Syntax
<a name="API_PutRecordBatch_ResponseSyntax"></a>

```
{
   "Encrypted": boolean,
   "FailedPutCount": number,
   "RequestResponses": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "RecordId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_PutRecordBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Encrypted](#API_PutRecordBatch_ResponseSyntax) **   <a name="Firehose-PutRecordBatch-response-Encrypted"></a>
Indicates whether server-side encryption (SSE) was enabled during this operation.
Type: Boolean

 ** [FailedPutCount](#API_PutRecordBatch_ResponseSyntax) **   <a name="Firehose-PutRecordBatch-response-FailedPutCount"></a>
The number of records that might have failed processing. This number might be greater than 0 even if the [PutRecordBatch](#API_PutRecordBatch) call succeeds. Check `FailedPutCount` to determine whether there are records that you need to resend.
Type: Integer
Valid Range: Minimum value of 0.

 ** [RequestResponses](#API_PutRecordBatch_ResponseSyntax) **   <a name="Firehose-PutRecordBatch-response-RequestResponses"></a>
The results array. For each record, the index of the response element is the same as the index used in the request array.
Type: Array of [PutRecordBatchResponseEntry](API_PutRecordBatchResponseEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.

## Errors
<a name="API_PutRecordBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgumentException **
The specified input parameter has a value that is not valid.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** InvalidKMSResourceException **
Firehose throws this exception when an attempt to put records or to start or stop Firehose stream encryption fails. This happens when the KMS service throws one of the following exception types: `AccessDeniedException`, `InvalidStateException`, `DisabledException`, or `NotFoundException`.
HTTP Status Code: 400

 ** InvalidSourceException **
Only requests from CloudWatch Logs are supported when CloudWatch Logs decompression is enabled.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service is unavailable. Back off and retry the operation. If you continue to see the exception, throughput limits for the Firehose stream may have been exceeded. For more information about limits and how to request an increase, see [Amazon Firehose Limits](https://docs.aws.amazon.com/firehose/latest/dev/limits.html).
 ** message **
A message that provides information about the error.
HTTP Status Code: 500

## Examples
<a name="API_PutRecordBatch_Examples"></a>

### Example
<a name="API_PutRecordBatch_Example_1"></a>

The following JSON puts two records in the Firehose stream named `some_delivery_stream`:

#### Sample Request
<a name="API_PutRecordBatch_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.PutRecordBatch
{
   "DeliveryStreamName": "some_delivery_stream",
   "Records": [
      {
         "Data": "Some data blob."
      },
      {
         "Data": "Another blob of data."
      }
   ]
}
```

#### Sample Response
<a name="API_PutRecordBatch_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "FailedPutCount": 0,
    "RequestResponses": [
        {
            "RecordId": "AJJBALlfiFN9HyhPj6Dc+XqcRlTjqyIbr927TsEmWWpN39EK/JbRTbXDZFNCCrWIs/4YUd3gjYUs6giZn76TuI4vv0ljDOMFJvLzqLuupu93RscZRmpW1CP8DeiFzJJGvqIr1LRE/MDozYenOz+v1ZIqEjECvfMwIz6silvDaGuYtIhVzwd8yWaDGFCX4ODes6W07W9W7Q5ViMPUKSt6F0nn7OhVkJ3/"
        },
        {
            "RecordId": "goGaFS919Mmv7lYET0oMaw+UL9iFpzi1O0o+csoIc31SmvkqpwzQuT0RPqZ7QqfR1FJ+HxJciW/8paFMWPByJ6qVDhiE7TtJxARKaP4YDccvWHXhD7x6Y4bc9AHZ0uzy+BEuTTnH5Zsip1IrEPgu8lj8a7fd6sluTe/kZ54GVG+Sc105IrxIu08kPbRiUTWL+Wg0A3HzOQeePqokRKKqmoXLG0pzx/8O"
        }
    ]
}
```

## See Also
<a name="API_PutRecordBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/PutRecordBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/PutRecordBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/PutRecordBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/PutRecordBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/PutRecordBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/PutRecordBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/PutRecordBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/PutRecordBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/PutRecordBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/PutRecordBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
