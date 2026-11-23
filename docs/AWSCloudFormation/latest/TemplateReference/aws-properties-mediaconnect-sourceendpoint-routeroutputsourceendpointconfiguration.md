---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint RouterOutputSourceEndpointConfiguration

The configuration settings for a source endpoint that represents a router output.

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointconfiguration-syntax.json"></a>

```json
{
  "[RouterOutputArn](#cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointconfiguration-routeroutputarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointconfiguration-syntax.yaml"></a>

```yaml
  [RouterOutputArn](#cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointconfiguration-routeroutputarn): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointconfiguration-properties"></a>

`RouterOutputArn`  <a name="cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointconfiguration-routeroutputarn"></a>
The Amazon Resource Name (ARN) of the router output that the source endpoint represents.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerOutput:[a-z0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
