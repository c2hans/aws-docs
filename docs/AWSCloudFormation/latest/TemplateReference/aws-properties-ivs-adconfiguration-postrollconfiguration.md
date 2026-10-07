---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-adconfiguration-postrollconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::AdConfiguration PostRollConfiguration
<a name="aws-properties-ivs-adconfiguration-postrollconfiguration"></a>

Configuration for the post-roll ad break to use for this ad configuration.

## Syntax
<a name="aws-properties-ivs-adconfiguration-postrollconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-adconfiguration-postrollconfiguration-syntax.json"></a>

```
{
  "[DurationSeconds](#cfn-ivs-adconfiguration-postrollconfiguration-durationseconds)" : {{Integer}},
  "[Enabled](#cfn-ivs-adconfiguration-postrollconfiguration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ivs-adconfiguration-postrollconfiguration-syntax.yaml"></a>

```
  [DurationSeconds](#cfn-ivs-adconfiguration-postrollconfiguration-durationseconds): {{Integer}}
  [Enabled](#cfn-ivs-adconfiguration-postrollconfiguration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ivs-adconfiguration-postrollconfiguration-properties"></a>

`DurationSeconds`  <a name="cfn-ivs-adconfiguration-postrollconfiguration-durationseconds"></a>
Duration of the post-roll ad break, in seconds.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-ivs-adconfiguration-postrollconfiguration-enabled"></a>
Whether the post-roll ad configuration is enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
