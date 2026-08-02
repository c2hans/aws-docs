---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ManagedInstanceRequest.html
---

# ManagedInstanceRequest
<a name="API_ManagedInstanceRequest"></a>

Defines comprehensive configuration for a managed WorkSpace Instance.

## Contents
<a name="API_ManagedInstanceRequest_Contents"></a>

 ** BlockDeviceMappings **   <a name="workspacesinstances-Type-ManagedInstanceRequest-BlockDeviceMappings"></a>
Configures block device mappings for storage.
Type: Array of [BlockDeviceMappingRequest](API_BlockDeviceMappingRequest.md) objects
Required: No

 ** CapacityReservationSpecification **   <a name="workspacesinstances-Type-ManagedInstanceRequest-CapacityReservationSpecification"></a>
Specifies capacity reservation preferences.
Type: [CapacityReservationSpecification](API_CapacityReservationSpecification.md) object
Required: No

 ** CpuOptions **   <a name="workspacesinstances-Type-ManagedInstanceRequest-CpuOptions"></a>
Configures CPU-specific settings.
Type: [CpuOptionsRequest](API_CpuOptionsRequest.md) object
Required: No

 ** CreditSpecification **   <a name="workspacesinstances-Type-ManagedInstanceRequest-CreditSpecification"></a>
Defines CPU credit configuration for burstable instances.
Type: [CreditSpecificationRequest](API_CreditSpecificationRequest.md) object
Required: No

 ** DisableApiStop **   <a name="workspacesinstances-Type-ManagedInstanceRequest-DisableApiStop"></a>
Prevents API-initiated instance stop.
Type: Boolean
Required: No

 ** EbsOptimized **   <a name="workspacesinstances-Type-ManagedInstanceRequest-EbsOptimized"></a>
Enables optimized EBS performance.
Type: Boolean
Required: No

 ** EnablePrimaryIpv6 **   <a name="workspacesinstances-Type-ManagedInstanceRequest-EnablePrimaryIpv6"></a>
Enables primary IPv6 address configuration.
Type: Boolean
Required: No

 ** EnclaveOptions **   <a name="workspacesinstances-Type-ManagedInstanceRequest-EnclaveOptions"></a>
Configures AWS Nitro Enclave settings.
Type: [EnclaveOptionsRequest](API_EnclaveOptionsRequest.md) object
Required: No

 ** HibernationOptions **   <a name="workspacesinstances-Type-ManagedInstanceRequest-HibernationOptions"></a>
Configures instance hibernation capabilities.
Type: [HibernationOptionsRequest](API_HibernationOptionsRequest.md) object
Required: No

 ** IamInstanceProfile **   <a name="workspacesinstances-Type-ManagedInstanceRequest-IamInstanceProfile"></a>
Specifies IAM instance profile configuration.
Type: [IamInstanceProfileSpecification](API_IamInstanceProfileSpecification.md) object
Required: No

 ** ImageId **   <a name="workspacesinstances-Type-ManagedInstanceRequest-ImageId"></a>
Identifies the Amazon Machine Image (AMI) for the instance.
Type: String
Pattern: `ami-[0-9a-zA-Z]{1,63}`
Required: No

 ** InstanceMarketOptions **   <a name="workspacesinstances-Type-ManagedInstanceRequest-InstanceMarketOptions"></a>
Configures marketplace-specific deployment options.
Type: [InstanceMarketOptionsRequest](API_InstanceMarketOptionsRequest.md) object
Required: No

 ** InstanceType **   <a name="workspacesinstances-Type-ManagedInstanceRequest-InstanceType"></a>
Specifies the WorkSpace Instance type.
Type: String
Pattern: `([a-z0-9-]+)\.([a-z0-9]+)`
Required: No

 ** Ipv6AddressCount **   <a name="workspacesinstances-Type-ManagedInstanceRequest-Ipv6AddressCount"></a>
Specifies number of IPv6 addresses to assign.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Ipv6Addresses **   <a name="workspacesinstances-Type-ManagedInstanceRequest-Ipv6Addresses"></a>
Configures specific IPv6 addresses.
Type: Array of [InstanceIpv6Address](API_InstanceIpv6Address.md) objects
Required: No

 ** KernelId **   <a name="workspacesinstances-Type-ManagedInstanceRequest-KernelId"></a>
