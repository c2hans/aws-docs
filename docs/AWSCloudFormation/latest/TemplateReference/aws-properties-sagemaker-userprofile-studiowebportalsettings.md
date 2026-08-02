---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-studiowebportalsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile StudioWebPortalSettings
<a name="aws-properties-sagemaker-userprofile-studiowebportalsettings"></a>

Studio settings. If these settings are applied on a user level, they take priority over the settings applied on a domain level.

## Syntax
<a name="aws-properties-sagemaker-userprofile-studiowebportalsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-studiowebportalsettings-syntax.json"></a>

```
{
  "[HiddenAppTypes](#cfn-sagemaker-userprofile-studiowebportalsettings-hiddenapptypes)" : {{[ String, ... ]}},
  "[HiddenInstanceTypes](#cfn-sagemaker-userprofile-studiowebportalsettings-hiddeninstancetypes)" : {{[ String, ... ]}},
  "[HiddenMlTools](#cfn-sagemaker-userprofile-studiowebportalsettings-hiddenmltools)" : {{[ String, ... ]}},
  "[HiddenSageMakerImageVersionAliases](#cfn-sagemaker-userprofile-studiowebportalsettings-hiddensagemakerimageversionaliases)" : {{[ HiddenSageMakerImage, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-studiowebportalsettings-syntax.yaml"></a>

```
  [HiddenAppTypes](#cfn-sagemaker-userprofile-studiowebportalsettings-hiddenapptypes): {{
    - String}}
  [HiddenInstanceTypes](#cfn-sagemaker-userprofile-studiowebportalsettings-hiddeninstancetypes): {{
    - String}}
  [HiddenMlTools](#cfn-sagemaker-userprofile-studiowebportalsettings-hiddenmltools): {{
    - String}}
  [HiddenSageMakerImageVersionAliases](#cfn-sagemaker-userprofile-studiowebportalsettings-hiddensagemakerimageversionaliases): {{
    - HiddenSageMakerImage}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-studiowebportalsettings-properties"></a>

`HiddenAppTypes`  <a name="cfn-sagemaker-userprofile-studiowebportalsettings-hiddenapptypes"></a>
The [Applications supported in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-apps.html) that are hidden from the Studio left navigation pane.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HiddenInstanceTypes`  <a name="cfn-sagemaker-userprofile-studiowebportalsettings-hiddeninstancetypes"></a>
 The instance types you are hiding from the Studio user interface.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HiddenMlTools`  <a name="cfn-sagemaker-userprofile-studiowebportalsettings-hiddenmltools"></a>
The machine learning tools that are hidden from the Studio left navigation pane.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HiddenSageMakerImageVersionAliases`  <a name="cfn-sagemaker-userprofile-studiowebportalsettings-hiddensagemakerimageversionaliases"></a>
 The version aliases you are hiding from the Studio user interface.
*Required*: No
*Type*: Array of [HiddenSageMakerImage](aws-properties-sagemaker-userprofile-hiddensagemakerimage.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
