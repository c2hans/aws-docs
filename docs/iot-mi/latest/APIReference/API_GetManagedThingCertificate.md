---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetManagedThingCertificate.html
---

# GetManagedThingCertificate
<a name="API_GetManagedThingCertificate"></a>

Retrieves the certificate PEM for a managed IoT thing.

## Request Syntax
<a name="API_GetManagedThingCertificate_RequestSyntax"></a>

```
GET /managed-things-certificate/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetManagedThingCertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetManagedThingCertificate_RequestSyntax) **   <a name="managedintegrations-GetManagedThingCertificate-request-uri-Identifier"></a>
The identifier of the managed thing.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

## Request Body
<a name="API_GetManagedThingCertificate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetManagedThingCertificate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CertificatePem": "string",
   "ManagedThingId": "string"
}
```

## Response Elements
<a name="API_GetManagedThingCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificatePem](#API_GetManagedThingCertificate_ResponseSyntax) **   <a name="managedintegrations-GetManagedThingCertificate-response-CertificatePem"></a>
The PEM-encoded certificate for the managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`

 ** [ManagedThingId](#API_GetManagedThingCertificate_ResponseSyntax) **   <a name="managedintegrations-GetManagedThingCertificate-response-ManagedThingId"></a>
The identifier of the managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`

## Errors
<a name="API_GetManagedThingCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
HTTP Status Code: 401

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_GetManagedThingCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetManagedThingCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetManagedThingCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetManagedThingCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetManagedThingCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetManagedThingCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetManagedThingCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetManagedThingCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetManagedThingCertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetManagedThingCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetManagedThingCertificate)
