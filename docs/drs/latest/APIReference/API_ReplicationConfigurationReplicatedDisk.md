---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_ReplicationConfigurationReplicatedDisk.html
---

# ReplicationConfigurationReplicatedDisk
<a name="API_ReplicationConfigurationReplicatedDisk"></a>

The configuration of a disk of the Source Server to be replicated.

## Contents
<a name="API_ReplicationConfigurationReplicatedDisk_Contents"></a>

 ** deviceName **   <a name="drs-Type-ReplicationConfigurationReplicatedDisk-deviceName"></a>
The name of the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** iops **   <a name="drs-Type-ReplicationConfigurationReplicatedDisk-iops"></a>
The requested number of I/O operations per second (IOPS).
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** isBootDisk **   <a name="drs-Type-ReplicationConfigurationReplicatedDisk-isBootDisk"></a>
Whether to boot from this disk or not.
Type: Boolean
Required: No

 ** optimizedStagingDiskType **   <a name="drs-Type-ReplicationConfigurationReplicatedDisk-optimizedStagingDiskType"></a>
The Staging Disk EBS volume type to be used during replication when `stagingDiskType` is set to Auto. This is a read-only field.
Type: String
Valid Values: `AUTO | GP2 | GP3 | IO1 | SC1 | ST1 | STANDARD`
Required: No

 ** stagingDiskType **   <a name="drs-Type-ReplicationConfigurationReplicatedDisk-stagingDiskType"></a>
The Staging Disk EBS volume type to be used during replication.
Type: String
Valid Values: `AUTO | GP2 | GP3 | IO1 | SC1 | ST1 | STANDARD`
Required: No

 ** throughput **   <a name="drs-Type-ReplicationConfigurationReplicatedDisk-throughput"></a>
The throughput to use for the EBS volume in MiB/s. This parameter is valid only for gp3 volumes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ReplicationConfigurationReplicatedDisk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/ReplicationConfigurationReplicatedDisk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/ReplicationConfigurationReplicatedDisk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/ReplicationConfigurationReplicatedDisk)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
