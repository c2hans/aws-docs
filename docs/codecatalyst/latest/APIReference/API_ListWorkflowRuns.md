---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListWorkflowRuns.html
---

# ListWorkflowRuns
<a name="API_ListWorkflowRuns"></a>

Retrieves a list of workflow runs of a specified workflow.

## Request Syntax
<a name="API_ListWorkflowRuns_RequestSyntax"></a>

```
POST /v1/spaces/{{spaceName}}/projects/{{projectName}}/workflowRuns?maxResults={{maxResults}}&nextToken={{nextToken}}&workflowId={{workflowId}} HTTP/1.1
Content-type: application/json

{
   "sortBy": [
      {
      }
   ]
}
```

## URI Request Parameters
<a name="API_ListWorkflowRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListWorkflowRuns_RequestSyntax) **   <a name="codecatalyst-ListWorkflowRuns-request-uri-maxResults"></a>
The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a `NextToken` element, which you can use to obtain additional results.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListWorkflowRuns_RequestSyntax) **   <a name="codecatalyst-ListWorkflowRuns-request-uri-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [projectName](#API_ListWorkflowRuns_RequestSyntax) **   <a name="codecatalyst-ListWorkflowRuns-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_ListWorkflowRuns_RequestSyntax) **   <a name="codecatalyst-ListWorkflowRuns-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [workflowId](#API_ListWorkflowRuns_RequestSyntax) **   <a name="codecatalyst-ListWorkflowRuns-request-uri-workflowId"></a>
The ID of the workflow. To retrieve a list of workflow IDs, use [ListWorkflows](API_ListWorkflows.md).
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## Request Body
<a name="API_ListWorkflowRuns_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sortBy](#API_ListWorkflowRuns_RequestSyntax) **   <a name="codecatalyst-ListWorkflowRuns-request-sortBy"></a>
Information used to sort the items in the returned list.
Type: Array of [WorkflowRunSortCriteria](API_WorkflowRunSortCriteria.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_ListWorkflowRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "endTime": "string",
         "id": "string",
         "lastUpdatedTime": "string",
         "startTime": "string",
         "status": "string",
         "statusReasons": [
            {
            }
         ],
         "workflowId": "string",
         "workflowName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListWorkflowRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListWorkflowRuns_ResponseSyntax) **   <a name="codecatalyst-ListWorkflowRuns-response-items"></a>
Information about the runs of a workflow.
Type: Array of [WorkflowRunSummary](API_WorkflowRunSummary.md) objects

 ** [nextToken](#API_ListWorkflowRuns_ResponseSyntax) **   <a name="codecatalyst-ListWorkflowRuns-response-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Type: String

## Errors
<a name="API_ListWorkflowRuns_Errors"></a>

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
<a name="API_ListWorkflowRuns_Examples"></a>

### Example
<a name="API_ListWorkflowRuns_Example_1"></a>

The following example illustrates using `ListWorkflowRun` to retrieve information about a workflow with the ID *my-demo-workflow-id-123abc* in the *MyDemoProject* project that is part of the *ExampleCorp* space. The request specifies that a maximum of *5* workflow runs be returned in the response, and that the workflow runs will be sorted by the time the workflow run started. In the example response, only one workflow run is found.

#### Sample Request
<a name="API_ListWorkflowRuns_Example_1_Request"></a>

```
POST https://codecatalyst.global.api.aws/v1/spaces/ExampleCorp/projects/MyDemoProject/workflowRuns
Host: codecatalyst.global.api.aws
User-Agent: aws-cli/2.9.12 Python/3.9.11 Darwin/21.6.0 exe/x86_64 prompt/off command/codecatalyst.list-workflow-runs
Content-Type: application/json
Authorization: Bearer AKIAI44QH8DHBEXAMPLE

{
    "workflowId": "my-demo-workflow-id-123abc"
    "nextToken": "EXAMPLE"
    "maxResults": 5
    "sortBy": {
        "key": "START_TIME"
        "direction": "ASCENDING"
    }
}
```

#### Sample Response
<a name="API_ListWorkflowRuns_Example_1_Response"></a>

```
200 OK 642b
Content-Type: application/json; charset=utf-8
Date: Tue, 01 Aug 2023 19:31:23 GMT

{
    "spaceName": "ExampleCorp",
    "projectName": "MyDemoProject",
    "nextToken": "EXAMPLE"
    "totalCount": 1
    "items": [
        {
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
                                "text": "MySummaryMessage",
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
        }
    ]
}
```

## See Also
<a name="API_ListWorkflowRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/ListWorkflowRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/ListWorkflowRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/ListWorkflowRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/ListWorkflowRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/ListWorkflowRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/ListWorkflowRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/ListWorkflowRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/ListWorkflowRuns)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/ListWorkflowRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/ListWorkflowRuns)
