---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-device-location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::Device Location
<a name="aws-properties-networkmanager-device-location"></a>

Describes a location.

## Syntax
<a name="aws-properties-networkmanager-device-location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-device-location-syntax.json"></a>

```
{
  "[Address](#cfn-networkmanager-device-location-address)" : {{String}},
  "[Latitude](#cfn-networkmanager-device-location-latitude)" : {{String}},
  "[Longitude](#cfn-networkmanager-device-location-longitude)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkmanager-device-location-syntax.yaml"></a>

```
  [Address](#cfn-networkmanager-device-location-address): {{String}}
  [Latitude](#cfn-networkmanager-device-location-latitude): {{String}}
  [Longitude](#cfn-networkmanager-device-location-longitude): {{String}}
```

## Properties
<a name="aws-properties-networkmanager-device-location-properties"></a>

`Address`  <a name="cfn-networkmanager-device-location-address"></a>
The physical address.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Latitude`  <a name="cfn-networkmanager-device-location-latitude"></a>
The latitude.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Longitude`  <a name="cfn-networkmanager-device-location-longitude"></a>
The longitude.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
