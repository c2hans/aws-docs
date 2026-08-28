---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetWorkflowRun.html
---

# GetWorkflowRun
<a name="API_GetWorkflowRun"></a>

Returns information about a specified run of a workflow.

## Request Syntax
<a name="API_GetWorkflowRun_RequestSyntax"></a>

```
GET /v1/spaces/{{spaceName}}/projects/{{projectName}}/workflowRuns/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflowRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetWorkflowRun_RequestSyntax) **   <a name="codecatalyst-GetWorkflowRun-request-uri-id"></a>
The ID of the workflow run. To retrieve a list of workflow run IDs, use [ListWorkflowRuns](API_ListWorkflowRuns.md).
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [projectName](#API_GetWorkflowRun_RequestSyntax) **   <a name="codecatalyst-GetWorkflowRun-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_GetWorkflowRun_RequestSyntax) **   <a name="codecatalyst-GetWorkflowRun-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_GetWorkflowRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflowRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endTime": "string",
   "id": "string",
   "lastUpdatedTime": "string",
   "projectName": "string",
   "spaceName": "string",
   "startTime": "string",
   "status": "string",
   "statusReasons": [
      {
      }
   ],
   "workflowId": "string"
}
```

## Response Elements
<a name="API_GetWorkflowRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endTime](#API_GetWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-GetWorkflowRun-response-endTime"></a>
The date and time the workflow run ended, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp

 ** [id](#API_GetWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-GetWorkflowRun-response-id"></a>
The ID of the workflow run.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [lastUpdatedTime](#API_GetWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-GetWorkflowRun-response-lastUpdatedTime"></a>
The date and time the workflow run status was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6)
Type: Timestamp

 ** [projectName](#API_GetWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-GetWorkflowRun-response-projectName"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [spaceName](#API_GetWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-GetWorkflowRun-response-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [startTime](#API_GetWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-GetWorkflowRun-response-startTime"></a>
The date and time the workflow run began, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6)
Type: Timestamp

 ** [status](#API_GetWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-GetWorkflowRun-response-status"></a>
The status of the workflow run.
Type: String
Valid Values: `SUCCEEDED | FAILED | STOPPED | SUPERSEDED | CANCELLED | NOT_RUN | VALIDATING | PROVISIONING | IN_PROGRESS | STOPPING | ABANDONED`

 ** [statusReasons](#API_GetWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-GetWorkflowRun-response-statusReasons"></a>
Information about the reasons for the status of the workflow run.
Type: Array of [WorkflowRunStatusReason](API_WorkflowRunStatusReason.md) objects

 ** [workflowId](#API_GetWorkflowRun_ResponseSyntax) **   <a name="codecatalyst-GetWorkflowRun-response-workflowId"></a>
The ID of the workflow.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## Errors
<a name="API_GetWorkflowRun_Errors"></a>

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
<a name="API_GetWorkflowRun_Examples"></a>

### Example
<a name="API_GetWorkflowRun_Example_1"></a>

The following example illustrates using `GetWorkflowRun` to retrieve information about a workflow run with the ID *example-workflow-run-id-123abc* in the *MyDemoProject* project that is part of the *ExampleCorp* space.

#### Sample Request
<a name="API_GetWorkflowRun_Example_1_Request"></a>

```
GET https://codecatalyst.global.api.aws/v1/spaces/ExampleCorp/projects/MyDemoProject/workflowRuns/example-workflow-run-id-123abc
Host: codecatalyst.global.api.aws
User-Agent: aws-cli/2.9.12 Python/3.9.11 Darwin/21.6.0 exe/x86_64 prompt/off command/codecatalyst.get-workflow-run
Content-Type: application/json
Authorization: Bearer AKIAI44QH8DHBEXAMPLE

{}
```

#### Sample Response
<a name="API_GetWorkflowRun_Example_1_Response"></a>

```
200 OK 642b
Content-Type: application/json; charset=utf-8
Date: Tue, 01 Aug 2023 19:31:23 GMT

{
    "spaceName": "ExampleCorp",
    "projectName": "MyDemoProject",
    "id": "example-workflow-run-id-123abc",
    "workflowId" "my-demo-workflow-id-123abc"
    "status": "SUCCEEDED",
    "statusReasons": []
    "startTime": "2022-10-31T16:48:41.123Z",
    "endTime": "2022-10-31T16:52:06.559Z",
    "lastUpdatedTime": "2022-10-31T16:48:35.623Z",
    "actionRuns": {
        "items": [
            {
                "name": "myAction",
                "status": "SUCCEEDED",
                "id": "example-action-run-id-123abc",
                "startTime": "2022-11-21T19:34:10.909Z",
                "endTime": "2022-11-21T19:34:13.084Z",
                "summary": {
                    "summaryMessage": {
                        "text": "ExampleSummaryMessage",
                        "label": "ExampleLabel"
                    }
                },
                "actionRunMessages": [],
                "outputArtifacts": [
                    {
                        "name": "MyOutputArtifact"
                    }
                ],
                "outputVariables": [
                    {
                        "name": "MyOutputVariable",
                        "value": "ExampleValue"
                    }
                ]
            }
        ]
    }
    "workflow": {
        "version": 3,
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "name": "MyDemoWorkflow",
        "runMode": "PARALLEL",
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
            "definition": "Name: MyDemoWorkflow\nSchemaVersion: 1.0\nRunMode: PARALLEL\n\nActions:\n  Example1:\n    Identifier: aws/workflows-example@v1\n    Outputs:\n      Artifacts:\n        - Name:\n            outputJar\n          Files:\n            - \"example.txt\"\n    Configuration:\n        Result: \"Succeed\"\n",
            "path": ".codecatalyst/workflows/MyDemoWorkflow.yaml"
        },
        "status": "ACTIVE",
        "statusReasons": [],
        "sourceBranchName": "main",
        "lastUpdatedTime": "2022-10-24T19:21:15.222Z",
        "createdTime": "2022-10-19T17:42:29.412Z",
        "latestRuns": {
            "items": [
                {
                  "workflowVersion": 3,
                  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
                }
            ]
        }
    }
}
```

## See Also
<a name="API_GetWorkflowRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/GetWorkflowRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/GetWorkflowRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/GetWorkflowRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/GetWorkflowRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/GetWorkflowRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/GetWorkflowRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/GetWorkflowRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/GetWorkflowRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/GetWorkflowRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/GetWorkflowRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
