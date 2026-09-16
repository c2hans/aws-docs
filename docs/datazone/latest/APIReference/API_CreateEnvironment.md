---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateEnvironment.html
---

# CreateEnvironment
<a name="API_CreateEnvironment"></a>

Create an Amazon DataZone environment.

## Request Syntax
<a name="API_CreateEnvironment_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/environments HTTP/1.1
Content-type: application/json

{
   "deploymentOrder": {{number}},
   "description": "{{string}}",
   "environmentAccountIdentifier": "{{string}}",
   "environmentAccountRegion": "{{string}}",
   "environmentBlueprintIdentifier": "{{string}}",
   "environmentConfigurationId": "{{string}}",
   "environmentConfigurationName": "{{string}}",
   "environmentProfileIdentifier": "{{string}}",
   "glossaryTerms": [ "{{string}}" ],
   "name": "{{string}}",
   "projectIdentifier": "{{string}}",
   "userParameters": [
      {
         "name": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which the environment is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deploymentOrder](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-deploymentOrder"></a>
The deployment order of the environment.
Type: Integer
Required: No

 ** [description](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-description"></a>
The description of the Amazon DataZone environment.
Type: String
Required: No

 ** [environmentAccountIdentifier](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-environmentAccountIdentifier"></a>
The ID of the account in which the environment is being created.
Type: String
Required: No

 ** [environmentAccountRegion](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-environmentAccountRegion"></a>
The region of the account in which the environment is being created.
Type: String
Required: No

 ** [environmentBlueprintIdentifier](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-environmentBlueprintIdentifier"></a>
The ID of the blueprint with which the environment is being created.
This parameter is only valid for V1 domains. If provided for a V2 domain, the service returns a ValidationException.
Type: String
Required: No

 ** [environmentConfigurationId](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-environmentConfigurationId"></a>
The configuration ID of the environment.
Type: String
Required: No

 ** [environmentConfigurationName](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-environmentConfigurationName"></a>
The configuration name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: No

 ** [environmentProfileIdentifier](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-environmentProfileIdentifier"></a>
The identifier of the environment profile that is used to create this Amazon DataZone environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`
Required: No

 ** [glossaryTerms](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-glossaryTerms"></a>
The glossary terms that can be used in this Amazon DataZone environment.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [name](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-name"></a>
The name of the Amazon DataZone environment.
Type: String
Required: Yes

 ** [projectIdentifier](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-projectIdentifier"></a>
The identifier of the Amazon DataZone project in which this environment is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [userParameters](#API_CreateEnvironment_RequestSyntax) **   <a name="datazone-CreateEnvironment-request-userParameters"></a>
The user parameters of this Amazon DataZone environment.
Type: Array of [EnvironmentParameter](API_EnvironmentParameter.md) objects
Required: No

## Response Syntax
<a name="API_CreateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [awsAccountId](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-awsAccountId"></a>
The AWS account in which the Amazon DataZone environment is created.
Type: String
Pattern: `\d{12}`

 ** [awsAccountRegion](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-awsAccountRegion"></a>
The AWS region in which the Amazon DataZone environment is created.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`

 ** [createdAt](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-createdAt"></a>
The timestamp of when the environment was created.
Type: Timestamp

 ** [createdBy](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-createdBy"></a>
The Amazon DataZone user who created this environment.
Type: String

 ** [deploymentProperties](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-deploymentProperties"></a>
The deployment properties of this Amazon DataZone environment.
Type: [DeploymentProperties](API_DeploymentProperties.md) object

 ** [description](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-description"></a>
The description of this Amazon DataZone environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-domainId"></a>
The identifier of the Amazon DataZone domain in which the environment is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentActions](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-environmentActions"></a>
The configurable actions of this Amazon DataZone environment.
Type: Array of [ConfigurableEnvironmentAction](API_ConfigurableEnvironmentAction.md) objects

 ** [environmentBlueprintId](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-environmentBlueprintId"></a>
The ID of the blueprint with which this Amazon DataZone environment was created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [environmentConfigurationId](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-environmentConfigurationId"></a>
The configuration ID of the environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [environmentConfigurationName](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-environmentConfigurationName"></a>
The configuration name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [environmentProfileId](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-environmentProfileId"></a>
The ID of the environment profile with which this Amazon DataZone environment was created.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`

 ** [glossaryTerms](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-glossaryTerms"></a>
The glossary terms that can be used in this Amazon DataZone environment.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-id"></a>
The ID of this Amazon DataZone environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastDeployment](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-lastDeployment"></a>
The details of the last deployment of this Amazon DataZone environment.
Type: [Deployment](API_Deployment.md) object

 ** [name](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-name"></a>
The name of this environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectId](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-projectId"></a>
The ID of the Amazon DataZone project in which this environment is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [provider](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-provider"></a>
The provider of this Amazon DataZone environment.
Type: String

 ** [provisionedResources](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-provisionedResources"></a>
The provisioned resources of this Amazon DataZone environment.
Type: Array of [Resource](API_Resource.md) objects

 ** [provisioningProperties](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-provisioningProperties"></a>
The provisioning properties of this Amazon DataZone environment.
Type: [ProvisioningProperties](API_ProvisioningProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-status"></a>
The status of this Amazon DataZone environment.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED | VALIDATION_FAILED | SUSPENDED | DISABLED | EXPIRED | DELETED | INACCESSIBLE`

 ** [updatedAt](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-updatedAt"></a>
The timestamp of when this environment was updated.
Type: Timestamp

 ** [userParameters](#API_CreateEnvironment_ResponseSyntax) **   <a name="datazone-CreateEnvironment-response-userParameters"></a>
The user parameters of this Amazon DataZone environment.
Type: Array of [CustomParameter](API_CustomParameter.md) objects

## Errors
<a name="API_CreateEnvironment_Errors"></a>

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
<a name="API_CreateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateEnvironment)
