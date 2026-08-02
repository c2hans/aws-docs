---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecord.html
---

# PutRecord
<a name="API_PutRecord"></a>

Writes a single data record into an Firehose stream. To write multiple data records into a Firehose stream, use [PutRecordBatch](API_PutRecordBatch.md). Applications using these operations are referred to as producers.

By default, each Firehose stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. If you use [PutRecord](#API_PutRecord) and [PutRecordBatch](API_PutRecordBatch.md), the limits are an aggregate across these two operations for each Firehose stream. For more information about limits and how to request an increase, see [Amazon Firehose Limits](https://docs.aws.amazon.com/firehose/latest/dev/limits.html).

Firehose accumulates and publishes a particular metric for a customer account in one minute intervals. It is possible that the bursts of incoming bytes/records ingested to a Firehose stream last only for a few seconds. Due to this, the actual spikes in the traffic might not be fully visible in the customer's 1 minute CloudWatch metrics.

You must specify the name of the Firehose stream and the data record when using [PutRecord](#API_PutRecord). The data record consists of a data blob that can be up to 1,000 KiB in size, and any kind of data. For example, it can be a segment from a log file, geographic location data, website clickstream data, and so on.

For multi record de-aggregation, you can not put more than 500 records even if the data blob length is less than 1000 KiB. If you include more than 500 records, the request succeeds but the record de-aggregation doesn't work as expected and transformation lambda is invoked with the complete base64 encoded data blob instead of de-aggregated base64 decoded records.

Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (`\n`) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination.

The `PutRecord` operation returns a `RecordId`, which is a unique string assigned to each record. Producer applications can use this ID for purposes such as auditability and investigation.

If the `PutRecord` operation throws a `ServiceUnavailableException`, the API is automatically reinvoked (retried) 3 times. If the exception persists, it is possible that the throughput limits have been exceeded for the Firehose stream.

Re-invoking the Put API operations (for example, PutRecord and PutRecordBatch) can result in data duplicates. For larger data assets, allow for a longer time out before retrying Put API operations.

Data records sent to Firehose are stored for 24 hours from the time they are added to a Firehose stream as it tries to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.

**Important**
Don't concatenate two or more base64 strings to form the data fields of your records. Instead, concatenate the raw data, then perform base64 encoding.

## Request Syntax
<a name="API_PutRecord_RequestSyntax"></a>

```
{
   "DeliveryStreamName": "{{string}}",
   "Record": {
      "Data": {{blob}}
   }
}
```

## Request Parameters
<a name="API_PutRecord_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeliveryStreamName](#API_PutRecord_RequestSyntax) **   <a name="Firehose-PutRecord-request-DeliveryStreamName"></a>
The name of the Firehose stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Record](#API_PutRecord_RequestSyntax) **   <a name="Firehose-PutRecord-request-Record"></a>
The record.
Type: [Record](API_Record.md) object
Required: Yes

## Response Syntax
<a name="API_PutRecord_ResponseSyntax"></a>

```
{
   "Encrypted": boolean,
   "RecordId": "string"
}
```

## Response Elements
<a name="API_PutRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Encrypted](#API_PutRecord_ResponseSyntax) **   <a name="Firehose-PutRecord-response-Encrypted"></a>
Indicates whether server-side encryption (SSE) was enabled during this operation.
Type: Boolean

 ** [RecordId](#API_PutRecord_ResponseSyntax) **   <a name="Firehose-PutRecord-response-RecordId"></a>
The ID of the record.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_PutRecord_Errors"></a>

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
<a name="API_PutRecord_Examples"></a>

### Example
<a name="API_PutRecord_Example_1"></a>

The following JSON puts a record in the Firehose stream named `some_delivery_stream`:

#### Sample Request
<a name="API_PutRecord_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.PutRecord
{
    "DeliveryStreamName": "some_delivery_stream",
    "Record": {
        "Data": "..."
    }
}
```

#### Sample Response
<a name="API_PutRecord_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "RecordId": "CGojNMJq3msHbGoc+1mgSpifCmfFm7lFhuts//4Ft6sFVokyE6t+5ioEAjNm+sgQ6iVf/YePEXBK6epIW4QeXqJp2xsbfZUNXsfOY1QrYXgRBCKznkjMMTP0BqJGObM3fB//dHgEE0XDTc4wW065i/tJyYI1Vy8qn8FMhpkZuh5bvG482XkkBxFmMGnhPTQwQ4A1IOP0sE0X99YnBK8RECdeQ2zxynvZ"
}
```

### Example
<a name="API_PutRecord_Example_2"></a>

The following example shows how you can use the [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/firehose/put-record.html) to put a record in a Firehose stream.

```
aws firehose put-record --delivery-stream-name mystream --record="{\"Data\":\"1\"}"
```

## See Also
<a name="API_PutRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/PutRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/PutRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/PutRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/PutRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/PutRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/PutRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/PutRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/PutRecord)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/PutRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/PutRecord)
