---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Ebs.html
---

# Ebs
<a name="API_Ebs"></a>

Describes information used to set up an Amazon EBS volume specified in a block device mapping.

## Contents
<a name="API_Ebs_Contents"></a>

 ** DeleteOnTermination **
Indicates whether the volume is deleted on instance termination. For Amazon EC2 Auto Scaling, the default value is `true`.
Type: Boolean
Required: No

 ** Encrypted **
Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be attached to instances that support Amazon EBS encryption. For more information, see [Requirements for Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html) in the *Amazon EBS User Guide*. If your AMI uses encrypted volumes, you can also only launch it on supported instance types.
If you are creating a volume from a snapshot, you cannot create an unencrypted volume from an encrypted snapshot. Also, you cannot specify a KMS key ID when using a launch configuration.
If you enable encryption by default, the EBS volumes that you create are always encrypted, either using the AWS managed KMS key or a customer-managed KMS key, regardless of whether the snapshot was encrypted.
For more information, see [Use AWS KMS keys to encrypt Amazon EBS volumes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html#encryption) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Boolean
Required: No

 ** Iops **
The number of input/output (I/O) operations per second (IOPS) to provision for the volume. For `gp3` and `io1` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.
The following are the supported values for each volume type:
+  `gp3`: 3,000-16,000 IOPS
+  `io1`: 100-64,000 IOPS
For `io1` volumes, we guarantee 64,000 IOPS only for [Instances built on the AWS Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html). Other instance families guarantee performance up to 32,000 IOPS.
 `Iops` is supported when the volume type is `gp3` or `io1` and required only when the volume type is `io1`. (Not used with `standard`, `gp2`, `st1`, or `sc1` volumes.)
Type: Integer
Valid Range: Minimum value of 100. Maximum value of 64000.
Required: No

 ** SnapshotId **
The snapshot ID of the volume to use.
You must specify either a `VolumeSize` or a `SnapshotId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Throughput **
The throughput (MiBps) to provision for a `gp3` volume.
Type: Integer
Valid Range: Minimum value of 125. Maximum value of 1000.
Required: No

 ** VolumeSize **
The volume size, in GiBs. The following are the supported volumes sizes for each volume type:
+  `gp2` and `gp3`: 1-16,384
+  `io1`: 4-16,384
+  `st1` and `sc1`: 125-16,384
+  `standard`: 1-1,024
You must specify either a `SnapshotId` or a `VolumeSize`. If you specify both `SnapshotId` and `VolumeSize`, the volume size must be equal or greater than the size of the snapshot.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 16384.
Required: No

 ** VolumeType **
The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide*.
Valid values: `standard` \| `io1` \| `gp2` \| `st1` \| `sc1` \| `gp3`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_Ebs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/Ebs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/Ebs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/Ebs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
