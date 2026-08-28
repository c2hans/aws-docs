---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-ancillarysourcesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AncillarySourceSettings
<a name="aws-properties-medialive-channel-ancillarysourcesettings"></a>

Information about the ancillary captions to extract from the input.

The parent of this entity is CaptionSelectorSettings.

## Syntax
<a name="aws-properties-medialive-channel-ancillarysourcesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-ancillarysourcesettings-syntax.json"></a>

```
{
  "[SourceAncillaryChannelNumber](#cfn-medialive-channel-ancillarysourcesettings-sourceancillarychannelnumber)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-ancillarysourcesettings-syntax.yaml"></a>

```
  [SourceAncillaryChannelNumber](#cfn-medialive-channel-ancillarysourcesettings-sourceancillarychannelnumber): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-ancillarysourcesettings-properties"></a>

`SourceAncillaryChannelNumber`  <a name="cfn-medialive-channel-ancillarysourcesettings-sourceancillarychannelnumber"></a>
Specifies the number (1 to 4) of the captions channel you want to extract from the ancillary captions. If you plan to convert the ancillary captions to another format, complete this field. If you plan to choose Embedded as the captions destination in the output (to pass through all the channels in the ancillary captions), leave this field blank because MediaLive ignores the field.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
