---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListWorkflows.html
---

# ListWorkflows
<a name="API_ListWorkflows"></a>

Retrieves a list of workflows in a specified project.

## Request Syntax
<a name="API_ListWorkflows_RequestSyntax"></a>

```
POST /v1/spaces/{{spaceName}}/projects/{{projectName}}/workflows?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "sortBy": [
      {
      }
   ]
}
```

## URI Request Parameters
<a name="API_ListWorkflows_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListWorkflows_RequestSyntax) **   <a name="codecatalyst-ListWorkflows-request-uri-maxResults"></a>
The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a `NextToken` element, which you can use to obtain additional results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListWorkflows_RequestSyntax) **   <a name="codecatalyst-ListWorkflows-request-uri-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [projectName](#API_ListWorkflows_RequestSyntax) **   <a name="codecatalyst-ListWorkflows-request-uri-projectName"></a>
The name of the project in the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** [spaceName](#API_ListWorkflows_RequestSyntax) **   <a name="codecatalyst-ListWorkflows-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_ListWorkflows_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sortBy](#API_ListWorkflows_RequestSyntax) **   <a name="codecatalyst-ListWorkflows-request-sortBy"></a>
Information used to sort the items in the returned list.
Type: Array of [WorkflowSortCriteria](API_WorkflowSortCriteria.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_ListWorkflows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdTime": "string",
         "definition": {
            "path": "string"
         },
         "id": "string",
         "lastUpdatedTime": "string",
         "name": "string",
         "runMode": "string",
         "sourceBranchName": "string",
         "sourceRepositoryName": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListWorkflows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListWorkflows_ResponseSyntax) **   <a name="codecatalyst-ListWorkflows-response-items"></a>
Information about the workflows in a project.
Type: Array of [WorkflowSummary](API_WorkflowSummary.md) objects

 ** [nextToken](#API_ListWorkflows_ResponseSyntax) **   <a name="codecatalyst-ListWorkflows-response-nextToken"></a>
A token returned from a call to this API to indicate the next batch of results to return, if any.
Type: String

## Errors
<a name="API_ListWorkflows_Errors"></a>

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
<a name="API_ListWorkflows_Examples"></a>

### Example
<a name="API_ListWorkflows_Example_1"></a>

The following example illustrates using `ListWorkflows` to retrieve information about workflows in the *MyDemoProject* project that is part of the *ExampleCorp* space. The request specifies that a maximum of *5* workflows be returned in the response, and that the workflows will be sorted by the time the workflow was created. In the example response, only two workflows are found.

#### Sample Request
<a name="API_ListWorkflows_Example_1_Request"></a>

```
POST https://codecatalyst.global.api.aws/v1/spaces/ExampleCorp/projects/MyDemoProject/workflows
Host: codecatalyst.global.api.aws
User-Agent: aws-cli/2.9.12 Python/3.9.11 Darwin/21.6.0 exe/x86_64 prompt/off command/codecatalyst.list-workflows
Content-Type: application/json
Authorization: Bearer AKIAI44QH8DHBEXAMPLE

{
    "nextToken": "EXAMPLE"
    "maxResults": 5
    "sortBy": {
        "key": "START_TIME"
        "direction": "ASCENDING"
    }
}
```

#### Sample Response
<a name="API_ListWorkflows_Example_1_Response"></a>

```
200 OK 642b
Content-Type: application/json; charset=utf-8
Date: Tue, 01 Aug 2023 19:31:23 GMT

{
    "spaceName": "ExampleCorp",
    "projectName": "MyDemoProject",
    "nextToken": "EXAMPLE"
    "totalCount": 2
    "items": [
        {
            "id": "my-demo-workflow-id-123abc",
            "name" "MyDemoWorkflow"
            "runMode": "QUEUED",
            "sourceRepository": {
              "name": "MyDemoRepo",
              "defaultBranch": "main",
              "metadata": null
            },
            "sourceBranch": {
              "branchName": "refs/heads/main",
              "headCommitId": "12345678EXAMPLE"
            },
            "status": "ACTIVE",
            "statusReasons": [],
            "definition": {
              "path": ".codecatalyst/workflows/myWorkflowName.yaml"
            },
            "lastUpdatedTime": "2022-10-31T16:48:35.623Z",
            "createdTime": "2022-10-27T22:34:57.734Z"
        },
        {
            "id": "an-example-workflow-id-123abc",
            "name" "ADemoWorkflow"
            "runMode": "QUEUED",
            "sourceRepository": {
              "name": "MyDemoRepo",
              "defaultBranch": "main",
              "metadata": null
            },
            "sourceBranch": {
              "branchName": "refs/heads/test",
              "headCommitId": "01234567EXAMPLE"
            },
            "status": "ACTIVE",
            "statusReasons": [],
            "definition": {
              "path": ".codecatalyst/workflows/ADemoWorkflow.yaml"
            },
            "lastUpdatedTime": "2022-10-31T16:48:35.623Z",
            "createdTime": "2022-10-27T22:34:57.734Z"
        }
    ]
}
```

## See Also
<a name="API_ListWorkflows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/ListWorkflows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/ListWorkflows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/ListWorkflows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/ListWorkflows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/ListWorkflows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/ListWorkflows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/ListWorkflows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/ListWorkflows)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/ListWorkflows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/ListWorkflows)
