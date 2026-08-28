---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_StartDeliveryStreamEncryption.html
---

# StartDeliveryStreamEncryption
<a name="API_StartDeliveryStreamEncryption"></a>

Enables server-side encryption (SSE) for the Firehose stream.

This operation is asynchronous. It returns immediately. When you invoke it, Firehose first sets the encryption status of the stream to `ENABLING`, and then to `ENABLED`. The encryption status of a Firehose stream is the `Status` property in [DeliveryStreamEncryptionConfiguration](API_DeliveryStreamEncryptionConfiguration.md). If the operation fails, the encryption status changes to `ENABLING_FAILED`. You can continue to read and write data to your Firehose stream while the encryption status is `ENABLING`, but the data is not encrypted. It can take up to 5 seconds after the encryption status changes to `ENABLED` before all records written to the Firehose stream are encrypted. To find out whether a record or a batch of records was encrypted, check the response elements [PutRecord:Encrypted](API_PutRecord.md#Firehose-PutRecord-response-Encrypted) and [PutRecordBatch:Encrypted](API_PutRecordBatch.md#Firehose-PutRecordBatch-response-Encrypted), respectively.

To check the encryption status of a Firehose stream, use [DescribeDeliveryStream](API_DescribeDeliveryStream.md).

Even if encryption is currently enabled for a Firehose stream, you can still invoke this operation on it to change the ARN of the CMK or both its type and ARN. If you invoke this method to change the CMK, and the old CMK is of type `CUSTOMER_MANAGED_CMK`, Firehose schedules the grant it had on the old CMK for retirement. If the new CMK is of type `CUSTOMER_MANAGED_CMK`, Firehose creates a grant that enables it to use the new CMK to encrypt and decrypt data and to manage the grant.

For the KMS grant creation to be successful, the Firehose API operations `StartDeliveryStreamEncryption` and `CreateDeliveryStream` should not be called with session credentials that are more than 6 hours old.

If a Firehose stream already has encryption enabled and then you invoke this operation to change the ARN of the CMK or both its type and ARN and you get `ENABLING_FAILED`, this only means that the attempt to change the CMK failed. In this case, encryption remains enabled with the old CMK.

If the encryption status of your Firehose stream is `ENABLING_FAILED`, you can invoke this operation again with a valid CMK. The CMK must be enabled and the key policy mustn't explicitly deny the permission for Firehose to invoke KMS encrypt and decrypt operations.

You can enable SSE for a Firehose stream only if it's a Firehose stream that uses `DirectPut` as its source.

The `StartDeliveryStreamEncryption` and `StopDeliveryStreamEncryption` operations have a combined limit of 25 calls per Firehose stream per 24 hours. For example, you reach the limit if you call `StartDeliveryStreamEncryption` 13 times and `StopDeliveryStreamEncryption` 12 times for the same Firehose stream in a 24-hour period.

## Request Syntax
<a name="API_StartDeliveryStreamEncryption_RequestSyntax"></a>

```
{
   "DeliveryStreamEncryptionConfigurationInput": {
      "KeyARN": "{{string}}",
      "KeyType": "{{string}}"
   },
   "DeliveryStreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartDeliveryStreamEncryption_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeliveryStreamEncryptionConfigurationInput](#API_StartDeliveryStreamEncryption_RequestSyntax) **   <a name="Firehose-StartDeliveryStreamEncryption-request-DeliveryStreamEncryptionConfigurationInput"></a>
Used to specify the type and Amazon Resource Name (ARN) of the KMS key needed for Server-Side Encryption (SSE).
Type: [DeliveryStreamEncryptionConfigurationInput](API_DeliveryStreamEncryptionConfigurationInput.md) object
Required: No

 ** [DeliveryStreamName](#API_StartDeliveryStreamEncryption_RequestSyntax) **   <a name="Firehose-StartDeliveryStreamEncryption-request-DeliveryStreamName"></a>
The name of the Firehose stream for which you want to enable server-side encryption (SSE).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Elements
<a name="API_StartDeliveryStreamEncryption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartDeliveryStreamEncryption_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgumentException **
The specified input parameter has a value that is not valid.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** InvalidKMSResourceException **
Firehose throws this exception when an attempt to put records or to start or stop Firehose stream encryption fails. This happens when the KMS service throws one of the following exception types: `AccessDeniedException`, `InvalidStateException`, `DisabledException`, or `NotFoundException`.
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
<a name="API_StartDeliveryStreamEncryption_Examples"></a>

### To start server-side encryption for a stream
<a name="API_StartDeliveryStreamEncryption_Example_1"></a>

The following JSON example starts server-side encryption (SSE) for the specified stream.

#### Sample Request
<a name="API_StartDeliveryStreamEncryption_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: firehose.<region>.<domain>
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Authorization: <AuthParams>
Connection: Keep-Alive
X-Amz-Date: <Date>
X-Amz-Target: Firehose_20150804.StartDeliveryStreamEncryption
{
  "DeliveryStreamName": "exampleDeliveryStreamName"
}
```

#### Sample Response
<a name="API_StartDeliveryStreamEncryption_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_StartDeliveryStreamEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/firehose-2015-08-04/StartDeliveryStreamEncryption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/firehose-2015-08-04/StartDeliveryStreamEncryption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/StartDeliveryStreamEncryption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/firehose-2015-08-04/StartDeliveryStreamEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/StartDeliveryStreamEncryption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/firehose-2015-08-04/StartDeliveryStreamEncryption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/firehose-2015-08-04/StartDeliveryStreamEncryption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/firehose-2015-08-04/StartDeliveryStreamEncryption)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/firehose-2015-08-04/StartDeliveryStreamEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/StartDeliveryStreamEncryption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
