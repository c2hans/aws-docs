---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_GetIntegration.html
---

# GetIntegration
<a name="API_GetIntegration"></a>

Retrieves information about an integration.

## Request Syntax
<a name="API_GetIntegration_RequestSyntax"></a>

```
POST /GetIntegration HTTP/1.1
Content-type: application/json

{
   "integrationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [integrationId](#API_GetIntegration_RequestSyntax) **   <a name="securityagent-GetIntegration-request-integrationId"></a>
The unique identifier of the integration to retrieve.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "displayName": "string",
   "installationId": "string",
   "integrationId": "string",
   "kmsKeyId": "string",
   "privateConnectionName": "string",
   "provider": "string",
   "providerType": "string",
   "targetUrl": "string",
   "webhookUrl": "string"
}
```

## Response Elements
<a name="API_GetIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_GetIntegration_ResponseSyntax) **   <a name="securityagent-GetIntegration-response-displayName"></a>
The display name of the integration.
Type: String

 ** [installationId](#API_GetIntegration_ResponseSyntax) **   <a name="securityagent-GetIntegration-response-installationId"></a>
The installation identifier from the integration provider.
Type: String

 ** [integrationId](#API_GetIntegration_ResponseSyntax) **   <a name="securityagent-GetIntegration-response-integrationId"></a>
The unique identifier of the integration.
Type: String

 ** [kmsKeyId](#API_GetIntegration_ResponseSyntax) **   <a name="securityagent-GetIntegration-response-kmsKeyId"></a>
The identifier of the AWS KMS key used to encrypt data associated with the integration.
Type: String

 ** [privateConnectionName](#API_GetIntegration_ResponseSyntax) **   <a name="securityagent-GetIntegration-response-privateConnectionName"></a>
The name of the private connection used to reach the integration's self-hosted instance over private networking, if one is configured.
Type: String

 ** [provider](#API_GetIntegration_ResponseSyntax) **   <a name="securityagent-GetIntegration-response-provider"></a>
The integration provider.
Type: String
Valid Values: `GITHUB | GITLAB | BITBUCKET | CONFLUENCE | AZURE_DEVOPS`

 ** [providerType](#API_GetIntegration_ResponseSyntax) **   <a name="securityagent-GetIntegration-response-providerType"></a>
The type of the integration provider.
Type: String
Valid Values: `SOURCE_CODE | DOCUMENTATION`

 ** [targetUrl](#API_GetIntegration_ResponseSyntax) **   <a name="securityagent-GetIntegration-response-targetUrl"></a>
The HTTPS URL of the customer self-hosted instance, such as a GitHub Enterprise Server or self-managed GitLab instance. This value is absent for SaaS integrations.
Type: String

 ** [webhookUrl](#API_GetIntegration_ResponseSyntax) **   <a name="securityagent-GetIntegration-response-webhookUrl"></a>
The payload URL of the integration's webhook, once it has been created. The signing secret is never returned on a read.
Type: String

## Errors
<a name="API_GetIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
Error description.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
 ** message **
Error description.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.
 ** message **
Error description.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Error description.
 ** quotaCode **
Quota code for throttling limit.
 ** serviceCode **
Service code for throttling limit.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered during validation.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/GetIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/GetIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/GetIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/GetIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/GetIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/GetIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/GetIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/GetIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/GetIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/GetIntegration)
