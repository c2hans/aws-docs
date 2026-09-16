---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCACertificate.html
---

# UpdateCACertificate
<a name="API_UpdateCACertificate"></a>

Updates a registered CA certificate.

Requires permission to access the [UpdateCACertificate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateCACertificate_RequestSyntax"></a>

```
PUT /cacertificate/{{caCertificateId}}?newAutoRegistrationStatus={{newAutoRegistrationStatus}}&newStatus={{newStatus}} HTTP/1.1
Content-type: application/json

{
   "registrationConfig": {
      "roleArn": "{{string}}",
      "templateBody": "{{string}}",
      "templateName": "{{string}}"
   },
   "removeAutoRegistration": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateCACertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caCertificateId](#API_UpdateCACertificate_RequestSyntax) **   <a name="iot-UpdateCACertificate-request-uri-certificateId"></a>
The CA certificate identifier.
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: Yes

 ** [newAutoRegistrationStatus](#API_UpdateCACertificate_RequestSyntax) **   <a name="iot-UpdateCACertificate-request-uri-newAutoRegistrationStatus"></a>
The new value for the auto registration status. Valid values are: "ENABLE" or "DISABLE".
Valid Values: `ENABLE | DISABLE`

 ** [newStatus](#API_UpdateCACertificate_RequestSyntax) **   <a name="iot-UpdateCACertificate-request-uri-newStatus"></a>
The updated status of the CA certificate.
 **Note:** The status value REGISTER\_INACTIVE is deprecated and should not be used.
Valid Values: `ACTIVE | INACTIVE`

## Request Body
<a name="API_UpdateCACertificate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [registrationConfig](#API_UpdateCACertificate_RequestSyntax) **   <a name="iot-UpdateCACertificate-request-registrationConfig"></a>
Information about the registration configuration.
Type: [RegistrationConfig](API_RegistrationConfig.md) object
Required: No

 ** [removeAutoRegistration](#API_UpdateCACertificate_RequestSyntax) **   <a name="iot-UpdateCACertificate-request-removeAutoRegistration"></a>
If true, removes auto registration.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateCACertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateCACertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCACertificate_Errors"></a>

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
<a name="API_UpdateCACertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateCACertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateCACertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateCACertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateCACertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateCACertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateCACertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateCACertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateCACertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateCACertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateCACertificate)
