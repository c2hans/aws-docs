---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaVolumeMount.html
---

# LambdaVolumeMount
<a name="API_LambdaVolumeMount"></a>

Contains information about a volume that Linux processes in a container can access. When you define a volume, the AWS IoT Greengrass Core software mounts the source files to the destination inside the container.

## Contents
<a name="API_LambdaVolumeMount_Contents"></a>

 ** destinationPath **   <a name="greengrassv2-Type-LambdaVolumeMount-destinationPath"></a>
The path to the logical volume in the file system.
Type: String
Required: Yes

 ** sourcePath **   <a name="greengrassv2-Type-LambdaVolumeMount-sourcePath"></a>
The path to the physical volume in the file system.
Type: String
Required: Yes

 ** addGroupOwner **   <a name="greengrassv2-Type-LambdaVolumeMount-addGroupOwner"></a>
Whether or not to add the AWS IoT Greengrass user group as an owner of the volume.
Default: `false`
Type: Boolean
Required: No

 ** permission **   <a name="greengrassv2-Type-LambdaVolumeMount-permission"></a>
The permission to access the volume: read/only (`ro`) or read/write (`rw`).
Default: `ro`
Type: String
Valid Values: `ro | rw`
Required: No

## See Also
<a name="API_LambdaVolumeMount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/LambdaVolumeMount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/LambdaVolumeMount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/LambdaVolumeMount)
