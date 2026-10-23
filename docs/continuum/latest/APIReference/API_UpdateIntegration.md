---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_UpdateIntegration.html
---

# UpdateIntegration
<a name="API_UpdateIntegration"></a>

Rotates the credentials used by an Amazon S3 integration. Only S3 integrations can be updated; GitHub integrations cannot be modified. The integration's name, provider type, and bucket remain fixed.

The caller must have iam:PassRole permission for the supplied role, including when only the external ID changes. Continuum verifies that the role can be assumed with the requested external ID and can access the existing bucket before saving both credentials atomically. Omitting externalId preserves its current value. Repeating both current credentials leaves updatedAt unchanged, but still requires authorization and access validation.

## Request Syntax
<a name="API_UpdateIntegration_RequestSyntax"></a>

```
PATCH /integrations/{{integrationId}} HTTP/1.1
Content-type: application/json

{
   "providerConfiguration": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateIntegration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [integrationId](#API_UpdateIntegration_RequestSyntax) **   <a name="continuum-UpdateIntegration-request-uri-integrationId"></a>
The identifier of the integration.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [providerConfiguration](#API_UpdateIntegration_RequestSyntax) **   <a name="continuum-UpdateIntegration-request-providerConfiguration"></a>
The provider Configuration.
Type: [UpdateProviderConfiguration](API_UpdateProviderConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_UpdateIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "integrationArn": "string",
   "integrationId": "string",
   "integrationType": "string",
   "name": "string",
   "providerDetails": { ... },
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateIntegration_ResponseSyntax) **   <a name="continuum-UpdateIntegration-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [integrationArn](#API_UpdateIntegration_ResponseSyntax) **   <a name="continuum-UpdateIntegration-response-integrationArn"></a>
The Amazon Resource Name (ARN) of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:integrations/[a-z0-9]+`

 ** [integrationId](#API_UpdateIntegration_ResponseSyntax) **   <a name="continuum-UpdateIntegration-response-integrationId"></a>
The identifier of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [integrationType](#API_UpdateIntegration_ResponseSyntax) **   <a name="continuum-UpdateIntegration-response-integrationType"></a>
The integration Type.
Type: String
Valid Values: `GITHUB | S3`

 ** [name](#API_UpdateIntegration_ResponseSyntax) **   <a name="continuum-UpdateIntegration-response-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [providerDetails](#API_UpdateIntegration_ResponseSyntax) **   <a name="continuum-UpdateIntegration-response-providerDetails"></a>
Provider-specific details for an integration. Only one member will be present.
Type: [ProviderDetails](API_ProviderDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [updatedAt](#API_UpdateIntegration_ResponseSyntax) **   <a name="continuum-UpdateIntegration-response-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/UpdateIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/UpdateIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/UpdateIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/UpdateIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/UpdateIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/UpdateIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/UpdateIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/UpdateIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/UpdateIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/UpdateIntegration)
