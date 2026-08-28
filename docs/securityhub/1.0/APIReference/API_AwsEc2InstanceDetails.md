---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2InstanceDetails.html
---

# AwsEc2InstanceDetails
<a name="API_AwsEc2InstanceDetails"></a>

The details of an Amazon EC2 instance.

## Contents
<a name="API_AwsEc2InstanceDetails_Contents"></a>

 ** IamInstanceProfileArn **   <a name="securityhub-Type-AwsEc2InstanceDetails-IamInstanceProfileArn"></a>
The IAM profile ARN of the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ImageId **   <a name="securityhub-Type-AwsEc2InstanceDetails-ImageId"></a>
The Amazon Machine Image (AMI) ID of the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IpV4Addresses **   <a name="securityhub-Type-AwsEc2InstanceDetails-IpV4Addresses"></a>
The IPv4 addresses associated with the instance.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** IpV6Addresses **   <a name="securityhub-Type-AwsEc2InstanceDetails-IpV6Addresses"></a>
The IPv6 addresses associated with the instance.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** KeyName **   <a name="securityhub-Type-AwsEc2InstanceDetails-KeyName"></a>
The key name associated with the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LaunchedAt **   <a name="securityhub-Type-AwsEc2InstanceDetails-LaunchedAt"></a>
Indicates when the instance was launched.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** MetadataOptions **   <a name="securityhub-Type-AwsEc2InstanceDetails-MetadataOptions"></a>
Details about the metadata options for the Amazon EC2 instance.
Type: [AwsEc2InstanceMetadataOptions](API_AwsEc2InstanceMetadataOptions.md) object
Required: No

 ** Monitoring **   <a name="securityhub-Type-AwsEc2InstanceDetails-Monitoring"></a>
 Describes the type of monitoring that’s turned on for an instance.
Type: [AwsEc2InstanceMonitoringDetails](API_AwsEc2InstanceMonitoringDetails.md) object
Required: No

 ** NetworkInterfaces **   <a name="securityhub-Type-AwsEc2InstanceDetails-NetworkInterfaces"></a>
The identifiers of the network interfaces for the EC2 instance. The details for each network interface are in a corresponding `AwsEc2NetworkInterfacesDetails` object.
Type: Array of [AwsEc2InstanceNetworkInterfacesDetails](API_AwsEc2InstanceNetworkInterfacesDetails.md) objects
Required: No

 ** SubnetId **   <a name="securityhub-Type-AwsEc2InstanceDetails-SubnetId"></a>
The identifier of the subnet that the instance was launched in.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsEc2InstanceDetails-Type"></a>
The instance type of the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VirtualizationType **   <a name="securityhub-Type-AwsEc2InstanceDetails-VirtualizationType"></a>
The virtualization type of the Amazon Machine Image (AMI) required to launch the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsEc2InstanceDetails-VpcId"></a>
The identifier of the VPC that the instance was launched in.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2InstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2InstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2InstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2InstanceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
