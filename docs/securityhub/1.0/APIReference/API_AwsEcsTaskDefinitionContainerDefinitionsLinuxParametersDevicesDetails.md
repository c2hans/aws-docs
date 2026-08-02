---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails"></a>

A host device to expose to the container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails_Contents"></a>

 ** ContainerPath **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails-ContainerPath"></a>
The path inside the container at which to expose the host device.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HostPath **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails-HostPath"></a>
The path for the device on the host container instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Permissions **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails-Permissions"></a>
The explicit permissions to provide to the container for the device. By default, the container has permissions for read, write, and `mknod` for the device.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails)
