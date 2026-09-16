---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateProject.html
---

# UpdateProject
<a name="API_UpdateProject"></a>

Updates the specified project in Amazon DataZone.

## Request Syntax
<a name="API_UpdateProject_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/projects/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "domainUnitId": "{{string}}",
   "environmentDeploymentDetails": {
      "environmentFailureReasons": {
         "{{string}}" : [
            {
               "code": "{{string}}",
               "message": "{{string}}"
            }
         ]
      },
      "overallDeploymentStatus": "{{string}}"
   },
   "glossaryTerms": [ "{{string}}" ],
   "name": "{{string}}",
   "projectProfileVersion": "{{string}}",
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
<a name="API_UpdateProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateProject_RequestSyntax) **   <a name="datazone-UpdateProject-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain where a project is being updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateProject_RequestSyntax) **   <a name="datazone-UpdateProject-request-uri-identifier"></a>
The identifier of the project that is to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateProject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateProject_RequestSyntax) **   <a name="datazone-UpdateProject-request-description"></a>
The description to be updated as part of the `UpdateProject` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [domainUnitId](#API_UpdateProject_RequestSyntax) **   <a name="datazone-UpdateProject-request-domainUnitId"></a>
The ID of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: No

 ** [environmentDeploymentDetails](#API_UpdateProject_RequestSyntax) **   <a name="datazone-UpdateProject-request-environmentDeploymentDetails"></a>
The environment deployment details of the project.
Type: [EnvironmentDeploymentDetails](API_EnvironmentDeploymentDetails.md) object
Required: No

 ** [glossaryTerms](#API_UpdateProject_RequestSyntax) **   <a name="datazone-UpdateProject-request-glossaryTerms"></a>
The glossary terms to be updated as part of the `UpdateProject` action.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [name](#API_UpdateProject_RequestSyntax) **   <a name="datazone-UpdateProject-request-name"></a>
The name to be updated as part of the `UpdateProject` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: No

 ** [projectProfileVersion](#API_UpdateProject_RequestSyntax) **   <a name="datazone-UpdateProject-request-projectProfileVersion"></a>
The project profile version to which the project should be updated. You can only specify the following string for this parameter: `latest`.
Type: String
Required: No

 ** [resourceTags](#API_UpdateProject_RequestSyntax) **   <a name="datazone-UpdateProject-request-resourceTags"></a>
The resource tags of the project.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w \.:/=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\w \.:/=+@-]*`
Required: No

 ** [userParameters](#API_UpdateProject_RequestSyntax) **   <a name="datazone-UpdateProject-request-userParameters"></a>
The user parameters of the project.
Type: Array of [EnvironmentConfigurationUserParameter](API_EnvironmentConfigurationUserParameter.md) objects
Required: No

## Response Syntax
<a name="API_UpdateProject_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-createdAt"></a>
The timestamp of when the project was created.
Type: Timestamp

 ** [createdBy](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-createdBy"></a>
The Amazon DataZone user who created the project.
Type: String

 ** [description](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-description"></a>
The description of the project that is to be updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-domainId"></a>
The identifier of the Amazon DataZone domain in which a project is updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [domainUnitId](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-domainUnitId"></a>
The ID of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [environmentDeploymentDetails](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-environmentDeploymentDetails"></a>
The environment deployment details of the project.
Type: [EnvironmentDeploymentDetails](API_EnvironmentDeploymentDetails.md) object

 ** [failureReasons](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-failureReasons"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: Array of [ProjectDeletionError](API_ProjectDeletionError.md) objects

 ** [glossaryTerms](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-glossaryTerms"></a>
The glossary terms of the project that are to be updated.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-id"></a>
The identifier of the project that is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastUpdatedAt](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-lastUpdatedAt"></a>
The timestamp of when the project was last updated.
Type: Timestamp

 ** [name](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-name"></a>
The name of the project that is to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectCategory](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-projectCategory"></a>
The category of the project.
Type: String

 ** [projectProfileId](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-projectProfileId"></a>
The ID of the project profile.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [projectStatus](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-projectStatus"></a>
The status of the project.
Type: String
Valid Values: `ACTIVE | DELETING | DELETE_FAILED | UPDATING | UPDATE_FAILED | MOVING`

 ** [resourceTags](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-resourceTags"></a>
The resource tags of the project.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [userParameters](#API_UpdateProject_ResponseSyntax) **   <a name="datazone-UpdateProject-response-userParameters"></a>
The user parameters of the project.
Type: Array of [EnvironmentConfigurationUserParameter](API_EnvironmentConfigurationUserParameter.md) objects

## Errors
<a name="API_UpdateProject_Errors"></a>

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
<a name="API_UpdateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateProject)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateProject)
