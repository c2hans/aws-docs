---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-logdrivervolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition LogDriverVolumeConfiguration
<a name="aws-properties-ecs-daemontaskdefinition-logdrivervolumeconfiguration"></a>

The configuration for a log driver volume in a daemon task definition. The volume contains the log files for each container on the container instance that uses the specified log driver in its `logConfiguration`. Containers that use a different log driver don't write log files to the volume.

For the `json-file` log driver, the volume has one directory for each container, named with the container ID. Each directory contains the container's log file, `<container-id>-json.log`, and any rotated log files. After a container stops and Amazon ECS removes it, Amazon ECS deletes the container's directory. Read the log files before the container is removed.

## Syntax
<a name="aws-properties-ecs-daemontaskdefinition-logdrivervolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemontaskdefinition-logdrivervolumeconfiguration-syntax.json"></a>

```
{
  "[Driver](#cfn-ecs-daemontaskdefinition-logdrivervolumeconfiguration-driver)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-daemontaskdefinition-logdrivervolumeconfiguration-syntax.yaml"></a>

```
  [Driver](#cfn-ecs-daemontaskdefinition-logdrivervolumeconfiguration-driver): {{String}}
```

## Properties
<a name="aws-properties-ecs-daemontaskdefinition-logdrivervolumeconfiguration-properties"></a>

`Driver`  <a name="cfn-ecs-daemontaskdefinition-logdrivervolumeconfiguration-driver"></a>
The log driver whose log files the volume contains. The only supported value is `json-file`.
*Required*: Yes
*Type*: String
*Allowed values*: `json-file | syslog | journald | gelf | fluentd | awslogs | splunk | awsfirelens`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
