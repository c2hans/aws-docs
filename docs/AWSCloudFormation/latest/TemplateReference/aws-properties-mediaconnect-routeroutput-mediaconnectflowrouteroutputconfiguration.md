---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput MediaConnectFlowRouterOutputConfiguration
<a name="aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration"></a>

Configuration settings for connecting a router output to a MediaConnect flow source.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-syntax.json"></a>

```
{
  "[DestinationTransitEncryption](#cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-destinationtransitencryption)" : {{FlowTransitEncryption}},
  "[FlowArn](#cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-flowarn)" : {{String}},
  "[FlowSourceArn](#cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-flowsourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-syntax.yaml"></a>

```
  [DestinationTransitEncryption](#cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-destinationtransitencryption): {{
    FlowTransitEncryption}}
  [FlowArn](#cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-flowarn): {{String}}
  [FlowSourceArn](#cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-flowsourcearn): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-properties"></a>

`DestinationTransitEncryption`  <a name="cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-destinationtransitencryption"></a>
The encryption configuration for the flow destination when connected to this router output.
*Required*: Yes
*Type*: [FlowTransitEncryption](aws-properties-mediaconnect-routeroutput-flowtransitencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowArn`  <a name="cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-flowarn"></a>
The ARN of the flow to connect to this router output.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:flow:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowSourceArn`  <a name="cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-flowsourcearn"></a>
The ARN of the flow source to connect to this router output.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:source:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
