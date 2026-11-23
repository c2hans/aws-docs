---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-destinationendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint DestinationEndpointConfiguration

The configuration settings for a destination endpoint. This is a union type, so exactly one of its members is set, depending on the type of the destination endpoint.

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-destinationendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-destinationendpointconfiguration-syntax.json"></a>

```json
{
  "[RouterInput](#cfn-mediaconnect-destinationendpoint-destinationendpointconfiguration-routerinput)" : {{RouterInputDestinationEndpointConfiguration}},
  "[Standard](#cfn-mediaconnect-destinationendpoint-destinationendpointconfiguration-standard)" : {{StandardDestinationEndpointConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-destinationendpointconfiguration-syntax.yaml"></a>

```yaml
  [RouterInput](#cfn-mediaconnect-destinationendpoint-destinationendpointconfiguration-routerinput): {{
    RouterInputDestinationEndpointConfiguration}}
  [Standard](#cfn-mediaconnect-destinationendpoint-destinationendpointconfiguration-standard): {{
    StandardDestinationEndpointConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-destinationendpointconfiguration-properties"></a>

`RouterInput`  <a name="cfn-mediaconnect-destinationendpoint-destinationendpointconfiguration-routerinput"></a>
The configuration settings for a destination endpoint that represents a router input.
*Required*: No
*Type*: [RouterInputDestinationEndpointConfiguration](aws-properties-mediaconnect-destinationendpoint-routerinputdestinationendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Standard`  <a name="cfn-mediaconnect-destinationendpoint-destinationendpointconfiguration-standard"></a>
The configuration settings for a standard destination endpoint, which represents an external destination.
*Required*: No
*Type*: [StandardDestinationEndpointConfiguration](aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
