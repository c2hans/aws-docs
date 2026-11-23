---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint DestinationEndpointAssociatedResourceDetails

The details of the resource that is associated with a destination endpoint. This is a union type, so exactly one of its members is set, depending on the type of the destination endpoint.

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails-syntax.json"></a>

```json
{
  "[RouterInput](#cfn-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails-routerinput)" : {{RouterInputDestinationEndpointAssociatedResourceDetails}},
  "[Standard](#cfn-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails-standard)" : {{Json}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails-syntax.yaml"></a>

```yaml
  [RouterInput](#cfn-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails-routerinput): {{
    RouterInputDestinationEndpointAssociatedResourceDetails}}
  [Standard](#cfn-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails-standard): {{Json}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails-properties"></a>

`RouterInput`  <a name="cfn-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails-routerinput"></a>
The associated resource details for a destination endpoint that represents a router input.
*Required*: No
*Type*: [RouterInputDestinationEndpointAssociatedResourceDetails](aws-properties-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Standard`  <a name="cfn-mediaconnect-destinationendpoint-destinationendpointassociatedresourcedetails-standard"></a>
The associated resource details for a standard destination endpoint.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
