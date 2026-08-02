---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateProvisioningProfile.html
---

# CreateProvisioningProfile
<a name="API_CreateProvisioningProfile"></a>

Create a provisioning profile for executing device provisioning flows. The provisioning profile is a document that defines the set of resources and policies applied to a device during the provisioning process.

## Request Syntax
<a name="API_CreateProvisioningProfile_RequestSyntax"></a>

```
POST /provisioning-profiles HTTP/1.1
Content-type: application/json

{
   "CaCertificate": "{{string}}",
   "ClaimCertificate": "{{string}}",
   "ClientToken": "{{string}}",
   "Name": "{{string}}",
   "ProvisioningType": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateProvisioningProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateProvisioningProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CaCertificate](#API_CreateProvisioningProfile_RequestSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-request-CaCertificate"></a>
The body of the PEM-encoded certificate authority (CA) certificate.
Type: String
Pattern: `-----BEGIN CERTIFICATE-----.*(.|\n)*-----END CERTIFICATE-----\n?`
Required: No

 ** [ClaimCertificate](#API_CreateProvisioningProfile_RequestSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-request-ClaimCertificate"></a>
The body of the PEM-encoded claim certificate. If a claim certificate is provided, it will be used for the provisioning profile. Otherwise, a claim certificate will be generated.
Type: String
Required: No

 ** [ClientToken](#API_CreateProvisioningProfile_RequestSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [Name](#API_CreateProvisioningProfile_RequestSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-request-Name"></a>
The name of the provisioning profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[0-9A-Za-z_-]+`
Required: No

 ** [ProvisioningType](#API_CreateProvisioningProfile_RequestSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-request-ProvisioningType"></a>
The type of provisioning workflow the device uses for onboarding to IoT managed integrations.
Type: String
Valid Values: `FLEET_PROVISIONING | JITR`
Required: Yes

 ** [Tags](#API_CreateProvisioningProfile_RequestSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-request-Tags"></a>
A set of key/value pairs that are used to manage the provisioning profile.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateProvisioningProfile_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "ClaimCertificate": "string",
   "ClaimCertificatePrivateKey": "string",
   "Id": "string",
   "Name": "string",
   "ProvisioningType": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateProvisioningProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-response-Arn"></a>
The Amazon Resource Name (ARN) of the provisioning profile.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:provisioning-profile/[0-9a-zA-Z]+`

 ** [ClaimCertificate](#API_CreateProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-response-ClaimCertificate"></a>
The body of the PEM-encoded claim certificate.
Type: String

 ** [ClaimCertificatePrivateKey](#API_CreateProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-response-ClaimCertificatePrivateKey"></a>
The private key of the claim certificate. This may be stored securely on the device for validating the connection endpoint with IoT managed integrations using the public key.
Type: String

 ** [Id](#API_CreateProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-response-Id"></a>
The identifier of the provisioning profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

 ** [Name](#API_CreateProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-response-Name"></a>
The name of the provisioning profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[0-9A-Za-z_-]+`

 ** [ProvisioningType](#API_CreateProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-response-ProvisioningType"></a>
The type of provisioning workflow the device uses for onboarding to IoT managed integrations.
Type: String
Valid Values: `FLEET_PROVISIONING | JITR`

 ** [Status](#API_CreateProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-CreateProvisioningProfile-response-Status"></a>
The status of a provisioning profile.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATED | DELETE_IN_PROGRESS | DELETE_FAILED`

## Errors
<a name="API_CreateProvisioningProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict with the request.
HTTP Status Code: 409

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
<a name="API_CreateProvisioningProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/CreateProvisioningProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/CreateProvisioningProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CreateProvisioningProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/CreateProvisioningProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CreateProvisioningProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/CreateProvisioningProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/CreateProvisioningProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/CreateProvisioningProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/CreateProvisioningProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CreateProvisioningProfile)
