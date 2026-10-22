---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-inputdestinationvpc.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input InputDestinationVpc
<a name="aws-properties-medialive-input-inputdestinationvpc"></a>

The properties for a VPC type input destination.

## Syntax
<a name="aws-properties-medialive-input-inputdestinationvpc-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-inputdestinationvpc-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-medialive-input-inputdestinationvpc-availabilityzone)" : {{String}},
  "[NetworkInterfaceId](#cfn-medialive-input-inputdestinationvpc-networkinterfaceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-inputdestinationvpc-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-medialive-input-inputdestinationvpc-availabilityzone): {{String}}
  [NetworkInterfaceId](#cfn-medialive-input-inputdestinationvpc-networkinterfaceid): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-inputdestinationvpc-properties"></a>

`AvailabilityZone`  <a name="cfn-medialive-input-inputdestinationvpc-availabilityzone"></a>
The availability zone of the Input destination.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterfaceId`  <a name="cfn-medialive-input-inputdestinationvpc-networkinterfaceid"></a>
The network interface ID of the Input destination in the VPC.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
