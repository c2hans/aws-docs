---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InstanceGroupMetadata.html
---

# InstanceGroupMetadata
<a name="API_InstanceGroupMetadata"></a>

Metadata information about an instance group in a HyperPod cluster.

## Contents
<a name="API_InstanceGroupMetadata_Contents"></a>

 ** AmiOverride **   <a name="sagemaker-Type-InstanceGroupMetadata-AmiOverride"></a>
If you use a custom Amazon Machine Image (AMI) for the instance group, this field shows the ID of the custom AMI.
Type: String
Required: No

 ** AvailabilityZoneId **   <a name="sagemaker-Type-InstanceGroupMetadata-AvailabilityZoneId"></a>
The ID of the Availability Zone where the instance group is located.
Type: String
Required: No

 ** CapacityReservation **   <a name="sagemaker-Type-InstanceGroupMetadata-CapacityReservation"></a>
Information about the Capacity Reservation used by the instance group.
Type: [CapacityReservation](API_CapacityReservation.md) object
Required: No

 ** FailureMessage **   <a name="sagemaker-Type-InstanceGroupMetadata-FailureMessage"></a>
An error message describing why the instance group level operation (such as creating, scaling, or deleting) failed.
Type: String
Required: No

 ** SecurityGroupIds **   <a name="sagemaker-Type-InstanceGroupMetadata-SecurityGroupIds"></a>
A list of security group IDs associated with the instance group.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

 ** SubnetId **   <a name="sagemaker-Type-InstanceGroupMetadata-SubnetId"></a>
The ID of the subnet where the instance group is located.
Type: String
Required: No

## See Also
<a name="API_InstanceGroupMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InstanceGroupMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InstanceGroupMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InstanceGroupMetadata)
