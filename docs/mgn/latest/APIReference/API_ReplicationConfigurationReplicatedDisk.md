---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ReplicationConfigurationReplicatedDisk.html
---

# ReplicationConfigurationReplicatedDisk
<a name="API_ReplicationConfigurationReplicatedDisk"></a>

Replication Configuration replicated disk.

## Contents
<a name="API_ReplicationConfigurationReplicatedDisk_Contents"></a>

 ** deviceName **   <a name="mgn-Type-ReplicationConfigurationReplicatedDisk-deviceName"></a>
Replication Configuration replicated disk device name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** iops **   <a name="mgn-Type-ReplicationConfigurationReplicatedDisk-iops"></a>
Replication Configuration replicated disk IOPs.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** isBootDisk **   <a name="mgn-Type-ReplicationConfigurationReplicatedDisk-isBootDisk"></a>
Replication Configuration replicated disk boot disk.
Type: Boolean
Required: No

 ** stagingDiskType **   <a name="mgn-Type-ReplicationConfigurationReplicatedDisk-stagingDiskType"></a>
Replication Configuration replicated disk staging disk type.
Type: String
Valid Values: `AUTO | GP2 | IO1 | SC1 | ST1 | STANDARD | GP3 | IO2 | FSX_ONTAP`
Required: No

 ** throughput **   <a name="mgn-Type-ReplicationConfigurationReplicatedDisk-throughput"></a>
Replication Configuration replicated disk throughput.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ReplicationConfigurationReplicatedDisk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ReplicationConfigurationReplicatedDisk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ReplicationConfigurationReplicatedDisk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ReplicationConfigurationReplicatedDisk)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
