---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DestinationBackup.html
---

# DestinationBackup
<a name="API_DestinationBackup"></a>

Contains information about the backup that will be copied and created by the [CopyBackupToRegion](API_CopyBackupToRegion.md) operation.

## Contents
<a name="API_DestinationBackup_Contents"></a>

 ** CreateTimestamp **   <a name="CloudHSMV2-Type-DestinationBackup-CreateTimestamp"></a>
The date and time when both the source backup was created.
Type: Timestamp
Required: No

 ** SourceBackup **   <a name="CloudHSMV2-Type-DestinationBackup-SourceBackup"></a>
The identifier (ID) of the source backup from which the new backup was copied.
Type: String
Pattern: `backup-[2-7a-zA-Z]{11,16}`
Required: No

 ** SourceCluster **   <a name="CloudHSMV2-Type-DestinationBackup-SourceCluster"></a>
The identifier (ID) of the cluster containing the source backup from which the new backup was copied.
Type: String
Pattern: `cluster-[2-7a-zA-Z]{11,16}`
Required: No

 ** SourceRegion **   <a name="CloudHSMV2-Type-DestinationBackup-SourceRegion"></a>
The AWS region that contains the source backup from which the new backup was copied.
Type: String
Pattern: `[a-z]{2}(-(gov))?-(east|west|north|south|central){1,2}-\d`
Required: No

## See Also
<a name="API_DestinationBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DestinationBackup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DestinationBackup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DestinationBackup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
