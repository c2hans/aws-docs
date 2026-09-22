---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetWorkflowStepExecution.html
---

# GetWorkflowStepExecution
<a name="API_GetWorkflowStepExecution"></a>

Retrieves runtime information for a specific runtime instance of the workflow step.

## Request Syntax
<a name="API_GetWorkflowStepExecution_RequestSyntax"></a>

```
GET /GetWorkflowStepExecution?stepExecutionId={{stepExecutionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflowStepExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [stepExecutionId](#API_GetWorkflowStepExecution_RequestSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-request-uri-stepExecutionId"></a>
The unique identifier for the runtime instance of the workflow step that you want to get runtime details for. To get the identifiers for the steps that ran in a workflow, call [ListWorkflowStepExecutions](API_ListWorkflowStepExecutions.md).
Pattern: `^step-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

## Request Body
<a name="API_GetWorkflowStepExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflowStepExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "action": "string",
   "attemptNumber": number,
   "description": "string",
   "endTime": "string",
   "imageBuildVersionArn": "string",
   "inputs": "string",
   "maxAttempts": number,
   "message": "string",
   "name": "string",
   "onFailure": "string",
   "outputs": "string",
   "requestId": "string",
   "rollbackStatus": "string",
   "startTime": "string",
   "status": "string",
   "stepExecutionId": "string",
   "timeoutSeconds": number,
   "workflowBuildVersionArn": "string",
   "workflowExecutionId": "string"
}
```

## Response Elements
<a name="API_GetWorkflowStepExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-action"></a>
The name of the action that the specified step performs.
Type: String
Pattern: `^[A-Za-z][A-Za-z0-9-_]{1,99}$`

 ** [attemptNumber](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-attemptNumber"></a>
The current attempt number for the specified runtime instance of the workflow step. The first run is attempt one. The number increases by one for each retry.
Type: Integer
Valid Range: Minimum value of 1.

 ** [description](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-description"></a>
Describes the specified workflow step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [endTime](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-endTime"></a>
The timestamp when the specified runtime instance of the workflow step finished.
Type: String

 ** [imageBuildVersionArn](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image build version that owns the specified runtime instance of the workflow step.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [inputs](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-inputs"></a>
Input parameters that Image Builder provided for the specified runtime instance of the workflow step, as a JSON-encoded string.
Type: String

 ** [maxAttempts](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-maxAttempts"></a>
The maximum number of attempts allowed for the specified runtime instance of the workflow step, based on the retry configuration in the workflow document. If the step doesn't configure retries, the maximum is one attempt.
Type: Integer
Valid Range: Minimum value of 1.

 ** [message](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-message"></a>
The output message from the specified runtime instance of the workflow step, if applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [name](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-name"></a>
The name of the specified runtime instance of the workflow step.
Type: String
Pattern: `^[A-Za-z][A-Za-z0-9-_]{1,99}$`

 ** [onFailure](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-onFailure"></a>
The action that the workflow takes if this step fails, as configured in the workflow document. `Abort` fails the workflow and rolls back completed steps. `Continue` proceeds to the next step. If the step doesn't set a value, it defaults to `Abort`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [outputs](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-outputs"></a>
The output values that the specified runtime instance of the workflow step produced, as a JSON-encoded string. For example, a step that launches an instance outputs the instance ID. If the step failed, this field contains the error message.
Type: String

 ** [requestId](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [rollbackStatus](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-rollbackStatus"></a>
Reports on the rollback status of the specified runtime instance of the workflow step, if applicable. Rollback runs when the workflow execution fails, and undoes the work that completed steps performed.
Type: String
Valid Values: `RUNNING | COMPLETED | SKIPPED | FAILED`

 ** [startTime](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-startTime"></a>
The timestamp when the specified runtime instance of the workflow step started.
Type: String

 ** [status](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-status"></a>
The current status for the specified runtime instance of the workflow step.
Type: String
Valid Values: `PENDING | SKIPPED | RUNNING | COMPLETED | FAILED | CANCELLED`

 ** [stepExecutionId](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-stepExecutionId"></a>
The unique identifier for the runtime instance of the workflow step that you specified in the request.
Type: String
Pattern: `^step-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

 ** [timeoutSeconds](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-timeoutSeconds"></a>
The maximum duration in seconds for this step to complete its action. If the workflow document doesn't set a timeout for the step, Image Builder applies the default timeout for the step's action. This field returns that value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 43200.

 ** [workflowBuildVersionArn](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-workflowBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the build version for the Image Builder workflow resource that defines this workflow step.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [workflowExecutionId](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-workflowExecutionId"></a>
The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.
Type: String
Pattern: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

## Errors
<a name="API_GetWorkflowStepExecution_Errors"></a>

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
<a name="API_GetWorkflowStepExecution_Examples"></a>

### Get the runtime details of a workflow step
<a name="API_GetWorkflowStepExecution_Example_1"></a>

The following example retrieves runtime details for the step that launched the build instance during an image build, with the step's input parameters and output values returned as JSON-encoded strings.

#### Sample Request
<a name="API_GetWorkflowStepExecution_Example_1_Request"></a>

```
GET /GetWorkflowStepExecution?stepExecutionId=step-2e6fef0d-657c-4b7e-8706-ff24da9afa01 HTTP/1.1
```

#### Sample Response
<a name="API_GetWorkflowStepExecution_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "9ba63d27-9568-4ea3-bfed-6b1ad4c09200",
    "stepExecutionId": "step-2e6fef0d-657c-4b7e-8706-ff24da9afa01",
    "workflowBuildVersionArn": "arn:aws:imagebuilder:us-west-2:aws:workflow/build/build-image/1.0.3/1",
    "workflowExecutionId": "wf-165b1cb6-3a62-4618-a021-94ddcbe32908",
    "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1",
    "name": "LaunchBuildInstance",
    "action": "LaunchInstance",
    "status": "COMPLETED",
    "inputs": "{\"waitFor\": \"ssmAgent\"}",
    "outputs": "{\"instanceId\": \"i-1234567890abcdef0\"}",
    "startTime": "2026-09-09T19:12:23.418Z",
    "endTime": "2026-09-09T19:14:50.822Z",
    "onFailure": "Abort",
    "timeoutSeconds": 4500
}
```

## See Also
<a name="API_GetWorkflowStepExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetWorkflowStepExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetWorkflowStepExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetWorkflowStepExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetWorkflowStepExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetWorkflowStepExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetWorkflowStepExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetWorkflowStepExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetWorkflowStepExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetWorkflowStepExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetWorkflowStepExecution)
