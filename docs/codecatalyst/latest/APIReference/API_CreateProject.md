---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_CreateProject.html
---

# CreateProject
<a name="API_CreateProject"></a>

Creates a project in a specified space.

## Request Syntax
<a name="API_CreateProject_RequestSyntax"></a>

```
PUT /v1/spaces/{{spaceName}}/projects HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "displayName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [spaceName](#API_CreateProject_RequestSyntax) **   <a name="codecatalyst-CreateProject-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_CreateProject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateProject_RequestSyntax) **   <a name="codecatalyst-CreateProject-request-description"></a>
The description of the project. This description will be displayed to all users of the project. We recommend providing a brief description of the project and its intended purpose.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[a-zA-Z0-9]+(?:[-_a-zA-Z0-9.,;:/\+=?&$% ])*`
Required: No

 ** [displayName](#API_CreateProject_RequestSyntax) **   <a name="codecatalyst-CreateProject-request-displayName"></a>
The friendly name of the project that will be displayed to users.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\. ][a-zA-Z0-9]+)*`
Required: Yes

## Response Syntax
<a name="API_CreateProject_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "description": "string",
   "displayName": "string",
   "name": "string",
   "spaceName": "string"
}
```

## Response Elements
<a name="API_CreateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CreateProject_ResponseSyntax) **   <a name="codecatalyst-CreateProject-response-description"></a>
The description of the project.
Type: String

 ** [displayName](#API_CreateProject_ResponseSyntax) **   <a name="codecatalyst-CreateProject-response-displayName"></a>
The friendly name of the project.
Type: String

 ** [name](#API_CreateProject_ResponseSyntax) **   <a name="codecatalyst-CreateProject-response-name"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [spaceName](#API_CreateProject_ResponseSyntax) **   <a name="codecatalyst-CreateProject-response-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

## Errors
<a name="API_CreateProject_Errors"></a>

 ** AccessDeniedException **
The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.
HTTP Status Code: 403

 ** ConflictException **
The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.
HTTP Status Code: 400

## See Also
<a name="API_CreateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/CreateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/CreateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/CreateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/CreateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/CreateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/CreateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/CreateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/CreateProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/CreateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/CreateProject)
