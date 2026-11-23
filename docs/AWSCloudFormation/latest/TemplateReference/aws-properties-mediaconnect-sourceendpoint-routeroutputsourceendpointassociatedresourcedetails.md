---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint RouterOutputSourceEndpointAssociatedResourceDetails

The details of the router output that is associated with a source endpoint.

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-syntax.json"></a>

```json
{
  "[MaximumBitrate](#cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-maximumbitrate)" : {{Integer}},
  "[Name](#cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-name)" : {{String}},
  "[State](#cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-syntax.yaml"></a>

```yaml
  [MaximumBitrate](#cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-maximumbitrate): {{Integer}}
  [Name](#cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-name): {{String}}
  [State](#cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-state): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-properties"></a>

`MaximumBitrate`  <a name="cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-maximumbitrate"></a>
The maximum bitrate of the router output, in bits per second.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-name"></a>
The name of the router output.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-mediaconnect-sourceendpoint-routeroutputsourceendpointassociatedresourcedetails-state"></a>
The state of the router output.
*Required*: Yes
*Type*: String
*Allowed values*: `CREATING | STANDBY | STARTING | ACTIVE | STOPPING | DELETING | UPDATING | ERROR | RECOVERING | MIGRATING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
