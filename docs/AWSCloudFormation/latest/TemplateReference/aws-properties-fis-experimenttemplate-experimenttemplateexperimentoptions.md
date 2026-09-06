---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experimenttemplate-experimenttemplateexperimentoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate ExperimentTemplateExperimentOptions
<a name="aws-properties-fis-experimenttemplate-experimenttemplateexperimentoptions"></a>

Describes the experiment options for an experiment template.

## Syntax
<a name="aws-properties-fis-experimenttemplate-experimenttemplateexperimentoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experimenttemplate-experimenttemplateexperimentoptions-syntax.json"></a>

```
{
  "[AccountTargeting](#cfn-fis-experimenttemplate-experimenttemplateexperimentoptions-accounttargeting)" : {{String}},
  "[EmptyTargetResolutionMode](#cfn-fis-experimenttemplate-experimenttemplateexperimentoptions-emptytargetresolutionmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-fis-experimenttemplate-experimenttemplateexperimentoptions-syntax.yaml"></a>

```
  [AccountTargeting](#cfn-fis-experimenttemplate-experimenttemplateexperimentoptions-accounttargeting): {{String}}
  [EmptyTargetResolutionMode](#cfn-fis-experimenttemplate-experimenttemplateexperimentoptions-emptytargetresolutionmode): {{String}}
```

## Properties
<a name="aws-properties-fis-experimenttemplate-experimenttemplateexperimentoptions-properties"></a>

`AccountTargeting`  <a name="cfn-fis-experimenttemplate-experimenttemplateexperimentoptions-accounttargeting"></a>
The account targeting setting for an experiment template.
*Required*: No
*Type*: String
*Allowed values*: `multi-account | single-account`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EmptyTargetResolutionMode`  <a name="cfn-fis-experimenttemplate-experimenttemplateexperimentoptions-emptytargetresolutionmode"></a>
The empty target resolution mode for an experiment template.
*Required*: No
*Type*: String
*Allowed values*: `fail | skip`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
