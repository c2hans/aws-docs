---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration PreRollAdDecisionServerConfiguration
<a name="aws-properties-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration"></a>

The ad decision server configuration for live pre-roll ads. It contains settings that control how MediaTailor processes VAST responses for pre-roll ad breaks.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration-syntax.json"></a>

```
{
  "[VastResponse](#cfn-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration-vastresponse)" : {{PreRollVastResponse}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration-syntax.yaml"></a>

```
  [VastResponse](#cfn-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration-vastresponse): {{
    PreRollVastResponse}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration-properties"></a>

`VastResponse`  <a name="cfn-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration-vastresponse"></a>
The settings that control how MediaTailor processes VAST responses for live pre-roll ad breaks.
*Required*: No
*Type*: [PreRollVastResponse](aws-properties-mediatailor-playbackconfiguration-prerollvastresponse.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
