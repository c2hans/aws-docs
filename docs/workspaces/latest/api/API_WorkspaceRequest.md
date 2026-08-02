---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceRequest.html
---

# WorkspaceRequest
<a name="API_WorkspaceRequest"></a>

Describes the information used to create a WorkSpace.

## Contents
<a name="API_WorkspaceRequest_Contents"></a>

 ** BundleId **   <a name="WorkSpaces-Type-WorkspaceRequest-BundleId"></a>
The identifier of the bundle for the WorkSpace. You can use [DescribeWorkspaceBundles](API_DescribeWorkspaceBundles.md) to list the available bundles.
Type: String
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: Yes

 ** DirectoryId **   <a name="WorkSpaces-Type-WorkspaceRequest-DirectoryId"></a>
The identifier of the Directory Service directory for the WorkSpace. You can use [DescribeWorkspaceDirectories](API_DescribeWorkspaceDirectories.md) to list the available directories.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** UserName **   <a name="WorkSpaces-Type-WorkspaceRequest-UserName"></a>
The user name of the user for the WorkSpace. This user name must exist in the Directory Service directory for the WorkSpace.
The username is not case-sensitive, but we recommend matching the case in the Directory Service directory to avoid potential incompatibilities.
The reserved keyword, `[UNDEFINED]`, is used when creating user-decoupled WorkSpaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: Yes

 ** Ipv6Address **   <a name="WorkSpaces-Type-WorkspaceRequest-Ipv6Address"></a>
The IPv6 address for the WorkSpace.
Type: String
Pattern: `^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}(?::[0-9a-fA-F]{1,4}){0,6}::[0-9a-fA-F]{1,4}$`
Required: No

 ** RootVolumeEncryptionEnabled **   <a name="WorkSpaces-Type-WorkspaceRequest-RootVolumeEncryptionEnabled"></a>
Indicates whether the data stored on the root volume is encrypted.
Type: Boolean
Required: No

 ** Tags **   <a name="WorkSpaces-Type-WorkspaceRequest-Tags"></a>
The tags for the WorkSpace.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** UserVolumeEncryptionEnabled **   <a name="WorkSpaces-Type-WorkspaceRequest-UserVolumeEncryptionEnabled"></a>
Indicates whether the data stored on the user volume is encrypted.
Type: Boolean
Required: No

 ** VolumeEncryptionKey **   <a name="WorkSpaces-Type-WorkspaceRequest-VolumeEncryptionKey"></a>
The ARN of the symmetric AWS KMS key used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric KMS keys.
Type: String
Required: No

 ** WorkspaceName **   <a name="WorkSpaces-Type-WorkspaceRequest-WorkspaceName"></a>
The name of the user-decoupled WorkSpace.
 `WorkspaceName` is required if `UserName` is `[UNDEFINED]` for user-decoupled WorkSpaces. `WorkspaceName` is not applicable if `UserName` is specified for user-assigned WorkSpaces.
Type: String
Pattern: `^[a-zA-Z0-9_()][a-zA-Z0-9_.()-]{1,63}$`
Required: No

 ** WorkspaceProperties **   <a name="WorkSpaces-Type-WorkspaceRequest-WorkspaceProperties"></a>
The WorkSpace properties.
Type: [WorkspaceProperties](API_WorkspaceProperties.md) object
Required: No

## See Also
<a name="API_WorkspaceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspaceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspaceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspaceRequest)
