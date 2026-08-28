---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetSourceRepository.html
---

# GetSourceRepository
<a name="API_GetSourceRepository"></a>

Returns information about a source repository.

## Request Syntax
<a name="API_GetSourceRepository_RequestSyntax"></a>

```
GET /v1/spaces/{{spaceName}}/projects/{{projectName}}/sourceRepositories/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSourceRepository_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_GetSourceRepository_RequestSyntax) **   <a name="codecatalyst-GetSourceRepository-request-uri-name"></a>
The name of the source repository.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!.*[.]git$)[\w\-.]*`
Required: Yes

 ** [projectName](#API_GetSourceRepository_RequestSyntax) **   <a name="codecatalyst-GetSourceRepository-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_GetSourceRepository_RequestSyntax) **   <a name="codecatalyst-GetSourceRepository-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_GetSourceRepository_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSourceRepository_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdTime": "string",
   "description": "string",
   "lastUpdatedTime": "string",
   "name": "string",
   "projectName": "string",
   "spaceName": "string"
}
```

## Response Elements
<a name="API_GetSourceRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdTime](#API_GetSourceRepository_ResponseSyntax) **   <a name="codecatalyst-GetSourceRepository-response-createdTime"></a>
The time the source repository was created, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp

 ** [description](#API_GetSourceRepository_ResponseSyntax) **   <a name="codecatalyst-GetSourceRepository-response-description"></a>
The description of the source repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [lastUpdatedTime](#API_GetSourceRepository_ResponseSyntax) **   <a name="codecatalyst-GetSourceRepository-response-lastUpdatedTime"></a>
The time the source repository was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp

 ** [name](#API_GetSourceRepository_ResponseSyntax) **   <a name="codecatalyst-GetSourceRepository-response-name"></a>
The name of the source repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!.*[.]git$)[\w\-.]*`

 ** [projectName](#API_GetSourceRepository_ResponseSyntax) **   <a name="codecatalyst-GetSourceRepository-response-projectName"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [spaceName](#API_GetSourceRepository_ResponseSyntax) **   <a name="codecatalyst-GetSourceRepository-response-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

## Errors
<a name="API_GetSourceRepository_Errors"></a>

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

## Examples
<a name="API_GetSourceRepository_Examples"></a>

### Example
<a name="API_GetSourceRepository_Example_1"></a>

The following example illustrates using `GetSourceRepository` to retrieve information about a repository named *MyDemoRepo* in the *MyDemoProject* project that is part of the *ExampleCorp* space.

#### Sample Request
<a name="API_GetSourceRepository_Example_1_Request"></a>

```
GET https://codecatalyst.global.api.aws/v1/spaces/ExampleCorp/projects/MyDemoProject/sourceRepositories/MyDemoRepo
Host: codecatalyst.global.api.aws
User-Agent: aws-cli/2.9.12 Python/3.9.11 Darwin/21.6.0 exe/x86_64 prompt/off command/codecatalyst.get-source-repository
Content-Type: application/json
Authorization: Bearer AKIAI44QH8DHBEXAMPLE
```

#### Sample Response
<a name="API_GetSourceRepository_Example_1_Response"></a>

```
200 OK 411b
Content-Type: application/json; charset=utf-8
Date: Wed, 07 Jun 2023 19:43:09 GMT

{
   "spaceName": "ExampleCorp",
   "projectName": "MyDemoProject",
   "name": "MyDemoRepo",
   "id": "EXAMPLE1-1a2b-345c-6789-de6f1EXAMPLE",
   "description": "A place for us to collaborate on our project code.",
   "createdTime": "2023-06-27T21:33:28+00:00"
}
```

## See Also
<a name="API_GetSourceRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/GetSourceRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/GetSourceRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/GetSourceRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/GetSourceRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/GetSourceRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/GetSourceRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/GetSourceRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/GetSourceRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/GetSourceRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/GetSourceRepository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
