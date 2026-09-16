---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_StopDeliveryStreamEncryption.html
---

# StopDeliveryStreamEncryption
<a name="API_StopDeliveryStreamEncryption"></a>

Disables server-side encryption (SSE) for the Firehose stream.

This operation is asynchronous. It returns immediately. When you invoke it, Firehose first sets the encryption status of the stream to `DISABLING`, and then to `DISABLED`. You can continue to read and write data to your stream while its status is `DISABLING`. It can take up to 5 seconds after the encryption status changes to `DISABLED` before all records written to the Firehose stream are no longer subject to encryption. To find out whether a record or a batch of records was encrypted, check the response elements [PutRecord:Encrypted](API_PutRecord.md#Firehose-PutRecord-response-Encrypted) and [PutRecordBatch:Encrypted](API_PutRecordBatch.md#Firehose-PutRecordBatch-response-Encrypted), respectively.

To check the encryption state of a Firehose stream, use [DescribeDeliveryStream](API_DescribeDeliveryStream.md).

If SSE is enabled using a customer managed CMK and then you invoke `StopDeliveryStreamEncryption`, Firehose schedules the related KMS grant for retirement and then retires it after it ensures that it is finished delivering records to the destination.

The `StartDeliveryStreamEncryption` and `StopDeliveryStreamEncryption` operations have a combined limit of 25 calls per Firehose stream per 24 hours. For example, you reach the limit if you call `StartDeliveryStreamEncryption` 13 times and `StopDeliveryStreamEncryption` 12 times for the same Firehose stream in a 24-hour period.

## Request Syntax
<a name="API_StopDeliveryStreamEncryption_RequestSyntax"></a>

```
{
   "DeliveryStreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_StopDeliveryStreamEncryption_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeliveryStreamName](#API_StopDeliveryStreamEncryption_RequestSyntax) **   <a name="Firehose-StopDeliveryStreamEncryption-request-DeliveryStreamName"></a>
The name of the Firehose stream for which you want to disable server-side encryption (SSE).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Elements
<a name="API_StopDeliveryStreamEncryption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopDeliveryStreamEncryption_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgumentException **
The specified input parameter has a value that is not valid.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** LimitExceededException **
You have already reached the limit for a requested resource.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is already in use and not available for this operation.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## Examples
<a name="API_StopDeliveryStreamEncryption_Examples"></a>

### To stop server-side encryption for a stream
<a name="API_StopDeliveryStreamEncryption_Example_1"></a>

The following JSON example stops server-side encryption (SSE) for the specified stream.

#### Sample Request
<a name="API_StopDeliveryStreamEncryption_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.StopDeliveryStreamEncryption
{
  "DeliveryStreamName": "exampleDeliveryStreamName"
}
```

#### Sample Response
<a name="API_StopDeliveryStreamEncryption_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_StopDeliveryStreamEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/StopDeliveryStreamEncryption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/StopDeliveryStreamEncryption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/StopDeliveryStreamEncryption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/StopDeliveryStreamEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/StopDeliveryStreamEncryption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/StopDeliveryStreamEncryption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/StopDeliveryStreamEncryption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/StopDeliveryStreamEncryption)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/StopDeliveryStreamEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/StopDeliveryStreamEncryption)
