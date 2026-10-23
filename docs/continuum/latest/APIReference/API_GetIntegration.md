---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetIntegration.html
---

# GetIntegration
<a name="API_GetIntegration"></a>

Retrieves information about an integration.

## Request Syntax
<a name="API_GetIntegration_RequestSyntax"></a>

```
GET /integrations/{{integrationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIntegration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [integrationId](#API_GetIntegration_RequestSyntax) **   <a name="continuum-GetIntegration-request-uri-integrationId"></a>
The identifier of the integration.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetIntegration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIntegration_ResponseSyntax"></a>

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
<a name="API_GetIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetIntegration_ResponseSyntax) **   <a name="continuum-GetIntegration-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [integrationArn](#API_GetIntegration_ResponseSyntax) **   <a name="continuum-GetIntegration-response-integrationArn"></a>
The Amazon Resource Name (ARN) of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:integrations/[a-z0-9]+`

 ** [integrationId](#API_GetIntegration_ResponseSyntax) **   <a name="continuum-GetIntegration-response-integrationId"></a>
The identifier of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [integrationType](#API_GetIntegration_ResponseSyntax) **   <a name="continuum-GetIntegration-response-integrationType"></a>
The integration Type.
Type: String
Valid Values: `GITHUB | S3`

 ** [name](#API_GetIntegration_ResponseSyntax) **   <a name="continuum-GetIntegration-response-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [providerDetails](#API_GetIntegration_ResponseSyntax) **   <a name="continuum-GetIntegration-response-providerDetails"></a>
Provider-specific details for an integration. Only one member will be present.
Type: [ProviderDetails](API_ProviderDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [updatedAt](#API_GetIntegration_ResponseSyntax) **   <a name="continuum-GetIntegration-response-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp

## Errors
<a name="API_GetIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

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
<a name="API_GetIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/GetIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/GetIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/GetIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/GetIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/GetIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/GetIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/GetIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/GetIntegration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/GetIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/GetIntegration)
