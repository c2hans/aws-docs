---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateWorkspace.html
---

# CreateWorkspace
<a name="API_CreateWorkspace"></a>

Creates a workspace in AWS IoT SiteWise. A workspace isolates its resources, such as datasets, time series, pipelines, and tasks, and their data from other workspaces, and has its own quotas and throttling limits. You must specify an encryption configuration when you create a workspace. The operation returns immediately with the workspace in the `CREATING` state. Provisioning completes asynchronously, after which the workspace state is `ACTIVE`, or `FAILED` if provisioning doesn't complete.

## Request Syntax
<a name="API_CreateWorkspace_RequestSyntax"></a>

```
POST /workspaces HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "encryptionConfiguration": {
      "encryptionType": "{{string}}",
      "kmsKeyId": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "workspaceDescription": "{{string}}",
   "workspaceName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkspace_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWorkspace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateWorkspace_RequestSyntax) **   <a name="iotsitewise-CreateWorkspace-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [encryptionConfiguration](#API_CreateWorkspace_RequestSyntax) **   <a name="iotsitewise-CreateWorkspace-request-encryptionConfiguration"></a>
The encryption configuration for the workspace.
Type: [WorkspaceEncryptionConfiguration](API_WorkspaceEncryptionConfiguration.md) object
Required: Yes

 ** [tags](#API_CreateWorkspace_RequestSyntax) **   <a name="iotsitewise-CreateWorkspace-request-tags"></a>
A list of key-value pairs that contain metadata for the workspace. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the * AWS IoT SiteWise User Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [workspaceDescription](#API_CreateWorkspace_RequestSyntax) **   <a name="iotsitewise-CreateWorkspace-request-workspaceDescription"></a>
A description for the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [workspaceName](#API_CreateWorkspace_RequestSyntax) **   <a name="iotsitewise-CreateWorkspace-request-workspaceName"></a>
The name of the workspace to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Response Syntax
<a name="API_CreateWorkspace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "workspaceArn": "string",
   "workspaceName": "string",
   "workspaceStatus": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   }
}
```

## Response Elements
<a name="API_CreateWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workspaceArn](#API_CreateWorkspace_ResponseSyntax) **   <a name="iotsitewise-CreateWorkspace-response-workspaceArn"></a>
The ARN of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [workspaceName](#API_CreateWorkspace_ResponseSyntax) **   <a name="iotsitewise-CreateWorkspace-response-workspaceName"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [workspaceStatus](#API_CreateWorkspace_ResponseSyntax) **   <a name="iotsitewise-CreateWorkspace-response-workspaceStatus"></a>
The status of the workspace, which is `CREATING` when the operation returns.
Type: [WorkspaceStatus](API_WorkspaceStatus.md) object

## Errors
<a name="API_CreateWorkspace_Errors"></a>

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

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CreateWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateWorkspace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateWorkspace)
