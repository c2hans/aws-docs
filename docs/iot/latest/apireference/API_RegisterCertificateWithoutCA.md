---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCertificateWithoutCA.html
---

# RegisterCertificateWithoutCA
<a name="API_RegisterCertificateWithoutCA"></a>

Register a certificate that does not have a certificate authority (CA). For supported certificates, consult [ Certificate signing algorithms supported by AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html#x509-cert-algorithms).

## Request Syntax
<a name="API_RegisterCertificateWithoutCA_RequestSyntax"></a>

```
POST /certificate/register-no-ca HTTP/1.1
Content-type: application/json

{
   "certificatePem": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterCertificateWithoutCA_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterCertificateWithoutCA_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificatePem](#API_RegisterCertificateWithoutCA_RequestSyntax) **   <a name="iot-RegisterCertificateWithoutCA-request-certificatePem"></a>
The certificate data, in PEM format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`
Required: Yes

 ** [status](#API_RegisterCertificateWithoutCA_RequestSyntax) **   <a name="iot-RegisterCertificateWithoutCA-request-status"></a>
The status of the register certificate request.
Type: String
Valid Values: `ACTIVE | INACTIVE | REVOKED | PENDING_TRANSFER | REGISTER_INACTIVE | PENDING_ACTIVATION`
Required: No

## Response Syntax
<a name="API_RegisterCertificateWithoutCA_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateArn": "string",
   "certificateId": "string"
}
```

## Response Elements
<a name="API_RegisterCertificateWithoutCA_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateArn](#API_RegisterCertificateWithoutCA_ResponseSyntax) **   <a name="iot-RegisterCertificateWithoutCA-response-certificateArn"></a>
The Amazon Resource Name (ARN) of the registered certificate.
Type: String

 ** [certificateId](#API_RegisterCertificateWithoutCA_ResponseSyntax) **   <a name="iot-RegisterCertificateWithoutCA-response-certificateId"></a>
The ID of the registered certificate. (The last part of the certificate ARN contains the certificate ID.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`

## Errors
<a name="API_RegisterCertificateWithoutCA_Errors"></a>

 ** CertificateStateException **
The certificate operation is not allowed.
 ** message **
The message for the exception.
HTTP Status Code: 406

 ** CertificateValidationException **
The certificate is invalid.
 ** message **
Additional information about the exception.
HTTP Status Code: 400

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

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

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
<a name="API_RegisterCertificateWithoutCA_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/RegisterCertificateWithoutCA)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/RegisterCertificateWithoutCA)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RegisterCertificateWithoutCA)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/RegisterCertificateWithoutCA)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RegisterCertificateWithoutCA)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/RegisterCertificateWithoutCA)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/RegisterCertificateWithoutCA)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/RegisterCertificateWithoutCA)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/RegisterCertificateWithoutCA)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RegisterCertificateWithoutCA)
