---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_UpdateProject.html
---

# UpdateProject
<a name="API_UpdateProject"></a>

Changes one or more values for a project.

## Request Syntax
<a name="API_UpdateProject_RequestSyntax"></a>

```
PATCH /v1/spaces/{{spaceName}}/projects/{{name}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateProject_RequestSyntax) **   <a name="codecatalyst-UpdateProject-request-uri-name"></a>
The name of the project.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_UpdateProject_RequestSyntax) **   <a name="codecatalyst-UpdateProject-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_UpdateProject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateProject_RequestSyntax) **   <a name="codecatalyst-UpdateProject-request-description"></a>
The description of the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[a-zA-Z0-9]+(?:[-_a-zA-Z0-9.,;:/\+=?&$% ])*`
Required: No

## Response Syntax
<a name="API_UpdateProject_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "displayName": "string",
   "name": "string",
   "spaceName": "string"
}
```

## Response Elements
<a name="API_UpdateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_UpdateProject_ResponseSyntax) **   <a name="codecatalyst-UpdateProject-response-description"></a>
The description of the project.
Type: String

 ** [displayName](#API_UpdateProject_ResponseSyntax) **   <a name="codecatalyst-UpdateProject-response-displayName"></a>
The friendly name of the project displayed to users in Amazon CodeCatalyst.
Type: String

 ** [name](#API_UpdateProject_ResponseSyntax) **   <a name="codecatalyst-UpdateProject-response-name"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [spaceName](#API_UpdateProject_ResponseSyntax) **   <a name="codecatalyst-UpdateProject-response-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

## Errors
<a name="API_UpdateProject_Errors"></a>

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
<a name="API_UpdateProject_Examples"></a>

### Example
<a name="API_UpdateProject_Example_1"></a>

The following example illustrates using `UpdateProject` to change the value of the description of the *MyDemoProject* project to *My project for the August demonstration.*.

#### Sample Request
<a name="API_UpdateProject_Example_1_Request"></a>

```
PATCH https://codecatalyst.global.api.aws/v1/spaces/ExampleCorp/projects/MyDemoProject
Host: codecatalyst.global.api.aws
User-Agent: aws-cli/2.9.12 Python/3.9.11 Darwin/21.6.0 exe/x86_64 prompt/off command/codecatalyst.update-project
Content-Type: application/json
Authorization: Bearer AKIAI44QH8DHBEXAMPLE

{"description": "My project for the August demonstration."}
```

#### Sample Response
<a name="API_UpdateProject_Example_1_Response"></a>

```
200 OK 411b
Content-Type: application/json; charset=utf-8
Date: Wed, 07 Jun 2023 19:43:09 GMT

{
    "spaceName": "ExampleCorp",
    "name": "MyDemoProject",
    "displayName": "My demonstration project",
    "description": "My project for the August demonstration."
}
```

## See Also
<a name="API_UpdateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/UpdateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/UpdateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/UpdateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/UpdateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/UpdateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/UpdateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/UpdateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/UpdateProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/UpdateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/UpdateProject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
