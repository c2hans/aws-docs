---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CancelPipelineExecution.html
---

# CancelPipelineExecution
<a name="API_CancelPipelineExecution"></a>

Cancels a pipeline execution in the specified workspace. If the execution is not in a terminal state (such as NOT\_STARTED or RUNNING), it transitions to CANCELLING and asynchronously to CANCELLED. This operation is idempotent: calling it on an execution that is already CANCELLING or CANCELLED returns success with the current state. Calling it on a terminal execution (SUCCEEDED or FAILED) returns a conflict error. You can optionally provide a reason; it is returned in the stateDetails field when you describe the execution.

## Request Syntax
<a name="API_CancelPipelineExecution_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/pipelines/{{pipelineName}}/executions/{{pipelineExecutionId}}/cancel HTTP/1.1
Content-type: application/json

{
   "reason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelPipelineExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [pipelineExecutionId](#API_CancelPipelineExecution_RequestSyntax) **   <a name="iotsitewise-CancelPipelineExecution-request-uri-pipelineExecutionId"></a>
The unique identifier of the pipeline execution.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [pipelineName](#API_CancelPipelineExecution_RequestSyntax) **   <a name="iotsitewise-CancelPipelineExecution-request-uri-pipelineName"></a>
The name of the pipeline.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [workspaceName](#API_CancelPipelineExecution_RequestSyntax) **   <a name="iotsitewise-CancelPipelineExecution-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_CancelPipelineExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [reason](#API_CancelPipelineExecution_RequestSyntax) **   <a name="iotsitewise-CancelPipelineExecution-request-reason"></a>
A message describing why the pipeline execution is being cancelled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_CancelPipelineExecution_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "state": "string"
}
```

## Response Elements
<a name="API_CancelPipelineExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [state](#API_CancelPipelineExecution_ResponseSyntax) **   <a name="iotsitewise-CancelPipelineExecution-response-state"></a>
The current execution state of the pipeline. Can only be CANCELLING or CANCELLED.
Type: String
Valid Values: `NOT_STARTED | RUNNING | SUCCEEDED | FAILED | CANCELLING | CANCELLED`

## Errors
<a name="API_CancelPipelineExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CancelPipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CancelPipelineExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CancelPipelineExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CancelPipelineExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CancelPipelineExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CancelPipelineExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CancelPipelineExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CancelPipelineExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CancelPipelineExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CancelPipelineExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CancelPipelineExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
