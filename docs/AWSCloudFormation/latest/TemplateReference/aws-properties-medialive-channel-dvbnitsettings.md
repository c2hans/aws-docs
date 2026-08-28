---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-dvbnitsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel DvbNitSettings
<a name="aws-properties-medialive-channel-dvbnitsettings"></a>

The configuration of DVB NIT.

The parent of this entity is M2tsSettings.

## Syntax
<a name="aws-properties-medialive-channel-dvbnitsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-dvbnitsettings-syntax.json"></a>

```
{
  "[NetworkId](#cfn-medialive-channel-dvbnitsettings-networkid)" : {{Integer}},
  "[NetworkName](#cfn-medialive-channel-dvbnitsettings-networkname)" : {{String}},
  "[RepInterval](#cfn-medialive-channel-dvbnitsettings-repinterval)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-dvbnitsettings-syntax.yaml"></a>

```
  [NetworkId](#cfn-medialive-channel-dvbnitsettings-networkid): {{Integer}}
  [NetworkName](#cfn-medialive-channel-dvbnitsettings-networkname): {{String}}
  [RepInterval](#cfn-medialive-channel-dvbnitsettings-repinterval): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-dvbnitsettings-properties"></a>

`NetworkId`  <a name="cfn-medialive-channel-dvbnitsettings-networkid"></a>
The numeric value placed in the Network Information Table (NIT).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkName`  <a name="cfn-medialive-channel-dvbnitsettings-networkname"></a>
The network name text placed in the networkNameDescriptor inside the Network Information Table (NIT). The maximum length is 256 characters.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepInterval`  <a name="cfn-medialive-channel-dvbnitsettings-repinterval"></a>
The number of milliseconds between instances of this table in the output transport stream.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
