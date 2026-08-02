---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails"></a>

>Linux-specific modifications that are applied to the container, such as Linux kernel capabilities.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails_Contents"></a>

 ** Capabilities **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails-Capabilities"></a>
The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.
Type: [AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails](API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails.md) object
Required: No

 ** Devices **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails-Devices"></a>
The host devices to expose to the container.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails](API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails.md) objects
Required: No

 ** InitProcessEnabled **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails-InitProcessEnabled"></a>
Whether to run an `init` process inside the container that forwards signals and reaps processes.
Type: Boolean
Required: No

 ** MaxSwap **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails-MaxSwap"></a>
The total amount of swap memory (in MiB) that a container can use.
Type: Integer
Required: No

 ** SharedMemorySize **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails-SharedMemorySize"></a>
The value for the size (in MiB) of the **/dev/shm** volume.
Type: Integer
Required: No

 ** Swappiness **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails-Swappiness"></a>
Configures the container's memory swappiness behavior. Determines how aggressively pages are swapped. The higher the value, the more aggressive the swappiness. The default is 60.
Type: Integer
Required: No

 ** Tmpfs **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails-Tmpfs"></a>
The container path, mount options, and size (in MiB) of the tmpfs mount.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails.md) objects
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails)
