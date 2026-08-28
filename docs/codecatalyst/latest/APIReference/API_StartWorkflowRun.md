---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_StartWorkflowRun.html
---

# StartWorkflowRun
<a name="API_StartWorkflowRun"></a>

Begins a run of a specified workflow.

## Request Syntax
<a name="API_StartWorkflowRun_RequestSyntax"></a>

```
PUT /v1/spaces/{{spaceName}}/projects/{{projectName}}/workflowRuns?workflowId={{workflowId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartWorkflowRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [projectName](#API_StartWorkflowRun_RequestSyntax) **   <a name="codecatalyst-StartWorkflowRun-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_StartWorkflowRun_RequestSyntax) **   <a name="codecatalyst-StartWorkflowRun-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [workflowId](#API_StartWorkflowRun_RequestSyntax) **   <a name="codecatalyst-StartWorkflowRun-request-uri-workflowId"></a>
The system-generated unique ID of the workflow. To retrieve a list of workflow IDs, use [ListWorkflows](API_ListWorkflows.md).
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

## Request Body
<a name="API_StartWorkflowRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartWorkflowRun_RequestSyntax) **   <a name="codecatalyst-StartWorkflowRun-request-clientToken"></a>
A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: No

## Response Syntax
<a name="API_StartWorkflowRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string",
   "projectName": "string",
   "spaceName": "string",
   "workflowId": "string"
}
```

## Response Elements
<a name="API_StartWorkflowRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_StartWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-StartWorkflowRun-response-id"></a>
The system-generated unique ID of the workflow run.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [projectName](#API_StartWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-StartWorkflowRun-response-projectName"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [spaceName](#API_StartWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-StartWorkflowRun-response-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [workflowId](#API_StartWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-StartWorkflowRun-response-workflowId"></a>
The system-generated unique ID of the workflow.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## Errors
<a name="API_StartWorkflowRun_Errors"></a>

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
<a name="API_StartWorkflowRun_Examples"></a>

### Example
<a name="API_StartWorkflowRun_Example_1"></a>

The following example illustrates using `StartWorkflowRun` to start a run of a workflow with the ID of *my-demo-workflow-id-123abc* in *MyDemoProject* project that is part of the *ExampleCorp* space.

#### Sample Request
<a name="API_StartWorkflowRun_Example_1_Request"></a>

```
POST https://codecatalyst.global.api.aws/v1/spaces/ExampleCorp/projects/MyDemoProject/workflowRuns
Host: codecatalyst.global.api.aws
User-Agent: aws-cli/2.9.12 Python/3.9.11 Darwin/21.6.0 exe/x86_64 prompt/off command/codecatalyst.list-workflows
Content-Type: application/json
Authorization: Bearer AKIAI44QH8DHBEXAMPLE

{
    "workflowId": "my-demo-workflow-id-123abc"
    "clientToken": "ExampleClientToken"
}
```

#### Sample Response
<a name="API_StartWorkflowRun_Example_1_Response"></a>

```
200 OK 642b
Content-Type: application/json; charset=utf-8
Date: Tue, 01 Aug 2023 19:31:23 GMT

{
    "spaceName": "ExampleCorp",
    "projectName": "MyDemoProject",
    "id": "example-workflow-run-id-123abc"
    "workflowId": "my-demo-workflow-id-123abc"
}
```

## See Also
<a name="API_StartWorkflowRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/StartWorkflowRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/StartWorkflowRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/StartWorkflowRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/StartWorkflowRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/StartWorkflowRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/StartWorkflowRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/StartWorkflowRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/StartWorkflowRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/StartWorkflowRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/StartWorkflowRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
