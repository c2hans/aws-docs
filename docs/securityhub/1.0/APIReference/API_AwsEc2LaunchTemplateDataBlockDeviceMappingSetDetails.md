---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails.html
---

# AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails
<a name="API_AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails"></a>

 Information about a block device mapping for an Amazon Elastic Compute Cloud (Amazon EC2) launch template.

## Contents
<a name="API_AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails_Contents"></a>

 ** DeviceName **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails-DeviceName"></a>
 The device name.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Ebs **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails-Ebs"></a>
 Parameters used to automatically set up Amazon EBS volumes when the instance is launched.
Type: [AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails](API_AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails.md) object
Required: No

 ** NoDevice **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails-NoDevice"></a>
 Omits the device from the block device mapping when an empty string is specified.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VirtualName **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails-VirtualName"></a>
 The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for `ephemeral0` and `ephemeral1`. The number of available instance store volumes depends on the instance type.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
