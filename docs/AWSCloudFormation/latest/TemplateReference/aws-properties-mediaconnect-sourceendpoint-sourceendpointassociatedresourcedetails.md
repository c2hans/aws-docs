---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint SourceEndpointAssociatedResourceDetails

The details of the resource that is associated with a source endpoint. This is a union type, so exactly one of its members is set, depending on the type of the source endpoint.

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails-syntax.json"></a>

```json
{
  "[RouterOutput](#cfn-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails-routeroutput)" : {{RouterOutputSourceEndpointAssociatedResourceDetails}},
  "[Standard](#cfn-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails-standard)" : {{Json}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails-syntax.yaml"></a>

```yaml
  [RouterOutput](#cfn-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails-routeroutput): {{
    RouterOutputSourceEndpointAssociatedResourceDetails}}
  [Standard](#cfn-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails-standard): {{Json}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails-properties"></a>

`RouterOutput`  <a name="cfn-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails-routeroutput"></a>
The associated resource details for a source endpoint that represents a router output.
*Required*: No
*Type*: [RouterOutputSourceEndpointAssociatedResourceDetails](aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Standard`  <a name="cfn-mediaconnect-sourceendpoint-sourceendpointassociatedresourcedetails-standard"></a>
The associated resource details for a standard source endpoint.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
