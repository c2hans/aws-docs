---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_PendingCreateStandbyWorkspacesRequest.html
---

# PendingCreateStandbyWorkspacesRequest
<a name="API_PendingCreateStandbyWorkspacesRequest"></a>

Information about the standby WorkSpace.

## Contents
<a name="API_PendingCreateStandbyWorkspacesRequest_Contents"></a>

 ** DirectoryId **   <a name="WorkSpaces-Type-PendingCreateStandbyWorkspacesRequest-DirectoryId"></a>
The identifier of the directory for the standby WorkSpace.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: No

 ** State **   <a name="WorkSpaces-Type-PendingCreateStandbyWorkspacesRequest-State"></a>
The operational state of the standby WorkSpace.
Type: String
Valid Values: `PENDING | AVAILABLE | IMPAIRED | UNHEALTHY | REBOOTING | STARTING | REBUILDING | RESTORING | MAINTENANCE | ADMIN_MAINTENANCE | TERMINATING | TERMINATED | SUSPENDED | UPDATING | STOPPING | STOPPED | ERROR`
Required: No

 ** UserName **   <a name="WorkSpaces-Type-PendingCreateStandbyWorkspacesRequest-UserName"></a>
Describes the standby WorkSpace that was created.
Because this operation is asynchronous, the identifier returned is not immediately available for use with other operations. For example, if you call [ DescribeWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html) before the WorkSpace is created, the information returned can be incomplete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: No

 ** WorkspaceId **   <a name="WorkSpaces-Type-PendingCreateStandbyWorkspacesRequest-WorkspaceId"></a>
The identifier of the standby WorkSpace.
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: No

## See Also
<a name="API_PendingCreateStandbyWorkspacesRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/PendingCreateStandbyWorkspacesRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/PendingCreateStandbyWorkspacesRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/PendingCreateStandbyWorkspacesRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
