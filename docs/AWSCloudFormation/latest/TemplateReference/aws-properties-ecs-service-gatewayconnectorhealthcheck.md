---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnectorhealthcheck.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service GatewayConnectorHealthCheck
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheck"></a>

The health check configuration that a gateway uses to evaluate the targets associated with a gateway connector.

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
The approximate amount of time, in seconds, between health checks of an individual target.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckPath`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckpath"></a>
The destination path for health check requests.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckPort`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckport"></a>
The port that the gateway uses to perform health checks on the targets.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckProtocol`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthcheckprotocol"></a>
The protocol that the gateway uses to perform health checks.
Valid values:
+ `HTTP` - Health checks are performed over HTTP.
+ `HTTPS` - Health checks are performed over HTTPS.
*Required*: No
*Type*: String
*Allowed values*: `HTTP | HTTPS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckTimeoutSeconds`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthchecktimeoutseconds"></a>
The amount of time, in seconds, during which no response from a target means a failed health check.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthyThresholdCount`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-healthythresholdcount"></a>
The number of consecutive successful health checks that a target must pass before the gateway considers it healthy.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Matcher`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-matcher"></a>
The HTTP or gRPC codes that indicate a successful health check response from a target.
*Required*: No
*Type*: [GatewayConnectorHealthCheckMatcher](aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnhealthyThresholdCount`  <a name="cfn-ecs-service-gatewayconnectorhealthcheck-unhealthythresholdcount"></a>
The number of consecutive failed health checks that a target must fail before the gateway considers it unhealthy.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
