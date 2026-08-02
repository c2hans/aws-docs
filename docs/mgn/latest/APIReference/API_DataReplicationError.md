---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DataReplicationError.html
---

# DataReplicationError
<a name="API_DataReplicationError"></a>

Error in data replication.

## Contents
<a name="API_DataReplicationError_Contents"></a>

 ** error **   <a name="mgn-Type-DataReplicationError-error"></a>
Error in data replication.
Type: String
Valid Values: `AGENT_NOT_SEEN | SNAPSHOTS_FAILURE | NOT_CONVERGING | UNSTABLE_NETWORK | FAILED_TO_CREATE_SECURITY_GROUP | FAILED_TO_LAUNCH_REPLICATION_SERVER | FAILED_TO_BOOT_REPLICATION_SERVER | FAILED_TO_AUTHENTICATE_WITH_SERVICE | FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE | FAILED_TO_CREATE_STAGING_DISKS | FAILED_TO_ATTACH_STAGING_DISKS | FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT | FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER | FAILED_TO_START_DATA_TRANSFER | UNSUPPORTED_VM_CONFIGURATION | LAST_SNAPSHOT_JOB_FAILED | FAILED_TO_SETUP_FSX_PROXY | FAILED_TO_CREATE_FSX_SNAPSHOT`
Required: No

 ** rawError **   <a name="mgn-Type-DataReplicationError-rawError"></a>
Error in data replication.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

## See Also
<a name="API_DataReplicationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DataReplicationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DataReplicationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DataReplicationError)
