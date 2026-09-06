---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetWorkflowExecution.html
---

# GetWorkflowExecution
<a name="API_GetWorkflowExecution"></a>

Get the runtime information that was logged for a specific runtime instance of the workflow.

## Request Syntax
<a name="API_GetWorkflowExecution_RequestSyntax"></a>

```
GET /GetWorkflowExecution?workflowExecutionId={{workflowExecutionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflowExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowExecutionId](#API_GetWorkflowExecution_RequestSyntax) **   <a name="imagebuilder-GetWorkflowExecution-request-uri-workflowExecutionId"></a>
Use the unique identifier for a runtime instance of the workflow to get runtime details.
Pattern: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

## Request Body
<a name="API_GetWorkflowExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflowExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endTime": "string",
   "imageBuildVersionArn": "string",
   "message": "string",
   "parallelGroup": "string",
   "requestId": "string",
   "startTime": "string",
   "status": "string",
   "totalStepCount": number,
   "totalStepsFailed": number,
   "totalStepsSkipped": number,
   "totalStepsSucceeded": number,
   "type": "string",
   "workflowBuildVersionArn": "string",
   "workflowExecutionId": "string"
}
```

## Response Elements
<a name="API_GetWorkflowExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endTime](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-endTime"></a>
The timestamp when the specified runtime instance of the workflow finished.
Type: String

 ** [imageBuildVersionArn](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image resource build version that the specified runtime instance of the workflow created.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [message](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-message"></a>
The output message from the specified runtime instance of the workflow, if applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [parallelGroup](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-parallelGroup"></a>
Test workflows are defined within named runtime groups. The parallel group is a named group that contains one or more test workflows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[A-Za-z0-9][A-Za-z0-9-_+#]{0,99}$`

 ** [requestId](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [startTime](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-startTime"></a>
The timestamp when the specified runtime instance of the workflow started.
Type: String

 ** [status](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-status"></a>
The current runtime status for the specified runtime instance of the workflow.
Type: String
Valid Values: `PENDING | SKIPPED | RUNNING | COMPLETED | FAILED | ROLLBACK_IN_PROGRESS | ROLLBACK_COMPLETED | CANCELLED`

 ** [totalStepCount](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-totalStepCount"></a>
The total number of steps in the specified runtime instance of the workflow that ran. This number should equal the sum of the step counts for steps that succeeded, were skipped, and failed.
Type: Integer

 ** [totalStepsFailed](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-totalStepsFailed"></a>
A runtime count for the number of steps that failed in the specified runtime instance of the workflow.
Type: Integer

 ** [totalStepsSkipped](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-totalStepsSkipped"></a>
A runtime count for the number of steps that were skipped in the specified runtime instance of the workflow.
Type: Integer

 ** [totalStepsSucceeded](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-totalStepsSucceeded"></a>
A runtime count for the number of steps that ran successfully in the specified runtime instance of the workflow.
Type: Integer

 ** [type](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-type"></a>
The type of workflow that Image Builder ran for the specified runtime instance of the workflow.
Type: String
Valid Values: `BUILD | TEST | DISTRIBUTION`

 ** [workflowBuildVersionArn](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-workflowBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the build version for the Image Builder workflow resource that defines the specified runtime instance of the workflow.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [workflowExecutionId](#API_GetWorkflowExecution_ResponseSyntax) **   <a name="imagebuilder-GetWorkflowExecution-response-workflowExecutionId"></a>
The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.
Type: String
Pattern: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

## Errors
<a name="API_GetWorkflowExecution_Errors"></a>

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
<a name="API_GetWorkflowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetWorkflowExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetWorkflowExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetWorkflowExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetWorkflowExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetWorkflowExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetWorkflowExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetWorkflowExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetWorkflowExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetWorkflowExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetWorkflowExecution)
