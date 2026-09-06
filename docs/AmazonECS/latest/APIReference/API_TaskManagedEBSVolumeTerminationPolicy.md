---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeTerminationPolicy.html
---

# TaskManagedEBSVolumeTerminationPolicy
<a name="API_TaskManagedEBSVolumeTerminationPolicy"></a>

The termination policy for the Amazon EBS volume when the task exits. For more information, see [Amazon ECS volume termination policy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types).

## Contents
<a name="API_TaskManagedEBSVolumeTerminationPolicy_Contents"></a>

 ** deleteOnTermination **   <a name="ECS-Type-TaskManagedEBSVolumeTerminationPolicy-deleteOnTermination"></a>
Indicates whether the volume should be deleted on when the task stops. If a value of `true` is specified, Amazon ECS deletes the Amazon EBS volume on your behalf when the task goes into the `STOPPED` state. If no value is specified, the default value is `true` is used. When set to `false`, Amazon ECS leaves the volume in your account.
Type: Boolean
Required: Yes

## See Also
<a name="API_TaskManagedEBSVolumeTerminationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TaskManagedEBSVolumeTerminationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TaskManagedEBSVolumeTerminationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TaskManagedEBSVolumeTerminationPolicy)
