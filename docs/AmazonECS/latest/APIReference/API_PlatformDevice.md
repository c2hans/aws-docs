---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PlatformDevice.html
---

# PlatformDevice
<a name="API_PlatformDevice"></a>

The devices that are available on the container instance. The supported device types are GPUs and Neuron devices.

## Contents
<a name="API_PlatformDevice_Contents"></a>

 ** id **   <a name="ECS-Type-PlatformDevice-id"></a>
The ID for the GPU or Neuron device on the container instance. For GPUs, the available GPU IDs can also be obtained on the container instance in the `/var/lib/ecs/gpu/nvidia_gpu_info.json` file. For Neuron devices, the ID corresponds to the device index (for example, `0` for `/dev/neuron0`).
Type: String
Required: Yes

 ** type **   <a name="ECS-Type-PlatformDevice-type"></a>
The type of device that's available on the container instance. The supported values are `GPU` and `NEURON_DEVICE`.
Type: String
Valid Values: `GPU | NEURON_DEVICE`
Required: Yes

## See Also
<a name="API_PlatformDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/PlatformDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/PlatformDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/PlatformDevice)
