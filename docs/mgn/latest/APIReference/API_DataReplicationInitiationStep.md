---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DataReplicationInitiationStep.html
---

# DataReplicationInitiationStep
<a name="API_DataReplicationInitiationStep"></a>

Data replication initiation step.

## Contents
<a name="API_DataReplicationInitiationStep_Contents"></a>

 ** name **   <a name="mgn-Type-DataReplicationInitiationStep-name"></a>
Request to query data initiation step name.
Type: String
Valid Values: `WAIT | CREATE_SECURITY_GROUP | LAUNCH_REPLICATION_SERVER | BOOT_REPLICATION_SERVER | AUTHENTICATE_WITH_SERVICE | DOWNLOAD_REPLICATION_SOFTWARE | CREATE_STAGING_DISKS | ATTACH_STAGING_DISKS | PAIR_REPLICATION_SERVER_WITH_AGENT | CONNECT_AGENT_TO_REPLICATION_SERVER | START_DATA_TRANSFER | SETUP_FSX_PROXY`
Required: No

 ** status **   <a name="mgn-Type-DataReplicationInitiationStep-status"></a>
Request to query data initiation status.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | SUCCEEDED | FAILED | SKIPPED`
Required: No

## See Also
<a name="API_DataReplicationInitiationStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DataReplicationInitiationStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DataReplicationInitiationStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DataReplicationInitiationStep)
