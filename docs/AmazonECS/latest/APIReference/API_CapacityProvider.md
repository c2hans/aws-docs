---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CapacityProvider.html
---

# CapacityProvider
<a name="API_CapacityProvider"></a>

The details for a capacity provider.

## Contents
<a name="API_CapacityProvider_Contents"></a>

 ** autoScalingGroupProvider **   <a name="ECS-Type-CapacityProvider-autoScalingGroupProvider"></a>
The Auto Scaling group settings for the capacity provider.
Type: [AutoScalingGroupProvider](API_AutoScalingGroupProvider.md) object
Required: No

 ** capacityProviderArn **   <a name="ECS-Type-CapacityProvider-capacityProviderArn"></a>
The Amazon Resource Name (ARN) that identifies the capacity provider.
Type: String
Required: No

 ** cluster **   <a name="ECS-Type-CapacityProvider-cluster"></a>
The cluster that this capacity provider is associated with. Managed instances capacity providers are cluster-scoped, meaning they can only be used within their associated cluster.
This is required for Managed instances.
Type: String
Required: No

 ** managedInstancesProvider **   <a name="ECS-Type-CapacityProvider-managedInstancesProvider"></a>
The configuration for the Amazon ECS Managed Instances provider. This includes the infrastructure role, the launch template configuration, and tag propagation settings.
Type: [ManagedInstancesProvider](API_ManagedInstancesProvider.md) object
Required: No

 ** name **   <a name="ECS-Type-CapacityProvider-name"></a>
The name of the capacity provider.
Type: String
Required: No

 ** status **   <a name="ECS-Type-CapacityProvider-status"></a>
The current status of the capacity provider. Only capacity providers in an `ACTIVE` state can be used in a cluster. When a capacity provider is successfully deleted, it has an `INACTIVE` status.
Type: String
Valid Values: `PROVISIONING | ACTIVE | DEPROVISIONING | INACTIVE`
Required: No

 ** tags **   <a name="ECS-Type-CapacityProvider-tags"></a>
The metadata that you apply to the capacity provider to help you categorize and organize it. Each tag consists of a key and an optional value. You define both.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** type **   <a name="ECS-Type-CapacityProvider-type"></a>
The type of capacity provider. For Amazon ECS Managed Instances, this value is `MANAGED_INSTANCES`, indicating that Amazon ECS manages the underlying Amazon EC2 instances on your behalf.
Type: String
Valid Values: `EC2_AUTOSCALING | MANAGED_INSTANCES | FARGATE | FARGATE_SPOT`
Required: No

 ** updateStatus **   <a name="ECS-Type-CapacityProvider-updateStatus"></a>
The update status of the capacity provider. The following are the possible states that is returned.
DELETE\_IN\_PROGRESS
The capacity provider is in the process of being deleted.
DELETE\_COMPLETE
The capacity provider was successfully deleted and has an `INACTIVE` status.
DELETE\_FAILED
The capacity provider can't be deleted. The update status reason provides further details about why the delete failed.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_COMPLETE | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_COMPLETE | DELETE_FAILED | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED`
Required: No

 ** updateStatusReason **   <a name="ECS-Type-CapacityProvider-updateStatusReason"></a>
The update status reason. This provides further details about the update status for the capacity provider.
Type: String
Required: No

## See Also
<a name="API_CapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/CapacityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/CapacityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/CapacityProvider)
