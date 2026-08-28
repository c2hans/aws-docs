---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_FailedCreateStandbyWorkspacesRequest.html
---

# FailedCreateStandbyWorkspacesRequest
<a name="API_FailedCreateStandbyWorkspacesRequest"></a>

Describes the standby WorkSpace that could not be created.

## Contents
<a name="API_FailedCreateStandbyWorkspacesRequest_Contents"></a>

 ** ErrorCode **   <a name="WorkSpaces-Type-FailedCreateStandbyWorkspacesRequest-ErrorCode"></a>
The error code that is returned if the standby WorkSpace could not be created.
Type: String
Required: No

 ** ErrorMessage **   <a name="WorkSpaces-Type-FailedCreateStandbyWorkspacesRequest-ErrorMessage"></a>
The text of the error message that is returned if the standby WorkSpace could not be created.
Type: String
Required: No

 ** StandbyWorkspaceRequest **   <a name="WorkSpaces-Type-FailedCreateStandbyWorkspacesRequest-StandbyWorkspaceRequest"></a>
Information about the standby WorkSpace that could not be created.
Type: [StandbyWorkspace](API_StandbyWorkspace.md) object
Required: No

## See Also
<a name="API_FailedCreateStandbyWorkspacesRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/FailedCreateStandbyWorkspacesRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/FailedCreateStandbyWorkspacesRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/FailedCreateStandbyWorkspacesRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
