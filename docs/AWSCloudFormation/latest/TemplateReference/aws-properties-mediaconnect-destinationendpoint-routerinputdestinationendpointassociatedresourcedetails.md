---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint RouterInputDestinationEndpointAssociatedResourceDetails

The details of the router input that is associated with a destination endpoint.

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-syntax.json"></a>

```json
{
  "[MaximumBitrate](#cfn-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-maximumbitrate)" : {{Integer}},
  "[Name](#cfn-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-name)" : {{String}},
  "[State](#cfn-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-syntax.yaml"></a>

```yaml
  [MaximumBitrate](#cfn-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-maximumbitrate): {{Integer}}
  [Name](#cfn-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-name): {{String}}
  [State](#cfn-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-state): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-properties"></a>

`MaximumBitrate`  <a name="cfn-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-maximumbitrate"></a>
The maximum bitrate of the router input, in bits per second.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-name"></a>
The name of the router input.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-mediaconnect-destinationendpoint-routerinputdestinationendpointassociatedresourcedetails-state"></a>
The state of the router input.
*Required*: Yes
*Type*: String
*Allowed values*: `CREATING | STANDBY | STARTING | ACTIVE | STOPPING | DELETING | UPDATING | ERROR | RECOVERING | MIGRATING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
