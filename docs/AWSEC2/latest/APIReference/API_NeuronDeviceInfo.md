---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NeuronDeviceInfo.html
---

# NeuronDeviceInfo
<a name="API_NeuronDeviceInfo"></a>

Describes the neuron accelerators for the instance type.

## Contents
<a name="API_NeuronDeviceInfo_Contents"></a>

 ** coreInfo **
Describes the cores available to each neuron accelerator.
Type: [NeuronDeviceCoreInfo](API_NeuronDeviceCoreInfo.md) object
Required: No

 ** count **
The number of neuron accelerators for the instance type.
Type: Integer
Required: No

 ** memoryInfo **
Describes the memory available to each neuron accelerator.
Type: [NeuronDeviceMemoryInfo](API_NeuronDeviceMemoryInfo.md) object
Required: No

 ** name **
The name of the neuron accelerator.
Type: String
Required: No

## See Also
<a name="API_NeuronDeviceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NeuronDeviceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NeuronDeviceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NeuronDeviceInfo)
