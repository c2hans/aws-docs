---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateEnvironmentBlueprint.html
---

# CreateEnvironmentBlueprint
<a name="API_CreateEnvironmentBlueprint"></a>

Creates a Amazon DataZone blueprint.

## Request Syntax
<a name="API_CreateEnvironmentBlueprint_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/environment-blueprints HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "provisioningProperties": { ... },
   "userParameters": [
      {
         "defaultValue": "{{string}}",
         "description": "{{string}}",
         "fieldType": "{{string}}",
         "isEditable": {{boolean}},
         "isOptional": {{boolean}},
         "isUpdateSupported": {{boolean}},
         "keyName": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateEnvironmentBlueprint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-request-uri-domainIdentifier"></a>
The identifier of the domain in which this blueprint is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateEnvironmentBlueprint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-request-description"></a>
The description of the Amazon DataZone blueprint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [name](#API_CreateEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-request-name"></a>
The name of this Amazon DataZone blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** [provisioningProperties](#API_CreateEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-request-provisioningProperties"></a>
The provisioning properties of this Amazon DataZone blueprint.
Type: [ProvisioningProperties](API_ProvisioningProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [userParameters](#API_CreateEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-request-userParameters"></a>
The user parameters of this Amazon DataZone blueprint.
Type: Array of [CustomParameter](API_CustomParameter.md) objects
Required: No

## Response Syntax
<a name="API_CreateEnvironmentBlueprint_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateEnvironmentBlueprint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-response-createdAt"></a>
The timestamp at which the environment blueprint was created.
Type: Timestamp

 ** [deploymentProperties](#API_CreateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-response-deploymentProperties"></a>
The deployment properties of this Amazon DataZone blueprint.
Type: [DeploymentProperties](API_DeploymentProperties.md) object

 ** [description](#API_CreateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-response-description"></a>
The description of this Amazon DataZone blueprint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [glossaryTerms](#API_CreateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-response-glossaryTerms"></a>
The glossary terms attached to this Amazon DataZone blueprint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-response-id"></a>
The ID of this Amazon DataZone blueprint.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_CreateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-response-name"></a>
The name of this Amazon DataZone blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [provider](#API_CreateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-response-provider"></a>
The provider of this Amazon DataZone blueprint.
Type: String

 ** [provisioningProperties](#API_CreateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-response-provisioningProperties"></a>
The provisioning properties of this Amazon DataZone blueprint.
Type: [ProvisioningProperties](API_ProvisioningProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [updatedAt](#API_CreateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-response-updatedAt"></a>
The timestamp of when this blueprint was updated.
Type: Timestamp

 ** [userParameters](#API_CreateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-CreateEnvironmentBlueprint-response-userParameters"></a>
The user parameters of this Amazon DataZone blueprint.
Type: Array of [CustomParameter](API_CustomParameter.md) objects

## Errors
<a name="API_CreateEnvironmentBlueprint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_CreateEnvironmentBlueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateEnvironmentBlueprint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateEnvironmentBlueprint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateEnvironmentBlueprint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateEnvironmentBlueprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateEnvironmentBlueprint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateEnvironmentBlueprint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateEnvironmentBlueprint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateEnvironmentBlueprint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateEnvironmentBlueprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateEnvironmentBlueprint)
