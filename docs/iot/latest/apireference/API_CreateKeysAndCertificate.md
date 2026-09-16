---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateKeysAndCertificate.html
---

# CreateKeysAndCertificate
<a name="API_CreateKeysAndCertificate"></a>

Creates a 2048-bit RSA key pair and issues an X.509 certificate using the issued public key. You can also call `CreateKeysAndCertificate` over MQTT from a device, for more information, see [Provisioning MQTT API](https://docs.aws.amazon.com/iot/latest/developerguide/provision-wo-cert.html#provision-mqtt-api).

 **Note** This is the only time AWS IoT issues the private key for this certificate, so it is important to keep it in a secure location.

Requires permission to access the [CreateKeysAndCertificate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateKeysAndCertificate_RequestSyntax"></a>

```
POST /keys-and-certificate?setAsActive={{setAsActive}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CreateKeysAndCertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [setAsActive](#API_CreateKeysAndCertificate_RequestSyntax) **   <a name="iot-CreateKeysAndCertificate-request-uri-setAsActive"></a>
Specifies whether the certificate is active.

## Request Body
<a name="API_CreateKeysAndCertificate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CreateKeysAndCertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateArn": "string",
   "certificateId": "string",
   "certificatePem": "string",
   "keyPair": {
      "PrivateKey": "string",
      "PublicKey": "string"
   }
}
```

## Response Elements
<a name="API_CreateKeysAndCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateArn](#API_CreateKeysAndCertificate_ResponseSyntax) **   <a name="iot-CreateKeysAndCertificate-response-certificateArn"></a>
The ARN of the certificate.
Type: String

 ** [certificateId](#API_CreateKeysAndCertificate_ResponseSyntax) **   <a name="iot-CreateKeysAndCertificate-response-certificateId"></a>
The ID of the certificate. AWS IoT issues a default subject name for the certificate (for example, AWS IoT Certificate).
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`

 ** [certificatePem](#API_CreateKeysAndCertificate_ResponseSyntax) **   <a name="iot-CreateKeysAndCertificate-response-certificatePem"></a>
The certificate data, in PEM format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`

 ** [keyPair](#API_CreateKeysAndCertificate_ResponseSyntax) **   <a name="iot-CreateKeysAndCertificate-response-keyPair"></a>
The generated key pair.
Type: [KeyPair](API_KeyPair.md) object

## Errors
<a name="API_CreateKeysAndCertificate_Errors"></a>

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
<a name="API_CreateKeysAndCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateKeysAndCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateKeysAndCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateKeysAndCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateKeysAndCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateKeysAndCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateKeysAndCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateKeysAndCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateKeysAndCertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateKeysAndCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateKeysAndCertificate)
