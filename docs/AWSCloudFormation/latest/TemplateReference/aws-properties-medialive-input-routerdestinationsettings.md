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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
