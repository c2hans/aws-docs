---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-inputdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input InputDestination
<a name="aws-properties-medialive-input-inputdestination"></a>

The settings for a PUSH type input.

## Syntax
<a name="aws-properties-medialive-input-inputdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-inputdestination-syntax.json"></a>

```
{
  "[Ip](#cfn-medialive-input-inputdestination-ip)" : {{String}},
  "[Network](#cfn-medialive-input-inputdestination-network)" : {{String}},
  "[NetworkRoutes](#cfn-medialive-input-inputdestination-networkroutes)" : {{[ InputDestinationRoute, ... ]}},
  "[Port](#cfn-medialive-input-inputdestination-port)" : {{String}},
  "[StaticIpAddress](#cfn-medialive-input-inputdestination-staticipaddress)" : {{String}},
  "[StreamName](#cfn-medialive-input-inputdestination-streamname)" : {{String}},
  "[Url](#cfn-medialive-input-inputdestination-url)" : {{String}},
  "[Vpc](#cfn-medialive-input-inputdestination-vpc)" : {{InputDestinationVpc}}
}
```

### YAML
<a name="aws-properties-medialive-input-inputdestination-syntax.yaml"></a>

```
  [Ip](#cfn-medialive-input-inputdestination-ip): {{String}}
  [Network](#cfn-medialive-input-inputdestination-network): {{String}}
  [NetworkRoutes](#cfn-medialive-input-inputdestination-networkroutes): {{
    - InputDestinationRoute}}
  [Port](#cfn-medialive-input-inputdestination-port): {{String}}
  [StaticIpAddress](#cfn-medialive-input-inputdestination-staticipaddress): {{String}}
  [StreamName](#cfn-medialive-input-inputdestination-streamname): {{String}}
  [Url](#cfn-medialive-input-inputdestination-url): {{String}}
  [Vpc](#cfn-medialive-input-inputdestination-vpc): {{
    InputDestinationVpc}}
```

## Properties
<a name="aws-properties-medialive-input-inputdestination-properties"></a>

`Ip`  <a name="cfn-medialive-input-inputdestination-ip"></a>
The system-generated static IP address of endpoint. It remains fixed for the lifetime of the input.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Network`  <a name="cfn-medialive-input-inputdestination-network"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkRoutes`  <a name="cfn-medialive-input-inputdestination-networkroutes"></a>
Property description not available.
*Required*: No
*Type*: Array of [InputDestinationRoute](aws-properties-medialive-input-inputdestinationroute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-medialive-input-inputdestination-port"></a>
The port number for the input.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticIpAddress`  <a name="cfn-medialive-input-inputdestination-staticipaddress"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamName`  <a name="cfn-medialive-input-inputdestination-streamname"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-medialive-input-inputdestination-url"></a>
This represents the endpoint that the customer stream will be pushed to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vpc`  <a name="cfn-medialive-input-inputdestination-vpc"></a>
Property description not available.
*Required*: No
*Type*: [InputDestinationVpc](aws-properties-medialive-input-inputdestinationvpc.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
