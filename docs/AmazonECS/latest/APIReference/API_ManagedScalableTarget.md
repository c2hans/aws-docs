---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedScalableTarget.html
---

# ManagedScalableTarget
<a name="API_ManagedScalableTarget"></a>

Represents a scalable target.

## Contents
<a name="API_ManagedScalableTarget_Contents"></a>

 ** maxCapacity **   <a name="ECS-Type-ManagedScalableTarget-maxCapacity"></a>
The maximum value to scale to in response to a scale-out activity.
Type: Integer
Required: Yes

 ** minCapacity **   <a name="ECS-Type-ManagedScalableTarget-minCapacity"></a>
The minimum value to scale to in response to a scale-in activity.
Type: Integer
Required: Yes

 ** status **   <a name="ECS-Type-ManagedScalableTarget-status"></a>
The status of the scalable target.
Type: String
Valid Values: `PROVISIONING | ACTIVE | DEPROVISIONING | DELETED | FAILED`
Required: Yes

 ** updatedAt **   <a name="ECS-Type-ManagedScalableTarget-updatedAt"></a>
The Unix timestamp for when the target was most recently updated.
Type: Timestamp
Required: Yes

 ** arn **   <a name="ECS-Type-ManagedScalableTarget-arn"></a>
The ARN of the scalable target.
Type: String
Required: No

 ** statusReason **   <a name="ECS-Type-ManagedScalableTarget-statusReason"></a>
Information about why the scalable target is in the current status.
Type: String
Required: No

## See Also
<a name="API_ManagedScalableTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedScalableTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedScalableTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedScalableTarget)
