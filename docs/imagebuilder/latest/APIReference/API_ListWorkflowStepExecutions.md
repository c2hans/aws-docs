---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflowStepExecutions.html
---

# ListWorkflowStepExecutions
<a name="API_ListWorkflowStepExecutions"></a>

Returns runtime data for each step in a runtime instance of the workflow that you specify in the request.

## Request Syntax
<a name="API_ListWorkflowStepExecutions_RequestSyntax"></a>

```
POST /ListWorkflowStepExecutions HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "workflowExecutionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWorkflowStepExecutions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWorkflowStepExecutions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListWorkflowStepExecutions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListWorkflowStepExecutions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [workflowExecutionId](#API_ListWorkflowStepExecutions_RequestSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-request-workflowExecutionId"></a>
The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.
Type: String
Pattern: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_ListWorkflowStepExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "imageBuildVersionArn": "string",
   "message": "string",
   "nextToken": "string",
   "requestId": "string",
   "steps": [
      {
         "action": "string",
         "attemptNumber": number,
         "description": "string",
         "endTime": "string",
         "inputs": "string",
         "maxAttempts": number,
         "message": "string",
         "name": "string",
         "outputs": "string",
         "rollbackStatus": "string",
         "startTime": "string",
         "status": "string",
         "stepExecutionId": "string"
      }
   ],
   "workflowBuildVersionArn": "string",
   "workflowExecutionId": "string"
}
```

## Response Elements
<a name="API_ListWorkflowStepExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageBuildVersionArn](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-imageBuildVersionArn"></a>
The image build version resource Amazon Resource Name (ARN) that's associated with the specified runtime instance of the workflow.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [message](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-message"></a>
The output message from the list action, if applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [nextToken](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [steps](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-steps"></a>
Contains an array of runtime details that represents each step in this runtime instance of the workflow.
Type: Array of [WorkflowStepMetadata](API_WorkflowStepMetadata.md) objects

 ** [workflowBuildVersionArn](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-workflowBuildVersionArn"></a>
The build version Amazon Resource Name (ARN) for the Image Builder workflow resource that defines the steps for this runtime instance of the workflow.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [workflowExecutionId](#API_ListWorkflowStepExecutions_ResponseSyntax) **   <a name="imagebuilder-ListWorkflowStepExecutions-response-workflowExecutionId"></a>
The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.
Type: String
Pattern: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

## Errors
<a name="API_ListWorkflowStepExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_ListWorkflowStepExecutions_Examples"></a>

### List the steps that ran in a workflow execution
<a name="API_ListWorkflowStepExecutions_Example_1"></a>

The following example lists runtime details for each step in the specified runtime instance of a workflow, in this case the build workflow from an image build.

#### Sample Request
<a name="API_ListWorkflowStepExecutions_Example_1_Request"></a>

```
POST /ListWorkflowStepExecutions HTTP/1.1
Content-type: application/json

{
    "workflowExecutionId": "wf-165b1cb6-3a62-4618-a021-94ddcbe32908"
}
```

#### Sample Response
<a name="API_ListWorkflowStepExecutions_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "c6258beb-bc78-40dc-8bf9-fa5a8a93d3f3",
    "steps": [
        {
            "stepExecutionId": "step-2e6fef0d-657c-4b7e-8706-ff24da9afa01",
            "name": "LaunchBuildInstance",
            "action": "LaunchInstance",
            "status": "COMPLETED",
            "inputs": "{\"waitFor\": \"ssmAgent\"}",
            "outputs": "{\"instanceId\": \"i-1234567890abcdef0\"}",
            "startTime": "2026-09-09T19:12:23.418Z",
            "endTime": "2026-09-09T19:14:50.822Z"
        },
        {
            "stepExecutionId": "step-f76c24fe-dc70-435b-8dc1-987a0ca6d5a5",
            "name": "ApplyBuildComponents",
            "action": "ExecuteComponents",
            "status": "SKIPPED",
            "inputs": "{\"instanceId.$\": \"$.stepOutputs.LaunchBuildInstance.instanceId\"}",
            "startTime": "2026-09-09T19:14:51.229Z",
            "endTime": "2026-09-09T19:14:51.229Z"
        },
        {
            "stepExecutionId": "step-aa880a39-e72c-4561-aa05-eb3de860441a",
            "name": "InventoryCollection",
            "action": "CollectImageMetadata",
            "status": "COMPLETED",
            "inputs": "{\"instanceId\": \"i-1234567890abcdef0\"}",
            "outputs": "{\"osVersion\": \"Amazon Linux 2023\", \"associationId\": \"7416ce2e-4ee8-4660-8c42-a09a03f61010\"}",
            "startTime": "2026-09-09T19:14:51.818Z",
            "endTime": "2026-09-09T19:16:26.267Z"
        },
        {
            "stepExecutionId": "step-572bdd17-25c4-4729-9f2e-7fd611807751",
            "name": "RunSanitizeScript",
            "action": "SanitizeInstance",
            "status": "COMPLETED",
            "outputs": "{\"status\": \"Success\", \"output\": \"Skipping cleanup\\n\", \"runCommandId\": \"9eef9fe1-12e8-4c97-8e9a-4e79632864f4\"}",
            "startTime": "2026-09-09T19:16:26.742Z",
            "endTime": "2026-09-09T19:16:36.559Z"
        },
        {
            "stepExecutionId": "step-06026579-939d-4b1b-b36e-fa58cb712a48",
            "name": "RunSysPrepScript",
            "action": "RunSysPrep",
            "status": "SKIPPED",
            "inputs": "{\"instanceId.$\": \"$.stepOutputs.LaunchBuildInstance.instanceId\"}",
            "startTime": "2026-09-09T19:16:36.973Z",
            "endTime": "2026-09-09T19:16:36.973Z"
        },
        {
            "stepExecutionId": "step-50e4312d-400c-453e-957c-714cbee6961c",
            "name": "CreateOutputAMI",
            "action": "CreateImage",
            "status": "COMPLETED",
            "inputs": "{\"instanceId\": \"i-1234567890abcdef0\"}",
            "outputs": "{\"imageId\": \"ami-1234567890abcdef0\"}",
            "startTime": "2026-09-09T19:16:37.499Z",
            "endTime": "2026-09-09T19:19:02.135Z"
        },
        {
            "stepExecutionId": "step-22673db0-e280-4948-b9b5-789791531c34",
            "name": "TerminateBuildInstance",
            "action": "TerminateInstance",
            "status": "COMPLETED",
            "inputs": "{\"instanceId\": \"i-1234567890abcdef0\"}",
            "startTime": "2026-09-09T19:19:02.546Z",
            "endTime": "2026-09-09T19:19:06.132Z"
        }
    ],
    "workflowBuildVersionArn": "arn:aws:imagebuilder:us-west-2:aws:workflow/build/build-image/1.0.3/1",
    "workflowExecutionId": "wf-165b1cb6-3a62-4618-a021-94ddcbe32908",
    "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1"
}
```

## See Also
<a name="API_ListWorkflowStepExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListWorkflowStepExecutions)
