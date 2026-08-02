---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetEnvironmentProfile.html
---

# GetEnvironmentProfile
<a name="API_GetEnvironmentProfile"></a>

Gets an evinronment profile in Amazon DataZone.

## Request Syntax
<a name="API_GetEnvironmentProfile_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/environment-profiles/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEnvironmentProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetEnvironmentProfile_RequestSyntax) **   <a name="datazone-GetEnvironmentProfile-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which this environment profile exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetEnvironmentProfile_RequestSyntax) **   <a name="datazone-GetEnvironmentProfile-request-uri-identifier"></a>
The ID of the environment profile.
Pattern: `[a-zA-Z0-9_-]{0,36}`
Required: Yes

## Request Body
<a name="API_GetEnvironmentProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEnvironmentProfile_ResponseSyntax"></a>

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
<a name="API_GetEnvironmentProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsAccountId](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-awsAccountId"></a>
The ID of the AWS account where this environment profile exists.
Type: String
Pattern: `\d{12}`

 ** [awsAccountRegion](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-awsAccountRegion"></a>
The AWS region where this environment profile exists.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`

 ** [createdAt](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-createdAt"></a>
The timestamp of when this environment profile was created.
Type: Timestamp

 ** [createdBy](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-createdBy"></a>
The Amazon DataZone user who created this environment profile.
Type: String

 ** [description](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-description"></a>
The description of the environment profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-domainId"></a>
The ID of the Amazon DataZone domain in which this environment profile exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentBlueprintId](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-environmentBlueprintId"></a>
The ID of the blueprint with which this environment profile is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-id"></a>
The ID of the environment profile.
Type: String
Pattern: `[a-zA-Z0-9_-]{0,36}`

 ** [name](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-name"></a>
The name of the environment profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [projectId](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-projectId"></a>
The ID of the Amazon DataZone project in which this environment profile is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [updatedAt](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-updatedAt"></a>
The timestamp of when this environment profile was upated.
Type: Timestamp

 ** [userParameters](#API_GetEnvironmentProfile_ResponseSyntax) **   <a name="datazone-GetEnvironmentProfile-response-userParameters"></a>
The user parameters of the environment profile.
Type: Array of [CustomParameter](API_CustomParameter.md) objects

## Errors
<a name="API_GetEnvironmentProfile_Errors"></a>

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
<a name="API_GetEnvironmentProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetEnvironmentProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetEnvironmentProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetEnvironmentProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetEnvironmentProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetEnvironmentProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetEnvironmentProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetEnvironmentProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetEnvironmentProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetEnvironmentProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetEnvironmentProfile)
