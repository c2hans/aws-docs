---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDeviceResponse.html
---

# EbsBlockDeviceResponse
<a name="API_EbsBlockDeviceResponse"></a>

Describes a block device for an EBS volume.

## Contents
<a name="API_EbsBlockDeviceResponse_Contents"></a>

 ** deleteOnTermination **
Indicates whether the volume is deleted on instance termination.
Type: Boolean
Required: No

 ** encrypted **
Indicates whether the volume is encrypted.
Type: Boolean
Required: No

 ** iops **
The number of I/O operations per second (IOPS). For `gp3`, `io1`, and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.
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

 ** volumeSize **
The size of the volume, in GiBs.
Type: Integer
Required: No

 ** volumeType **
The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide*.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## See Also
<a name="API_EbsBlockDeviceResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EbsBlockDeviceResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EbsBlockDeviceResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EbsBlockDeviceResponse)
