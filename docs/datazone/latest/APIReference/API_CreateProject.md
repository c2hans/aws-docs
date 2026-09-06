---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateProject.html
---

# CreateProject
<a name="API_CreateProject"></a>

Creates an Amazon DataZone project.

## Request Syntax
<a name="API_CreateProject_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/projects HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "domainUnitId": "{{string}}",
   "glossaryTerms": [ "{{string}}" ],
   "membershipAssignments": [
      {
         "designation": "{{string}}",
         "member": { ... }
      }
   ],
   "name": "{{string}}",
   "projectCategory": "{{string}}",
   "projectExecutionRole": "{{string}}",
   "projectProfileId": "{{string}}",
   "resourceTags": {
      "{{string}}" : "{{string}}"
   },
   "userParameters": [
      {
         "environmentConfigurationName": "{{string}}",
         "environmentId": "{{string}}",
         "environmentParameters": [
            {
               "name": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "environmentResolvedAccount": {
            "awsAccountId": "{{string}}",
            "regionName": "{{string}}",
            "sourceAccountPoolId": "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which this project is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateProject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-description"></a>
The description of the Amazon DataZone project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [domainUnitId](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-domainUnitId"></a>
The ID of the domain unit. This parameter is not required and if it is not specified, then the project is created at the root domain unit level.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: No

 ** [glossaryTerms](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-glossaryTerms"></a>
The glossary terms that can be used in this Amazon DataZone project.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [membershipAssignments](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-membershipAssignments"></a>
The members to be assigned to the project.
Type: Array of [ProjectMembershipAssignment](API_ProjectMembershipAssignment.md) objects
Required: No

 ** [name](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-name"></a>
The name of the Amazon DataZone project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** [projectCategory](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-projectCategory"></a>
The category of the project. Set to 'ADMIN' designates this as an administrative project for the Amazon DataZone domain.
Type: String
Required: No

 ** [projectExecutionRole](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-projectExecutionRole"></a>
The default project IAM role that is used to access project resources and run computes such as Glue and Sagemaker.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

 ** [projectProfileId](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-projectProfileId"></a>
The ID of the project profile.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [resourceTags](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-resourceTags"></a>
The resource tags of the project.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w \.:/=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\w \.:/=+@-]*`
Required: No

 ** [userParameters](#API_CreateProject_RequestSyntax) **   <a name="datazone-CreateProject-request-userParameters"></a>
The user parameters of the project.
Type: Array of [EnvironmentConfigurationUserParameter](API_EnvironmentConfigurationUserParameter.md) objects
Required: No

## Response Syntax
<a name="API_CreateProject_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": "string",
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "domainUnitId": "string",
   "environmentDeploymentDetails": {
      "environmentFailureReasons": {
         "string" : [
            {
               "code": "string",
               "message": "string"
            }
         ]
      },
      "overallDeploymentStatus": "string"
   },
   "failureReasons": [
      {
         "code": "string",
         "message": "string"
      }
   ],
   "glossaryTerms": [ "string" ],
   "id": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "projectCategory": "string",
   "projectProfileId": "string",
   "projectStatus": "string",
   "resourceTags": [
      {
         "key": "string",
         "source": "string",
         "value": "string"
      }
   ],
   "userParameters": [
      {
         "environmentConfigurationName": "string",
         "environmentId": "string",
         "environmentParameters": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "environmentResolvedAccount": {
            "awsAccountId": "string",
            "regionName": "string",
            "sourceAccountPoolId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_CreateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-createdAt"></a>
The timestamp of when the project was created.
Type: Timestamp

 ** [createdBy](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-createdBy"></a>
The Amazon DataZone user who created the project.
Type: String

 ** [description](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-description"></a>
The description of the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-domainId"></a>
The identifier of the Amazon DataZone domain in which the project was created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [domainUnitId](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-domainUnitId"></a>
The ID of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [environmentDeploymentDetails](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-environmentDeploymentDetails"></a>
The environment deployment details.
Type: [EnvironmentDeploymentDetails](API_EnvironmentDeploymentDetails.md) object

 ** [failureReasons](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-failureReasons"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: Array of [ProjectDeletionError](API_ProjectDeletionError.md) objects

 ** [glossaryTerms](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-glossaryTerms"></a>
The glossary terms that can be used in the project.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-id"></a>
The ID of the Amazon DataZone project.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastUpdatedAt](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-lastUpdatedAt"></a>
The timestamp of when the project was last updated.
Type: Timestamp

 ** [name](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-name"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectCategory](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-projectCategory"></a>
The category of the project.
Type: String

 ** [projectProfileId](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-projectProfileId"></a>
The project profile ID.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [projectStatus](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-projectStatus"></a>
The status of the Amazon DataZone project that was created.
Type: String
Valid Values: `ACTIVE | DELETING | DELETE_FAILED | UPDATING | UPDATE_FAILED | MOVING`

 ** [resourceTags](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-resourceTags"></a>
The resource tags of the project.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [userParameters](#API_CreateProject_ResponseSyntax) **   <a name="datazone-CreateProject-response-userParameters"></a>
The user parameters of the project.
Type: Array of [EnvironmentConfigurationUserParameter](API_EnvironmentConfigurationUserParameter.md) objects

## Errors
<a name="API_CreateProject_Errors"></a>

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
<a name="API_CreateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateProject)
