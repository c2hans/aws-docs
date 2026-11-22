---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnectorderegistrationdelay.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service GatewayConnectorDeregistrationDelay

The amount of time to allow in-flight requests to complete before a deregistering target is removed.

## Syntax
<a name="aws-properties-ecs-service-gatewayconnectorderegistrationdelay-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-gatewayconnectorderegistrationdelay-syntax.json"></a>

```json
{
  "[TimeoutSeconds](#cfn-ecs-service-gatewayconnectorderegistrationdelay-timeoutseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-service-gatewayconnectorderegistrationdelay-syntax.yaml"></a>

```yaml
  [TimeoutSeconds](#cfn-ecs-service-gatewayconnectorderegistrationdelay-timeoutseconds): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-service-gatewayconnectorderegistrationdelay-properties"></a>

`TimeoutSeconds`  <a name="cfn-ecs-service-gatewayconnectorderegistrationdelay-timeoutseconds"></a>
The amount of time, in seconds, to wait before a deregistering target is removed. A value of `0` removes the target immediately. The valid range is 0-3600 seconds. The default value is 300 seconds.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
