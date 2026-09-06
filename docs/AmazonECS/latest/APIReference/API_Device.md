---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Device.html
---

# Device
<a name="API_Device"></a>

An object representing a container instance host device.

## Contents
<a name="API_Device_Contents"></a>

 ** hostPath **   <a name="ECS-Type-Device-hostPath"></a>
The path for the device on the host container instance.
Type: String
Required: Yes

 ** containerPath **   <a name="ECS-Type-Device-containerPath"></a>
The path inside the container at which to expose the host device.
Type: String
Required: No

 ** permissions **   <a name="ECS-Type-Device-permissions"></a>
The explicit permissions to provide to the container for the device. By default, the container has permissions for `read`, `write`, and `mknod` for the device.
Type: Array of strings
Valid Values: `read | write | mknod`
Required: No

## See Also
<a name="API_Device_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Device)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Device)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Device)
