---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_FailedWorkspaceChangeRequest.html
---

# FailedWorkspaceChangeRequest
<a name="API_FailedWorkspaceChangeRequest"></a>

Describes a WorkSpace that could not be rebooted. ([RebootWorkspaces](API_RebootWorkspaces.md)), rebuilt ([RebuildWorkspaces](API_RebuildWorkspaces.md)), restored ([RestoreWorkspace](API_RestoreWorkspace.md)), terminated ([TerminateWorkspaces](API_TerminateWorkspaces.md)), started ([StartWorkspaces](API_StartWorkspaces.md)), or stopped ([StopWorkspaces](API_StopWorkspaces.md)).

## Contents
<a name="API_FailedWorkspaceChangeRequest_Contents"></a>

 ** ErrorCode **   <a name="WorkSpaces-Type-FailedWorkspaceChangeRequest-ErrorCode"></a>
The error code that is returned if the WorkSpace cannot be rebooted.
Type: String
Required: No

 ** ErrorMessage **   <a name="WorkSpaces-Type-FailedWorkspaceChangeRequest-ErrorMessage"></a>
The text of the error message that is returned if the WorkSpace cannot be rebooted.
Type: String
Required: No

 ** WorkspaceId **   <a name="WorkSpaces-Type-FailedWorkspaceChangeRequest-WorkspaceId"></a>
The identifier of the WorkSpace.
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: No

## See Also
<a name="API_FailedWorkspaceChangeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/FailedWorkspaceChangeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/FailedWorkspaceChangeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/FailedWorkspaceChangeRequest)
