---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appconfig-experimentdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::ExperimentDefinition
<a name="aws-resource-appconfig-experimentdefinition"></a>

Describes an experiment definition, including the target audience, feature flag, treatments, and current status.

## Syntax
<a name="aws-resource-appconfig-experimentdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appconfig-experimentdefinition-syntax.json"></a>

```
{
  "Type" : "AWS::AppConfig::ExperimentDefinition",
  "Properties" : {
      "[ApplicationIdentifier](#cfn-appconfig-experimentdefinition-applicationidentifier)" : {{String}},
      "[AudienceDescription](#cfn-appconfig-experimentdefinition-audiencedescription)" : {{String}},
      "[AudienceRule](#cfn-appconfig-experimentdefinition-audiencerule)" : {{String}},
      "[ConfigurationProfileIdentifier](#cfn-appconfig-experimentdefinition-configurationprofileidentifier)" : {{String}},
      "[Control](#cfn-appconfig-experimentdefinition-control)" : {{Treatment}},
      "[EnvironmentIdentifier](#cfn-appconfig-experimentdefinition-environmentidentifier)" : {{String}},
      "[FlagKey](#cfn-appconfig-experimentdefinition-flagkey)" : {{String}},
      "[Hypothesis](#cfn-appconfig-experimentdefinition-hypothesis)" : {{String}},
      "[LaunchCriteria](#cfn-appconfig-experimentdefinition-launchcriteria)" : {{String}},
      "[Name](#cfn-appconfig-experimentdefinition-name)" : {{String}},
      "[Tags](#cfn-appconfig-experimentdefinition-tags)" : {{[ Tag, ... ]}},
      "[Treatments](#cfn-appconfig-experimentdefinition-treatments)" : {{[ Treatment, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-appconfig-experimentdefinition-syntax.yaml"></a>

```
Type: AWS::AppConfig::ExperimentDefinition
Properties:
  [ApplicationIdentifier](#cfn-appconfig-experimentdefinition-applicationidentifier): {{String}}
  [AudienceDescription](#cfn-appconfig-experimentdefinition-audiencedescription): {{String}}
  [AudienceRule](#cfn-appconfig-experimentdefinition-audiencerule): {{String}}
  [ConfigurationProfileIdentifier](#cfn-appconfig-experimentdefinition-configurationprofileidentifier): {{String}}
  [Control](#cfn-appconfig-experimentdefinition-control): {{
    Treatment}}
  [EnvironmentIdentifier](#cfn-appconfig-experimentdefinition-environmentidentifier): {{String}}
  [FlagKey](#cfn-appconfig-experimentdefinition-flagkey): {{String}}
  [Hypothesis](#cfn-appconfig-experimentdefinition-hypothesis): {{String}}
  [LaunchCriteria](#cfn-appconfig-experimentdefinition-launchcriteria): {{String}}
  [Name](#cfn-appconfig-experimentdefinition-name): {{String}}
  [Tags](#cfn-appconfig-experimentdefinition-tags): {{
    - Tag}}
  [Treatments](#cfn-appconfig-experimentdefinition-treatments): {{
    - Treatment}}
```

## Properties
<a name="aws-resource-appconfig-experimentdefinition-properties"></a>

`ApplicationIdentifier`  <a name="cfn-appconfig-experimentdefinition-applicationidentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AudienceDescription`  <a name="cfn-appconfig-experimentdefinition-audiencedescription"></a>
A description of the intended audience for the experiment.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AudienceRule`  <a name="cfn-appconfig-experimentdefinition-audiencerule"></a>
The rule that defines which users are eligible to be assigned to treatments.
*Required*: Yes
*Type*: String
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigurationProfileIdentifier`  <a name="cfn-appconfig-experimentdefinition-configurationprofileidentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Control`  <a name="cfn-appconfig-experimentdefinition-control"></a>
The control treatment used as the baseline for comparison.
*Required*: Yes
*Type*: [Treatment](aws-properties-appconfig-experimentdefinition-treatment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentIdentifier`  <a name="cfn-appconfig-experimentdefinition-environmentidentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FlagKey`  <a name="cfn-appconfig-experimentdefinition-flagkey"></a>
The key of the feature flag used by the experiment.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Hypothesis`  <a name="cfn-appconfig-experimentdefinition-hypothesis"></a>
The hypothesis that the experiment is designed to validate.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LaunchCriteria`  <a name="cfn-appconfig-experimentdefinition-launchcriteria"></a>
The conditions under which the winning treatment should be launched.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appconfig-experimentdefinition-name"></a>
The name of the experiment definition.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-appconfig-experimentdefinition-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-appconfig-experimentdefinition-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Treatments`  <a name="cfn-appconfig-experimentdefinition-treatments"></a>
The list of treatments defined for the experiment.
*Required*: Yes
*Type*: Array of [Treatment](aws-properties-appconfig-experimentdefinition-treatment.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appconfig-experimentdefinition-return-values"></a>

### Ref
<a name="aws-resource-appconfig-experimentdefinition-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-appconfig-experimentdefinition-return-values-fn--getatt"></a>

####
<a name="aws-resource-appconfig-experimentdefinition-return-values-fn--getatt-fn--getatt"></a>

`ApplicationId`  <a name="ApplicationId-fn::getatt"></a>
The application ID.

`Control.Key`  <a name="Control.Key-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time the experiment definition was created, in ISO 8601 format.

`Id`  <a name="Id-fn::getatt"></a>
The experiment definition ID.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the experiment definition. Valid values: `ACTIVE`, `IDLE`, `ARCHIVED`.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time the experiment definition was last updated, in ISO 8601 format.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
