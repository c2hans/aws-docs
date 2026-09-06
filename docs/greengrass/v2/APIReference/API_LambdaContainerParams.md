---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaContainerParams.html
---

# LambdaContainerParams
<a name="API_LambdaContainerParams"></a>

Contains information about a container in which AWS Lambda functions run on Greengrass core devices.

## Contents
<a name="API_LambdaContainerParams_Contents"></a>

 ** devices **   <a name="greengrassv2-Type-LambdaContainerParams-devices"></a>
The list of system devices that the container can access.
Type: Array of [LambdaDeviceMount](API_LambdaDeviceMount.md) objects
Required: No

 ** memorySizeInKB **   <a name="greengrassv2-Type-LambdaContainerParams-memorySizeInKB"></a>
The memory size of the container, expressed in kilobytes.
Default: `16384` (16 MB)
Type: Integer
Required: No

 ** mountROSysfs **   <a name="greengrassv2-Type-LambdaContainerParams-mountROSysfs"></a>
Whether or not the container can read information from the device's `/sys` folder.
Default: `false`
Type: Boolean
Required: No

 ** volumes **   <a name="greengrassv2-Type-LambdaContainerParams-volumes"></a>
The list of volumes that the container can access.
Type: Array of [LambdaVolumeMount](API_LambdaVolumeMount.md) objects
Required: No

## See Also
<a name="API_LambdaContainerParams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/LambdaContainerParams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/LambdaContainerParams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/LambdaContainerParams)
