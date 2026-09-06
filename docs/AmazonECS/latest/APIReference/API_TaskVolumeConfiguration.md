---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskVolumeConfiguration.html
---

# TaskVolumeConfiguration
<a name="API_TaskVolumeConfiguration"></a>

Configuration settings for the task volume that was `configuredAtLaunch` that weren't set during `RegisterTaskDef`.

## Contents
<a name="API_TaskVolumeConfiguration_Contents"></a>

 ** name **   <a name="ECS-Type-TaskVolumeConfiguration-name"></a>
The name of the volume. This value must match the volume name from the `Volume` object in the task definition.
Type: String
Required: Yes

 ** managedEBSVolume **   <a name="ECS-Type-TaskVolumeConfiguration-managedEBSVolume"></a>
The configuration for the Amazon EBS volume that Amazon ECS creates and manages on your behalf. These settings are used to create each Amazon EBS volume, with one volume created for each task. The Amazon EBS volumes are visible in your account in the Amazon EC2 console once they are created.
Type: [TaskManagedEBSVolumeConfiguration](API_TaskManagedEBSVolumeConfiguration.md) object
Required: No

## See Also
<a name="API_TaskVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TaskVolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TaskVolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TaskVolumeConfiguration)
