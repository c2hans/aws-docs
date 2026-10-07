---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-adconfiguration-mediatailorplaybackconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::AdConfiguration MediaTailorPlaybackConfiguration
<a name="aws-properties-ivs-adconfiguration-mediatailorplaybackconfiguration"></a>

Object specifying a configuration for integration with an AWS Elemental MediaTailor (EMT).

## Syntax
<a name="aws-properties-ivs-adconfiguration-mediatailorplaybackconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-adconfiguration-mediatailorplaybackconfiguration-syntax.json"></a>

```
{
  "[PlaybackConfigurationArn](#cfn-ivs-adconfiguration-mediatailorplaybackconfiguration-playbackconfigurationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ivs-adconfiguration-mediatailorplaybackconfiguration-syntax.yaml"></a>

```
  [PlaybackConfigurationArn](#cfn-ivs-adconfiguration-mediatailorplaybackconfiguration-playbackconfigurationarn): {{String}}
```

## Properties
<a name="aws-properties-ivs-adconfiguration-mediatailorplaybackconfiguration-properties"></a>

`PlaybackConfigurationArn`  <a name="cfn-ivs-adconfiguration-mediatailorplaybackconfiguration-playbackconfigurationarn"></a>
ARN of the customer-created EMT PlaybackConfiguration resource in the same region and account.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws:mediatailor:[a-z0-9-]+:[0-9]+:playbackConfiguration/[a-zA-Z0-9-]+$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
