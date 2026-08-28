---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_EbsInstanceBlockDeviceSpecification.html
---

# EbsInstanceBlockDeviceSpecification
<a name="API_EbsInstanceBlockDeviceSpecification"></a>

Amazon EBS-specific block device mapping specifications.

## Contents
<a name="API_EbsInstanceBlockDeviceSpecification_Contents"></a>

 ** deleteOnTermination **   <a name="imagebuilder-Type-EbsInstanceBlockDeviceSpecification-deleteOnTermination"></a>
Use to configure delete on termination of the associated device.
Type: Boolean
Required: No

 ** encrypted **   <a name="imagebuilder-Type-EbsInstanceBlockDeviceSpecification-encrypted"></a>
Use to configure device encryption.
Type: Boolean
Required: No

 ** iops **   <a name="imagebuilder-Type-EbsInstanceBlockDeviceSpecification-iops"></a>
Use to configure device IOPS.
Type: Integer
Valid Range: Minimum value of 100. Maximum value of 64000.
Required: No

 ** kmsKeyId **   <a name="imagebuilder-Type-EbsInstanceBlockDeviceSpecification-kmsKeyId"></a>
The Amazon Resource Name (ARN) that uniquely identifies the KMS key to use when encrypting the device. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** snapshotId **   <a name="imagebuilder-Type-EbsInstanceBlockDeviceSpecification-snapshotId"></a>
The snapshot that defines the device contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** throughput **   <a name="imagebuilder-Type-EbsInstanceBlockDeviceSpecification-throughput"></a>
 **For GP3 volumes only** – The throughput in MiB/s that the volume supports.
Type: Integer
Valid Range: Minimum value of 125. Maximum value of 1000.
Required: No

 ** volumeSize **   <a name="imagebuilder-Type-EbsInstanceBlockDeviceSpecification-volumeSize"></a>
Use to override the device's volume size.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 16000.
Required: No

 ** volumeType **   <a name="imagebuilder-Type-EbsInstanceBlockDeviceSpecification-volumeType"></a>
Use to override the device's volume type.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | gp3 | sc1 | st1`
Required: No

## See Also
<a name="API_EbsInstanceBlockDeviceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/EbsInstanceBlockDeviceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/EbsInstanceBlockDeviceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/EbsInstanceBlockDeviceSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
