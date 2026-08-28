---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDisk.html
---

# RecoveryInstanceDisk
<a name="API_RecoveryInstanceDisk"></a>

An object representing a block storage device on the Recovery Instance.

## Contents
<a name="API_RecoveryInstanceDisk_Contents"></a>

 ** bytes **   <a name="drs-Type-RecoveryInstanceDisk-bytes"></a>
The amount of storage on the disk in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** ebsVolumeID **   <a name="drs-Type-RecoveryInstanceDisk-ebsVolumeID"></a>
The EBS Volume ID of this disk.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `vol-([0-9a-fA-F]{8}|[0-9a-fA-F]{17})`
Required: No

 ** internalDeviceName **   <a name="drs-Type-RecoveryInstanceDisk-internalDeviceName"></a>
The internal device name of this disk. This is the name that is visible on the machine itself and not from the EC2 console.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_RecoveryInstanceDisk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryInstanceDisk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryInstanceDisk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryInstanceDisk)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
