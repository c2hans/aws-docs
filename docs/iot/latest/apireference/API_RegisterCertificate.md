---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCertificate.html
---

# RegisterCertificate
<a name="API_RegisterCertificate"></a>

Registers a device certificate with AWS IoT in the same [certificate mode](https://docs.aws.amazon.com/iot/latest/apireference/API_CertificateDescription.html#iot-Type-CertificateDescription-certificateMode) as the signing CA. If you have more than one CA certificate that has the same subject field, you must specify the CA certificate that was used to sign the device certificate being registered.

Requires permission to access the [RegisterCertificate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_RegisterCertificate_RequestSyntax"></a>

```
POST /certificate/register?setAsActive={{setAsActive}} HTTP/1.1
Content-type: application/json

{
   "caCertificatePem": "{{string}}",
   "certificatePem": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterCertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [setAsActive](#API_RegisterCertificate_RequestSyntax) **   <a name="iot-RegisterCertificate-request-uri-setAsActive"></a>
 *This parameter has been deprecated.*
A boolean value that specifies if the certificate is set to active.
Valid values: `ACTIVE | INACTIVE`

## Request Body
<a name="API_RegisterCertificate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [caCertificatePem](#API_RegisterCertificate_RequestSyntax) **   <a name="iot-RegisterCertificate-request-caCertificatePem"></a>
The CA certificate used to sign the device certificate being registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`
Required: No

 ** [certificatePem](#API_RegisterCertificate_RequestSyntax) **   <a name="iot-RegisterCertificate-request-certificatePem"></a>
The certificate data, in PEM format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`
Required: Yes

 ** [status](#API_RegisterCertificate_RequestSyntax) **   <a name="iot-RegisterCertificate-request-status"></a>
The status of the register certificate request. Valid values that you can use include `ACTIVE`, `INACTIVE`, and `REVOKED`.
Type: String
Valid Values: `ACTIVE | INACTIVE | REVOKED | PENDING_TRANSFER | REGISTER_INACTIVE | PENDING_ACTIVATION`
Required: No

## Response Syntax
<a name="API_RegisterCertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateArn": "string",
   "certificateId": "string"
}
```

## Response Elements
<a name="API_RegisterCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateArn](#API_RegisterCertificate_ResponseSyntax) **   <a name="iot-RegisterCertificate-response-certificateArn"></a>
The certificate ARN.
Type: String

 ** [certificateId](#API_RegisterCertificate_ResponseSyntax) **   <a name="iot-RegisterCertificate-response-certificateId"></a>
The certificate identifier.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`

## Errors
<a name="API_RegisterCertificate_Errors"></a>

 ** CertificateConflictException **
Unable to verify the CA certificate used to sign the device certificate you are attempting to register. This is happens when you have registered more than one CA certificate that has the same subject field and public key.
 ** message **
The message for the exception.
HTTP Status Code: 409

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
<a name="API_RegisterCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/RegisterCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/RegisterCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RegisterCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/RegisterCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RegisterCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/RegisterCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/RegisterCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/RegisterCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/RegisterCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RegisterCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
