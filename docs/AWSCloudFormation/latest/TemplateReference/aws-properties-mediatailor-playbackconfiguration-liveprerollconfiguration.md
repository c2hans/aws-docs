---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration LivePreRollConfiguration
<a name="aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration"></a>

The configuration for pre-roll ad insertion.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration-syntax.json"></a>

```
{
  "[AdDecisionServerConfiguration](#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-addecisionserverconfiguration)" : {{PreRollAdDecisionServerConfiguration}},
  "[AdDecisionServerUrl](#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-addecisionserverurl)" : {{String}},
  "[MaxDurationSeconds](#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-maxdurationseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration-syntax.yaml"></a>

```
  [AdDecisionServerConfiguration](#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-addecisionserverconfiguration): {{
    PreRollAdDecisionServerConfiguration}}
  [AdDecisionServerUrl](#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-addecisionserverurl): {{String}}
  [MaxDurationSeconds](#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-maxdurationseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration-properties"></a>

`AdDecisionServerConfiguration`  <a name="cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-addecisionserverconfiguration"></a>
The configuration for the ad decision server (ADS) for live pre-roll ads. The configuration contains settings that control how MediaTailor processes VAST responses for pre-roll ad breaks.
*Required*: No
*Type*: [PreRollAdDecisionServerConfiguration](aws-properties-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdDecisionServerUrl`  <a name="cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-addecisionserverurl"></a>
The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxDurationSeconds`  <a name="cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-maxdurationseconds"></a>
The maximum allowed duration for the pre-roll ad avail. AWS Elemental MediaTailor won't play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
