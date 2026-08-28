---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceConnectionStatus.html
---

# WorkspaceConnectionStatus
<a name="API_WorkspaceConnectionStatus"></a>

Describes the connection status of a WorkSpace.

## Contents
<a name="API_WorkspaceConnectionStatus_Contents"></a>

 ** ConnectionState **   <a name="WorkSpaces-Type-WorkspaceConnectionStatus-ConnectionState"></a>
The connection state of the WorkSpace. The connection state is unknown if the WorkSpace is stopped.
Type: String
Valid Values: `CONNECTED | DISCONNECTED | UNKNOWN`
Required: No

 ** ConnectionStateCheckTimestamp **   <a name="WorkSpaces-Type-WorkspaceConnectionStatus-ConnectionStateCheckTimestamp"></a>
The timestamp of the connection status check.
Type: Timestamp
Required: No

 ** LastKnownUserConnectionTimestamp **   <a name="WorkSpaces-Type-WorkspaceConnectionStatus-LastKnownUserConnectionTimestamp"></a>
The timestamp of the last known user connection.
Type: Timestamp
Required: No

 ** WorkspaceId **   <a name="WorkSpaces-Type-WorkspaceConnectionStatus-WorkspaceId"></a>
The identifier of the WorkSpace.
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: No

## See Also
<a name="API_WorkspaceConnectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspaceConnectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspaceConnectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspaceConnectionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
