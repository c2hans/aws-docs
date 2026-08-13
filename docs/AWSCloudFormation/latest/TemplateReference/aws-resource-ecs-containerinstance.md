---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-containerinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ContainerInstance
<a name="aws-resource-ecs-containerinstance"></a>

An Amazon EC2 or External instance that's running the Amazon ECS agent and has been registered with a cluster.

## Syntax
<a name="aws-resource-ecs-containerinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecs-containerinstance-syntax.json"></a>

```
{
  "Type" : "AWS::ECS::ContainerInstance"
}
```

### YAML
<a name="aws-resource-ecs-containerinstance-syntax.yaml"></a>

```
Type: AWS::ECS::ContainerInstance
```

## Return values
<a name="aws-resource-ecs-containerinstance-return-values"></a>

### Ref
<a name="aws-resource-ecs-containerinstance-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ecs-containerinstance-return-values-fn--getatt"></a>

####
<a name="aws-resource-ecs-containerinstance-return-values-fn--getatt-fn--getatt"></a>

`AgentConnected`  <a name="AgentConnected-fn::getatt"></a>
This parameter returns `true` if the agent is connected to Amazon ECS. An instance with an agent that may be unhealthy or stopped return `false`. Only instances connected to an agent can accept task placement requests.

`Attributes`  <a name="Attributes-fn::getatt"></a>
The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the [PutAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAttributes.html) operation.

`Cluster`  <a name="Cluster-fn::getatt"></a>
The short name or full Amazon Resource Name (ARN) of the cluster to register your container instance with. If you do not specify a cluster, the default cluster is assumed.

`ContainerInstanceArn`  <a name="ContainerInstanceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the container instance. For more information about the ARN format, see [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids) in the *Amazon ECS Developer Guide*.

`ContainerInstanceId`  <a name="ContainerInstanceId-fn::getatt"></a>
Property description not available.

`Ec2InstanceId`  <a name="Ec2InstanceId-fn::getatt"></a>
The ID of the container instance. For Amazon EC2 instances, this value is the Amazon EC2 instance ID. For external instances, this value is the AWS Systems Manager managed instance ID.

`PendingTasksCount`  <a name="PendingTasksCount-fn::getatt"></a>
The number of tasks on the container instance that are in the `PENDING` status.

`RegisteredAt`  <a name="RegisteredAt-fn::getatt"></a>
The Unix timestamp for the time when the container instance was registered.

`RegisteredResources`  <a name="RegisteredResources-fn::getatt"></a>
For CPU and memory resource types, this parameter describes the amount of each resource that was available on the container instance when the container agent registered it with Amazon ECS. This value represents the total amount of CPU and memory that can be allocated on this container instance to tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.

`RemainingResources`  <a name="RemainingResources-fn::getatt"></a>
For CPU and memory resource types, this parameter describes the remaining CPU and memory that wasn't already allocated to tasks and is therefore available for new tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent (at instance registration time) and any task containers that have reserved port mappings on the host (with the `host` or `bridge` network mode). Any port that's not specified here is available for new tasks.

`RunningTasksCount`  <a name="RunningTasksCount-fn::getatt"></a>
The number of tasks on the container instance that have a desired status (`desiredStatus`) of `RUNNING`.

`Status`  <a name="Status-fn::getatt"></a>
The status of the container instance. The valid values are `REGISTERING`, `REGISTRATION_FAILED`, `ACTIVE`, `INACTIVE`, `DEREGISTERING`, or `DRAINING`.
If your account has opted in to the `awsvpcTrunking` account setting, then any newly registered container instance will transition to a `REGISTERING` status while the trunk elastic network interface is provisioned for the instance. If the registration fails, the instance will transition to a `REGISTRATION_FAILED` status. You can describe the container instance and see the reason for failure in the `statusReason` parameter. Once the container instance is terminated, the instance transitions to a `DEREGISTERING` status while the trunk elastic network interface is deprovisioned. The instance then transitions to an `INACTIVE` status.
The `ACTIVE` status indicates that the container instance can accept tasks. The `DRAINING` indicates that new tasks aren't placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see [Container instance draining](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html) in the *Amazon Elastic Container Service Developer Guide*.

`Tags`  <a name="Tags-fn::getatt"></a>
The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

`Version`  <a name="Version-fn::getatt"></a>
The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you're replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the `detail` object) to verify that the version in your event stream is current.
