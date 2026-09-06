---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateProjectProfile.html
---

# UpdateProjectProfile
<a name="API_UpdateProjectProfile"></a>

Updates a project profile.

## Request Syntax
<a name="API_UpdateProjectProfile_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/project-profiles/{{identifier}} HTTP/1.1
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
<a name="API_UpdateProjectProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateProjectProfile_RequestSyntax) **   <a name="datazone-UpdateProjectProfile-request-uri-domainIdentifier"></a>
The ID of the domain where a project profile is to be updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateProjectProfile_RequestSyntax) **   <a name="datazone-UpdateProjectProfile-request-uri-identifier"></a>
The ID of a project profile that is to be updated.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateProjectProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowCustomProjectResourceTags](#API_UpdateProjectProfile_RequestSyntax) **   <a name="datazone-UpdateProjectProfile-request-allowCustomProjectResourceTags"></a>
Specifies whether custom project resource tags are supported.
Type: Boolean
Required: No

 ** [description](#API_UpdateProjectProfile_RequestSyntax) **   <a name="datazone-UpdateProjectProfile-request-description"></a>
The description of a project profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [domainUnitIdentifier](#API_UpdateProjectProfile_RequestSyntax) **   <a name="datazone-UpdateProjectProfile-request-domainUnitIdentifier"></a>
The ID of the domain unit where a project profile is to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: No

 ** [environmentConfigurations](#API_UpdateProjectProfile_RequestSyntax) **   <a name="datazone-UpdateProjectProfile-request-environmentConfigurations"></a>
The environment configurations of a project profile.
Type: Array of [EnvironmentConfiguration](API_EnvironmentConfiguration.md) objects
Required: No

 ** [name](#API_UpdateProjectProfile_RequestSyntax) **   <a name="datazone-UpdateProjectProfile-request-name"></a>
The name of a project profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: No

 ** [projectResourceTags](#API_UpdateProjectProfile_RequestSyntax) **   <a name="datazone-UpdateProjectProfile-request-projectResourceTags"></a>
The resource tags of the project profile.
Type: Array of [ResourceTagParameter](API_ResourceTagParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** [projectResourceTagsDescription](#API_UpdateProjectProfile_RequestSyntax) **   <a name="datazone-UpdateProjectProfile-request-projectResourceTagsDescription"></a>
Field viewable through the UI that provides a project user with the allowed resource tag specifications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [status](#API_UpdateProjectProfile_RequestSyntax) **   <a name="datazone-UpdateProjectProfile-request-status"></a>
The status of a project profile.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_UpdateProjectProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateProjectProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowCustomProjectResourceTags](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-allowCustomProjectResourceTags"></a>
Specifies whether custom project resource tags are supported.
Type: Boolean

 ** [createdAt](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-createdAt"></a>
The timestamp at which a project profile is created.
Type: Timestamp

 ** [createdBy](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-createdBy"></a>
The user who created a project profile.
Type: String

 ** [description](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-description"></a>
The description of a project profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-domainId"></a>
The ID of the domain where project profile is to be updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [domainUnitId](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-domainUnitId"></a>
The domain unit ID of the project profile to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [environmentConfigurations](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-environmentConfigurations"></a>
The environment configurations of a project profile.
Type: Array of [EnvironmentConfiguration](API_EnvironmentConfiguration.md) objects

 ** [id](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-id"></a>
The ID of the project profile.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastUpdatedAt](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-lastUpdatedAt"></a>
The timestamp at which a project profile was last updated.
Type: Timestamp

 ** [name](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-name"></a>
The name of the project profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectResourceTags](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-projectResourceTags"></a>
The resource tags of the project profile.
Type: Array of [ResourceTagParameter](API_ResourceTagParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [projectResourceTagsDescription](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-projectResourceTagsDescription"></a>
Field viewable through the UI that provides a project user with the allowed resource tag specifications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [status](#API_UpdateProjectProfile_ResponseSyntax) **   <a name="datazone-UpdateProjectProfile-response-status"></a>
The status of the project profile.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_UpdateProjectProfile_Errors"></a>

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
<a name="API_UpdateProjectProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateProjectProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateProjectProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateProjectProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateProjectProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateProjectProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateProjectProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateProjectProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateProjectProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateProjectProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateProjectProfile)
