---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InferenceAcceleratorOverride.html
---

# InferenceAcceleratorOverride
<a name="API_InferenceAcceleratorOverride"></a>

 *This data type has been deprecated.*

Details on an Elastic Inference accelerator task override. This parameter is used to override the Elastic Inference accelerator specified in the task definition. For more information, see [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_InferenceAcceleratorOverride_Contents"></a>

 ** deviceName **   <a name="ECS-Type-InferenceAcceleratorOverride-deviceName"></a>
The Elastic Inference accelerator device name to override for the task. This parameter must match a `deviceName` specified in the task definition.
Type: String
Required: No

 ** deviceType **   <a name="ECS-Type-InferenceAcceleratorOverride-deviceType"></a>
The Elastic Inference accelerator type to use.
Type: String
Required: No

## See Also
<a name="API_InferenceAcceleratorOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/InferenceAcceleratorOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/InferenceAcceleratorOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/InferenceAcceleratorOverride)
