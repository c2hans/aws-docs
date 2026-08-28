---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateEbsBlockDevice.html
---

# LaunchTemplateEbsBlockDevice
<a name="API_LaunchTemplateEbsBlockDevice"></a>

Describes a block device for an EBS volume.

## Contents
<a name="API_LaunchTemplateEbsBlockDevice_Contents"></a>

 ** deleteOnTermination **
Indicates whether the EBS volume is deleted on instance termination.
Type: Boolean
Required: No

 ** ebsCardIndex **
The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.
Type: Integer
Required: No

 ** encrypted **
Indicates whether the EBS volume is encrypted.
Type: Boolean
Required: No

 ** iops **
The number of I/O operations per second (IOPS) that the volume supports.
Type: Integer
Required: No

 ** kmsKeyId **
Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.
Type: String
Required: No

 ** snapshotId **
The ID of the snapshot.
Type: String
Required: No

 ** throughput **
The throughput that the volume supports, in MiB/s.
Type: Integer
Required: No

 ** volumeInitializationRate **
The Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate) specified for the volume, in MiB/s. If no volume initialization rate was specified, the value is `null`.
Type: Integer
Required: No

 ** volumeSize **
The size of the volume, in GiB.
Type: Integer
Required: No

 ** volumeType **
The volume type.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## See Also
<a name="API_LaunchTemplateEbsBlockDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateEbsBlockDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateEbsBlockDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateEbsBlockDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
