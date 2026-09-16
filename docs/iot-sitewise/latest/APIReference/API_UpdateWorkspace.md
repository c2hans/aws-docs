---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateWorkspace.html
---

# UpdateWorkspace
<a name="API_UpdateWorkspace"></a>

Updates a workspace. You can update only workspaces in the `ACTIVE` or `FAILED` state. Fields that you omit from the request are left unchanged. To recover a workspace in the `FAILED` state, call this operation and supply its encryption configuration again.

## Request Syntax
<a name="API_UpdateWorkspace_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceName}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "encryptionConfiguration": {
      "encryptionType": "{{string}}",
      "kmsKeyId": "{{string}}"
   },
   "workspaceDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWorkspace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceName](#API_UpdateWorkspace_RequestSyntax) **   <a name="iotsitewise-UpdateWorkspace-request-uri-workspaceName"></a>
The name of the workspace to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_UpdateWorkspace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateWorkspace_RequestSyntax) **   <a name="iotsitewise-UpdateWorkspace-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [encryptionConfiguration](#API_UpdateWorkspace_RequestSyntax) **   <a name="iotsitewise-UpdateWorkspace-request-encryptionConfiguration"></a>
The encryption configuration for the workspace. Omit this field to leave encryption unchanged. After a customer managed key configuration becomes active, the key can't be changed; supplying the same key is accepted.
Type: [WorkspaceEncryptionConfiguration](API_WorkspaceEncryptionConfiguration.md) object
Required: No

 ** [workspaceDescription](#API_UpdateWorkspace_RequestSyntax) **   <a name="iotsitewise-UpdateWorkspace-request-workspaceDescription"></a>
A new description for the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## Response Syntax
<a name="API_UpdateWorkspace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
<a name="API_UpdateWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workspaceStatus](#API_UpdateWorkspace_ResponseSyntax) **   <a name="iotsitewise-UpdateWorkspace-response-workspaceStatus"></a>
The status of the workspace after the update, which is `UPDATING` when the operation returns.
Type: [WorkspaceStatus](API_WorkspaceStatus.md) object

## Errors
<a name="API_UpdateWorkspace_Errors"></a>

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
<a name="API_UpdateWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/UpdateWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/UpdateWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/UpdateWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/UpdateWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/UpdateWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/UpdateWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/UpdateWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/UpdateWorkspace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/UpdateWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/UpdateWorkspace)
