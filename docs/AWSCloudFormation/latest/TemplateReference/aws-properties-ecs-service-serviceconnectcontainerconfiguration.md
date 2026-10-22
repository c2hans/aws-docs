---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnectcontainerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service ServiceConnectContainerConfiguration
<a name="aws-properties-ecs-service-serviceconnectcontainerconfiguration"></a>

Contains a configuration setting for the Service Connect proxy container, such as the log level. Specify exactly one member in each object.

## Syntax
<a name="aws-properties-ecs-service-serviceconnectcontainerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-serviceconnectcontainerconfiguration-syntax.json"></a>

```
{
  "[LogLevel](#cfn-ecs-service-serviceconnectcontainerconfiguration-loglevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-serviceconnectcontainerconfiguration-syntax.yaml"></a>

```
  [LogLevel](#cfn-ecs-service-serviceconnectcontainerconfiguration-loglevel): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-serviceconnectcontainerconfiguration-properties"></a>

`LogLevel`  <a name="cfn-ecs-service-serviceconnectcontainerconfiguration-loglevel"></a>
The log level of the Service Connect proxy container. Set the log level to `debug` to collect more detailed proxy logs when you troubleshoot connectivity issues between services, and set it back to `info` when you finish. Debug logging increases the volume of logs that the proxy container writes. If you don't specify a log level, the default is `info`.
*Required*: No
*Type*: String
*Allowed values*: `debug | info`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
