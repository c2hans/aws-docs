---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateEnvironmentBlueprint.html
---

# UpdateEnvironmentBlueprint
<a name="API_UpdateEnvironmentBlueprint"></a>

Updates an environment blueprint in Amazon DataZone.

## Request Syntax
<a name="API_UpdateEnvironmentBlueprint_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/environment-blueprints/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
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
<a name="API_UpdateEnvironmentBlueprint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which an environment blueprint is to be updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-request-uri-identifier"></a>
The identifier of the environment blueprint to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateEnvironmentBlueprint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-request-description"></a>
The description to be updated as part of the `UpdateEnvironmentBlueprint` action.
Type: String
Required: No

 ** [provisioningProperties](#API_UpdateEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-request-provisioningProperties"></a>
The provisioning properties to be updated as part of the `UpdateEnvironmentBlueprint` action.
Type: [ProvisioningProperties](API_ProvisioningProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [userParameters](#API_UpdateEnvironmentBlueprint_RequestSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-request-userParameters"></a>
The user parameters to be updated as part of the `UpdateEnvironmentBlueprint` action.
Type: Array of [CustomParameter](API_CustomParameter.md) objects
Required: No

## Response Syntax
<a name="API_UpdateEnvironmentBlueprint_ResponseSyntax"></a>

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
<a name="API_UpdateEnvironmentBlueprint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-response-createdAt"></a>
The timestamp of when the environment blueprint was created.
Type: Timestamp

 ** [deploymentProperties](#API_UpdateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-response-deploymentProperties"></a>
The deployment properties to be updated as part of the `UpdateEnvironmentBlueprint` action.
Type: [DeploymentProperties](API_DeploymentProperties.md) object

 ** [description](#API_UpdateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-response-description"></a>
The description to be updated as part of the `UpdateEnvironmentBlueprint` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [glossaryTerms](#API_UpdateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-response-glossaryTerms"></a>
The glossary terms to be updated as part of the `UpdateEnvironmentBlueprint` action.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_UpdateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-response-id"></a>
The identifier of the blueprint to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_UpdateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-response-name"></a>
The name to be updated as part of the `UpdateEnvironmentBlueprint` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [provider](#API_UpdateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-response-provider"></a>
The provider of the blueprint to be udpated.
Type: String

 ** [provisioningProperties](#API_UpdateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-response-provisioningProperties"></a>
The provisioning properties to be updated as part of the `UpdateEnvironmentBlueprint` action.
Type: [ProvisioningProperties](API_ProvisioningProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [updatedAt](#API_UpdateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-response-updatedAt"></a>
The timestamp of when the blueprint was updated.
Type: Timestamp

 ** [userParameters](#API_UpdateEnvironmentBlueprint_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentBlueprint-response-userParameters"></a>
The user parameters to be updated as part of the `UpdateEnvironmentBlueprint` action.
Type: Array of [CustomParameter](API_CustomParameter.md) objects

## Errors
<a name="API_UpdateEnvironmentBlueprint_Errors"></a>

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
<a name="API_UpdateEnvironmentBlueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateEnvironmentBlueprint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateEnvironmentBlueprint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateEnvironmentBlueprint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateEnvironmentBlueprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateEnvironmentBlueprint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateEnvironmentBlueprint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateEnvironmentBlueprint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateEnvironmentBlueprint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateEnvironmentBlueprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateEnvironmentBlueprint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
