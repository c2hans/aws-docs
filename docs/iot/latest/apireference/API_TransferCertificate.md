---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TransferCertificate.html
---

# TransferCertificate
<a name="API_TransferCertificate"></a>

Transfers the specified certificate to the specified AWS account.

Requires permission to access the [TransferCertificate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

You can cancel the transfer until it is accepted by the recipient.

No notification is sent to the transfer destination's account. The caller is responsible for notifying the transfer target.

The certificate being transferred must not be in the `ACTIVE` state. You can use the [UpdateCertificate](API_UpdateCertificate.md) action to deactivate it.

The certificate must not have any policies attached to it. You can use the [DetachPolicy](API_DetachPolicy.md) action to detach them.

 **Customer managed key behavior:** When you use a customer managed key to encrypt your data and then transfer the certificate to a customer in a different account using the `TransferCertificate` operation, the certificates will no longer be encrypted by their customer managed key configuration. During the transfer process, certificates are encrypted using AWS IoT Core owned keys.

While a certificate is in the **PENDING\_TRANSFER** state, it's always protected by AWS IoT Core owned keys, regardless of the customer managed key configuration of either the source or destination account.

Once the transfer is completed through [AcceptCertificateTransfer](API_AcceptCertificateTransfer.md), [RejectCertificateTransfer](API_RejectCertificateTransfer.md), or [CancelCertificateTransfer](API_CancelCertificateTransfer.md), the certificate will be protected by the customer managed key configuration of the account that owns the certificate after the transfer operation:
+ If the transfer is accepted: The certificate is encrypted by the target account's customer managed key configuration.
+ If the transfer is rejected or cancelled: The certificate is protected by the source account's customer managed key configuration.

## Request Syntax
<a name="API_TransferCertificate_RequestSyntax"></a>

```
PATCH /transfer-certificate/{{certificateId}}?targetAwsAccount={{targetAwsAccount}} HTTP/1.1
Content-type: application/json

{
   "transferMessage": "{{string}}"
}
```

## URI Request Parameters
<a name="API_TransferCertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificateId](#API_TransferCertificate_RequestSyntax) **   <a name="iot-TransferCertificate-request-uri-certificateId"></a>
The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: Yes

 ** [targetAwsAccount](#API_TransferCertificate_RequestSyntax) **   <a name="iot-TransferCertificate-request-uri-targetAwsAccount"></a>
The AWS account.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_TransferCertificate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [transferMessage](#API_TransferCertificate_RequestSyntax) **   <a name="iot-TransferCertificate-request-transferMessage"></a>
The transfer message.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_TransferCertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "transferredCertificateArn": "string"
}
```

## Response Elements
<a name="API_TransferCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [transferredCertificateArn](#API_TransferCertificate_ResponseSyntax) **   <a name="iot-TransferCertificate-response-transferredCertificateArn"></a>
The ARN of the certificate.
Type: String

## Errors
<a name="API_TransferCertificate_Errors"></a>

 ** CertificateStateException **
The certificate operation is not allowed.
 ** message **
The message for the exception.
HTTP Status Code: 406

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** TransferConflictException **
You can't transfer the certificate because authorization policies are still attached.
 ** message **
The message for the exception.
HTTP Status Code: 409

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_TransferCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/TransferCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/TransferCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TransferCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/TransferCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TransferCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/TransferCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/TransferCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/TransferCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/TransferCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TransferCertificate)
