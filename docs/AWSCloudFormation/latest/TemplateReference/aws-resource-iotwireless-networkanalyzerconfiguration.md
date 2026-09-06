---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotwireless-networkanalyzerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::NetworkAnalyzerConfiguration
<a name="aws-resource-iotwireless-networkanalyzerconfiguration"></a>

Network analyzer configuration.

## Syntax
<a name="aws-resource-iotwireless-networkanalyzerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotwireless-networkanalyzerconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::IoTWireless::NetworkAnalyzerConfiguration",
  "Properties" : {
      "[Description](#cfn-iotwireless-networkanalyzerconfiguration-description)" : {{String}},
      "[Name](#cfn-iotwireless-networkanalyzerconfiguration-name)" : {{String}},
      "[Tags](#cfn-iotwireless-networkanalyzerconfiguration-tags)" : {{[ Tag, ... ]}},
      "[TraceContent](#cfn-iotwireless-networkanalyzerconfiguration-tracecontent)" : {{TraceContent}},
      "[WirelessDevices](#cfn-iotwireless-networkanalyzerconfiguration-wirelessdevices)" : {{[ String, ... ]}},
      "[WirelessGateways](#cfn-iotwireless-networkanalyzerconfiguration-wirelessgateways)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotwireless-networkanalyzerconfiguration-syntax.yaml"></a>

```
Type: AWS::IoTWireless::NetworkAnalyzerConfiguration
Properties:
  [Description](#cfn-iotwireless-networkanalyzerconfiguration-description): {{String}}
  [Name](#cfn-iotwireless-networkanalyzerconfiguration-name): {{String}}
  [Tags](#cfn-iotwireless-networkanalyzerconfiguration-tags): {{
    - Tag}}
  [TraceContent](#cfn-iotwireless-networkanalyzerconfiguration-tracecontent): {{
    TraceContent}}
  [WirelessDevices](#cfn-iotwireless-networkanalyzerconfiguration-wirelessdevices): {{
    - String}}
  [WirelessGateways](#cfn-iotwireless-networkanalyzerconfiguration-wirelessgateways): {{
    - String}}
```

## Properties
<a name="aws-resource-iotwireless-networkanalyzerconfiguration-properties"></a>

`Description`  <a name="cfn-iotwireless-networkanalyzerconfiguration-description"></a>
The description of the resource.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iotwireless-networkanalyzerconfiguration-name"></a>
Name of the network analyzer configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]+$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotwireless-networkanalyzerconfiguration-tags"></a>
The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotwireless-networkanalyzerconfiguration-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TraceContent`  <a name="cfn-iotwireless-networkanalyzerconfiguration-tracecontent"></a>
Trace content for your wireless gateway and wireless device resources.
*Required*: No
*Type*: [TraceContent](aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WirelessDevices`  <a name="cfn-iotwireless-networkanalyzerconfiguration-wirelessdevices"></a>
Wireless device resources to add to the network analyzer configuration. Provide the `WirelessDeviceId` of the resource to add in the input array.
*Required*: No
*Type*: Array of String
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WirelessGateways`  <a name="cfn-iotwireless-networkanalyzerconfiguration-wirelessgateways"></a>
Wireless gateway resources to add to the network analyzer configuration. Provide the `WirelessGatewayId` of the resource to add in the input array.
*Required*: No
*Type*: Array of String
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotwireless-networkanalyzerconfiguration-return-values"></a>

### Ref
<a name="aws-resource-iotwireless-networkanalyzerconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the network analyzer configuration.

### Fn::GetAtt
<a name="aws-resource-iotwireless-networkanalyzerconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-iotwireless-networkanalyzerconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the resource.
