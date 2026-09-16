---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_StartPipelineExecution.html
---

# StartPipelineExecution
<a name="API_StartPipelineExecution"></a>

Starts execution of a pipeline in the specified workspace. Each compute node runs according to the DAG dependency order defined in the pipeline. Nodes without dependencies start immediately, while dependent nodes wait for all upstream nodes to complete successfully.

You can provide runtime environment variable overrides that take the highest priority in the environment variable hierarchy, without modifying the pipeline definition.

## Request Syntax
<a name="API_StartPipelineExecution_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/pipelines/{{pipelineName}}/executions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "executionEnvironmentVariableOverrides": {
      "computeNodes": {
         "{{string}}" : {
            "{{string}}" : "{{string}}"
         }
      },
      "global": {
         "{{string}}" : "{{string}}"
      }
   },
   "executionMountOverrides": {
      "computeNodes": {
         "{{string}}" : [
            {
               "name": "{{string}}",
               "relativePath": "{{string}}",
               "source": { ... },
               "storageType": "{{string}}"
            }
         ]
      }
   },
   "executionPriority": {{number}}
}
```

## URI Request Parameters
<a name="API_StartPipelineExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [pipelineName](#API_StartPipelineExecution_RequestSyntax) **   <a name="iotsitewise-StartPipelineExecution-request-uri-pipelineName"></a>
The name of the pipeline to execute.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [workspaceName](#API_StartPipelineExecution_RequestSyntax) **   <a name="iotsitewise-StartPipelineExecution-request-uri-workspaceName"></a>
The name of the workspace containing the pipeline.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_StartPipelineExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartPipelineExecution_RequestSyntax) **   <a name="iotsitewise-StartPipelineExecution-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the cached result from the original successful request without performing the operation again.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [executionEnvironmentVariableOverrides](#API_StartPipelineExecution_RequestSyntax) **   <a name="iotsitewise-StartPipelineExecution-request-executionEnvironmentVariableOverrides"></a>
Runtime environment variable overrides for the execution. Includes global variables that apply to all compute nodes and computeNodes for per-node overrides. These take the highest priority in the environment variable hierarchy.
Type: [ExecutionEnvironmentVariables](API_ExecutionEnvironmentVariables.md) object
Required: No

 ** [executionMountOverrides](#API_StartPipelineExecution_RequestSyntax) **   <a name="iotsitewise-StartPipelineExecution-request-executionMountOverrides"></a>
Runtime mount overrides for the execution. Overrides are merged by mount name into each listed compute node's task-defined mounts: a matching name replaces the task-defined mount, a new name adds a mount, and task-defined mounts not referenced remain unchanged. Compute nodes not listed use their task-defined mounts as-is.
Type: [MountOverrides](API_MountOverrides.md) object
Required: No

 ** [executionPriority](#API_StartPipelineExecution_RequestSyntax) **   <a name="iotsitewise-StartPipelineExecution-request-executionPriority"></a>
Scheduling priority for the execution. Lower values indicate higher priority. Defaults to 2 when not specified.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.
Required: No

## Response Syntax
<a name="API_StartPipelineExecution_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "pipelineExecutionId": "string"
}
```

## Response Elements
<a name="API_StartPipelineExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [pipelineExecutionId](#API_StartPipelineExecution_ResponseSyntax) **   <a name="iotsitewise-StartPipelineExecution-response-pipelineExecutionId"></a>
The unique identifier of the created pipeline execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_StartPipelineExecution_Errors"></a>

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

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_StartPipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/StartPipelineExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/StartPipelineExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/StartPipelineExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/StartPipelineExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/StartPipelineExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/StartPipelineExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/StartPipelineExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/StartPipelineExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/StartPipelineExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/StartPipelineExecution)
