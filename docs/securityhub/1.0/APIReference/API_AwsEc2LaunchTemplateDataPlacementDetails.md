---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataPlacementDetails.html
---

# AwsEc2LaunchTemplateDataPlacementDetails
<a name="API_AwsEc2LaunchTemplateDataPlacementDetails"></a>

 Provides details about the placement of an Amazon EC2 instance.

## Contents
<a name="API_AwsEc2LaunchTemplateDataPlacementDetails_Contents"></a>

 ** Affinity **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPlacementDetails-Affinity"></a>
 The affinity setting for an instance on an EC2 Dedicated Host.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AvailabilityZone **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPlacementDetails-AvailabilityZone"></a>
 The Availability Zone for the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** GroupName **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPlacementDetails-GroupName"></a>
 The name of the placement group for the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HostId **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPlacementDetails-HostId"></a>
 The ID of the Dedicated Host for the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HostResourceGroupArn **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPlacementDetails-HostResourceGroupArn"></a>
 The Amazon Resource Name (ARN) of the host resource group in which to launch the instances.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PartitionNumber **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPlacementDetails-PartitionNumber"></a>
 The number of the partition the instance should launch in.
Type: Integer
Required: No

 ** SpreadDomain **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPlacementDetails-SpreadDomain"></a>
 Reserved for future use.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Tenancy **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPlacementDetails-Tenancy"></a>
 The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataPlacementDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataPlacementDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataPlacementDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataPlacementDetails)
