---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails.html
---

# AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails
<a name="API_AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails"></a>

 Parameters for a block device for an Amazon Elastic Block Store (Amazon EBS) volume in an Amazon EC2 launch template.

## Contents
<a name="API_AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails_Contents"></a>

 ** DeleteOnTermination **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails-DeleteOnTermination"></a>
 Indicates whether the EBS volume is deleted on instance termination.
Type: Boolean
Required: No

 ** Encrypted **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails-Encrypted"></a>
 Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. If you're creating a volume from a snapshot, you can't specify an encryption value.
Type: Boolean
Required: No

 ** Iops **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails-Iops"></a>
 The number of I/O operations per second (IOPS).
Type: Integer
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails-KmsKeyId"></a>
 The Amazon Resource Name (ARN) of the symmetric AWS Key Management Service (AWS KMS) customer managed key used for encryption.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SnapshotId **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails-SnapshotId"></a>
 The ID of the EBS snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Throughput **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails-Throughput"></a>
 The throughput to provision for a gp3 volume, with a maximum of 1,000 MiB/s.
Type: Integer
Required: No

 ** VolumeSize **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails-VolumeSize"></a>
 The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size.
Type: Integer
Required: No

 ** VolumeType **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails-VolumeType"></a>
 The volume type.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
