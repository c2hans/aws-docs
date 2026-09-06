---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCertificate.html
---

# UpdateCertificate
<a name="API_UpdateCertificate"></a>

Updates the status of the specified certificate. This operation is idempotent.

Requires permission to access the [UpdateCertificate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

Certificates must be in the ACTIVE state to authenticate devices that use a certificate to connect to AWS IoT.

Within a few minutes of updating a certificate from the ACTIVE state to any other state, AWS IoT disconnects all devices that used that certificate to connect. Devices cannot use a certificate that is not in the ACTIVE state to reconnect.

## Request Syntax
<a name="API_UpdateCertificate_RequestSyntax"></a>

```
PUT /certificates/{{certificateId}}?newStatus={{newStatus}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UpdateCertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificateId](#API_UpdateCertificate_RequestSyntax) **   <a name="iot-UpdateCertificate-request-uri-certificateId"></a>
The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: Yes

 ** [newStatus](#API_UpdateCertificate_RequestSyntax) **   <a name="iot-UpdateCertificate-request-uri-newStatus"></a>
The new status.
 **Note:** Setting the status to PENDING\_TRANSFER or PENDING\_ACTIVATION will result in an exception being thrown. PENDING\_TRANSFER and PENDING\_ACTIVATION are statuses used internally by AWS IoT. They are not intended for developer use.
 **Note:** The status value REGISTER\_INACTIVE is deprecated and should not be used.
Valid Values: `ACTIVE | INACTIVE | REVOKED | PENDING_TRANSFER | REGISTER_INACTIVE | PENDING_ACTIVATION`
Required: Yes

## Request Body
<a name="API_UpdateCertificate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UpdateCertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCertificate_Errors"></a>

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

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_UpdateCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateCertificate)
