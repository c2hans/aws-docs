---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetProject.html
---

# GetProject
<a name="API_GetProject"></a>

Gets a project in Amazon DataZone.

## Request Syntax
<a name="API_GetProject_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/projects/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetProject_RequestSyntax) **   <a name="datazone-GetProject-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the project exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetProject_RequestSyntax) **   <a name="datazone-GetProject-request-uri-identifier"></a>
The ID of the project.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetProject_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetProject_ResponseSyntax"></a>

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
<a name="API_GetProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-createdAt"></a>
The timestamp of when the project was created.
Type: Timestamp

 ** [createdBy](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-createdBy"></a>
The Amazon DataZone user who created the project.
Type: String

 ** [description](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-description"></a>
The description of the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-domainId"></a>
The ID of the Amazon DataZone domain in which the project exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [domainUnitId](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-domainUnitId"></a>
The ID of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [environmentDeploymentDetails](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-environmentDeploymentDetails"></a>
The environment deployment status of a project.
Type: [EnvironmentDeploymentDetails](API_EnvironmentDeploymentDetails.md) object

 ** [failureReasons](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-failureReasons"></a>
Specifies the error message that is returned if the operation cannot be successfully completed.
Type: Array of [ProjectDeletionError](API_ProjectDeletionError.md) objects

 ** [glossaryTerms](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-glossaryTerms"></a>
The business glossary terms that can be used in the project.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-id"></a>
>The ID of the project.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastUpdatedAt](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-lastUpdatedAt"></a>
The timestamp of when the project was last updated.
Type: Timestamp

 ** [name](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-name"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectCategory](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-projectCategory"></a>
The category of the project.
Type: String

 ** [projectProfileId](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-projectProfileId"></a>
The ID of the project profile of a project.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [projectStatus](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-projectStatus"></a>
The status of the project.
Type: String
Valid Values: `ACTIVE | DELETING | DELETE_FAILED | UPDATING | UPDATE_FAILED | MOVING`

 ** [resourceTags](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-resourceTags"></a>
The resource tags of the project.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [userParameters](#API_GetProject_ResponseSyntax) **   <a name="datazone-GetProject-response-userParameters"></a>
The user parameters of a project.
Type: Array of [EnvironmentConfigurationUserParameter](API_EnvironmentConfigurationUserParameter.md) objects

## Errors
<a name="API_GetProject_Errors"></a>

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
<a name="API_GetProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetProject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
