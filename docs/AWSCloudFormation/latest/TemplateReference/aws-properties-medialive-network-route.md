---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-network-route.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Network Route
<a name="aws-properties-medialive-network-route"></a>

A route for the network.

## Syntax
<a name="aws-properties-medialive-network-route-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-network-route-syntax.json"></a>

```
{
  "[Cidr](#cfn-medialive-network-route-cidr)" : {{String}},
  "[Gateway](#cfn-medialive-network-route-gateway)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-network-route-syntax.yaml"></a>

```
  [Cidr](#cfn-medialive-network-route-cidr): {{String}}
  [Gateway](#cfn-medialive-network-route-gateway): {{String}}
```

## Properties
<a name="aws-properties-medialive-network-route-properties"></a>

`Cidr`  <a name="cfn-medialive-network-route-cidr"></a>
The IP address CIDR for the route.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gateway`  <a name="cfn-medialive-network-route-gateway"></a>
IP address for the route packet paths.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
