---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetProvisioningProfile.html
---

# GetProvisioningProfile
<a name="API_GetProvisioningProfile"></a>

Get details of a provisioning profile.

## Request Syntax
<a name="API_GetProvisioningProfile_RequestSyntax"></a>

```
GET /provisioning-profiles/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetProvisioningProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetProvisioningProfile_RequestSyntax) **   <a name="managedintegrations-GetProvisioningProfile-request-uri-Identifier"></a>
The id of a provisioning profile.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

## Request Body
<a name="API_GetProvisioningProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetProvisioningProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "ClaimCertificate": "string",
   "Id": "string",
   "Name": "string",
   "ProvisioningType": "string",
   "Status": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetProvisioningProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-GetProvisioningProfile-response-Arn"></a>
The Amazon Resource Name (ARN) of the provisioning profile.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:provisioning-profile/[0-9a-zA-Z]+`

 ** [ClaimCertificate](#API_GetProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-GetProvisioningProfile-response-ClaimCertificate"></a>
The body of the PEM-encoded claim certificate.
Type: String

 ** [Id](#API_GetProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-GetProvisioningProfile-response-Id"></a>
The provisioning profile id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

 ** [Name](#API_GetProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-GetProvisioningProfile-response-Name"></a>
The name of the provisioning profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[0-9A-Za-z_-]+`

 ** [ProvisioningType](#API_GetProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-GetProvisioningProfile-response-ProvisioningType"></a>
The type of provisioning workflow the device uses for onboarding to IoT managed integrations.
Type: String
Valid Values: `FLEET_PROVISIONING | JITR`

 ** [Status](#API_GetProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-GetProvisioningProfile-response-Status"></a>
The status of a provisioning profile.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATED | DELETE_IN_PROGRESS | DELETE_FAILED`

 ** [Tags](#API_GetProvisioningProfile_ResponseSyntax) **   <a name="managedintegrations-GetProvisioningProfile-response-Tags"></a>
A set of key/value pairs that are used to manage the provisioning profile.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetProvisioningProfile_Errors"></a>

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
<a name="API_GetProvisioningProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetProvisioningProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetProvisioningProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetProvisioningProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetProvisioningProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetProvisioningProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetProvisioningProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetProvisioningProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetProvisioningProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetProvisioningProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetProvisioningProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
