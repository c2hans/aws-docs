---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_Workspace.html
---

# Workspace
<a name="API_Workspace"></a>

Describes a WorkSpace.

## Contents
<a name="API_Workspace_Contents"></a>

 ** BundleId **   <a name="WorkSpaces-Type-Workspace-BundleId"></a>
The identifier of the bundle used to create the WorkSpace.
Type: String
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: No

 ** ComputerName **   <a name="WorkSpaces-Type-Workspace-ComputerName"></a>
The name of the WorkSpace, as seen by the operating system. The format of this name varies. For more information, see [ Launch a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspaces-tutorials.html).
Type: String
Required: No

 ** DataReplicationSettings **   <a name="WorkSpaces-Type-Workspace-DataReplicationSettings"></a>
Indicates the settings of the data replication.
Type: [DataReplicationSettings](API_DataReplicationSettings.md) object
Required: No

 ** DirectoryId **   <a name="WorkSpaces-Type-Workspace-DirectoryId"></a>
The identifier of the Directory Service directory for the WorkSpace.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: No

 ** ErrorCode **   <a name="WorkSpaces-Type-Workspace-ErrorCode"></a>
The error code that is returned if the WorkSpace cannot be created.
Type: String
Required: No

 ** ErrorMessage **   <a name="WorkSpaces-Type-Workspace-ErrorMessage"></a>
The text of the error message that is returned if the WorkSpace cannot be created.
Type: String
Required: No

 ** IpAddress **   <a name="WorkSpaces-Type-Workspace-IpAddress"></a>
The IP address of the WorkSpace.
Type: String
Required: No

 ** Ipv6Address **   <a name="WorkSpaces-Type-Workspace-Ipv6Address"></a>
The IPv6 address of the WorkSpace.
Type: String
Pattern: `^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}(?::[0-9a-fA-F]{1,4}){0,6}::[0-9a-fA-F]{1,4}$`
Required: No

 ** ModificationStates **   <a name="WorkSpaces-Type-Workspace-ModificationStates"></a>
The modification states of the WorkSpace.
Type: Array of [ModificationState](API_ModificationState.md) objects
Required: No

 ** RelatedWorkspaces **   <a name="WorkSpaces-Type-Workspace-RelatedWorkspaces"></a>
The standby WorkSpace or primary WorkSpace related to the specified WorkSpace.
Type: Array of [RelatedWorkspaceProperties](API_RelatedWorkspaceProperties.md) objects
Required: No

 ** RootVolumeEncryptionEnabled **   <a name="WorkSpaces-Type-Workspace-RootVolumeEncryptionEnabled"></a>
Indicates whether the data stored on the root volume is encrypted.
Type: Boolean
Required: No

 ** StandbyWorkspacesProperties **   <a name="WorkSpaces-Type-Workspace-StandbyWorkspacesProperties"></a>
The properties of the standby WorkSpace
Type: Array of [StandbyWorkspacesProperties](API_StandbyWorkspacesProperties.md) objects
Required: No

 ** State **   <a name="WorkSpaces-Type-Workspace-State"></a>
The operational state of the WorkSpace.
+  `PENDING` – The WorkSpace is in a waiting state (for example, the WorkSpace is being created).
+  `AVAILABLE` – The WorkSpace is running and has passed the health checks.
+  `IMPAIRED` – Refer to `UNHEALTHY` state.
+  `UNHEALTHY` – The WorkSpace is not responding to health checks.
+  `REBOOTING` – The WorkSpace is being rebooted (restarted).
+  `STARTING` – The WorkSpace is starting up and health checks are being run.
+  `REBUILDING` – The WorkSpace is being rebuilt.
+  `RESTORING` – The WorkSpace is being restored.
+  `MAINTENANCE` – The WorkSpace is undergoing scheduled maintenance by AWS.
+  `ADMIN_MAINTENANCE` – The WorkSpace is undergoing maintenance by the WorkSpaces administrator.
+  `TERMINATING` – The WorkSpace is being deleted.
+  `TERMINATED` – The WorkSpace has been deleted.
+  `SUSPENDED` – The WorkSpace has been suspended for image creation.
+  `UPDATING` – The WorkSpace is undergoing an update.
+  `STOPPING` – The WorkSpace is being stopped.
+  `STOPPED` – The WorkSpace has been stopped.
+  `ERROR ` – The WorkSpace is an error state (for example, an error occurred during startup).
After a WorkSpace is terminated, the `TERMINATED` state is returned only briefly before the WorkSpace directory metadata is cleaned up, so this state is rarely returned. To confirm that a WorkSpace is terminated, check for the WorkSpace ID by using [ DescribeWorkSpaces](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html). If the WorkSpace ID isn't returned, then the WorkSpace has been successfully terminated.
Type: String
Valid Values: `PENDING | AVAILABLE | IMPAIRED | UNHEALTHY | REBOOTING | STARTING | REBUILDING | RESTORING | MAINTENANCE | ADMIN_MAINTENANCE | TERMINATING | TERMINATED | SUSPENDED | UPDATING | STOPPING | STOPPED | ERROR`
Required: No

 ** SubnetId **   <a name="WorkSpaces-Type-Workspace-SubnetId"></a>
The identifier of the subnet for the WorkSpace.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `^(subnet-([0-9a-f]{8}|[0-9a-f]{17}))$`
Required: No

 ** UserName **   <a name="WorkSpaces-Type-Workspace-UserName"></a>
The user for the WorkSpace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: No

 ** UserVolumeEncryptionEnabled **   <a name="WorkSpaces-Type-Workspace-UserVolumeEncryptionEnabled"></a>
Indicates whether the data stored on the user volume is encrypted.
Type: Boolean
Required: No

 ** VolumeEncryptionKey **   <a name="WorkSpaces-Type-Workspace-VolumeEncryptionKey"></a>
The ARN of the symmetric AWS KMS key used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric KMS keys.
Type: String
Required: No

 ** WorkspaceId **   <a name="WorkSpaces-Type-Workspace-WorkspaceId"></a>
The identifier of the WorkSpace.
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: No

 ** WorkspaceName **   <a name="WorkSpaces-Type-Workspace-WorkspaceName"></a>
The name of the user-decoupled WorkSpace.
Type: String
Pattern: `^[a-zA-Z0-9_()][a-zA-Z0-9_.()-]{1,63}$`
Required: No

 ** WorkspaceProperties **   <a name="WorkSpaces-Type-Workspace-WorkspaceProperties"></a>
The properties of the WorkSpace.
Type: [WorkspaceProperties](API_WorkspaceProperties.md) object
Required: No

## See Also
<a name="API_Workspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/Workspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/Workspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/Workspace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
