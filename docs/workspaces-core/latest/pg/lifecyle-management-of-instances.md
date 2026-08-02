---
source_url: https://docs.aws.amazon.com/workspaces-core/latest/pg/lifecyle-management-of-instances.html
---

# WorkSpaces Core bundles management
<a name="lifecyle-management-of-instances"></a>

 To perform various actions for Amazon WorkSpaces Core, use the following API operations. To help you create your workflow, we have provided a recommendation for each API operation. We recommend partners solutions use as many of these APIs as possible so that admin customers don’t need to access the WorkSpaces console.
+ Deployment and setup
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_CreateTags.html](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateTags.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccount.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccount.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccountModifications.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccountModifications.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_ImportWorkspaceImage.html](https://docs.aws.amazon.com/workspaces/latest/api/API_ImportWorkspaceImage.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyAccount.html](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyAccount.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_ListAvailableManagementCidrRanges.html](https://docs.aws.amazon.com/workspaces/latest/api/API_ListAvailableManagementCidrRanges.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_RegisterWorkspaceDirectory.html](https://docs.aws.amazon.com/workspaces/latest/api/API_RegisterWorkspaceDirectory.html)
+ Operations
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_CopyWorkspaceImage.html](https://docs.aws.amazon.com/workspaces/latest/api/API_CopyWorkspaceImage.html) – Supports an `UpdateWorkspaceBundle` image process and copying from one AWS Region to another Region.
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceImage.html](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceImage.html) – Supports custom images and workflows for day-two operations.
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeTags.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeTags.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceBundles.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceBundles.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImagePermissions.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImagePermissions.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceSnapshots.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceSnapshots.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_MigrateWorkspace.html](https://docs.aws.amazon.com/workspaces/latest/api/API_MigrateWorkspace.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceCreationProperties.html](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceCreationProperties.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceProperties.html](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceProperties.html) – Supports modification of the following properties:
    + [https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html](https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html)
    + [https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html](https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html)
    + [https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html](https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html) – BYOP must use `ALWAYS_ON` or `MANUAL`.
    + [https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html](https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceState.html](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceState.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_RebootWorkspaces.html](https://docs.aws.amazon.com/workspaces/latest/api/API_RebootWorkspaces.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_RebuildWorkspaces.html](https://docs.aws.amazon.com/workspaces/latest/api/API_RebuildWorkspaces.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_RestoreWorkspace.html](https://docs.aws.amazon.com/workspaces/latest/api/API_RestoreWorkspace.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_StartWorkspaces.html](https://docs.aws.amazon.com/workspaces/latest/api/API_StartWorkspaces.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_StopWorkspaces.html](https://docs.aws.amazon.com/workspaces/latest/api/API_StopWorkspaces.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceBundle.html](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceBundle.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceImagePermission.html](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceImagePermission.html)
+ Termination
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteTags.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteTags.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceBundle.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceBundle.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceImage.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceImage.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_DeregisterWorkspaceDirectory.html](https://docs.aws.amazon.com/workspaces/latest/api/API_DeregisterWorkspaceDirectory.html)
  + [https://docs.aws.amazon.com/workspaces/latest/api/API_TerminateWorkspaces.html](https://docs.aws.amazon.com/workspaces/latest/api/API_TerminateWorkspaces.html)
