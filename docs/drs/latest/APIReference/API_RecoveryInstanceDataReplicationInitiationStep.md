---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDataReplicationInitiationStep.html
---

# RecoveryInstanceDataReplicationInitiationStep
<a name="API_RecoveryInstanceDataReplicationInitiationStep"></a>

Data replication initiation step.

## Contents
<a name="API_RecoveryInstanceDataReplicationInitiationStep_Contents"></a>

 ** name **   <a name="drs-Type-RecoveryInstanceDataReplicationInitiationStep-name"></a>
The name of the step.
Type: String
Valid Values: `LINK_FAILBACK_CLIENT_WITH_RECOVERY_INSTANCE | COMPLETE_VOLUME_MAPPING | ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION | DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT | CONFIGURE_REPLICATION_SOFTWARE | PAIR_AGENT_WITH_REPLICATION_SOFTWARE | ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION | WAIT | CREATE_SECURITY_GROUP | LAUNCH_REPLICATION_SERVER | BOOT_REPLICATION_SERVER | AUTHENTICATE_WITH_SERVICE | DOWNLOAD_REPLICATION_SOFTWARE | CREATE_STAGING_DISKS | ATTACH_STAGING_DISKS | PAIR_REPLICATION_SERVER_WITH_AGENT | CONNECT_AGENT_TO_REPLICATION_SERVER | START_DATA_TRANSFER`
Required: No

 ** status **   <a name="drs-Type-RecoveryInstanceDataReplicationInitiationStep-status"></a>
The status of the step.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | SUCCEEDED | FAILED | SKIPPED`
Required: No

## See Also
<a name="API_RecoveryInstanceDataReplicationInitiationStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryInstanceDataReplicationInitiationStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryInstanceDataReplicationInitiationStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryInstanceDataReplicationInitiationStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
