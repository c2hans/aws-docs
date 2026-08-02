---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-inputrequestdestinationroute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input InputRequestDestinationRoute
<a name="aws-properties-medialive-input-inputrequestdestinationroute"></a>

A route for an on-premises input destination.

The parent of this entity is InputDestinationRequest.

## Syntax
<a name="aws-properties-medialive-input-inputrequestdestinationroute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-inputrequestdestinationroute-syntax.json"></a>

```
{
  "[Cidr](#cfn-medialive-input-inputrequestdestinationroute-cidr)" : {{String}},
  "[Gateway](#cfn-medialive-input-inputrequestdestinationroute-gateway)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-inputrequestdestinationroute-syntax.yaml"></a>

```
  [Cidr](#cfn-medialive-input-inputrequestdestinationroute-cidr): {{String}}
  [Gateway](#cfn-medialive-input-inputrequestdestinationroute-gateway): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-inputrequestdestinationroute-properties"></a>

`Cidr`  <a name="cfn-medialive-input-inputrequestdestinationroute-cidr"></a>
The CIDR of the route.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gateway`  <a name="cfn-medialive-input-inputrequestdestinationroute-gateway"></a>
An optional gateway for the route.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