Identifies the kernel for the instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** KeyName **   <a name="workspacesinstances-Type-ManagedInstanceRequest-KeyName"></a>
Specifies the key pair for instance access.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** LicenseSpecifications **   <a name="workspacesinstances-Type-ManagedInstanceRequest-LicenseSpecifications"></a>
Configures license-related settings.
Type: Array of [LicenseConfigurationRequest](API_LicenseConfigurationRequest.md) objects
Required: No

 ** MaintenanceOptions **   <a name="workspacesinstances-Type-ManagedInstanceRequest-MaintenanceOptions"></a>
Defines automatic maintenance settings.
Type: [InstanceMaintenanceOptionsRequest](API_InstanceMaintenanceOptionsRequest.md) object
Required: No

 ** MetadataOptions **   <a name="workspacesinstances-Type-ManagedInstanceRequest-MetadataOptions"></a>
Configures instance metadata service settings.
Type: [InstanceMetadataOptionsRequest](API_InstanceMetadataOptionsRequest.md) object
Required: No

 ** Monitoring **   <a name="workspacesinstances-Type-ManagedInstanceRequest-Monitoring"></a>
Enables or disables detailed instance monitoring.
Type: [RunInstancesMonitoringEnabled](API_RunInstancesMonitoringEnabled.md) object
Required: No

 ** NetworkInterfaces **   <a name="workspacesinstances-Type-ManagedInstanceRequest-NetworkInterfaces"></a>
Configures network interface settings.
Type: Array of [InstanceNetworkInterfaceSpecification](API_InstanceNetworkInterfaceSpecification.md) objects
Required: No

 ** NetworkPerformanceOptions **   <a name="workspacesinstances-Type-ManagedInstanceRequest-NetworkPerformanceOptions"></a>
Defines network performance configuration.
Type: [InstanceNetworkPerformanceOptionsRequest](API_InstanceNetworkPerformanceOptionsRequest.md) object
Required: No

 ** Placement **   <a name="workspacesinstances-Type-ManagedInstanceRequest-Placement"></a>
Specifies instance placement preferences.
Type: [Placement](API_Placement.md) object
Required: No

 ** PrivateDnsNameOptions **   <a name="workspacesinstances-Type-ManagedInstanceRequest-PrivateDnsNameOptions"></a>
Configures private DNS name settings.
Type: [PrivateDnsNameOptionsRequest](API_PrivateDnsNameOptionsRequest.md) object
Required: No

 ** PrivateIpAddress **   <a name="workspacesinstances-Type-ManagedInstanceRequest-PrivateIpAddress"></a>
Specifies the primary private IP address.
Type: String
Pattern: `(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}`
Required: No

 ** RamdiskId **   <a name="workspacesinstances-Type-ManagedInstanceRequest-RamdiskId"></a>
Identifies the ramdisk for the instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** SecurityGroupIds **   <a name="workspacesinstances-Type-ManagedInstanceRequest-SecurityGroupIds"></a>
Specifies security group identifiers.
Type: Array of strings
Pattern: `sg-[0-9a-zA-Z]{1,63}`
Required: No

 ** SecurityGroups **   <a name="workspacesinstances-Type-ManagedInstanceRequest-SecurityGroups"></a>
Configures security group settings.
Type: Array of strings
Pattern: `(?!sg-)[\w .:/()#,@\[\]+=&;{}!$*-]{0,255}`
Required: No

 ** SubnetId **   <a name="workspacesinstances-Type-ManagedInstanceRequest-SubnetId"></a>
Identifies the subnet for the instance.
Type: String
Pattern: `subnet-[0-9a-zA-Z]{1,63}`
Required: No

 ** TagSpecifications **   <a name="workspacesinstances-Type-ManagedInstanceRequest-TagSpecifications"></a>
Configures resource tagging specifications.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** UserData **   <a name="workspacesinstances-Type-ManagedInstanceRequest-UserData"></a>
Provides custom initialization data for the instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16000.
Required: No

## See Also
<a name="API_ManagedInstanceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/ManagedInstanceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/ManagedInstanceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/ManagedInstanceRequest)
