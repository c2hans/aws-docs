---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-gatewayconnectorfilters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service GatewayConnectorFilters
<a name="aws-properties-ecs-service-gatewayconnectorfilters"></a>

The filters that determine which gateway ingress paths a connector applies to.

## Syntax
<a name="aws-properties-ecs-service-gatewayconnectorfilters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-gatewayconnectorfilters-syntax.json"></a>

```
{
  "[AccessTypes](#cfn-ecs-service-gatewayconnectorfilters-accesstypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-service-gatewayconnectorfilters-syntax.yaml"></a>

```
  [AccessTypes](#cfn-ecs-service-gatewayconnectorfilters-accesstypes): {{
    - String}}
```

## Properties
<a name="aws-properties-ecs-service-gatewayconnectorfilters-properties"></a>

`AccessTypes`  <a name="cfn-ecs-service-gatewayconnectorfilters-accesstypes"></a>
The access types of the gateway ingress paths that the connector applies to.
The access type can be one of the following values:
+ `PUBLIC` - The ingress path is publicly accessible.
+ `PRIVATE` - The ingress path is only accessible privately.
*Required*: No
*Type*: Array of String
*Allowed values*: `PUBLIC | PRIVATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
