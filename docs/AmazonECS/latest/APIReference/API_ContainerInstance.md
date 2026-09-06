---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerInstance.html
---

# ContainerInstance
<a name="API_ContainerInstance"></a>

An Amazon EC2 or External instance that's running the Amazon ECS agent and has been registered with a cluster.

## Contents
<a name="API_ContainerInstance_Contents"></a>

 ** agentConnected **   <a name="ECS-Type-ContainerInstance-agentConnected"></a>
This parameter returns `true` if the agent is connected to Amazon ECS. An instance with an agent that may be unhealthy or stopped return `false`. Only instances connected to an agent can accept task placement requests.
Type: Boolean
Required: No

 ** agentUpdateStatus **   <a name="ECS-Type-ContainerInstance-agentUpdateStatus"></a>
The status of the most recent agent update. If an update wasn't ever requested, this value is `NULL`.
Type: String
Valid Values: `PENDING | STAGING | STAGED | UPDATING | UPDATED | FAILED`
Required: No

 ** attachments **   <a name="ECS-Type-ContainerInstance-attachments"></a>
The resources attached to a container instance, such as an elastic network interface.
Type: Array of [Attachment](API_Attachment.md) objects
Required: No

 ** attributes **   <a name="ECS-Type-ContainerInstance-attributes"></a>
The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the [PutAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAttributes.html) operation.
Type: Array of [Attribute](API_Attribute.md) objects
Required: No

 ** capacityProviderName **   <a name="ECS-Type-ContainerInstance-capacityProviderName"></a>
The capacity provider that's associated with the container instance.
Type: String
Required: No

 ** containerInstanceArn **   <a name="ECS-Type-ContainerInstance-containerInstanceArn"></a>
The Amazon Resource Name (ARN) of the container instance. For more information about the ARN format, see [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids) in the *Amazon ECS Developer Guide*.
Type: String
Required: No

 ** ec2InstanceId **   <a name="ECS-Type-ContainerInstance-ec2InstanceId"></a>
The ID of the container instance. For Amazon EC2 instances, this value is the Amazon EC2 instance ID. For external instances, this value is the AWS Systems Manager managed instance ID.
Type: String
Required: No

 ** healthStatus **   <a name="ECS-Type-ContainerInstance-healthStatus"></a>
An object representing the health status of the container instance.
Type: [ContainerInstanceHealthStatus](API_ContainerInstanceHealthStatus.md) object
Required: No

 ** pendingTasksCount **   <a name="ECS-Type-ContainerInstance-pendingTasksCount"></a>
The number of tasks on the container instance that are in the `PENDING` status.
Type: Integer
Required: No

 ** registeredAt **   <a name="ECS-Type-ContainerInstance-registeredAt"></a>
The Unix timestamp for the time when the container instance was registered.
Type: Timestamp
Required: No

 ** registeredResources **   <a name="ECS-Type-ContainerInstance-registeredResources"></a>
For CPU and memory resource types, this parameter describes the amount of each resource that was available on the container instance when the container agent registered it with Amazon ECS. This value represents the total amount of CPU and memory that can be allocated on this container instance to tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.
Type: Array of [Resource](API_Resource.md) objects
Required: No

 ** remainingResources **   <a name="ECS-Type-ContainerInstance-remainingResources"></a>
For CPU and memory resource types, this parameter describes the remaining CPU and memory that wasn't already allocated to tasks and is therefore available for new tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent (at instance registration time) and any task containers that have reserved port mappings on the host (with the `host` or `bridge` network mode). Any port that's not specified here is available for new tasks.
Type: Array of [Resource](API_Resource.md) objects
Required: No

 ** runningTasksCount **   <a name="ECS-Type-ContainerInstance-runningTasksCount"></a>
The number of tasks on the container instance that have a desired status (`desiredStatus`) of `RUNNING`.
Type: Integer
Required: No

 ** status **   <a name="ECS-Type-ContainerInstance-status"></a>
The status of the container instance. The valid values are `REGISTERING`, `REGISTRATION_FAILED`, `ACTIVE`, `INACTIVE`, `DEREGISTERING`, or `DRAINING`.
If your account has opted in to the `awsvpcTrunking` account setting, then any newly registered container instance will transition to a `REGISTERING` status while the trunk elastic network interface is provisioned for the instance. If the registration fails, the instance will transition to a `REGISTRATION_FAILED` status. You can describe the container instance and see the reason for failure in the `statusReason` parameter. Once the container instance is terminated, the instance transitions to a `DEREGISTERING` status while the trunk elastic network interface is deprovisioned. The instance then transitions to an `INACTIVE` status.
The `ACTIVE` status indicates that the container instance can accept tasks. The `DRAINING` indicates that new tasks aren't placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see [Container instance draining](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** statusReason **   <a name="ECS-Type-ContainerInstance-statusReason"></a>
The reason that the container instance reached its current status.
Type: String
Required: No

 ** tags **   <a name="ECS-Type-ContainerInstance-tags"></a>
The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.
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

 ** version **   <a name="ECS-Type-ContainerInstance-version"></a>
The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you're replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the `detail` object) to verify that the version in your event stream is current.
Type: Long
Required: No

 ** versionInfo **   <a name="ECS-Type-ContainerInstance-versionInfo"></a>
The version information for the Amazon ECS container agent and Docker daemon running on the container instance.
Type: [VersionInfo](API_VersionInfo.md) object
Required: No

## See Also
<a name="API_ContainerInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ContainerInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ContainerInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ContainerInstance)
