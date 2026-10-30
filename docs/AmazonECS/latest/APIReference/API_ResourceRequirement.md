---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ResourceRequirement.html
---

# ResourceRequirement
<a name="API_ResourceRequirement"></a>

The type and amount of a resource to assign to a container. The supported resource types are GPUs, Neuron devices, and Elastic Inference accelerators. For more information, see [Working with GPUs on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html) or [Working with Amazon Elastic Inference on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html) in the *Amazon Elastic Container Service Developer Guide*

## Contents
<a name="API_ResourceRequirement_Contents"></a>

 ** type **   <a name="ECS-Type-ResourceRequirement-type"></a>
The type of resource to assign to a container.
Type: String
Valid Values: `GPU | InferenceAccelerator | NeuronDevice`
Required: Yes

 ** sharingStrategy **   <a name="ECS-Type-ResourceRequirement-sharingStrategy"></a>
The strategy that the container uses to share a GPU with other containers. Specify a sharing strategy only when the type is `GPU`. For a GPU resource requirement, specify either `value` or `sharingStrategy`, but not both. If you don't specify a sharing strategy, the container has exclusive use of each GPU that Amazon ECS assigns to it. The containers in a task that request GPUs must all use the same option.
You can use GPU sharing with tasks that run on Amazon EC2 instances or Amazon ECS Managed Instances. Task definitions that require `EXTERNAL` compatibility don't support GPU sharing.
Type: [SharingStrategy](API_SharingStrategy.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** value **   <a name="ECS-Type-ResourceRequirement-value"></a>
The value for the specified resource type.
You must specify this parameter unless the type is `GPU` and you specify `sharingStrategy`.
When the type is `GPU`, the value is the number of physical `GPUs` the Amazon ECS container agent reserves for the container. The number of GPUs that's reserved for all containers in a task can't exceed the number of available GPUs on the container instance that the task is launched on. You can also specify `ALL` to allocate all available GPUs on the instance to the container.
When the type is `NeuronDevice`, the value must be `ALL`. This allocates all available Neuron devices on the instance to the container. Only one container in a task can specify `NeuronDevice` resources. This resource type is only supported on Managed Instances.
When the type is `InferenceAccelerator`, the `value` matches the `deviceName` for an [InferenceAccelerator](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InferenceAccelerator.html) specified in a task definition.
Type: String
Required: No

## See Also
<a name="API_ResourceRequirement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ResourceRequirement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ResourceRequirement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ResourceRequirement)
