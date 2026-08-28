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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
