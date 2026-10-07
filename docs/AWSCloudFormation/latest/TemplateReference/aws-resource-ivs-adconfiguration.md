---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ivs-adconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::AdConfiguration
<a name="aws-resource-ivs-adconfiguration"></a>

Object specifying a configuration for a server-side advertising insertion (which can be triggered with the API\_InsertAdBreak operation).

## Syntax
<a name="aws-resource-ivs-adconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ivs-adconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::IVS::AdConfiguration",
  "Properties" : {
      "[MediaTailorPlaybackConfigurations](#cfn-ivs-adconfiguration-mediatailorplaybackconfigurations)" : {{[ MediaTailorPlaybackConfiguration, ... ]}},
      "[Name](#cfn-ivs-adconfiguration-name)" : {{String}},
      "[PostRollConfiguration](#cfn-ivs-adconfiguration-postrollconfiguration)" : {{PostRollConfiguration}},
      "[Tags](#cfn-ivs-adconfiguration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ivs-adconfiguration-syntax.yaml"></a>

```
Type: AWS::IVS::AdConfiguration
Properties:
  [MediaTailorPlaybackConfigurations](#cfn-ivs-adconfiguration-mediatailorplaybackconfigurations): {{
    - MediaTailorPlaybackConfiguration}}
  [Name](#cfn-ivs-adconfiguration-name): {{String}}
  [PostRollConfiguration](#cfn-ivs-adconfiguration-postrollconfiguration): {{
    PostRollConfiguration}}
  [Tags](#cfn-ivs-adconfiguration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ivs-adconfiguration-properties"></a>

`MediaTailorPlaybackConfigurations`  <a name="cfn-ivs-adconfiguration-mediatailorplaybackconfigurations"></a>
List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see [Generate and Sign IVS Playback Tokens](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html).
*Required*: Yes
*Type*: Array of [MediaTailorPlaybackConfiguration](aws-properties-ivs-adconfiguration-mediatailorplaybackconfiguration.md)
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ivs-adconfiguration-name"></a>
Ad configuration name. Defaults to “”.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostRollConfiguration`  <a name="cfn-ivs-adconfiguration-postrollconfiguration"></a>
Configuration for the post-roll ad break to use for this ad configuration.
*Required*: No
*Type*: [PostRollConfiguration](aws-properties-ivs-adconfiguration-postrollconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ivs-adconfiguration-tags"></a>
Tags attached to the resource. Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
*Required*: No
*Type*: Array of [Tag](aws-properties-ivs-adconfiguration-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ivs-adconfiguration-return-values"></a>

### Ref
<a name="aws-resource-ivs-adconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ivs-adconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-ivs-adconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Ad configuration ARN.
