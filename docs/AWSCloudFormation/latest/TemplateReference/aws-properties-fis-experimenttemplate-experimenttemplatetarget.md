---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate ExperimentTemplateTarget
<a name="aws-properties-fis-experimenttemplate-experimenttemplatetarget"></a>

Specifies a target for an experiment. You must specify at least one Amazon Resource Name (ARN) or at least one resource tag. You cannot specify both ARNs and tags.

For more information, see [Targets](https://docs.aws.amazon.com/fis/latest/userguide/targets.html) in the *AWS Fault Injection Service User Guide*.

## Syntax
<a name="aws-properties-fis-experimenttemplate-experimenttemplatetarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experimenttemplate-experimenttemplatetarget-syntax.json"></a>

```
{
  "[Filters](#cfn-fis-experimenttemplate-experimenttemplatetarget-filters)" : {{[ ExperimentTemplateTargetFilter, ... ]}},
  "[Parameters](#cfn-fis-experimenttemplate-experimenttemplatetarget-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ResourceArns](#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcearns)" : {{[ String, ... ]}},
  "[ResourceTags](#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetags)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ResourceType](#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetype)" : {{String}},
  "[SelectionMode](#cfn-fis-experimenttemplate-experimenttemplatetarget-selectionmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-fis-experimenttemplate-experimenttemplatetarget-syntax.yaml"></a>

```
  [Filters](#cfn-fis-experimenttemplate-experimenttemplatetarget-filters): {{
    - ExperimentTemplateTargetFilter}}
  [Parameters](#cfn-fis-experimenttemplate-experimenttemplatetarget-parameters): {{
    {{Key}}: {{Value}}}}
  [ResourceArns](#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcearns): {{
    - String}}
  [ResourceTags](#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetags): {{
    {{Key}}: {{Value}}}}
  [ResourceType](#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetype): {{String}}
  [SelectionMode](#cfn-fis-experimenttemplate-experimenttemplatetarget-selectionmode): {{String}}
```

## Properties
<a name="aws-properties-fis-experimenttemplate-experimenttemplatetarget-properties"></a>

`Filters`  <a name="cfn-fis-experimenttemplate-experimenttemplatetarget-filters"></a>
The filters to apply to identify target resources using specific attributes.
*Required*: No
*Type*: Array of [ExperimentTemplateTargetFilter](aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-fis-experimenttemplate-experimenttemplatetarget-parameters"></a>
The parameters for the resource type.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,64}`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArns`  <a name="cfn-fis-experimenttemplate-experimenttemplatetarget-resourcearns"></a>
The Amazon Resource Names (ARNs) of the targets.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTags`  <a name="cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetags"></a>
The tags for the target resources.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,128}`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetype"></a>
The resource type.
*Required*: Yes
*Type*: String
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectionMode`  <a name="cfn-fis-experimenttemplate-experimenttemplatetarget-selectionmode"></a>
Scopes the identified resources to a specific count or percentage.
*Required*: Yes
*Type*: String
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
