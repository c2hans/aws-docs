---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Workspace.html
---

# Workspace
<a name="API_Workspace"></a>

Contains information about a workspace, which defines the user experience by mapping views to pages.

## Contents
<a name="API_Workspace_Contents"></a>

 ** Arn **   <a name="connect-Type-Workspace-Arn"></a>
The Amazon Resource Name (ARN) of the workspace.
Type: String
Required: Yes

 ** Id **   <a name="connect-Type-Workspace-Id"></a>
The unique identifier of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-Workspace-LastModifiedTime"></a>
The timestamp when the workspace was last modified.
Type: Timestamp
Required: Yes

 ** Name **   <a name="connect-Type-Workspace-Name"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: Yes

 ** Description **   <a name="connect-Type-Workspace-Description"></a>
The description of the workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^[\\P{C}\r\n\t]*$`
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-Workspace-LastModifiedRegion"></a>
The AWS Region where the workspace was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** Tags **   <a name="connect-Type-Workspace-Tags"></a>
The tags used to organize, track, or control access for the workspace.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** Theme **   <a name="connect-Type-Workspace-Theme"></a>
The theme configuration for the workspace, including colors and styling.
Type: [WorkspaceTheme](API_WorkspaceTheme.md) object
Required: No

 ** Title **   <a name="connect-Type-Workspace-Title"></a>
The title displayed for the workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 127.
Pattern: `^[\\P{C}]*$`
Required: No

 ** Visibility **   <a name="connect-Type-Workspace-Visibility"></a>
Controls who can access the workspace. Valid values are: `ALL` (all users), `ASSIGNED` (only assigned users and routing profiles), and `NONE` (not visible).
Type: String
Valid Values: `ALL | ASSIGNED | NONE`
Required: No

## See Also
<a name="API_Workspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Workspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Workspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Workspace)
