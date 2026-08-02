---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateEnvironmentProfile.html
---

# UpdateEnvironmentProfile
<a name="API_UpdateEnvironmentProfile"></a>

Updates the specified environment profile in Amazon DataZone.

## Request Syntax
<a name="API_UpdateEnvironmentProfile_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/environment-profiles/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "awsAccountId": "{{string}}",
   "awsAccountRegion": "{{string}}",
   "description": "{{string}}",
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
<a name="API_UpdateEnvironmentProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateEnvironmentProfile_RequestSyntax) **   <a name="datazone-UpdateEnvironmentProfile-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which an environment profile is to be updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateEnvironmentProfile_RequestSyntax) **   <a name="datazone-UpdateEnvironmentProfile-request-uri-identifier"></a>
The identifier of the environment profile that is to be updated.
Pattern: `[a-zA-Z0-9_-]{0,36}`
Required: Yes

## Request Body
<a name="API_UpdateEnvironmentProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [awsAccountId](#API_UpdateEnvironmentProfile_RequestSyntax) **   <a name="datazone-UpdateEnvironmentProfile-request-awsAccountId"></a>
The AWS account in which a specified environment profile is to be udpated.
Type: String
Pattern: `\d{12}`
Required: No

 ** [awsAccountRegion](#API_UpdateEnvironmentProfile_RequestSyntax) **   <a name="datazone-UpdateEnvironmentProfile-request-awsAccountRegion"></a>
The AWS Region in which a specified environment profile is to be updated.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`
Required: No

 ** [description](#API_UpdateEnvironmentProfile_RequestSyntax) **   <a name="datazone-UpdateEnvironmentProfile-request-description"></a>
The description to be updated as part of the `UpdateEnvironmentProfile` action.
Type: String
Required: No

 ** [name](#API_UpdateEnvironmentProfile_RequestSyntax) **   <a name="datazone-UpdateEnvironmentProfile-request-name"></a>
The name to be updated as part of the `UpdateEnvironmentProfile` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: No

 ** [userParameters](#API_UpdateEnvironmentProfile_RequestSyntax) **   <a name="datazone-UpdateEnvironmentProfile-request-userParameters"></a>
The user parameters to be updated as part of the `UpdateEnvironmentProfile` action.
Type: Array of [EnvironmentParameter](API_EnvironmentParameter.md) objects
Required: No

## Response Syntax
<a name="API_UpdateEnvironmentProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateEnvironmentProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsAccountId](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-awsAccountId"></a>
The AWS account in which a specified environment profile is to be udpated.
Type: String
Pattern: `\d{12}`

 ** [awsAccountRegion](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-awsAccountRegion"></a>
The AWS Region in which a specified environment profile is to be updated.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`

 ** [createdAt](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-createdAt"></a>
The timestamp of when the environment profile was created.
Type: Timestamp

 ** [createdBy](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-createdBy"></a>
The Amazon DataZone user who created the environment profile.
Type: String

 ** [description](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-description"></a>
The description to be updated as part of the `UpdateEnvironmentProfile` action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-domainId"></a>
The identifier of the Amazon DataZone domain in which the environment profile is to be updated.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentBlueprintId](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-environmentBlueprintId"></a>
The identifier of the blueprint of the environment profile that is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-id"></a>
The identifier of the environment profile that is to be udpated.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`

 ** [name](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-name"></a>
The name to be updated as part of the `UpdateEnvironmentProfile` action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectId](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-projectId"></a>
The identifier of the project of the environment profile that is to be updated.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [updatedAt](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-updatedAt"></a>
The timestamp of when the environment profile was updated.
Type: Timestamp

 ** [userParameters](#API_UpdateEnvironmentProfile_ResponseSyntax) **   <a name="datazone-UpdateEnvironmentProfile-response-userParameters"></a>
The user parameters to be updated as part of the `UpdateEnvironmentProfile` action.
Type: Array of [CustomParameter](API_CustomParameter.md) objects

## Errors
<a name="API_UpdateEnvironmentProfile_Errors"></a>

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
<a name="API_UpdateEnvironmentProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateEnvironmentProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateEnvironmentProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateEnvironmentProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateEnvironmentProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateEnvironmentProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateEnvironmentProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateEnvironmentProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateEnvironmentProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateEnvironmentProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateEnvironmentProfile)
