---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_TerminateWorkspaces.html
---

# TerminateWorkspaces
<a name="API_TerminateWorkspaces"></a>

Terminates the specified WorkSpaces.

**Important**
Terminating a WorkSpace is a permanent action and cannot be undone. The user's data is destroyed. If you need to archive any user data, contact Support before terminating the WorkSpace.

You can terminate a WorkSpace that is in any state except `SUSPENDED`.

This operation is asynchronous and returns before the WorkSpaces have been completely terminated. After a WorkSpace is terminated, the `TERMINATED` state is returned only briefly before the WorkSpace directory metadata is cleaned up, so this state is rarely returned. To confirm that a WorkSpace is terminated, check for the WorkSpace ID by using [ DescribeWorkSpaces](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html). If the WorkSpace ID isn't returned, then the WorkSpace has been successfully terminated.

**Note**
Simple AD and AD Connector are made available to you free of charge to use with WorkSpaces. If there are no WorkSpaces being used with your Simple AD or AD Connector directory for 30 consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces, and you will be charged for this directory as per the [Directory Service pricing terms](http://aws.amazon.com/directoryservice/pricing/).
To delete empty directories, see [ Delete the Directory for Your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-workspaces-directory.html). If you delete your Simple AD or AD Connector directory, you can always create a new one when you want to start using WorkSpaces again.

## Request Syntax
<a name="API_TerminateWorkspaces_RequestSyntax"></a>

```
{
   "TerminateWorkspaceRequests": [
      {
         "WorkspaceId": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TerminateWorkspaces_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [TerminateWorkspaceRequests](#API_TerminateWorkspaces_RequestSyntax) **   <a name="WorkSpaces-TerminateWorkspaces-request-TerminateWorkspaceRequests"></a>
The WorkSpaces to terminate. You can specify up to 25 WorkSpaces.
Type: Array of [TerminateRequest](API_TerminateRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_TerminateWorkspaces_ResponseSyntax"></a>

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
<a name="API_TerminateWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedRequests](#API_TerminateWorkspaces_ResponseSyntax) **   <a name="WorkSpaces-TerminateWorkspaces-response-FailedRequests"></a>
Information about the WorkSpaces that could not be terminated.
Type: Array of [FailedWorkspaceChangeRequest](API_FailedWorkspaceChangeRequest.md) objects

## Errors
<a name="API_TerminateWorkspaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_TerminateWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/TerminateWorkspaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/TerminateWorkspaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/TerminateWorkspaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/TerminateWorkspaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/TerminateWorkspaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/TerminateWorkspaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/TerminateWorkspaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/TerminateWorkspaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/TerminateWorkspaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/TerminateWorkspaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
