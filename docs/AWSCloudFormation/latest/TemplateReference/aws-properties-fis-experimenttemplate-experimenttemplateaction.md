---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experimenttemplate-experimenttemplateaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate ExperimentTemplateAction
<a name="aws-properties-fis-experimenttemplate-experimenttemplateaction"></a>

Specifies an action for an experiment template.

For more information, see [Actions](https://docs.aws.amazon.com/fis/latest/userguide/actions.html) in the *AWS Fault Injection Service User Guide*.

## Syntax
<a name="aws-properties-fis-experimenttemplate-experimenttemplateaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experimenttemplate-experimenttemplateaction-syntax.json"></a>

```
{
  "[ActionId](#cfn-fis-experimenttemplate-experimenttemplateaction-actionid)" : {{String}},
  "[Description](#cfn-fis-experimenttemplate-experimenttemplateaction-description)" : {{String}},
  "[Parameters](#cfn-fis-experimenttemplate-experimenttemplateaction-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[StartAfter](#cfn-fis-experimenttemplate-experimenttemplateaction-startafter)" : {{[ String, ... ]}},
  "[Targets](#cfn-fis-experimenttemplate-experimenttemplateaction-targets)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-fis-experimenttemplate-experimenttemplateaction-syntax.yaml"></a>

```
  [ActionId](#cfn-fis-experimenttemplate-experimenttemplateaction-actionid): {{String}}
  [Description](#cfn-fis-experimenttemplate-experimenttemplateaction-description): {{String}}
  [Parameters](#cfn-fis-experimenttemplate-experimenttemplateaction-parameters): {{
    {{Key}}: {{Value}}}}
  [StartAfter](#cfn-fis-experimenttemplate-experimenttemplateaction-startafter): {{
    - String}}
  [Targets](#cfn-fis-experimenttemplate-experimenttemplateaction-targets): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-fis-experimenttemplate-experimenttemplateaction-properties"></a>

`ActionId`  <a name="cfn-fis-experimenttemplate-experimenttemplateaction-actionid"></a>
The ID of the action.
*Required*: Yes
*Type*: String
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-fis-experimenttemplate-experimenttemplateaction-description"></a>
A description for the action.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-fis-experimenttemplate-experimenttemplateaction-parameters"></a>
The parameters for the action.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,64}`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartAfter`  <a name="cfn-fis-experimenttemplate-experimenttemplateaction-startafter"></a>
The name of the action that must be completed before the current action starts.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Targets`  <a name="cfn-fis-experimenttemplate-experimenttemplateaction-targets"></a>
The targets for the action.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,64}`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
