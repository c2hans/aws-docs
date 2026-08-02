---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-inputdestinationrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input InputDestinationRequest
<a name="aws-properties-medialive-input-inputdestinationrequest"></a>

Settings that apply only if the input is a push type of input.

The parent of this entity is Input.

## Syntax
<a name="aws-properties-medialive-input-inputdestinationrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-inputdestinationrequest-syntax.json"></a>

```
{
  "[Network](#cfn-medialive-input-inputdestinationrequest-network)" : {{String}},
  "[NetworkRoutes](#cfn-medialive-input-inputdestinationrequest-networkroutes)" : {{[ InputRequestDestinationRoute, ... ]}},
  "[StaticIpAddress](#cfn-medialive-input-inputdestinationrequest-staticipaddress)" : {{String}},
  "[StreamName](#cfn-medialive-input-inputdestinationrequest-streamname)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-inputdestinationrequest-syntax.yaml"></a>

```
  [Network](#cfn-medialive-input-inputdestinationrequest-network): {{String}}
  [NetworkRoutes](#cfn-medialive-input-inputdestinationrequest-networkroutes): {{
    - InputRequestDestinationRoute}}
  [StaticIpAddress](#cfn-medialive-input-inputdestinationrequest-staticipaddress): {{String}}
  [StreamName](#cfn-medialive-input-inputdestinationrequest-streamname): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-inputdestinationrequest-properties"></a>

`Network`  <a name="cfn-medialive-input-inputdestinationrequest-network"></a>
If the push input has an input location of ON-PREM, the ID of the attached network.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkRoutes`  <a name="cfn-medialive-input-inputdestinationrequest-networkroutes"></a>
If the push input has an input location of ON-PREM it's a requirement to specify what the route of the input is going to be on the customer local network.
*Required*: No
*Type*: Array of [InputRequestDestinationRoute](aws-properties-medialive-input-inputrequestdestinationroute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticIpAddress`  <a name="cfn-medialive-input-inputdestinationrequest-staticipaddress"></a>
If the push input has an input location of ON-PREM it's optional to specify what the IP address of the input is going to be on the customer local network.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamName`  <a name="cfn-medialive-input-inputdestinationrequest-streamname"></a>
The stream name (application name/application instance) for the location the RTMP source content will be pushed to in MediaLive.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
