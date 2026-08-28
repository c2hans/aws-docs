---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediaconnectroutergroupsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaConnectRouterGroupSettings
<a name="aws-properties-medialive-channel-mediaconnectroutergroupsettings"></a>

MediaConnect Router group settings.

The parent of this entity is OutputGroupSettings.

## Syntax
<a name="aws-properties-medialive-channel-mediaconnectroutergroupsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediaconnectroutergroupsettings-syntax.json"></a>

```
{
  "[AvailabilityZones](#cfn-medialive-channel-mediaconnectroutergroupsettings-availabilityzones)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediaconnectroutergroupsettings-syntax.yaml"></a>

```
  [AvailabilityZones](#cfn-medialive-channel-mediaconnectroutergroupsettings-availabilityzones): {{
    - String}}
```

## Properties
<a name="aws-properties-medialive-channel-mediaconnectroutergroupsettings-properties"></a>

`AvailabilityZones`  <a name="cfn-medialive-channel-mediaconnectroutergroupsettings-availabilityzones"></a>
The names of the Availability Zones in which to write output to MediaConnect Router.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
