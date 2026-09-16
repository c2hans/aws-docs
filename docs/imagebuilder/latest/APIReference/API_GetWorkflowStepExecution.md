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
Use the unique identifier for a specific runtime instance of the workflow step to get runtime details for that step.
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
The Amazon Resource Name (ARN) of the image resource build version that the specified runtime instance of the workflow step creates.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [inputs](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-inputs"></a>
Input parameters that Image Builder provided for the specified runtime instance of the workflow step.
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
The action to perform if the workflow step fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [outputs](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-outputs"></a>
The file names that the specified runtime version of the workflow step created as output.
Type: String

 ** [requestId](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [rollbackStatus](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-rollbackStatus"></a>
Reports on the rollback status of the specified runtime version of the workflow step, if applicable.
Type: String
Valid Values: `RUNNING | COMPLETED | SKIPPED | FAILED`

 ** [startTime](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-startTime"></a>
The timestamp when the specified runtime version of the workflow step started.
Type: String

 ** [status](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-status"></a>
The current status for the specified runtime version of the workflow step.
Type: String
Valid Values: `PENDING | SKIPPED | RUNNING | COMPLETED | FAILED | CANCELLED`

 ** [stepExecutionId](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-stepExecutionId"></a>
The unique identifier for the runtime version of the workflow step that you specified in the request.
Type: String
Pattern: `^step-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

 ** [timeoutSeconds](#API_GetWorkflowStepExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowStepExecution-response-timeoutSeconds"></a>
The maximum duration in seconds for this step to complete its action.
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
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

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
