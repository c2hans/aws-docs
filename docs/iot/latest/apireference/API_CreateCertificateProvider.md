---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateProvider.html
---

# CreateCertificateProvider
<a name="API_CreateCertificateProvider"></a>

Creates an AWS IoT Core certificate provider. You can use AWS IoT Core certificate provider to customize how to sign a certificate signing request (CSR) in AWS IoT fleet provisioning. For more information, see [Customizing certificate signing using AWS IoT Core certificate provider](https://docs.aws.amazon.com/iot/latest/developerguide/provisioning-cert-provider.html) from * AWS IoT Core Developer Guide*.

Requires permission to access the [CreateCertificateProvider](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

**Important**
After you create a certificate provider, the behavior of [`CreateCertificateFromCsr` API for fleet provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/fleet-provision-api.html#create-cert-csr) will change and all API calls to `CreateCertificateFromCsr` will invoke the certificate provider to create the certificates. It can take up to a few minutes for this behavior to change after a certificate provider is created.

## Request Syntax
<a name="API_CreateCertificateProvider_RequestSyntax"></a>

```
POST /certificate-providers/{{certificateProviderName}} HTTP/1.1
Content-type: application/json

{
   "accountDefaultForOperations": [ "{{string}}" ],
   "clientToken": "{{string}}",
   "lambdaFunctionArn": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateCertificateProvider_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificateProviderName](#API_CreateCertificateProvider_RequestSyntax) **   <a name="iot-CreateCertificateProvider-request-uri-certificateProviderName"></a>
The name of the certificate provider.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`
Required: Yes

## Request Body
<a name="API_CreateCertificateProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountDefaultForOperations](#API_CreateCertificateProvider_RequestSyntax) **   <a name="iot-CreateCertificateProvider-request-accountDefaultForOperations"></a>
A list of the operations that the certificate provider will use to generate certificates. Valid value: `CreateCertificateFromCsr`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `CreateCertificateFromCsr`
Required: Yes

 ** [clientToken](#API_CreateCertificateProvider_RequestSyntax) **   <a name="iot-CreateCertificateProvider-request-clientToken"></a>
A string that you can optionally pass in the `CreateCertificateProvider` request to make sure the request is idempotent.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [lambdaFunctionArn](#API_CreateCertificateProvider_RequestSyntax) **   <a name="iot-CreateCertificateProvider-request-lambdaFunctionArn"></a>
The ARN of the Lambda function that defines the authentication logic.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\s\S]*`
Required: Yes

 ** [tags](#API_CreateCertificateProvider_RequestSyntax) **   <a name="iot-CreateCertificateProvider-request-tags"></a>
Metadata which can be used to manage the certificate provider.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateCertificateProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateProviderArn": "string",
   "certificateProviderName": "string"
}
```

## Response Elements
<a name="API_CreateCertificateProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateProviderArn](#API_CreateCertificateProvider_ResponseSyntax) **   <a name="iot-CreateCertificateProvider-response-certificateProviderArn"></a>
The ARN of the certificate provider.
Type: String
Length Constraints: Maximum length of 2048.

 ** [certificateProviderName](#API_CreateCertificateProvider_ResponseSyntax) **   <a name="iot-CreateCertificateProvider-response-certificateProviderName"></a>
The name of the certificate provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`

## Errors
<a name="API_CreateCertificateProvider_Errors"></a>

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
<a name="API_CreateCertificateProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateCertificateProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateCertificateProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateCertificateProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateCertificateProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateCertificateProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateCertificateProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateCertificateProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateCertificateProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateCertificateProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateCertificateProvider)
