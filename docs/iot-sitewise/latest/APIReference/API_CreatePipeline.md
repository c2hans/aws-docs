---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreatePipeline.html
---

# CreatePipeline
<a name="API_CreatePipeline"></a>

Creates a new pipeline in the specified workspace. A pipeline defines a directed acyclic graph (DAG) of compute nodes, where each node references a task and can declare dependencies on other nodes. Cyclic dependencies are not allowed. Nodes without dependencies run in parallel, while nodes with dependencies wait for all upstream nodes to complete successfully before starting.

You can set environment variables at the pipeline level that are shared across all compute nodes, and override them at the individual compute node level.

## Request Syntax
<a name="API_CreatePipeline_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/pipelines HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "computations": [
      {
         "computeNodeName": "{{string}}",
         "dependsOn": [ "{{string}}" ],
         "environmentVariables": {
            "{{string}}" : "{{string}}"
         },
         "taskName": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "environmentVariables": {
      "{{string}}" : "{{string}}"
   },
   "pipelineName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePipeline_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceName](#API_CreatePipeline_RequestSyntax) **   <a name="iotsitewise-CreatePipeline-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_CreatePipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreatePipeline_RequestSyntax) **   <a name="iotsitewise-CreatePipeline-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the cached result from the original successful request without performing the operation again.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [computations](#API_CreatePipeline_RequestSyntax) **   <a name="iotsitewise-CreatePipeline-request-computations"></a>
The list of compute nodes that form the pipeline DAG. Each compute node references a task and can declare dependencies on other nodes.
Type: Array of [ComputeNode](API_ComputeNode.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** [description](#API_CreatePipeline_RequestSyntax) **   <a name="iotsitewise-CreatePipeline-request-description"></a>
A description of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [environmentVariables](#API_CreatePipeline_RequestSyntax) **   <a name="iotsitewise-CreatePipeline-request-environmentVariables"></a>
Environment variables shared across all compute nodes in the pipeline. Individual compute nodes can override these values with their own environment variables.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `(?!(?i)AWS_)[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [pipelineName](#API_CreatePipeline_RequestSyntax) **   <a name="iotsitewise-CreatePipeline-request-pipelineName"></a>
The name of the pipeline to create. Must be unique within the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [tags](#API_CreatePipeline_RequestSyntax) **   <a name="iotsitewise-CreatePipeline-request-tags"></a>
A list of key-value pairs that contain metadata for the pipeline. For more information, see [Tagging your IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the IoT SiteWise User Guide.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreatePipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "pipelineArn": "string",
   "pipelineName": "string",
   "status": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   },
   "version": "string"
}
```

## Response Elements
<a name="API_CreatePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pipelineArn](#API_CreatePipeline_ResponseSyntax) **   <a name="iotsitewise-CreatePipeline-response-pipelineArn"></a>
The ARN of the created pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [pipelineName](#API_CreatePipeline_ResponseSyntax) **   <a name="iotsitewise-CreatePipeline-response-pipelineName"></a>
The name of the created pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [status](#API_CreatePipeline_ResponseSyntax) **   <a name="iotsitewise-CreatePipeline-response-status"></a>
The current lifecycle status of the pipeline.
Type: [ResourceStatus](API_ResourceStatus.md) object

 ** [version](#API_CreatePipeline_ResponseSyntax) **   <a name="iotsitewise-CreatePipeline-response-version"></a>
The version of the newly created pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

## Errors
<a name="API_CreatePipeline_Errors"></a>

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
<a name="API_CreatePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreatePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreatePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreatePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreatePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreatePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreatePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreatePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreatePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreatePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreatePipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
