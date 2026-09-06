---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService ExpressGatewayServiceAwsLogsConfiguration
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration"></a>

Specifies the Amazon CloudWatch Logs configuration for the Express service container.

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration-syntax.json"></a>

```
{
  "[LogGroup](#cfn-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration-loggroup)" : {{String}},
  "[LogStreamPrefix](#cfn-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration-logstreamprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration-syntax.yaml"></a>

```
  [LogGroup](#cfn-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration-loggroup): {{String}}
  [LogStreamPrefix](#cfn-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration-logstreamprefix): {{String}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration-properties"></a>

`LogGroup`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration-loggroup"></a>
The name of the CloudWatch Logs log group to send container logs to.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogStreamPrefix`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceawslogsconfiguration-logstreamprefix"></a>
The prefix for the CloudWatch Logs log stream names. The default for an Express service is `ecs`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
