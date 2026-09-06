---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-gateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Gateway
<a name="aws-resource-iotsitewise-gateway"></a>

Creates a gateway, which is a virtual or edge device that delivers industrial data streams from local servers to AWS IoT SiteWise. For more information, see [Ingesting data using a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-connector.html) in the *AWS IoT SiteWise User Guide*.

## Syntax
<a name="aws-resource-iotsitewise-gateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotsitewise-gateway-syntax.json"></a>

```
{
  "Type" : "AWS::IoTSiteWise::Gateway",
  "Properties" : {
      "[GatewayCapabilitySummaries](#cfn-iotsitewise-gateway-gatewaycapabilitysummaries)" : {{[ GatewayCapabilitySummary, ... ]}},
      "[GatewayName](#cfn-iotsitewise-gateway-gatewayname)" : {{String}},
      "[GatewayPlatform](#cfn-iotsitewise-gateway-gatewayplatform)" : {{GatewayPlatform}},
      "[GatewayVersion](#cfn-iotsitewise-gateway-gatewayversion)" : {{String}},
      "[Tags](#cfn-iotsitewise-gateway-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotsitewise-gateway-syntax.yaml"></a>

```
Type: AWS::IoTSiteWise::Gateway
Properties:
  [GatewayCapabilitySummaries](#cfn-iotsitewise-gateway-gatewaycapabilitysummaries): {{
    - GatewayCapabilitySummary}}
  [GatewayName](#cfn-iotsitewise-gateway-gatewayname): {{String}}
  [GatewayPlatform](#cfn-iotsitewise-gateway-gatewayplatform): {{
    GatewayPlatform}}
  [GatewayVersion](#cfn-iotsitewise-gateway-gatewayversion): {{String}}
  [Tags](#cfn-iotsitewise-gateway-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotsitewise-gateway-properties"></a>

`GatewayCapabilitySummaries`  <a name="cfn-iotsitewise-gateway-gatewaycapabilitysummaries"></a>
A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration's definition, use [DescribeGatewayCapabilityConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html).
*Required*: No
*Type*: Array of [GatewayCapabilitySummary](aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GatewayName`  <a name="cfn-iotsitewise-gateway-gatewayname"></a>
A unique name for the gateway.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GatewayPlatform`  <a name="cfn-iotsitewise-gateway-gatewayplatform"></a>
The gateway's platform. You can only specify one platform in a gateway.
*Required*: Yes
*Type*: [GatewayPlatform](aws-properties-iotsitewise-gateway-gatewayplatform.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GatewayVersion`  <a name="cfn-iotsitewise-gateway-gatewayversion"></a>
The version of the gateway. A value of `3` indicates an MQTT-enabled, V3 gateway, while `2` indicates a Classic streams, V2 gateway.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotsitewise-gateway-tags"></a>
A list of key-value pairs that contain metadata for the gateway. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-gateway-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotsitewise-gateway-return-values"></a>

### Ref
<a name="aws-resource-iotsitewise-gateway-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `GatewayId`.

### Fn::GetAtt
<a name="aws-resource-iotsitewise-gateway-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotsitewise-gateway-return-values-fn--getatt-fn--getatt"></a>

`GatewayId`  <a name="GatewayId-fn::getatt"></a>
The ID for the gateway.
For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
