---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-daemontaskdefinition-firelensconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::DaemonTaskDefinition FirelensConfiguration
<a name="aws-properties-ecs-daemontaskdefinition-firelensconfiguration"></a>

The FireLens configuration for the container. This is used to specify and configure a log router for container logs. For more information, see [Custom log routing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-daemontaskdefinition-firelensconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-daemontaskdefinition-firelensconfiguration-syntax.json"></a>

```
{
  "[Options](#cfn-ecs-daemontaskdefinition-firelensconfiguration-options)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Type](#cfn-ecs-daemontaskdefinition-firelensconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-daemontaskdefinition-firelensconfiguration-syntax.yaml"></a>

```
  [Options](#cfn-ecs-daemontaskdefinition-firelensconfiguration-options): {{
    {{Key}}: {{Value}}}}
  [Type](#cfn-ecs-daemontaskdefinition-firelensconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-ecs-daemontaskdefinition-firelensconfiguration-properties"></a>

`Options`  <a name="cfn-ecs-daemontaskdefinition-firelensconfiguration-options"></a>
The options to use when configuring the log router. This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event. If specified, the syntax to use is `"options":{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::mybucket/fluent.conf|filepath"}`. For more information, see [Creating a task definition that uses a FireLens configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html#firelens-taskdef) in the *Amazon Elastic Container Service Developer Guide*.
Tasks hosted on AWS Fargate only support the `file` configuration file type.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-ecs-daemontaskdefinition-firelensconfiguration-type"></a>
The log router to use. The valid values are `fluentd` or `fluentbit`.
*Required*: No
*Type*: String
*Allowed values*: `fluentd | fluentbit`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
