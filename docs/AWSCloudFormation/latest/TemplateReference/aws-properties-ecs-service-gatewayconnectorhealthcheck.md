---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnectorhealthcheck.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service GatewayConnectorHealthCheck
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheck"></a>

<a name="aws-properties-ecs-service-gatewayconnectorhealthcheck-description"></a>The `GatewayConnectorHealthCheck` property type specifies Property description not available. for an [AWS::ECS::Service](aws-resource-ecs-service.md).

## Syntax
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheck-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheck-syntax.json"></a>

```
{
  "[HealthCheckIntervalSeconds](#cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckintervalseconds)" : {{Integer}},
  "[HealthCheckPath](#cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckpath)" : {{String}},
  "[HealthCheckPort](#cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckport)" : {{Integer}},
  "[HealthCheckProtocol](#cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckprotocol)" : {{String}},
  "[HealthCheckTimeoutSeconds](#cfn-ecs-service-gatewayconnectorhealthcheck-healthchecktimeoutseconds)" : {{Integer}},
  "[HealthyThresholdCount](#cfn-ecs-service-gatewayconnectorhealthcheck-healthythresholdcount)" : {{Integer}},
  "[Matcher](#cfn-ecs-service-gatewayconnectorhealthcheck-matcher)" : {{GatewayConnectorHealthCheckMatcher}},
  "[UnhealthyThresholdCount](#cfn-ecs-service-gatewayconnectorhealthcheck-unhealthythresholdcount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheck-syntax.yaml"></a>

```
  [HealthCheckIntervalSeconds](#cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckintervalseconds): {{Integer}}
  [HealthCheckPath](#cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckpath): {{String}}
  [HealthCheckPort](#cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckport): {{Integer}}
  [HealthCheckProtocol](#cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckprotocol): {{String}}
  [HealthCheckTimeoutSeconds](#cfn-ecs-service-gatewayconnectorhealthcheck-healthchecktimeoutseconds): {{Integer}}
  [HealthyThresholdCount](#cfn-ecs-service-gatewayconnectorhealthcheck-healthythresholdcount): {{Integer}}
  [Matcher](#cfn-ecs-service-gatewayconnectorhealthcheck-matcher): {{
    GatewayConnectorHealthCheckMatcher}}
  [UnhealthyThresholdCount](#cfn-ecs-service-gatewayconnectorhealthcheck-unhealthythresholdcount): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheck-properties"></a>

`HealthCheckIntervalSeconds`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckintervalseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckPath`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckpath"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckPort`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckport"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckProtocol`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckprotocol"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `HTTP | HTTPS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckTimeoutSeconds`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthchecktimeoutseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthyThresholdCount`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthythresholdcount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Matcher`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-matcher"></a>
Property description not available.
*Required*: No
*Type*: [GatewayConnectorHealthCheckMatcher](aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnhealthyThresholdCount`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-unhealthythresholdcount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
