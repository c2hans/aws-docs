---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWaitingWorkflowSteps.html
---

# ListWaitingWorkflowSteps
<a name="API_ListWaitingWorkflowSteps"></a>

Lists the workflow steps in your AWS account that have paused at a `WaitForAction` step, and are waiting for you to respond. To send a response, call [SendWorkflowStepAction](API_SendWorkflowStepAction.md).

## Request Syntax
<a name="API_ListWaitingWorkflowSteps_RequestSyntax"></a>

```
POST /ListWaitingWorkflowSteps HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWaitingWorkflowSteps_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWaitingWorkflowSteps_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListWaitingWorkflowSteps_RequestSyntax) **   <a name="imagebuilder-ListWaitingWorkflowSteps-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListWaitingWorkflowSteps_RequestSyntax) **   <a name="imagebuilder-ListWaitingWorkflowSteps-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListWaitingWorkflowSteps_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "steps": [
      {
         "action": "string",
         "imageBuildVersionArn": "string",
         "name": "string",
         "startTime": "string",
         "stepExecutionId": "string",
         "workflowBuildVersionArn": "string",
         "workflowExecutionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWaitingWorkflowSteps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWaitingWorkflowSteps_ResponseSyntax) **   <a name="imagebuilder-ListWaitingWorkflowSteps-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [steps](#API_ListWaitingWorkflowSteps_ResponseSyntax) **   <a name="imagebuilder-ListWaitingWorkflowSteps-response-steps"></a>
An array of the workflow steps that are waiting for action in your AWS account. Each step is paused at a `WaitForAction` step, and remains in the list until you respond with [SendWorkflowStepAction](API_SendWorkflowStepAction.md) or the wait times out.
Type: Array of [WorkflowStepExecution](API_WorkflowStepExecution.md) objects

## Errors
<a name="API_ListWaitingWorkflowSteps_Errors"></a>

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
<a name="API_ListWaitingWorkflowSteps_Examples"></a>

### List workflow steps that are waiting for an action
<a name="API_ListWaitingWorkflowSteps_Example_1"></a>

The following example lists the workflow steps in your account that are paused at a WaitForAction step, waiting for you to resume or stop the workflow with SendWorkflowStepAction.

#### Sample Request
<a name="API_ListWaitingWorkflowSteps_Example_1_Request"></a>

```
POST /ListWaitingWorkflowSteps HTTP/1.1
Content-type: application/json

{
    "maxResults": 25
}
```

#### Sample Response
<a name="API_ListWaitingWorkflowSteps_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "steps": [
        {
            "stepExecutionId": "step-8eb24d7a-036e-46b5-94a3-90a5d8b5ac4a",
            "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-wait-recipe/1.0.0/1",
            "workflowExecutionId": "wf-782460a6-8dc5-4262-90ff-0509eef0053c",
            "workflowBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-wait-workflow/1.0.0/1",
            "name": "WaitForApproval",
            "action": "WaitForAction",
            "startTime": "2026-09-09T20:02:59.931Z"
        }
    ]
}
```

## See Also
<a name="API_ListWaitingWorkflowSteps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListWaitingWorkflowSteps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListWaitingWorkflowSteps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListWaitingWorkflowSteps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListWaitingWorkflowSteps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListWaitingWorkflowSteps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListWaitingWorkflowSteps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListWaitingWorkflowSteps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListWaitingWorkflowSteps)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListWaitingWorkflowSteps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListWaitingWorkflowSteps)
