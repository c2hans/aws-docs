---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service GatewayConnectorHealthCheckMatcher
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher"></a>

The codes that indicate a successful health check response from a target.

## Syntax
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher-syntax.json"></a>

```
{
  "[GrpcCode](#cfn-ecs-service-gatewayconnectorhealthcheckmatcher-grpccode)" : {{String}},
  "[HttpCode](#cfn-ecs-service-gatewayconnectorhealthcheckmatcher-httpcode)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher-syntax.yaml"></a>

```
  [GrpcCode](#cfn-ecs-service-gatewayconnectorhealthcheckmatcher-grpccode): {{String}}
  [HttpCode](#cfn-ecs-service-gatewayconnectorhealthcheckmatcher-httpcode): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-gatewayconnectorhealthcheckmatcher-properties"></a>

`GrpcCode`  <a name="cfn-ecs-service-gatewayconnectorhealthcheckmatcher-grpccode"></a>
The gRPC codes that indicate a successful response from a target.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpCode`  <a name="cfn-ecs-service-gatewayconnectorhealthcheckmatcher-httpcode"></a>
The HTTP codes that indicate a successful response from a target.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
