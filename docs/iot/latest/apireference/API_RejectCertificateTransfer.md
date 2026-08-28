---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RejectCertificateTransfer.html
---

# RejectCertificateTransfer
<a name="API_RejectCertificateTransfer"></a>

Rejects a pending certificate transfer. After AWS IoT rejects a certificate transfer, the certificate status changes from **PENDING\_TRANSFER** to **INACTIVE**.

To check for pending certificate transfers, call [ListCertificates](API_ListCertificates.md) to enumerate your certificates.

This operation can only be called by the transfer destination. After it is called, the certificate will be returned to the source's account in the INACTIVE state.

Requires permission to access the [RejectCertificateTransfer](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_RejectCertificateTransfer_RequestSyntax"></a>

```
PATCH /reject-certificate-transfer/{{certificateId}} HTTP/1.1
Content-type: application/json

{
   "rejectReason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RejectCertificateTransfer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificateId](#API_RejectCertificateTransfer_RequestSyntax) **   <a name="iot-RejectCertificateTransfer-request-uri-certificateId"></a>
The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: Yes

## Request Body
<a name="API_RejectCertificateTransfer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [rejectReason](#API_RejectCertificateTransfer_RequestSyntax) **   <a name="iot-RejectCertificateTransfer-request-rejectReason"></a>
The reason the certificate transfer was rejected.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_RejectCertificateTransfer_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_RejectCertificateTransfer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RejectCertificateTransfer_Errors"></a>

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

 ** TransferAlreadyCompletedException **
You can't revert the certificate transfer because the transfer is already complete.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_RejectCertificateTransfer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/RejectCertificateTransfer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/RejectCertificateTransfer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RejectCertificateTransfer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/RejectCertificateTransfer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RejectCertificateTransfer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/RejectCertificateTransfer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/RejectCertificateTransfer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/RejectCertificateTransfer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/RejectCertificateTransfer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RejectCertificateTransfer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
