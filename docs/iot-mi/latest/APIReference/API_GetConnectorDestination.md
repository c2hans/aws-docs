---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetConnectorDestination.html
---

# GetConnectorDestination
<a name="API_GetConnectorDestination"></a>

Get connector destination details linked to a cloud-to-cloud (C2C) connector.

## Request Syntax
<a name="API_GetConnectorDestination_RequestSyntax"></a>

```
GET /connector-destinations/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConnectorDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetConnectorDestination_RequestSyntax) **   <a name="managedintegrations-GetConnectorDestination-request-uri-Identifier"></a>
The identifier of the C2C connector destination.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

## Request Body
<a name="API_GetConnectorDestination_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConnectorDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AuthConfig": {
      "GeneralAuthorization": [
         {
            "AuthMaterialName": "string",
            "SecretsManager": {
               "arn": "string",
               "versionId": "string"
            }
         }
      ],
      "oAuth": {
         "authUrl": "string",
         "oAuthCompleteRedirectUrl": "string",
         "proactiveRefreshTokenRenewal": {
            "DaysBeforeRenewal": number,
            "enabled": boolean
         },
         "scope": "string",
         "tokenEndpointAuthenticationScheme": "string",
         "tokenUrl": "string"
      }
   },
   "AuthType": "string",
   "CloudConnectorId": "string",
   "Description": "string",
   "Id": "string",
   "Name": "string",
   "OAuthCompleteRedirectUrl": "string",
   "SecretsManager": {
      "arn": "string",
      "versionId": "string"
   }
}
```

## Response Elements
<a name="API_GetConnectorDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthConfig](#API_GetConnectorDestination_ResponseSyntax) **   <a name="managedintegrations-GetConnectorDestination-response-AuthConfig"></a>
The authentication configuration details for the connector destination, including OAuth settings and other authentication parameters.
Type: [AuthConfig](API_AuthConfig.md) object

 ** [AuthType](#API_GetConnectorDestination_ResponseSyntax) **   <a name="managedintegrations-GetConnectorDestination-response-AuthType"></a>
The authentication type used for the connector destination, which determines how credentials and access are managed.
Type: String
Valid Values: `OAUTH`

 ** [CloudConnectorId](#API_GetConnectorDestination_ResponseSyntax) **   <a name="managedintegrations-GetConnectorDestination-response-CloudConnectorId"></a>
The identifier of the C2C connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

 ** [Description](#API_GetConnectorDestination_ResponseSyntax) **   <a name="managedintegrations-GetConnectorDestination-response-Description"></a>
A description of the connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`

 ** [Id](#API_GetConnectorDestination_ResponseSyntax) **   <a name="managedintegrations-GetConnectorDestination-response-Id"></a>
The unique identifier of the connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

 ** [Name](#API_GetConnectorDestination_ResponseSyntax) **   <a name="managedintegrations-GetConnectorDestination-response-Name"></a>
The display name of the connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`

 ** [OAuthCompleteRedirectUrl](#API_GetConnectorDestination_ResponseSyntax) **   <a name="managedintegrations-GetConnectorDestination-response-OAuthCompleteRedirectUrl"></a>
The URL where users are redirected after completing the OAuth authorization process for the connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(http|https)://.*`

 ** [SecretsManager](#API_GetConnectorDestination_ResponseSyntax) **   <a name="managedintegrations-GetConnectorDestination-response-SecretsManager"></a>
The AWS Secrets Manager configuration used to securely store and manage sensitive information for the connector destination.
Type: [SecretsManager](API_SecretsManager.md) object

## Errors
<a name="API_GetConnectorDestination_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_GetConnectorDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetConnectorDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetConnectorDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetConnectorDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetConnectorDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetConnectorDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetConnectorDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetConnectorDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetConnectorDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetConnectorDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetConnectorDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
