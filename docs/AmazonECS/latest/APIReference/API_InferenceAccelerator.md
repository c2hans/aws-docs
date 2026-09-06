---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InferenceAccelerator.html
---

# InferenceAccelerator
<a name="API_InferenceAccelerator"></a>

 *This data type has been deprecated.*

Details on an Elastic Inference accelerator. For more information, see [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_InferenceAccelerator_Contents"></a>

 ** deviceName **   <a name="ECS-Type-InferenceAccelerator-deviceName"></a>
The Elastic Inference accelerator device name. The `deviceName` must also be referenced in a container definition as a [ResourceRequirement](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ResourceRequirement.html).
Type: String
Required: Yes

 ** deviceType **   <a name="ECS-Type-InferenceAccelerator-deviceType"></a>
The Elastic Inference accelerator type to use.
Type: String
Required: Yes

## See Also
<a name="API_InferenceAccelerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/InferenceAccelerator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/InferenceAccelerator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/InferenceAccelerator)
