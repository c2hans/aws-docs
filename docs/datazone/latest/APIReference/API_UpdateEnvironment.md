---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateEnvironment.html
---

# UpdateEnvironment
<a name="API_UpdateEnvironment"></a>

Updates the specified environment in Amazon DataZone.

## Request Syntax
<a name="API_UpdateEnvironment_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/environments/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "blueprintVersion": "{{string}}",
   "description": "{{string}}",
   "environmentConfigurationName": "{{string}}",
   "glossaryTerms": [ "{{string}}" ],
   "name": "{{string}}",
   "userParameters": [
      {
         "name": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateEnvironment_RequestSyntax) **   <a name="datazone-UpdateEnvironment-request-uri-domainIdentifier"></a>
The identifier of the domain in which the environment is to be updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateEnvironment_RequestSyntax) **   <a name="datazone-UpdateEnvironment-request-uri-identifier"></a>
The identifier of the environment that is to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [blueprintVersion](#API_UpdateEnvironment_RequestSyntax) **   <a name="datazone-UpdateEnvironment-request-blueprintVersion"></a>
The blueprint version to which the environment should be updated. You can only specify the following string for this parameter: `latest`.
Type: String
Required: No

 ** [description](#API_UpdateEnvironment_RequestSyntax) **   <a name="datazone-UpdateEnvironment-request-description"></a>
The description to be updated as part of the `UpdateEnvironment` action.
Type: String
Required: No

 ** [environmentConfigurationName](#API_UpdateEnvironment_RequestSyntax) **   <a name="datazone-UpdateEnvironment-request-environmentConfigurationName"></a>
The configuration name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: No

 ** [glossaryTerms](#API_UpdateEnvironment_RequestSyntax) **   <a name="datazone-UpdateEnvironment-request-glossaryTerms"></a>
The glossary terms to be updated as part of the `UpdateEnvironment` action.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [name](#API_UpdateEnvironment_RequestSyntax) **   <a name="datazone-UpdateEnvironment-request-name"></a>
The name to be updated as part of the `UpdateEnvironment` action.
Type: String
Required: No

 ** [userParameters](#API_UpdateEnvironment_RequestSyntax) **   <a name="datazone-UpdateEnvironment-request-userParameters"></a>
The user parameters of the environment.
Type: Array of [EnvironmentParameter](API_EnvironmentParameter.md) objects
Required: No

## Response Syntax
<a name="API_UpdateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "awsAccountId": "string",
   "awsAccountRegion": "string",
   "createdAt": "string",
   "createdBy": "string",
   "deploymentProperties": {
      "endTimeoutMinutes": number,
      "startTimeoutMinutes": number
   },
   "description": "string",
   "domainId": "string",
   "environmentActions": [
      {
         "auth": "string",
         "parameters": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "type": "string"
      }
   ],
   "environmentBlueprintId": "string",
   "environmentConfigurationId": "string",
   "environmentConfigurationName": "string",
   "environmentProfileId": "string",
   "glossaryTerms": [ "string" ],
   "id": "string",
   "lastDeployment": {
      "deploymentId": "string",
      "deploymentStatus": "string",
      "deploymentType": "string",
      "failureReason": {
         "code": "string",
         "message": "string"
      },
      "isDeploymentComplete": boolean,
      "messages": [ "string" ]
   },
   "name": "string",
   "projectId": "string",
   "provider": "string",
   "provisionedResources": [
      {
         "name": "string",
         "provider": "string",
         "type": "string",
         "value": "string"
      }
   ],
   "provisioningProperties": { ... },
   "status": "string",
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
<a name="API_UpdateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsAccountId](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-awsAccountId"></a>
The identifier of the AWS account in which the environment is to be updated.
Type: String
Pattern: `\d{12}`

 ** [awsAccountRegion](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-awsAccountRegion"></a>
The AWS Region in which the environment is updated.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`

 ** [createdAt](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-createdAt"></a>
The timestamp of when the environment was created.
Type: Timestamp

 ** [createdBy](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-createdBy"></a>
The Amazon DataZone user who created the environment.
Type: String

 ** [deploymentProperties](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-deploymentProperties"></a>
The deployment properties to be updated as part of the `UpdateEnvironment` action.
Type: [DeploymentProperties](API_DeploymentProperties.md) object

 ** [description](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-description"></a>
The description to be updated as part of the `UpdateEnvironment` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-domainId"></a>
The identifier of the domain in which the environment is to be updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentActions](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-environmentActions"></a>
The environment actions to be updated as part of the `UpdateEnvironment` action.
Type: Array of [ConfigurableEnvironmentAction](API_ConfigurableEnvironmentAction.md) objects

 ** [environmentBlueprintId](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-environmentBlueprintId"></a>
The blueprint identifier of the environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [environmentConfigurationId](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-environmentConfigurationId"></a>
The configuration ID of the environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [environmentConfigurationName](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-environmentConfigurationName"></a>
The configuration name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [environmentProfileId](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-environmentProfileId"></a>
The profile identifier of the environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`

 ** [glossaryTerms](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-glossaryTerms"></a>
The glossary terms to be updated as part of the `UpdateEnvironment` action.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-id"></a>
The identifier of the environment that is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastDeployment](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-lastDeployment"></a>
The last deployment of the environment.
Type: [Deployment](API_Deployment.md) object

 ** [name](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-name"></a>
The name to be updated as part of the `UpdateEnvironment` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectId](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-projectId"></a>
The project identifier of the environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [provider](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-provider"></a>
The provider identifier of the environment.
Type: String

 ** [provisionedResources](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-provisionedResources"></a>
The provisioned resources to be updated as part of the `UpdateEnvironment` action.
Type: Array of [Resource](API_Resource.md) objects

 ** [provisioningProperties](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-provisioningProperties"></a>
The provisioning properties to be updated as part of the `UpdateEnvironment` action.
Type: [ProvisioningProperties](API_ProvisioningProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-status"></a>
The status to be updated as part of the `UpdateEnvironment` action.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED | VALIDATION_FAILED | SUSPENDED | DISABLED | EXPIRED | DELETED | INACCESSIBLE`

 ** [updatedAt](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-updatedAt"></a>
The timestamp of when the environment was updated.
Type: Timestamp

 ** [userParameters](#API_UpdateEnvironment_ResponseSyntax) **   <a name="datazone-UpdateEnvironment-response-userParameters"></a>
The user parameters to be updated as part of the `UpdateEnvironment` action.
Type: Array of [CustomParameter](API_CustomParameter.md) objects

## Errors
<a name="API_UpdateEnvironment_Errors"></a>

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
<a name="API_UpdateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateEnvironment)
