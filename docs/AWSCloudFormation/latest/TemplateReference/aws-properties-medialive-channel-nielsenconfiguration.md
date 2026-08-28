---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-nielsenconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel NielsenConfiguration
<a name="aws-properties-medialive-channel-nielsenconfiguration"></a>

The settings to configure Nielsen watermarks.

The parent of this entity is EncoderSettings.

## Syntax
<a name="aws-properties-medialive-channel-nielsenconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-nielsenconfiguration-syntax.json"></a>

```
{
  "[DistributorId](#cfn-medialive-channel-nielsenconfiguration-distributorid)" : {{String}},
  "[NielsenPcmToId3Tagging](#cfn-medialive-channel-nielsenconfiguration-nielsenpcmtoid3tagging)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-nielsenconfiguration-syntax.yaml"></a>

```
  [DistributorId](#cfn-medialive-channel-nielsenconfiguration-distributorid): {{String}}
  [NielsenPcmToId3Tagging](#cfn-medialive-channel-nielsenconfiguration-nielsenpcmtoid3tagging): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-nielsenconfiguration-properties"></a>

`DistributorId`  <a name="cfn-medialive-channel-nielsenconfiguration-distributorid"></a>
Enter the Distributor ID assigned to your organization by Nielsen.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NielsenPcmToId3Tagging`  <a name="cfn-medialive-channel-nielsenconfiguration-nielsenpcmtoid3tagging"></a>
Enables Nielsen PCM to ID3 tagging
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
