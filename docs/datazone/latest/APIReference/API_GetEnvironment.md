---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetEnvironment.html
---

# GetEnvironment
<a name="API_GetEnvironment"></a>

Gets an Amazon DataZone environment.

## Request Syntax
<a name="API_GetEnvironment_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/environments/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetEnvironment_RequestSyntax) **   <a name="datazone-GetEnvironment-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain where the environment exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetEnvironment_RequestSyntax) **   <a name="datazone-GetEnvironment-request-uri-identifier"></a>
The ID of the Amazon DataZone environment.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetEnvironment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEnvironment_ResponseSyntax"></a>

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
<a name="API_GetEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsAccountId](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-awsAccountId"></a>
The ID of the AWS account where the environment exists.
Type: String
Pattern: `\d{12}`

 ** [awsAccountRegion](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-awsAccountRegion"></a>
The AWS region where the environment exists.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`

 ** [createdAt](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-createdAt"></a>
The timestamp of when the environment was created.
Type: Timestamp

 ** [createdBy](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-createdBy"></a>
The Amazon DataZone user who created the environment.
Type: String

 ** [deploymentProperties](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-deploymentProperties"></a>
The deployment properties of the environment.
Type: [DeploymentProperties](API_DeploymentProperties.md) object

 ** [description](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-description"></a>
The description of the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-domainId"></a>
The ID of the Amazon DataZone domain where the environment exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentActions](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-environmentActions"></a>
The actions of the environment.
Type: Array of [ConfigurableEnvironmentAction](API_ConfigurableEnvironmentAction.md) objects

 ** [environmentBlueprintId](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-environmentBlueprintId"></a>
The blueprint with which the environment is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [environmentConfigurationId](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-environmentConfigurationId"></a>
The configuration ID that is used to create the environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [environmentConfigurationName](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-environmentConfigurationName"></a>
The configuration name that is used to create the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [environmentProfileId](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-environmentProfileId"></a>
The ID of the environment profile with which the environment is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`

 ** [glossaryTerms](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-glossaryTerms"></a>
The business glossary terms that can be used in this environment.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-id"></a>
The ID of the environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastDeployment](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-lastDeployment"></a>
The details of the last deployment of the environment.
Type: [Deployment](API_Deployment.md) object

 ** [name](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectId](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-projectId"></a>
The ID of the Amazon DataZone project in which this environment is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [provider](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-provider"></a>
The provider of this Amazon DataZone environment.
Type: String

 ** [provisionedResources](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-provisionedResources"></a>
The provisioned resources of this Amazon DataZone environment.
Type: Array of [Resource](API_Resource.md) objects

 ** [provisioningProperties](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-provisioningProperties"></a>
The provisioning properties of this Amazon DataZone environment.
Type: [ProvisioningProperties](API_ProvisioningProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-status"></a>
The status of this Amazon DataZone environment.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED | VALIDATION_FAILED | SUSPENDED | DISABLED | EXPIRED | DELETED | INACCESSIBLE`

 ** [updatedAt](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-updatedAt"></a>
The timestamp of when this environment was updated.
Type: Timestamp

 ** [userParameters](#API_GetEnvironment_ResponseSyntax) **   <a name="datazone-GetEnvironment-response-userParameters"></a>
The user parameters of this Amazon DataZone environment.
Type: Array of [CustomParameter](API_CustomParameter.md) objects

## Errors
<a name="API_GetEnvironment_Errors"></a>

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
<a name="API_GetEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetEnvironment)
