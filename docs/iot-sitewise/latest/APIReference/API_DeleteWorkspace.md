---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteWorkspace.html
---

# DeleteWorkspace
<a name="API_DeleteWorkspace"></a>

Deletes a workspace. Before you delete a workspace, you must delete all resources contained in or associated with the workspace, such as datasets, time series, pipelines, and tasks.

## Request Syntax
<a name="API_DeleteWorkspace_RequestSyntax"></a>

```
DELETE /workspaces/{{workspaceName}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWorkspace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteWorkspace_RequestSyntax) **   <a name="iotsitewise-DeleteWorkspace-request-uri-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

 ** [workspaceName](#API_DeleteWorkspace_RequestSyntax) **   <a name="iotsitewise-DeleteWorkspace-request-uri-workspaceName"></a>
The name of the workspace to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_DeleteWorkspace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWorkspace_ResponseSyntax"></a>

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
<a name="API_DeleteWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workspaceStatus](#API_DeleteWorkspace_ResponseSyntax) **   <a name="iotsitewise-DeleteWorkspace-response-workspaceStatus"></a>
The status of the workspace after the deletion request, which is `DELETING` when the operation returns.
Type: [WorkspaceStatus](API_WorkspaceStatus.md) object

## Errors
<a name="API_DeleteWorkspace_Errors"></a>

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
<a name="API_DeleteWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DeleteWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DeleteWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DeleteWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DeleteWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DeleteWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DeleteWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DeleteWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DeleteWorkspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DeleteWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DeleteWorkspace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
