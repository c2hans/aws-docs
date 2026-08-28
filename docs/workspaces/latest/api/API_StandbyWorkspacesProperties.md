---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_StandbyWorkspacesProperties.html
---

# StandbyWorkspacesProperties
<a name="API_StandbyWorkspacesProperties"></a>

Describes the properties of the related standby WorkSpaces.

## Contents
<a name="API_StandbyWorkspacesProperties_Contents"></a>

 ** DataReplication **   <a name="WorkSpaces-Type-StandbyWorkspacesProperties-DataReplication"></a>
Indicates whether data replication is enabled, and if enabled, the type of data replication.
Type: String
Valid Values: `NO_REPLICATION | PRIMARY_AS_SOURCE`
Required: No

 ** RecoverySnapshotTime **   <a name="WorkSpaces-Type-StandbyWorkspacesProperties-RecoverySnapshotTime"></a>
The date and time at which the last successful snapshot was taken of the primary WorkSpace used for replicating data.
Type: Timestamp
Required: No

 ** StandbyWorkspaceId **   <a name="WorkSpaces-Type-StandbyWorkspacesProperties-StandbyWorkspaceId"></a>
The identifier of the standby WorkSpace
Type: String
Pattern: `^ws-[0-9a-z]{8,63}$`
Required: No

## See Also
<a name="API_StandbyWorkspacesProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/StandbyWorkspacesProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/StandbyWorkspacesProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/StandbyWorkspacesProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
