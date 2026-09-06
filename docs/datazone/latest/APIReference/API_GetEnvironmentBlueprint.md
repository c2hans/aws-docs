---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetEnvironmentBlueprint.html
---

# GetEnvironmentBlueprint
<a name="API_GetEnvironmentBlueprint"></a>

Gets an Amazon DataZone blueprint.

## Request Syntax
<a name="API_GetEnvironmentBlueprint_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/environment-blueprints/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEnvironmentBlueprint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-GetEnvironmentBlueprint-request-uri-domainIdentifier"></a>
The identifier of the domain in which this blueprint exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-GetEnvironmentBlueprint-request-uri-identifier"></a>
The ID of this Amazon DataZone blueprint.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetEnvironmentBlueprint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEnvironmentBlueprint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "deploymentProperties": {
      "endTimeoutMinutes": number,
      "startTimeoutMinutes": number
   },
   "description": "string",
   "glossaryTerms": [ "string" ],
   "id": "string",
   "name": "string",
   "provider": "string",
   "provisioningProperties": { ... },
   "updatedAt": "string",
   "userParameters": [
      {
         "defaultValue": "string",
         "description": "string",
         "fieldType": "string",
         "isEditable": boolean,
         "isOptional": boolean,
         "isUpdateSupported": boolean,
         "keyName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetEnvironmentBlueprint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprint-response-createdAt"></a>
A timestamp of when this blueprint was created.
Type: Timestamp

 ** [deploymentProperties](#API_GetEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprint-response-deploymentProperties"></a>
The deployment properties of this Amazon DataZone blueprint.
Type: [DeploymentProperties](API_DeploymentProperties.md) object

 ** [description](#API_GetEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprint-response-description"></a>
The description of this Amazon DataZone blueprint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [glossaryTerms](#API_GetEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprint-response-glossaryTerms"></a>
The glossary terms attached to this Amazon DataZone blueprint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprint-response-id"></a>
The ID of this Amazon DataZone blueprint.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_GetEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprint-response-name"></a>
The name of this Amazon DataZone blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [provider](#API_GetEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprint-response-provider"></a>
The provider of this Amazon DataZone blueprint.
Type: String

 ** [provisioningProperties](#API_GetEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprint-response-provisioningProperties"></a>
The provisioning properties of this Amazon DataZone blueprint.
Type: [ProvisioningProperties](API_ProvisioningProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [updatedAt](#API_GetEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprint-response-updatedAt"></a>
The timestamp of when this blueprint was updated.
Type: Timestamp

 ** [userParameters](#API_GetEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-GetEnvironmentBlueprint-response-userParameters"></a>
The user parameters of this blueprint.
Type: Array of [CustomParameter](API_CustomParameter.md) objects

## Errors
<a name="API_GetEnvironmentBlueprint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetEnvironmentBlueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetEnvironmentBlueprint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetEnvironmentBlueprint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetEnvironmentBlueprint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetEnvironmentBlueprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetEnvironmentBlueprint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetEnvironmentBlueprint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetEnvironmentBlueprint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetEnvironmentBlueprint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetEnvironmentBlueprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetEnvironmentBlueprint)
