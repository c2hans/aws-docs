---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetProjectProfile.html
---

# GetProjectProfile
<a name="API_GetProjectProfile"></a>

The details of the project profile.

## Request Syntax
<a name="API_GetProjectProfile_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/project-profiles/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetProjectProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetProjectProfile_RequestSyntax) **   <a name="datazone-GetProjectProfile-request-uri-domainIdentifier"></a>
The ID of the domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetProjectProfile_RequestSyntax) **   <a name="datazone-GetProjectProfile-request-uri-identifier"></a>
The ID of the project profile.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetProjectProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetProjectProfile_ResponseSyntax"></a>

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
<a name="API_GetProjectProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowCustomProjectResourceTags](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-allowCustomProjectResourceTags"></a>
Specifies whether custom project resource tags are supported.
Type: Boolean

 ** [createdAt](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-createdAt"></a>
The timestamp of when the project profile was created.
Type: Timestamp

 ** [createdBy](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-createdBy"></a>
The user who created the project profile.
Type: String

 ** [description](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-description"></a>
The description of the project profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-domainId"></a>
The ID of the domain of the project profile.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [domainUnitId](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-domainUnitId"></a>
The ID of the domain unit of the project profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [environmentConfigurations](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-environmentConfigurations"></a>
The environment configurations of the project profile.
Type: Array of [EnvironmentConfiguration](API_EnvironmentConfiguration.md) objects

 ** [id](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-id"></a>
The ID of the project profile.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastUpdatedAt](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-lastUpdatedAt"></a>
The timestamp of when project profile was last updated.
Type: Timestamp

 ** [name](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-name"></a>
The name of the project profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectResourceTags](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-projectResourceTags"></a>
The resource tags of the project profile.
Type: Array of [ResourceTagParameter](API_ResourceTagParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [projectResourceTagsDescription](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-projectResourceTagsDescription"></a>
Field viewable through the UI that provides a project user with the allowed resource tag specifications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [status](#API_GetProjectProfile_ResponseSyntax) **   <a name="datazone-GetProjectProfile-response-status"></a>
The status of the project profile.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_GetProjectProfile_Errors"></a>

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
<a name="API_GetProjectProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetProjectProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetProjectProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetProjectProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetProjectProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetProjectProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetProjectProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetProjectProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetProjectProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetProjectProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetProjectProfile)
