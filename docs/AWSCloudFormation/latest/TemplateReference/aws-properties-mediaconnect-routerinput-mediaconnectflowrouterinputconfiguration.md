---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput MediaConnectFlowRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration"></a>

Configuration settings for connecting a router input to a flow output.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-syntax.json"></a>

```
{
  "[FlowArn](#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-flowarn)" : {{String}},
  "[FlowOutputArn](#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-flowoutputarn)" : {{String}},
  "[SourceTransitDecryption](#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-sourcetransitdecryption)" : {{FlowTransitEncryption}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-syntax.yaml"></a>

```
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
