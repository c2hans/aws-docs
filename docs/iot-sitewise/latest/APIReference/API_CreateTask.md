---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateTask.html
---

# CreateTask
<a name="API_CreateTask"></a>

Creates a new task in the specified workspace. A task defines a reusable containerized compute workload that can be referenced by one or more pipeline compute nodes.

Specify a [https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ContainerTaskConfiguration.html](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ContainerTaskConfiguration.html) for custom container workloads with configurable ECR image, processing type, processing unit, and environment variables.

## Request Syntax
<a name="API_CreateTask_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/tasks HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "taskConfiguration": { ... },
   "taskName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceName](#API_CreateTask_RequestSyntax) **   <a name="iotsitewise-CreateTask-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_CreateTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateTask_RequestSyntax) **   <a name="iotsitewise-CreateTask-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the cached result from the original successful request without performing the operation again.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [description](#API_CreateTask_RequestSyntax) **   <a name="iotsitewise-CreateTask-request-description"></a>
A description of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [tags](#API_CreateTask_RequestSyntax) **   <a name="iotsitewise-CreateTask-request-tags"></a>
A list of key-value pairs that contain metadata for the task. For more information, see [Tagging your IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the IoT SiteWise User Guide.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [taskConfiguration](#API_CreateTask_RequestSyntax) **   <a name="iotsitewise-CreateTask-request-taskConfiguration"></a>
The task execution configuration. Specify a [containerTaskConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ContainerTaskConfiguration.html) for custom container workloads.
Type: [TaskConfiguration](API_TaskConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [taskName](#API_CreateTask_RequestSyntax) **   <a name="iotsitewise-CreateTask-request-taskName"></a>
The name of the task to create. Must be unique within the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_CreateTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   },
   "taskArn": "string",
   "taskName": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_CreateTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_CreateTask_ResponseSyntax) **   <a name="iotsitewise-CreateTask-response-status"></a>
The current lifecycle status of the task.
Type: [ResourceStatus](API_ResourceStatus.md) object

 ** [taskArn](#API_CreateTask_ResponseSyntax) **   <a name="iotsitewise-CreateTask-response-taskArn"></a>
The ARN of the created task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [taskName](#API_CreateTask_ResponseSyntax) **   <a name="iotsitewise-CreateTask-response-taskName"></a>
The name of the created task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [version](#API_CreateTask_ResponseSyntax) **   <a name="iotsitewise-CreateTask-response-version"></a>
The version of the newly created task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

## Errors
<a name="API_CreateTask_Errors"></a>

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
<a name="API_CreateTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateTask)
