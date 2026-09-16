---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCertificateProvider.html
---

# UpdateCertificateProvider
<a name="API_UpdateCertificateProvider"></a>

Updates a certificate provider.

Requires permission to access the [UpdateCertificateProvider](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateCertificateProvider_RequestSyntax"></a>

```
PUT /certificate-providers/{{certificateProviderName}} HTTP/1.1
Content-type: application/json

{
   "accountDefaultForOperations": [ "{{string}}" ],
   "lambdaFunctionArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCertificateProvider_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificateProviderName](#API_UpdateCertificateProvider_RequestSyntax) **   <a name="iot-UpdateCertificateProvider-request-uri-certificateProviderName"></a>
The name of the certificate provider.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`
Required: Yes

## Request Body
<a name="API_UpdateCertificateProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountDefaultForOperations](#API_UpdateCertificateProvider_RequestSyntax) **   <a name="iot-UpdateCertificateProvider-request-accountDefaultForOperations"></a>
A list of the operations that the certificate provider will use to generate certificates. Valid value: `CreateCertificateFromCsr`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `CreateCertificateFromCsr`
Required: No

 ** [lambdaFunctionArn](#API_UpdateCertificateProvider_RequestSyntax) **   <a name="iot-UpdateCertificateProvider-request-lambdaFunctionArn"></a>
The Lambda function ARN that's associated with the certificate provider.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_UpdateCertificateProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateProviderArn": "string",
   "certificateProviderName": "string"
}
```

## Response Elements
<a name="API_UpdateCertificateProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateProviderArn](#API_UpdateCertificateProvider_ResponseSyntax) **   <a name="iot-UpdateCertificateProvider-response-certificateProviderArn"></a>
The ARN of the certificate provider.
Type: String
Length Constraints: Maximum length of 2048.

 ** [certificateProviderName](#API_UpdateCertificateProvider_ResponseSyntax) **   <a name="iot-UpdateCertificateProvider-response-certificateProviderName"></a>
The name of the certificate provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`

## Errors
<a name="API_UpdateCertificateProvider_Errors"></a>

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
<a name="API_UpdateCertificateProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateCertificateProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateCertificateProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateCertificateProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateCertificateProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateCertificateProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateCertificateProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateCertificateProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateCertificateProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateCertificateProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateCertificateProvider)
