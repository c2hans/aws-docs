---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ServiceManagedEc2FleetConfiguration.html
---

# ServiceManagedEc2FleetConfiguration
<a name="API_ServiceManagedEc2FleetConfiguration"></a>

The configuration details for a service managed EC2 fleet.

## Contents
<a name="API_ServiceManagedEc2FleetConfiguration_Contents"></a>

 ** instanceCapabilities **   <a name="deadlinecloud-Type-ServiceManagedEc2FleetConfiguration-instanceCapabilities"></a>
The instance capabilities for the service managed EC2 fleet.
Type: [ServiceManagedEc2InstanceCapabilities](API_ServiceManagedEc2InstanceCapabilities.md) object
Required: Yes

 ** instanceMarketOptions **   <a name="deadlinecloud-Type-ServiceManagedEc2FleetConfiguration-instanceMarketOptions"></a>
The instance market options for the service managed EC2 fleet.
Type: [ServiceManagedEc2InstanceMarketOptions](API_ServiceManagedEc2InstanceMarketOptions.md) object
Required: Yes

 ** autoScalingConfiguration **   <a name="deadlinecloud-Type-ServiceManagedEc2FleetConfiguration-autoScalingConfiguration"></a>
The auto scaling configuration settings for the service managed EC2 fleet.
Type: [ServiceManagedEc2AutoScalingConfiguration](API_ServiceManagedEc2AutoScalingConfiguration.md) object
Required: No

 ** persistentVolumeConfiguration **   <a name="deadlinecloud-Type-ServiceManagedEc2FleetConfiguration-persistentVolumeConfiguration"></a>
The persistent volume configuration for the service managed EC2 fleet.
Type: [PersistentVolumeConfiguration](API_PersistentVolumeConfiguration.md) object
Required: No

 ** storageProfileId **   <a name="deadlinecloud-Type-ServiceManagedEc2FleetConfiguration-storageProfileId"></a>
The storage profile ID for the service managed EC2 fleet.
Type: String
Pattern: `sp-[0-9a-f]{32}`
Required: No

 ** vpcConfiguration **   <a name="deadlinecloud-Type-ServiceManagedEc2FleetConfiguration-vpcConfiguration"></a>
The VPC configuration for the service managed EC2 fleet.
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

## See Also
<a name="API_ServiceManagedEc2FleetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ServiceManagedEc2FleetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ServiceManagedEc2FleetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ServiceManagedEc2FleetConfiguration)
