---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_UpdateConnectorDestination.html
---

# UpdateConnectorDestination
<a name="API_UpdateConnectorDestination"></a>

Updates the properties of an existing connector destination.

## Request Syntax
<a name="API_UpdateConnectorDestination_RequestSyntax"></a>

```
PUT /connector-destinations/{{Identifier}} HTTP/1.1
Content-type: application/json

{
   "AuthConfig": {
      "GeneralAuthorizationUpdate": {
         "AuthMaterialsToAdd": [
            {
               "AuthMaterialName": "{{string}}",
               "SecretsManager": {
                  "arn": "{{string}}",
                  "versionId": "{{string}}"
               }
            }
         ],
         "AuthMaterialsToUpdate": [
            {
               "AuthMaterialName": "{{string}}",
               "SecretsManager": {
                  "arn": "{{string}}",
                  "versionId": "{{string}}"
               }
            }
         ]
      },
      "oAuthUpdate": {
         "oAuthCompleteRedirectUrl": "{{string}}",
         "proactiveRefreshTokenRenewal": {
            "DaysBeforeRenewal": {{number}},
            "enabled": {{boolean}}
         }
      }
   },
   "AuthType": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "SecretsManager": {
      "arn": "{{string}}",
      "versionId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateConnectorDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_UpdateConnectorDestination_RequestSyntax) **   <a name="managedintegrations-UpdateConnectorDestination-request-uri-Identifier"></a>
The unique identifier of the connector destination to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

## Request Body
<a name="API_UpdateConnectorDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AuthConfig](#API_UpdateConnectorDestination_RequestSyntax) **   <a name="managedintegrations-UpdateConnectorDestination-request-AuthConfig"></a>
The updated authentication configuration details for the connector destination.
Type: [AuthConfigUpdate](API_AuthConfigUpdate.md) object
Required: No

 ** [AuthType](#API_UpdateConnectorDestination_RequestSyntax) **   <a name="managedintegrations-UpdateConnectorDestination-request-AuthType"></a>
The new authentication type to use for the connector destination.
Type: String
Valid Values: `OAUTH`
Required: No

 ** [Description](#API_UpdateConnectorDestination_RequestSyntax) **   <a name="managedintegrations-UpdateConnectorDestination-request-Description"></a>
The new description to assign to the connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** [Name](#API_UpdateConnectorDestination_RequestSyntax) **   <a name="managedintegrations-UpdateConnectorDestination-request-Name"></a>
The new display name to assign to the connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [SecretsManager](#API_UpdateConnectorDestination_RequestSyntax) **   <a name="managedintegrations-UpdateConnectorDestination-request-SecretsManager"></a>
The updated AWS Secrets Manager configuration for the connector destination.
Type: [SecretsManager](API_SecretsManager.md) object
Required: No

## Response Syntax
<a name="API_UpdateConnectorDestination_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateConnectorDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateConnectorDestination_Errors"></a>

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
<a name="API_UpdateConnectorDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/UpdateConnectorDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/UpdateConnectorDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/UpdateConnectorDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/UpdateConnectorDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/UpdateConnectorDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/UpdateConnectorDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/UpdateConnectorDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/UpdateConnectorDestination)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/UpdateConnectorDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/UpdateConnectorDestination)
