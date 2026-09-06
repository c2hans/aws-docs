---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-disk-location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Disk Location
<a name="aws-properties-lightsail-disk-location"></a>

The AWS Region and Availability Zone where the disk is located.

## Syntax
<a name="aws-properties-lightsail-disk-location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-disk-location-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-lightsail-disk-location-availabilityzone)" : {{String}},
  "[RegionName](#cfn-lightsail-disk-location-regionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-disk-location-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-lightsail-disk-location-availabilityzone): {{String}}
  [RegionName](#cfn-lightsail-disk-location-regionname): {{String}}
```

## Properties
<a name="aws-properties-lightsail-disk-location-properties"></a>

`AvailabilityZone`  <a name="cfn-lightsail-disk-location-availabilityzone"></a>
The Availability Zone where the disk is located.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionName`  <a name="cfn-lightsail-disk-location-regionname"></a>
The AWS Region where the disk is located.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
