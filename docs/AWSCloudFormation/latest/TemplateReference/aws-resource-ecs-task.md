---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-task.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Task
<a name="aws-resource-ecs-task"></a>

Details on a task in a cluster.

## Syntax
<a name="aws-resource-ecs-task-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecs-task-syntax.json"></a>

```
{
  "Type" : "AWS::ECS::Task"
}
```

### YAML
<a name="aws-resource-ecs-task-syntax.yaml"></a>

```
Type: AWS::ECS::Task
```

## Return values
<a name="aws-resource-ecs-task-return-values"></a>

### Ref
<a name="aws-resource-ecs-task-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ecs-task-return-values-fn--getatt"></a>

####
<a name="aws-resource-ecs-task-return-values-fn--getatt-fn--getatt"></a>

`Cluster`  <a name="Cluster-fn::getatt"></a>
The short name or full Amazon Resource Name (ARN) of the cluster to run your task on. If you do not specify a cluster, the default cluster is assumed.
Each account receives a default cluster the first time you use the service, but you may also create other clusters.

`Cpu`  <a name="Cpu-fn::getatt"></a>
The number of CPU units used by the task as expressed in a task definition. It can be expressed as an integer using CPU units (for example, `1024`). It can also be expressed as a string using vCPUs (for example, `1 vCPU` or `1 vcpu`). String values are converted to an integer that indicates the CPU units when the task definition is registered.
If you're using the EC2 launch type or the external launch type, this field is optional. Supported values are between `128` CPU units (`0.125` vCPUs) and `196608` CPU units (`192` vCPUs). If you do not specify a value, the parameter is ignored.
This field is required for Fargate. For information about the valid values, see [Task size](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size) in the *Amazon Elastic Container Service Developer Guide*.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp for the time when the task was created. More specifically, it's for the time when the task entered the `PENDING` state.

`DesiredStatus`  <a name="DesiredStatus-fn::getatt"></a>
The desired status of the task. For more information, see [Task Lifecycle](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle.html).

`Group`  <a name="Group-fn::getatt"></a>
The name of the task group that's associated with the task.

`LastStatus`  <a name="LastStatus-fn::getatt"></a>
The last known status for the task. For more information, see [Task Lifecycle](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle.html).

`LaunchType`  <a name="LaunchType-fn::getatt"></a>
The infrastructure where your task runs on. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.

`Memory`  <a name="Memory-fn::getatt"></a>
The amount of memory (in MiB) that the task uses as expressed in a task definition. It can be expressed as an integer using MiB (for example, `1024`). If it's expressed as a string using GB (for example, `1GB` or `1 GB`), it's converted to an integer indicating the MiB when the task definition is registered.
If you use the EC2 launch type, this field is optional.
If you use the Fargate launch type, this field is required. You must use one of the following values. The value that you choose determines the range of supported values for the `cpu` parameter.
+ 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available `cpu` values: 256 (.25 vCPU)
+ 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available `cpu` values: 512 (.5 vCPU)
+ 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available `cpu` values: 1024 (1 vCPU)
+ Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available `cpu` values: 2048 (2 vCPU)
+ Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available `cpu` values: 4096 (4 vCPU)
+ Between 16 GB and 60 GB in 4 GB increments - Available `cpu` values: 8192 (8 vCPU)

  This option requires Linux platform `1.4.0` or later.
+ Between 32GB and 120 GB in 8 GB increments - Available `cpu` values: 16384 (16 vCPU)

  This option requires Linux platform `1.4.0` or later.

`StartedBy`  <a name="StartedBy-fn::getatt"></a>
The tag specified when a task is started. If an Amazon ECS service started the task, the `startedBy` parameter contains the deployment ID of that service.

`Tags`  <a name="Tags-fn::getatt"></a>
The metadata that you apply to the task to help you categorize and organize the task. Each tag consists of a key and an optional value. You define both the key and value.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

`TaskArn`  <a name="TaskArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the task.

`TaskDefinition`  <a name="TaskDefinition-fn::getatt"></a>
The `family` and `revision` (`family:revision`) or full ARN of the task definition to run. If a `revision` isn't specified, the latest `ACTIVE` revision is used.
The full ARN value must match the value that you specified as the `Resource` of the principal's permissions policy.
When you specify a task definition, you must either specify a specific revision, or all revisions in the ARN.
To specify a specific revision, include the revision number in the ARN. For example, to specify revision 2, use `arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:2`.
To specify all revisions, use the wildcard (\*) in the ARN. For example, to specify all revisions, use `arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:*`.
For more information, see [Policy Resources for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources) in the Amazon Elastic Container Service Developer Guide.

`TaskId`  <a name="TaskId-fn::getatt"></a>
Property description not available.
