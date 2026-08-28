---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-fecoutputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel FecOutputSettings
<a name="aws-properties-medialive-channel-fecoutputsettings"></a>

The settings for FEC.

The parent of this entity is UdpOutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-fecoutputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-fecoutputsettings-syntax.json"></a>

```
{
  "[ColumnDepth](#cfn-medialive-channel-fecoutputsettings-columndepth)" : {{Integer}},
  "[IncludeFec](#cfn-medialive-channel-fecoutputsettings-includefec)" : {{String}},
  "[RowLength](#cfn-medialive-channel-fecoutputsettings-rowlength)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-fecoutputsettings-syntax.yaml"></a>

```
  [ColumnDepth](#cfn-medialive-channel-fecoutputsettings-columndepth): {{Integer}}
  [IncludeFec](#cfn-medialive-channel-fecoutputsettings-includefec): {{String}}
  [RowLength](#cfn-medialive-channel-fecoutputsettings-rowlength): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-fecoutputsettings-properties"></a>

`ColumnDepth`  <a name="cfn-medialive-channel-fecoutputsettings-columndepth"></a>
The parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The number of transport stream packets per column error correction packet. The number must be between 4 and 20, inclusive.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeFec`  <a name="cfn-medialive-channel-fecoutputsettings-includefec"></a>
Enables column only or column and row-based FEC.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RowLength`  <a name="cfn-medialive-channel-fecoutputsettings-rowlength"></a>
The parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must be between 1 and 20, inclusive. If only Column FEC is used, then larger values increase robustness. If Row FEC is used, then this is the number of transport stream packets per row error correction packet, and the value must be between 4 and 20, inclusive, if includeFec is columnAndRow. If includeFec is column, this value must be 1 to 20, inclusive.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
