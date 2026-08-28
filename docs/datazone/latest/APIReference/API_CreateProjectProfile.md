---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateProjectProfile.html
---

# CreateProjectProfile
<a name="API_CreateProjectProfile"></a>

Creates a project profile.

## Request Syntax
<a name="API_CreateProjectProfile_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/project-profiles HTTP/1.1
Content-type: application/json

{
   "allowCustomProjectResourceTags": {{boolean}},
   "description": "{{string}}",
   "domainUnitIdentifier": "{{string}}",
   "environmentConfigurations": [
      {
         "accountPools": [ "{{string}}" ],
         "awsAccount": { ... },
         "awsRegion": { ... },
         "configurationParameters": {
            "parameterOverrides": [
               {
                  "isEditable": {{boolean}},
                  "name": "{{string}}",
                  "value": "{{string}}"
               }
            ],
            "resolvedParameters": [
               {
                  "isEditable": {{boolean}},
                  "name": "{{string}}",
                  "value": "{{string}}"
               }
            ],
            "ssmPath": "{{string}}"
         },
         "deploymentMode": "{{string}}",
         "deploymentOrder": {{number}},
         "description": "{{string}}",
         "environmentBlueprintId": "{{string}}",
         "id": "{{string}}",
         "name": "{{string}}"
      }
   ],
   "name": "{{string}}",
   "projectResourceTags": [
      {
         "isValueEditable": {{boolean}},
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "projectResourceTagsDescription": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateProjectProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateProjectProfile_RequestSyntax) **   <a name="datazone-CreateProjectProfile-request-uri-domainIdentifier"></a>
A domain ID of the project profile.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateProjectProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowCustomProjectResourceTags](#API_CreateProjectProfile_RequestSyntax) **   <a name="datazone-CreateProjectProfile-request-allowCustomProjectResourceTags"></a>
Specifies whether custom project resource tags are supported.
Type: Boolean
Required: No

 ** [description](#API_CreateProjectProfile_RequestSyntax) **   <a name="datazone-CreateProjectProfile-request-description"></a>
A description of a project profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [domainUnitIdentifier](#API_CreateProjectProfile_RequestSyntax) **   <a name="datazone-CreateProjectProfile-request-domainUnitIdentifier"></a>
A domain unit ID of the project profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: No

 ** [environmentConfigurations](#API_CreateProjectProfile_RequestSyntax) **   <a name="datazone-CreateProjectProfile-request-environmentConfigurations"></a>
Environment configurations of the project profile.
Type: Array of [EnvironmentConfiguration](API_EnvironmentConfiguration.md) objects
Required: No

 ** [name](#API_CreateProjectProfile_RequestSyntax) **   <a name="datazone-CreateProjectProfile-request-name"></a>
Project profile name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** [projectResourceTags](#API_CreateProjectProfile_RequestSyntax) **   <a name="datazone-CreateProjectProfile-request-projectResourceTags"></a>
The resource tags of the project profile.
Type: Array of [ResourceTagParameter](API_ResourceTagParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** [projectResourceTagsDescription](#API_CreateProjectProfile_RequestSyntax) **   <a name="datazone-CreateProjectProfile-request-projectResourceTagsDescription"></a>
Field viewable through the UI that provides a project user with the allowed resource tag specifications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [status](#API_CreateProjectProfile_RequestSyntax) **   <a name="datazone-CreateProjectProfile-request-status"></a>
Project profile status.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_CreateProjectProfile_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "allowCustomProjectResourceTags": boolean,
   "createdAt": "string",
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "domainUnitId": "string",
   "environmentConfigurations": [
      {
         "accountPools": [ "string" ],
         "awsAccount": { ... },
         "awsRegion": { ... },
         "configurationParameters": {
            "parameterOverrides": [
               {
                  "isEditable": boolean,
                  "name": "string",
                  "value": "string"
               }
            ],
            "resolvedParameters": [
               {
                  "isEditable": boolean,
                  "name": "string",
                  "value": "string"
               }
            ],
            "ssmPath": "string"
         },
         "deploymentMode": "string",
         "deploymentOrder": number,
         "description": "string",
         "environmentBlueprintId": "string",
         "id": "string",
         "name": "string"
      }
   ],
   "id": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "projectResourceTags": [
      {
         "isValueEditable": boolean,
         "key": "string",
         "value": "string"
      }
   ],
   "projectResourceTagsDescription": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateProjectProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [allowCustomProjectResourceTags](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-allowCustomProjectResourceTags"></a>
Specifies whether custom project resource tags are supported.
Type: Boolean

 ** [createdAt](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-createdAt"></a>
A timestamp at which a project profile is created.
Type: Timestamp

 ** [createdBy](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-createdBy"></a>
A user who created a project profile.
Type: String

 ** [description](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-description"></a>
A project profile description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-domainId"></a>
The ID of the domain where a project profile is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [domainUnitId](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-domainUnitId"></a>
The ID of the domain unit where a project profile is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [environmentConfigurations](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-environmentConfigurations"></a>
Environment configurations of a project profile.
Type: Array of [EnvironmentConfiguration](API_EnvironmentConfiguration.md) objects

 ** [id](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-id"></a>
Project profile ID.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastUpdatedAt](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-lastUpdatedAt"></a>
A timestamp when a project profile was last updated.
Type: Timestamp

 ** [name](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-name"></a>
Project profile name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectResourceTags](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-projectResourceTags"></a>
The resource tags of the project profile.
Type: Array of [ResourceTagParameter](API_ResourceTagParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [projectResourceTagsDescription](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-projectResourceTagsDescription"></a>
Field viewable through the UI that provides a project user with the allowed resource tag specifications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [status](#API_CreateProjectProfile_ResponseSyntax) **   <a name="datazone-CreateProjectProfile-response-status"></a>
Project profile status.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_CreateProjectProfile_Errors"></a>

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
<a name="API_CreateProjectProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateProjectProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateProjectProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateProjectProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateProjectProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateProjectProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateProjectProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateProjectProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateProjectProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateProjectProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateProjectProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
