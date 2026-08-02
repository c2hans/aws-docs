---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDataReplicationError.html
---

# RecoveryInstanceDataReplicationError
<a name="API_RecoveryInstanceDataReplicationError"></a>

Error in data replication.

## Contents
<a name="API_RecoveryInstanceDataReplicationError_Contents"></a>

 ** error **   <a name="drs-Type-RecoveryInstanceDataReplicationError-error"></a>
Error in data replication.
Type: String
Valid Values: `AGENT_NOT_SEEN | FAILBACK_CLIENT_NOT_SEEN | NOT_CONVERGING | UNSTABLE_NETWORK | FAILED_TO_ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION | FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT | FAILED_TO_CONFIGURE_REPLICATION_SOFTWARE | FAILED_TO_PAIR_AGENT_WITH_REPLICATION_SOFTWARE | FAILED_TO_ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION | FAILED_GETTING_REPLICATION_STATE | SNAPSHOTS_FAILURE | FAILED_TO_CREATE_SECURITY_GROUP | FAILED_TO_LAUNCH_REPLICATION_SERVER | FAILED_TO_BOOT_REPLICATION_SERVER | FAILED_TO_AUTHENTICATE_WITH_SERVICE | FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE | FAILED_TO_CREATE_STAGING_DISKS | FAILED_TO_ATTACH_STAGING_DISKS | FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT | FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER | FAILED_TO_START_DATA_TRANSFER`
Required: No

 ** rawError **   <a name="drs-Type-RecoveryInstanceDataReplicationError-rawError"></a>
Error in data replication.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

## See Also
<a name="API_RecoveryInstanceDataReplicationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryInstanceDataReplicationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryInstanceDataReplicationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryInstanceDataReplicationError)
