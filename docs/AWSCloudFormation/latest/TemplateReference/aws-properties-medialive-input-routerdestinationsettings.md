---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-routerdestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input RouterDestinationSettings
<a name="aws-properties-medialive-input-routerdestinationsettings"></a>

Settings for a MediaConnect Router destination.

The parent of this entity is RouterSettings.

## Syntax
<a name="aws-properties-medialive-input-routerdestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-routerdestinationsettings-syntax.json"></a>

```
{
  "[AvailabilityZoneName](#cfn-medialive-input-routerdestinationsettings-availabilityzonename)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-routerdestinationsettings-syntax.yaml"></a>

```
  [AvailabilityZoneName](#cfn-medialive-input-routerdestinationsettings-availabilityzonename): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-routerdestinationsettings-properties"></a>

`AvailabilityZoneName`  <a name="cfn-medialive-input-routerdestinationsettings-availabilityzonename"></a>
The Availability Zone for this MediaConnect Router destination endpoint.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
