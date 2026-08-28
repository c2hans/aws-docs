---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCACertificate.html
---

# RegisterCACertificate
<a name="API_RegisterCACertificate"></a>

Registers a CA certificate with AWS IoT Core. There is no limit to the number of CA certificates you can register in your AWS account. You can register up to 10 CA certificates with the same `CA subject field` per AWS account.

Requires permission to access the [RegisterCACertificate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_RegisterCACertificate_RequestSyntax"></a>

```
POST /cacertificate?allowAutoRegistration={{allowAutoRegistration}}&setAsActive={{setAsActive}} HTTP/1.1
Content-type: application/json

{
   "caCertificate": "{{string}}",
   "certificateMode": "{{string}}",
   "registrationConfig": {
      "roleArn": "{{string}}",
      "templateBody": "{{string}}",
      "templateName": "{{string}}"
   },
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "verificationCertificate": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterCACertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [allowAutoRegistration](#API_RegisterCACertificate_RequestSyntax) **   <a name="iot-RegisterCACertificate-request-uri-allowAutoRegistration"></a>
Allows this CA certificate to be used for auto registration of device certificates.

 ** [setAsActive](#API_RegisterCACertificate_RequestSyntax) **   <a name="iot-RegisterCACertificate-request-uri-setAsActive"></a>
A boolean value that specifies if the CA certificate is set to active.
Valid values: `ACTIVE | INACTIVE`

## Request Body
<a name="API_RegisterCACertificate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [caCertificate](#API_RegisterCACertificate_RequestSyntax) **   <a name="iot-RegisterCACertificate-request-caCertificate"></a>
The CA certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`
Required: Yes

 ** [certificateMode](#API_RegisterCACertificate_RequestSyntax) **   <a name="iot-RegisterCACertificate-request-certificateMode"></a>
Describes the certificate mode in which the Certificate Authority (CA) will be registered. If the `verificationCertificate` field is not provided, set `certificateMode` to be `SNI_ONLY`. If the `verificationCertificate` field is provided, set `certificateMode` to be `DEFAULT`. When `certificateMode` is not provided, it defaults to `DEFAULT`. All the device certificates that are registered using this CA will be registered in the same certificate mode as the CA. For more information about certificate mode for device certificates, see [ certificate mode](https://docs.aws.amazon.com/iot/latest/apireference/API_CertificateDescription.html#iot-Type-CertificateDescription-certificateMode).
Type: String
Valid Values: `DEFAULT | SNI_ONLY`
Required: No

 ** [registrationConfig](#API_RegisterCACertificate_RequestSyntax) **   <a name="iot-RegisterCACertificate-request-registrationConfig"></a>
Information about the registration configuration.
Type: [RegistrationConfig](API_RegistrationConfig.md) object
Required: No

 ** [tags](#API_RegisterCACertificate_RequestSyntax) **   <a name="iot-RegisterCACertificate-request-tags"></a>
Metadata which can be used to manage the CA certificate.
For URI Request parameters use format: ...key1=value1&key2=value2...
For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."
For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [verificationCertificate](#API_RegisterCACertificate_RequestSyntax) **   <a name="iot-RegisterCACertificate-request-verificationCertificate"></a>
The private key verification certificate. If `certificateMode` is `SNI_ONLY`, the `verificationCertificate` field must be empty. If `certificateMode` is `DEFAULT` or not provided, the `verificationCertificate` field must not be empty.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_RegisterCACertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateArn": "string",
   "certificateId": "string"
}
```

## Response Elements
<a name="API_RegisterCACertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateArn](#API_RegisterCACertificate_ResponseSyntax) **   <a name="iot-RegisterCACertificate-response-certificateArn"></a>
The CA certificate ARN.
Type: String

 ** [certificateId](#API_RegisterCACertificate_ResponseSyntax) **   <a name="iot-RegisterCACertificate-response-certificateId"></a>
The CA certificate identifier.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`

## Errors
<a name="API_RegisterCACertificate_Errors"></a>

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

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** RegistrationCodeValidationException **
The registration code is invalid.
 ** message **
Additional information about the exception.
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
<a name="API_RegisterCACertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/RegisterCACertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/RegisterCACertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RegisterCACertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/RegisterCACertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RegisterCACertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/RegisterCACertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/RegisterCACertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/RegisterCACertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/RegisterCACertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RegisterCACertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
