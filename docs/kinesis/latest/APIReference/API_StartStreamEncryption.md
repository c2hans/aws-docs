---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StartStreamEncryption.html
---

# StartStreamEncryption
<a name="API_StartStreamEncryption"></a>

Enables or updates server-side encryption using an AWS KMS key for a specified stream.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

Starting encryption is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to `UPDATING`. After the update is complete, Kinesis Data Streams sets the status of the stream back to `ACTIVE`. Updating or applying encryption normally takes a few seconds to complete, but it can take minutes. You can continue to read and write data to your stream while its status is `UPDATING`. Once the status of the stream is `ACTIVE`, encryption begins for records written to the stream.

API Limits: You can successfully apply a new AWS KMS key for server-side encryption 25 times in a rolling 24-hour period.

Note: It can take up to 5 seconds after the stream is in an `ACTIVE` status before all records written to the stream are encrypted. After you enable encryption, you can verify that encryption is applied by inspecting the API response from `PutRecord` or `PutRecords`.

## Request Syntax
<a name="API_StartStreamEncryption_RequestSyntax"></a>

```
{
   "EncryptionType": "{{string}}",
   "KeyId": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartStreamEncryption_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [EncryptionType](#API_StartStreamEncryption_RequestSyntax) **   <a name="Streams-StartStreamEncryption-request-EncryptionType"></a>
The encryption type to use. The only valid value is `KMS`.
Type: String
Valid Values: `KMS`
Required: Yes

 ** [KeyId](#API_StartStreamEncryption_RequestSyntax) **   <a name="Streams-StartStreamEncryption-request-KeyId"></a>
The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias `aws/kinesis`.
+ Key ARN example: `arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012`
+ Alias ARN example: `arn:aws:kms:us-east-1:123456789012:alias/MyAliasName`
+ Globally unique key ID example: `12345678-1234-1234-1234-123456789012`
+ Alias name example: `alias/MyAliasName`
+ Master key owned by Kinesis Data Streams: `alias/aws/kinesis`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [StreamARN](#API_StartStreamEncryption_RequestSyntax) **   <a name="Streams-StartStreamEncryption-request-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_StartStreamEncryption_RequestSyntax) **   <a name="Streams-StartStreamEncryption-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_StartStreamEncryption_RequestSyntax) **   <a name="Streams-StartStreamEncryption-request-StreamName"></a>
The name of the stream for which to start encrypting records.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Elements
<a name="API_StartStreamEncryption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartStreamEncryption_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

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
<a name="API_StartStreamEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/StartStreamEncryption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/StartStreamEncryption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/StartStreamEncryption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/StartStreamEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/StartStreamEncryption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/StartStreamEncryption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/StartStreamEncryption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/StartStreamEncryption)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/StartStreamEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/StartStreamEncryption)
