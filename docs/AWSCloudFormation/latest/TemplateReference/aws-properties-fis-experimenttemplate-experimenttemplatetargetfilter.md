---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate ExperimentTemplateTargetFilter
<a name="aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter"></a>

Specifies a filter used for the target resource input in an experiment template.

For more information, see [Resource filters](https://docs.aws.amazon.com/fis/latest/userguide/targets.html#target-filters) in the *AWS Fault Injection Service User Guide*.

## Syntax
<a name="aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter-syntax.json"></a>

```
{
  "[Path](#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-path)" : {{String}},
  "[Values](#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter-syntax.yaml"></a>

```
  [Path](#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-path): {{String}}
  [Values](#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-values): {{
    - String}}
```

## Properties
<a name="aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter-properties"></a>

`Path`  <a name="cfn-fis-experimenttemplate-experimenttemplatetargetfilter-path"></a>
The attribute path for the filter.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-fis-experimenttemplate-experimenttemplatetargetfilter-values"></a>
The attribute values for the filter.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
