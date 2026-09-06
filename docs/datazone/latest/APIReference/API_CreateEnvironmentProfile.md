---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateEnvironmentProfile.html
---

# CreateEnvironmentProfile
<a name="API_CreateEnvironmentProfile"></a>

Creates an Amazon DataZone environment profile.

## Request Syntax
<a name="API_CreateEnvironmentProfile_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/environment-profiles HTTP/1.1
Content-type: application/json

{
   "awsAccountId": "{{string}}",
   "awsAccountRegion": "{{string}}",
   "description": "{{string}}",
   "environmentBlueprintIdentifier": "{{string}}",
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
<a name="API_CreateEnvironmentProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateEnvironmentProfile_RequestSyntax) **   <a name="datazone-CreateEnvironmentProfile-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which this environment profile is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateEnvironmentProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [awsAccountId](#API_CreateEnvironmentProfile_RequestSyntax) **   <a name="datazone-CreateEnvironmentProfile-request-awsAccountId"></a>
The AWS account in which the Amazon DataZone environment is created.
Type: String
Pattern: `\d{12}`
Required: No

 ** [awsAccountRegion](#API_CreateEnvironmentProfile_RequestSyntax) **   <a name="datazone-CreateEnvironmentProfile-request-awsAccountRegion"></a>
The AWS region in which this environment profile is created.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`
Required: No

 ** [description](#API_CreateEnvironmentProfile_RequestSyntax) **   <a name="datazone-CreateEnvironmentProfile-request-description"></a>
The description of this Amazon DataZone environment profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [environmentBlueprintIdentifier](#API_CreateEnvironmentProfile_RequestSyntax) **   <a name="datazone-CreateEnvironmentProfile-request-environmentBlueprintIdentifier"></a>
The ID of the blueprint with which this environment profile is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [name](#API_CreateEnvironmentProfile_RequestSyntax) **   <a name="datazone-CreateEnvironmentProfile-request-name"></a>
The name of this Amazon DataZone environment profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** [projectIdentifier](#API_CreateEnvironmentProfile_RequestSyntax) **   <a name="datazone-CreateEnvironmentProfile-request-projectIdentifier"></a>
The identifier of the project in which to create the environment profile.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [userParameters](#API_CreateEnvironmentProfile_RequestSyntax) **   <a name="datazone-CreateEnvironmentProfile-request-userParameters"></a>
The user parameters of this Amazon DataZone environment profile.
Type: Array of [EnvironmentParameter](API_EnvironmentParameter.md) objects
Required: No

## Response Syntax
<a name="API_CreateEnvironmentProfile_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "awsAccountId": "string",
   "awsAccountRegion": "string",
   "createdAt": "string",
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "environmentBlueprintId": "string",
   "id": "string",
   "name": "string",
   "projectId": "string",
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
<a name="API_CreateEnvironmentProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [awsAccountId](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-awsAccountId"></a>
The AWS account ID in which this Amazon DataZone environment profile is created.
Type: String
Pattern: `\d{12}`

 ** [awsAccountRegion](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-awsAccountRegion"></a>
The AWS region in which this Amazon DataZone environment profile is created.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`

 ** [createdAt](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-createdAt"></a>
The timestamp of when this environment profile was created.
Type: Timestamp

 ** [createdBy](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-createdBy"></a>
The Amazon DataZone user who created this environment profile.
Type: String

 ** [description](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-description"></a>
The description of this Amazon DataZone environment profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-domainId"></a>
The ID of the Amazon DataZone domain in which this environment profile is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentBlueprintId](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-environmentBlueprintId"></a>
The ID of the blueprint with which this environment profile is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-id"></a>
The ID of this Amazon DataZone environment profile.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`

 ** [name](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-name"></a>
The name of this Amazon DataZone environment profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectId](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-projectId"></a>
The ID of the Amazon DataZone project in which this environment profile is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [updatedAt](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-updatedAt"></a>
The timestamp of when this environment profile was updated.
Type: Timestamp

 ** [userParameters](#API_CreateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-CreateEnvironmentProfile-response-userParameters"></a>
The user parameters of this Amazon DataZone environment profile.
Type: Array of [CustomParameter](API_CustomParameter.md) objects

## Errors
<a name="API_CreateEnvironmentProfile_Errors"></a>

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
<a name="API_CreateEnvironmentProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateEnvironmentProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateEnvironmentProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateEnvironmentProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateEnvironmentProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateEnvironmentProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateEnvironmentProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateEnvironmentProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateEnvironmentProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateEnvironmentProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateEnvironmentProfile)
