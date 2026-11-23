---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput MediaConnectFlowRouterInputConfiguration

Configuration settings for connecting a router input to a flow output.

To connect the router input to the flow output, specify both `FlowArn` and `FlowOutputArn`. To disconnect it, update the stack without these properties and keep the `MediaConnectFlow` configuration.

**Note**
The `EncryptionKeyType` of `SourceTransitDecryption` must match the `EncryptionKeyType` of the flow output's `RouterIntegrationTransitEncryption`. If you change `SourceTransitDecryption` while the router input is connected, CloudFormation temporarily disconnects the router input before it applies the update.
To change the key type, first update the stack to disconnect the router input. Then change `RouterIntegrationTransitEncryption` on the flow output (`AWS::MediaConnect::FlowOutput`). Finally, update the router input with the new `SourceTransitDecryption` and both ARNs. This reconnects it in the same update.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-syntax.json"></a>

```json
{
  "[FlowArn](#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-flowarn)" : {{String}},
  "[FlowOutputArn](#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-flowoutputarn)" : {{String}},
  "[SourceTransitDecryption](#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-sourcetransitdecryption)" : {{FlowTransitEncryption}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-syntax.yaml"></a>

```yaml
  [FlowArn](#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-flowarn): {{String}}
  [FlowOutputArn](#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-flowoutputarn): {{String}}
  [SourceTransitDecryption](#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-sourcetransitdecryption): {{
    FlowTransitEncryption}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-properties"></a>

`FlowArn`  <a name="cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-flowarn"></a>
The ARN of the flow to connect to.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:flow:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowOutputArn`  <a name="cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-flowoutputarn"></a>
The ARN of the flow output to connect to this router input.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:output:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceTransitDecryption`  <a name="cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-sourcetransitdecryption"></a>
The decryption configuration for the flow source when connected to this router input.
*Required*: Yes
*Type*: [FlowTransitEncryption](aws-properties-mediaconnect-routerinput-flowtransitencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
