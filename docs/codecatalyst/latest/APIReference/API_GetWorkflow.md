---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetWorkflow.html
---

# GetWorkflow
<a name="API_GetWorkflow"></a>

Returns information about a workflow.

## Request Syntax
<a name="API_GetWorkflow_RequestSyntax"></a>

```
GET /v1/spaces/{{spaceName}}/projects/{{projectName}}/workflows/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetWorkflow_RequestSyntax) **   <a name="codecatalyst-GetWorkflow-request-uri-id"></a>
The ID of the workflow. To rerieve a list of workflow IDs, use [ListWorkflows](API_ListWorkflows.md).
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [projectName](#API_GetWorkflow_RequestSyntax) **   <a name="codecatalyst-GetWorkflow-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_GetWorkflow_RequestSyntax) **   <a name="codecatalyst-GetWorkflow-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_GetWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdTime": "string",
   "definition": {
      "path": "string"
   },
   "id": "string",
   "lastUpdatedTime": "string",
   "name": "string",
   "projectName": "string",
   "runMode": "string",
   "sourceBranchName": "string",
   "sourceRepositoryName": "string",
   "spaceName": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdTime](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-createdTime"></a>
The date and time the workflow was created, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6)
Type: Timestamp

 ** [definition](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-definition"></a>
Information about the workflow definition file for the workflow.
Type: [WorkflowDefinition](API_WorkflowDefinition.md) object

 ** [id](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-id"></a>
The ID of the workflow.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [lastUpdatedTime](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-lastUpdatedTime"></a>
The date and time the workflow was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6)
Type: Timestamp

 ** [name](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-name"></a>
The name of the workflow.
Type: String

 ** [projectName](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-projectName"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [runMode](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-runMode"></a>
The behavior to use when multiple workflows occur at the same time. For more information, see [https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-configure-runs.html](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-configure-runs.html) in the Amazon CodeCatalyst User Guide.
Type: String
Valid Values: `QUEUED | PARALLEL | SUPERSEDED`

 ** [sourceBranchName](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-sourceBranchName"></a>
The name of the branch that contains the workflow YAML.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [sourceRepositoryName](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-sourceRepositoryName"></a>
The name of the source repository where the workflow YAML is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!.*[.]git$)[\w\-.]*`

 ** [spaceName](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [status](#API_GetWorkflow_ResponseSyntax) **   <a name="codecatalyst-GetWorkflow-response-status"></a>
The status of the workflow.
Type: String
Valid Values: `INVALID | ACTIVE`

## Errors
<a name="API_GetWorkflow_Errors"></a>

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
<a name="API_GetWorkflow_Examples"></a>

### Example
<a name="API_GetWorkflow_Example_1"></a>

The following example illustrates using `GetWorkflow` to retrieve information about a workflow named *MyDemoWorkflow* in the *MyDemoProject* project that is part of the *ExampleCorp* space.

#### Sample Request
<a name="API_GetWorkflow_Example_1_Request"></a>

```
GET https://codecatalyst.global.api.aws/v1/spaces/ExampleCorp/projects/MyDemoProject/workflows/MyDemoWorkflow
Host: codecatalyst.global.api.aws
User-Agent: aws-cli/2.9.12 Python/3.9.11 Darwin/21.6.0 exe/x86_64 prompt/off command/codecatalyst.get-workflow
Content-Type: application/json
Authorization: Bearer AKIAI44QH8DHBEXAMPLE

{}
```

#### Sample Response
<a name="API_GetWorkflow_Example_1_Response"></a>

```
200 OK 642b
Content-Type: application/json; charset=utf-8
Date: Tue, 01 Aug 2023 19:31:23 GMT

{
   "spaceName": "ExampleCorp",
   "projectName": "MyDemoProject",
   "name": "MyDemoWorkflow",
   "sourceRepository": {
        "name": "MyDemoRepo",
        "defaultBranch": "main",
        "metadata": null
    },
    "sourceBranch": {
        "branchName": "refs/heads/main",
        "headCommitId": "12345678EXAMPLE"
    },
    "definition": {
        "definition": "...",
        "path": ".codecatalyst/workflows/MyDemoWorkflow.yaml",
        "format": "YAML"
    },
    "createdTime": "2022-10-27T22:34:57.734Z",
    "lastUpdatedTime": "2022-10-31T16:48:35.623Z"
    "runMode": "QUEUED",
    "status": "ACTIVE"
    "latestRuns": {
        "items": [
            {
                "workflowVersion": 1,
                "id": "example-workflow-run-id-123abc"
            }
        ]
    }
}
```

## See Also
<a name="API_GetWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/GetWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/GetWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/GetWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/GetWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/GetWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/GetWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/GetWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/GetWorkflow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/GetWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/GetWorkflow)
