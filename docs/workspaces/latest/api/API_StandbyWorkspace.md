---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_StandbyWorkspace.html
---

# StandbyWorkspace
<a name="API_StandbyWorkspace"></a>

Describes a standby WorkSpace.

## Contents
<a name="API_StandbyWorkspace_Contents"></a>

 ** DirectoryId **   <a name="WorkSpaces-Type-StandbyWorkspace-DirectoryId"></a>
The identifier of the directory for the standby WorkSpace.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** PrimaryWorkspaceId **   <a name="WorkSpaces-Type-StandbyWorkspace-PrimaryWorkspaceId"></a>
The identifier of the standby WorkSpace.
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: Yes

 ** DataReplication **   <a name="WorkSpaces-Type-StandbyWorkspace-DataReplication"></a>
Indicates whether data replication is enabled, and if enabled, the type of data replication.
Type: String
Valid Values: `NO_REPLICATION | PRIMARY_AS_SOURCE`
Required: No

 ** Tags **   <a name="WorkSpaces-Type-StandbyWorkspace-Tags"></a>
The tags associated with the standby WorkSpace.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** VolumeEncryptionKey **   <a name="WorkSpaces-Type-StandbyWorkspace-VolumeEncryptionKey"></a>
The volume encryption key of the standby WorkSpace.
Type: String
Required: No

## See Also
<a name="API_StandbyWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/StandbyWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/StandbyWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/StandbyWorkspace)
