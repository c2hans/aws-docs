---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition DockerVolumeConfiguration
<a name="aws-properties-ecs-taskdefinition-dockervolumeconfiguration"></a>

The `DockerVolumeConfiguration` property specifies a Docker volume configuration and is used when you use Docker volumes. Docker volumes are only supported when you are using the EC2 launch type. Windows containers only support the use of the `local` driver. To use bind mounts, specify a `host` instead.

## Syntax
<a name="aws-properties-ecs-taskdefinition-dockervolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-dockervolumeconfiguration-syntax.json"></a>

```
{
  "[Autoprovision](#cfn-ecs-taskdefinition-dockervolumeconfiguration-autoprovision)" : {{Boolean}},
  "[Driver](#cfn-ecs-taskdefinition-dockervolumeconfiguration-driver)" : {{String}},
  "[DriverOpts](#cfn-ecs-taskdefinition-dockervolumeconfiguration-driveropts)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Labels](#cfn-ecs-taskdefinition-dockervolumeconfiguration-labels)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Scope](#cfn-ecs-taskdefinition-dockervolumeconfiguration-scope)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-dockervolumeconfiguration-syntax.yaml"></a>

```
  [Autoprovision](#cfn-ecs-taskdefinition-dockervolumeconfiguration-autoprovision): {{Boolean}}
  [Driver](#cfn-ecs-taskdefinition-dockervolumeconfiguration-driver): {{String}}
  [DriverOpts](#cfn-ecs-taskdefinition-dockervolumeconfiguration-driveropts): {{
    {{Key}}: {{Value}}}}
  [Labels](#cfn-ecs-taskdefinition-dockervolumeconfiguration-labels): {{
    {{Key}}: {{Value}}}}
  [Scope](#cfn-ecs-taskdefinition-dockervolumeconfiguration-scope): {{String}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-dockervolumeconfiguration-properties"></a>

`Autoprovision`  <a name="cfn-ecs-taskdefinition-dockervolumeconfiguration-autoprovision"></a>
If this value is `true`, the Docker volume is created if it doesn't already exist.
This field is only used if the `scope` is `shared`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Driver`  <a name="cfn-ecs-taskdefinition-dockervolumeconfiguration-driver"></a>
The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use `docker plugin ls` to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. This parameter maps to `Driver` in the docker container create command and the `xxdriver` option to docker volume create.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DriverOpts`  <a name="cfn-ecs-taskdefinition-dockervolumeconfiguration-driveropts"></a>
A map of Docker driver-specific options passed through. This parameter maps to `DriverOpts` in the docker create-volume command and the `xxopt` option to docker volume create.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Labels`  <a name="cfn-ecs-taskdefinition-dockervolumeconfiguration-labels"></a>
Custom metadata to add to your Docker volume. This parameter maps to `Labels` in the docker container create command and the `xxlabel` option to docker volume create.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scope`  <a name="cfn-ecs-taskdefinition-dockervolumeconfiguration-scope"></a>
The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a `task` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as `shared` persist after the task stops.
*Required*: No
*Type*: String
*Allowed values*: `task | shared`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
