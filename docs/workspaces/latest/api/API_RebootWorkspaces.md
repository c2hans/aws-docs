---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_RebootWorkspaces.html
---

# RebootWorkspaces
<a name="API_RebootWorkspaces"></a>

Reboots the specified WorkSpaces.

You cannot reboot a WorkSpace unless its state is `AVAILABLE`, `UNHEALTHY`, or `REBOOTING`. Reboot a WorkSpace in the `REBOOTING` state only if your WorkSpace has been stuck in the `REBOOTING` state for over 20 minutes.

This operation is asynchronous and returns before the WorkSpaces have rebooted.

## Request Syntax
<a name="API_RebootWorkspaces_RequestSyntax"></a>

```
{
   "RebootWorkspaceRequests": [
      {
         "WorkspaceId": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_RebootWorkspaces_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [RebootWorkspaceRequests](#API_RebootWorkspaces_RequestSyntax) **   <a name="WorkSpaces-RebootWorkspaces-request-RebootWorkspaceRequests"></a>
The WorkSpaces to reboot. You can specify up to 25 WorkSpaces.
Type: Array of [RebootRequest](API_RebootRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_RebootWorkspaces_ResponseSyntax"></a>

```
{
   "FailedRequests": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "WorkspaceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_RebootWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedRequests](#API_RebootWorkspaces_ResponseSyntax) **   <a name="WorkSpaces-RebootWorkspaces-response-FailedRequests"></a>
Information about the WorkSpaces that could not be rebooted.
Type: Array of [FailedWorkspaceChangeRequest](API_FailedWorkspaceChangeRequest.md) objects

## Errors
<a name="API_RebootWorkspaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotSupportedException **
This operation is not supported.
 ** message **
The exception error message.
 ** reason **
The exception error reason.
HTTP Status Code: 400

## See Also
<a name="API_RebootWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/RebootWorkspaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/RebootWorkspaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/RebootWorkspaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/RebootWorkspaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/RebootWorkspaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/RebootWorkspaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/RebootWorkspaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/RebootWorkspaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/RebootWorkspaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/RebootWorkspaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
